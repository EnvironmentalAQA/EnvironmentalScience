"""Turns a question part's marking points into an explicit 'what earns each mark' scheme,
shared by the PDF mark schemes and the website.

Returns (rule, points) where rule is a short sentence and points is a list of
(text, marks_label) - the label is what an examiner would write next to the point."""
import math


def mark_points(p):
    n, m = len(p.ms), p.marks
    if p.mcq:
        return "Correct answer only.", [(x, "1") for x in p.ms]
    if p.level:
        return "Levels of response: decide the level from the descriptors, then use the indicative content to place the mark within the level.", [(x, "") for x in p.ms]
    if p.ms_note:
        rule = p.ms_note
    elif p.calc:
        rule = ("A correct final answer (with unit where asked) scores full marks. If the answer is wrong, award 1 mark for each correct step of working shown."
                if n > 1 else "1 mark for the correct answer.")
    elif n == m:
        rule = "1 mark for each point." if m > 1 else "1 mark."
    elif n > m:
        rule = f"Any {m} from the points below - 1 mark each, maximum {m}."
    else:
        per = m / n
        if per == int(per):
            rule = f"{int(per)} marks for each point (partial credit for a partly correct point)."
        else:
            rule = f"Up to {m} marks in total; award marks in proportion to the completeness of each point."
    if n == 0:
        return rule, []
    if n >= m:
        pts = [(x, "1") for x in p.ms]
    else:
        per = m / n
        lab = str(int(per)) if per == int(per) else f"up to {math.ceil(per)}"
        pts = [(x, lab) for x in p.ms]
    return rule, pts
