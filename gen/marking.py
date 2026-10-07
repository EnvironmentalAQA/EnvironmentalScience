"""Turns a question part's marking points into a scheme that can be read a line at a time.

``scheme(p)`` returns a dict that both the website and the PDF mark schemes render:

    {
      "tag":    "Any 3 of 5",            # short chip: how the marks are shared out
      "rule":   "1 mark each for ...",   # one sentence of marking guidance
      "levels": False,                   # True = levels-of-response, points are indicative
      "points": [ {"marks": "1", "label": "", "main": "...",
                   "detail": ["..."],    # extra detail that belongs to the same mark
                   "alts":   ["..."]} ], # other routes to the same mark
      "accept": ["..."],                 # anything else that earns the mark
      "reject": ["..."],                 # answers that look right and earn nothing
      "note":   "...",                   # the convention that applies to every scheme
    }

Marking points are written as prose in the bank, often with several clauses.  The
first clause is the point an examiner looks for; clauses after a semicolon are
development or a second route to the same mark, so they are split out instead of
being left in one long line.  A clause that begins "accept"/"allow"/"credit" is
lifted into ``accept``, and "or"/"either"/"also" marks an alternative route.
``||`` can be used in a marking point to force an alternative split.
"""
import math
import re

from bank.accept import EQUIV, MISCONCEPTIONS

_ALT = re.compile(r"^(or|either|also)\b[,:]?\s+", re.I)
_ACC = re.compile(r"^(accept|allow|credit)\b[,:]?\s+", re.I)
_LABEL = re.compile(r"^([A-Z][^:<()]{1,44}):\s+(\S.*)$")
_NUMRE = re.compile(r"\b(one|two|three|four|five|six|1|2|3|4|5|6)\b", re.I)
_CMP = re.compile(r"\b(compare|compares|comparison|difference|differences|contrast|whereas)\b", re.I)
_EG = re.compile(r"(named example|named examples|give an example|give one example|name a |name one |name two |name three |named species|named country)", re.I)
_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
          "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6}

#: The convention that applies to every scheme on the site, shown under the points.
NOTE = ("Wording does not have to match: credit any answer that makes the same scientific "
        "point, however it is phrased.")

_STRIP = re.compile(r"<[^>]+>")


def _plain(s):
    return _STRIP.sub(" ", s)


def _trig(words):
    return re.compile("|".join(r"(?<!\w)" + re.escape(w) + r"(?!\w)" for w in words), re.I)


_EQUIV_RE = [(_trig(t), txt) for t, txt in EQUIV]
_MISC_RE = [(_trig(t), txt) for t, txt in MISCONCEPTIONS]


_ENT_END = re.compile(r"&#?\w+$")


def _segments(text):
    """Split a marking point on its semicolons, but not inside brackets or an HTML entity."""
    out, buf, depth = [], [], 0
    for i, c in enumerate(text):
        if c in "([":
            depth += 1
        elif c in ")]":
            depth = max(0, depth - 1)
        if (c == ";" and depth == 0 and i + 1 < len(text) and text[i + 1] == " "
                and not _ENT_END.search("".join(buf))):
            out.append("".join(buf).strip())
            buf = []
            continue
        buf.append(c)
    out.append("".join(buf).strip())
    return [x for x in out if x]


def _parse(text):
    """One marking point -> (label, main clause, development clauses, alternatives, accepts)."""
    text = text.strip()
    alts, accepts = [], []
    if "||" in text:
        bits = [b.strip() for b in text.split("||") if b.strip()]
        text, alts = bits[0], bits[1:]
    segs = _segments(text)
    main, detail = segs[0], []
    for s in segs[1:]:
        if _ACC.match(s):
            accepts.append(_ACC.sub("", s)[:1].upper() + _ACC.sub("", s)[1:])
        elif _ALT.match(s):
            alts.append(_ALT.sub("", s))
        else:
            detail.append(s)
    label = ""
    m = _LABEL.match(main)
    if m and len(m.group(1).split()) <= 5:
        label, main = m.group(1).strip(), m.group(2).strip()
    return label, main, detail, [_ALT.sub("", a) for a in alts], accepts


def _share(p, n, m):
    """(tag, rule, per-point mark label) - how the marks are shared between the points."""
    if p.mcq:
        return "Correct answer only", "1 mark for the correct option. No mark if more than one box is ticked.", "1"
    if p.calc:
        if n > 1:
            return ("Calculation", "A correct final answer scores full marks on its own. "
                    "If the answer is wrong, each correct step of working below earns its mark.", "1")
        return "Calculation", "1 mark for the correct answer; working does not have to be shown.", "1"
    if n == 0:
        return "", "", ""
    if n == m:
        if m == 1:
            return "", "1 mark for the point below.", "1"
        return "1 mark each", f"1 mark for each of the {m} points below.", "1"
    if n > m:
        return (f"Any {m} of {n}",
                f"1 mark each for any {m} of the {n} points below, in any order, maximum {m}.", "1")
    per = m / n
    if per == int(per):
        if n == 1:
            return (f"{m} marks", f"{m} marks for the point below; award fewer where it is only partly made.", str(m))
        return (f"{int(per)} marks per point",
                f"{int(per)} marks for each of the {n} points below; award 1 mark where a point is only "
                "partly made.", str(int(per)))
    return ("Marks shared",
            f"Up to {m} marks in total - share them between the {n} points below according to how "
            "completely each one is made.", f"up to {math.ceil(per)}")


def _auto_accept(p, n, m, blob):
    out = []
    if not p.mcq and not p.calc and n:
        out.append("Any other correct, relevant point of the same kind - wording never has to match these notes.")
    if p.level:
        out.append("Any accurate, relevant material that is not in the indicative content.")
    if p.calc:
        out.append("The correct answer however it is set out, including a different but valid method.")
        out.append("An answer carried forward from an earlier incorrect step (error carried forward).")
        out.append("An answer rounded to 2 or more significant figures, and the answer written as a fraction, "
                   "decimal or percentage where the question does not specify.")
    if _CMP.search(_plain(p.text)):
        out.append("The converse of any point, ie the same comparison written the other way round.")
    if _EG.search(_plain(p.text)):
        out.append("Any appropriate named example, including ones that are not listed here.")
    if p.unit:
        out.append(f"The value alone - the unit ({p.unit}) is already printed on the answer line.")
    hits, words = [], set()
    for rx, txt in _EQUIV_RE:
        mt = rx.search(blob)
        if mt and mt.group(0).strip().lower() not in words:
            words.add(mt.group(0).strip().lower())
            hits.append((mt.start(), f"<b>{mt.group(0).strip()}</b> &rarr; {txt}"))
    hits.sort(key=lambda h: h[0])       # the vocabulary of the question itself comes first
    return out, [t for _, t in hits[:3]]


def _auto_reject(p, n, m, blob):
    out = []
    mt = _NUMRE.search(_plain(p.text))
    if mt and n > 1 and _WORDS.get(mt.group(1).lower()) == m and m > 1:
        out.append(f"Points after the first {mt.group(1).lower()} - the question asks for {mt.group(1).lower()}, "
                   "so a list of extras cannot pick up the marks.")
    if p.calc:
        out.append("A bare wrong answer with no working.")
    mis = []
    for rx, txt in _MISC_RE:
        if rx.search(blob):
            mis.append(txt)
            if len(mis) == 2:
                break
    return out + mis


def scheme(p):
    m = p.marks
    blob = _plain(p.text + " " + " ".join(p.ms))

    # Parse first: a marking point written as "Or ..."/"Accept ..." is another route to the
    # mark before it, not a mark of its own, so it must not change how the marks are shared.
    points, accepts = [], []
    for x in p.ms:
        label, main, detail, alts, acc = _parse(x)
        accepts += acc
        lead = x.strip()
        if points and _ALT.match(lead):
            points[-1]["alts"] += [_ALT.sub("", main)] + alts
            points[-1]["detail"] += detail
            continue
        if points and _ACC.match(lead):
            accepts.append(_ACC.sub("", main))
            continue
        points.append({"marks": "", "label": label, "main": main, "detail": detail, "alts": alts})

    n = len(points)
    tag, rule, lab = _share(p, n, m)
    if p.ms_note:
        rule = p.ms_note
    if p.level:
        tag = "Levels of response"
        rule = ("Decide the level from the descriptors first, then use the indicative content to place the "
                "mark within that level. The points below are not a checklist.")
        lab = ""
    for pt in points:
        pt["marks"] = lab
    if p.mcq and points:
        letter = chr(65 + p.mcq.index(p.ms[0])) if p.ms[0] in p.mcq else ""
        points[0]["label"] = letter

    auto, wording = _auto_accept(p, n, m, blob)
    accept = accepts + list(getattr(p, "accept", []) or []) + auto + wording
    reject = list(getattr(p, "reject", []) or []) + _auto_reject(p, n, m, blob)
    out, seen = [], set()
    for a in accept:
        if a.lower() not in seen:
            seen.add(a.lower()); out.append(a)
    accept = out
    out, seen = [], set()
    for a in reject:
        if a.lower() not in seen:
            seen.add(a.lower()); out.append(a)
    note = "" if (p.mcq or p.calc) else NOTE
    return {"tag": tag, "rule": rule, "levels": bool(p.level), "points": points,
            "accept": accept, "reject": out, "note": note}


def indicative(items):
    """Indicative content (levels-of-response and essays) split the same way as marking points."""
    out = []
    for x in items:
        label, main, detail, alts, acc = _parse(x)
        out.append({"marks": "", "label": label, "main": main, "detail": detail + acc, "alts": alts})
    return out


def mark_points(p):
    """Older flat form: (rule, [(text, mark label), ...]).  Kept for any outside caller."""
    s = scheme(p)
    return s["rule"], [("; ".join([q["main"]] + q["detail"] + q["alts"]), q["marks"]) for q in s["points"]]
