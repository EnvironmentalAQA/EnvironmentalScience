"""Assemble full AQA-style mock papers from the question bank.

Real AQA 7447 papers: 10 questions worth 5, 10 or 15 marks each (total 95)
plus one 25-mark essay chosen from two -> 120 marks.  e.g. June 2023 Paper 1:
5, 10, 10, 10, 15, 5, 5, 10, 10, 15 + 25.

A real paper carries exactly **one** 9-mark levels-of-response question, so each mock
takes exactly one question that contains one and fills every other slot from questions
that do not.  See bank/long_15.py for the 15-markers written to make that possible.
"""
import random
from collections import Counter
from bank.topics import subtopic_index

# (number of 15s, number of 10s, number of 5s).  Every published 7447 paper uses one of
# these two shapes, six of each across the twelve papers released so far, so the sets
# alternate between them rather than inventing others.
PATTERNS = [(2, 5, 3), (1, 7, 2)]
assert all(sum(p) == 10 and 15 * p[0] + 10 * p[1] + 5 * p[2] == 95 for p in PATTERNS)


def assemble_paper(paper_no, set_no, questions, essays, used_counter):
    """Return (list_of_Q, (Essay, Essay)).  `used_counter` tracks how often each
    question has been used so that sets rotate through the whole bank before repeating."""
    idx = subtopic_index()
    rng = random.Random(1000 * paper_no + set_no)
    pool = [q for q in questions if paper_no in idx[q.topic]["papers"]]
    ext_pool = [q for q in pool if q.has_extended]
    plain_pool = [q for q in pool if not q.has_extended]
    availp = Counter(q.marks for q in plain_pool)
    ext_sizes = {q.marks for q in ext_pool}

    # Alternate the two real paper shapes between sets; a shape is usable only if the nine
    # non-extended slots can be filled from questions with no 9-mark part, once the single
    # extended question has taken a 15 or a 10.
    def options(p):
        need = dict(zip((15, 10, 5), p))
        return [(p, size) for size in (15, 10)
                if size in ext_sizes and need[size] >= 1
                and all(availp[s] >= need[s] - (1 if s == size else 0) for s in (15, 10, 5))]

    order = [PATTERNS[(set_no - 1) % len(PATTERNS)]] + [p for p in PATTERNS if p != PATTERNS[(set_no - 1) % len(PATTERNS)]]
    feasible = next((o for o in (options(p) for p in order) if o), [((0, 9, 1), 10)])

    def least_used(cands, n):
        return sorted(used_counter[q.id] for q in cands)[:n]

    def cost(choice):
        """Within the shape, put the 9-mark question in whichever slot has been used least,
        so the sets rotate evenly through the bank."""
        p, size = choice
        tot = 0
        for s, n in zip((15, 10, 5), p):
            tot += sum(least_used([q for q in plain_pool if q.marks == s], n - (1 if s == size else 0)))
        tot += sum(least_used([q for q in ext_pool if q.marks == size], 1))
        return tot

    (a, b, c), ext_size = min(feasible, key=lambda ch: (cost(ch), ch[1]))

    def pick(cands, n, chosen):
        cands = [q for q in cands if q not in chosen]
        rng.shuffle(cands)
        cands.sort(key=lambda q: used_counter[q.id])
        out = []
        for q in cands:
            if len(out) == n:
                break
            subs = {x.topic for x in chosen + out}
            tops = Counter(idx[x.topic]["topic_slug"] for x in chosen + out)
            tslug = idx[q.topic]["topic_slug"]
            if q.topic in subs:
                continue
            if tslug == "research" and tops["research"] >= 1:
                continue
            if tops[tslug] >= 5:
                continue
            out.append(q)
        if len(out) < n:  # relax constraints if the bank is thin
            for q in cands:
                if len(out) == n:
                    break
                if q not in out:
                    out.append(q)
        return out

    # exactly one question carrying the 9-mark levels-of-response part
    chosen = pick([q for q in ext_pool if q.marks == ext_size], 1, [])
    for size, n in zip((15, 10, 5), (a, b, c)):
        want = n - (1 if size == ext_size else 0)
        if want > 0:
            chosen += pick([q for q in plain_pool if q.marks == size], want, chosen)
    for q in chosen:
        used_counter[q.id] += 1
    # order: shuffle, but put the 9-mark extended response last (as AQA does)
    rng.shuffle(chosen)
    ext = [q for q in chosen if q.has_extended]
    if ext:
        last = ext[-1]
        chosen.remove(last)
        chosen.append(last)
    # essays: rotate through pairs
    ep = [e for e in essays if e.paper == paper_no]
    if len(ep) >= 2:
        i = (set_no - 1) % len(ep)
        j = (i + 1 + (set_no // len(ep))) % len(ep)
        if j == i:
            j = (i + 1) % len(ep)
        pair = (ep[i], ep[j])
    else:
        pair = tuple(ep) if ep else None
    return chosen, pair
