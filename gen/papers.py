"""Assemble full AQA-style mock papers from the question bank.

Real AQA 7447 papers: 10 questions worth 5, 10 or 15 marks each (total 95)
plus one 25-mark essay chosen from two -> 120 marks.  e.g. June 2023 Paper 1:
5, 10, 10, 10, 15, 5, 5, 10, 10, 15 + 25.
"""
import random
from collections import Counter
from bank.topics import subtopic_index

# (number of 15s, number of 10s, number of 5s) -> 10 questions, 95 marks, in order of preference
PATTERNS = [(2, 5, 3), (1, 7, 2), (0, 9, 1), (3, 3, 4), (1, 6, 3)]  # last is 9 questions? no: keep only 10-question sums
PATTERNS = [p for p in PATTERNS if sum(p) == 10 and 15 * p[0] + 10 * p[1] + 5 * p[2] == 95]


def assemble_paper(paper_no, set_no, questions, essays, used_counter):
    """Return (list_of_Q, (Essay, Essay)).  `used_counter` tracks how often each
    question has been used so that sets rotate through the whole bank before repeating."""
    idx = subtopic_index()
    rng = random.Random(1000 * paper_no + set_no)
    pool = [q for q in questions if paper_no in idx[q.topic]["papers"]]
    avail = Counter(q.marks for q in pool)
    # rotate the preferred pattern between sets, but only use feasible ones
    feasible = [p for p in PATTERNS if avail[15] >= p[0] and avail[10] >= p[1] and avail[5] >= p[2]]
    if not feasible:
        feasible = [(0, 9, 1)]
    # choose the feasible pattern whose questions have been used least so far (spreads reuse evenly)
    def cost(p):
        tot = 0
        for size, n in zip((15, 10, 5), p):
            us = sorted(used_counter[q.id] for q in pool if q.marks == size)
            tot += sum(us[:n])
        # small bias towards the real AQA pattern (2 x 15, 5 x 10, 3 x 5) when usage is similar
        return tot - 2 * p[0]
    a, b, c = min(feasible, key=lambda p: (cost(p), PATTERNS.index(p)))

    def pick(size, n, chosen, need_extended=False):
        cands = [q for q in pool if q.marks == size and q not in chosen]
        rng.shuffle(cands)
        cands.sort(key=lambda q: used_counter[q.id])
        out = []
        if need_extended:  # make sure a 9-mark levels question is included
            for q in [x for x in cands if x.has_extended]:
                subs = {x.topic for x in chosen}
                if q.topic not in subs:
                    out.append(q)
                    cands = [x for x in cands if x is not q]
                    break
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

    chosen = []
    chosen += pick(15, a, chosen)
    has_ext = any(q.has_extended for q in chosen)
    chosen += pick(10, b, chosen, need_extended=not has_ext)
    chosen += pick(5, c, chosen)
    for q in chosen:
        used_counter[q.id] += 1
    # order: shuffle, but put a question containing the 9-mark extended response last (as AQA does)
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
