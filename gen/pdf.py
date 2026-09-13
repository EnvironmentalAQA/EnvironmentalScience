"""AQA-style PDF renderer for question papers and mark schemes (reportlab)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, PageBreak, KeepTogether, Flowable, CondPageBreak)
from reportlab.graphics.shapes import Drawing, String, Line, Rect
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.widgets.markers import makeMarker
import re, html

from .marking import mark_points
from bank.exemplars import EXEMPLARS, ESSAY_EXEMPLARS
from .model import Q, P, Table as QTable, Chart, Essay
from bank.topics import BOOK

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
try:
    pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Italic", "C:/Windows/Fonts/ariali.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-BoldItalic", "C:/Windows/Fonts/arialbi.ttf"))
    addMapping("Arial", 0, 0, "Arial"); addMapping("Arial", 1, 0, "Arial-Bold")
    addMapping("Arial", 0, 1, "Arial-Italic"); addMapping("Arial", 1, 1, "Arial-BoldItalic")
    FONT, FONTB = "Arial", "Arial-Bold"
except Exception:
    FONT, FONTB = "Helvetica", "Helvetica-Bold"

SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def plain(s: str) -> str:
    """For canvas-drawn strings: CO_2 -> CO2 subscript, m^-3 -> superscript, strip tags."""
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"\s*([A-Za-z°%]+)\^-(\d+)", lambda m: "/" + m.group(1) + (m.group(2).translate(SUP) if m.group(2) != "1" else ""), s)
    s = re.sub(r"\^(\d+)", lambda m: m.group(1).translate(SUP), s)
    s = re.sub(r"_(\d+)", lambda m: m.group(1).translate(SUB), s)
    return s

PAGE_W, PAGE_H = A4
LM, RM, TM, BM = 2.0 * cm, 2.0 * cm, 1.8 * cm, 1.8 * cm
LINE_GAP = 0.85 * cm

# ---------- styles ----------
BASE = ParagraphStyle("base", fontName=FONT, fontSize=10.5, leading=14)
BOLD = ParagraphStyle("bold", parent=BASE, fontName=FONTB)
SMALL = ParagraphStyle("small", parent=BASE, fontSize=8.5, leading=11)
MARKS = ParagraphStyle("marks", parent=BASE, alignment=TA_RIGHT, fontName=FONTB)
CENTER = ParagraphStyle("center", parent=BASE, alignment=TA_CENTER)
TITLE = ParagraphStyle("title", parent=BASE, fontName=FONTB, fontSize=20, leading=24)
H1 = ParagraphStyle("h1", parent=BASE, fontName=FONTB, fontSize=14, leading=18, spaceAfter=6)
H2 = ParagraphStyle("h2", parent=BASE, fontName=FONTB, fontSize=11.5, leading=15)
CAP = ParagraphStyle("cap", parent=BASE, fontName=FONTB, alignment=TA_CENTER, spaceBefore=4, spaceAfter=4)
CELL = ParagraphStyle("cell", parent=BASE, fontSize=9.5, leading=12)
CELLB = ParagraphStyle("cellb", parent=CELL, fontName=FONTB)
MSCELL = ParagraphStyle("mscell", parent=BASE, fontSize=9.5, leading=12.5)


def esc(s: str) -> str:
    """Escape text for reportlab Paragraph but keep simple <b>/<i>/<sub>/<sup>/<br/> tags."""
    s = html.escape(s, quote=False)
    s = re.sub(r"&amp;(#?\w+);", r"&\1;", s)  # keep entities such as &deg; &pound;
    for tag in ("b", "i", "sub", "sup", "u"):
        s = s.replace(f"&lt;{tag}&gt;", f"<{tag}>").replace(f"&lt;/{tag}&gt;", f"</{tag}>")
    s = s.replace("&lt;br/&gt;", "<br/>").replace("&lt;br&gt;", "<br/>")
    # allow chemistry subscripts like CO2 -> CO<sub>2</sub> when written as CO_2
    s = re.sub(r"_(\d+)", r"<sub>\1</sub>", s)
    s = re.sub(r"\^(-?\d+)", r"<sup>\1</sup>", s)
    return s


# ---------- flowables ----------
class AnswerLines(Flowable):
    """Dotted answer lines, splittable across pages."""
    def __init__(self, n, width=None):
        super().__init__()
        self.n = n
        self.w = width

    def wrap(self, aw, ah):
        self.w = self.w or aw
        return self.w, self.n * LINE_GAP

    def split(self, aw, ah):
        fit = int(ah // LINE_GAP)
        if fit <= 0:
            return []
        if fit >= self.n:
            return [self]
        return [AnswerLines(fit, self.w), AnswerLines(self.n - fit, self.w)]

    def draw(self):
        c = self.canv
        c.saveState()
        c.setDash(1, 2)
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.black)
        for i in range(self.n):
            y = self.n * LINE_GAP - (i + 1) * LINE_GAP + 3
            c.line(0, y, self.w, y)
        c.restoreState()


class LabelledLines(Flowable):
    """'1 ......' / 'Advantage ......' answer slots."""
    def __init__(self, labels, lines_each=2):
        super().__init__()
        self.labels = labels
        self.le = lines_each

    def wrap(self, aw, ah):
        self.w = aw
        self.h = len(self.labels) * (self.le * LINE_GAP + 4)
        return aw, self.h

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFont(FONTB, 10.5)
        y = self.h
        for lab in self.labels:
            y -= LINE_GAP
            c.setDash()
            c.drawString(0, y + 3, lab)
            lw = c.stringWidth(lab, FONTB, 10.5) + 8
            c.setDash(1, 2)
            c.setLineWidth(0.5)
            c.line(lw, y + 3, self.w, y + 3)
            for i in range(self.le - 1):
                y -= LINE_GAP
                c.line(0, y + 3, self.w, y + 3)
            y -= 4
        c.restoreState()


class CalcSpace(Flowable):
    """Working space + boxed answer line with unit."""
    def __init__(self, unit="", lines=6):
        super().__init__()
        self.unit = unit
        self.n = lines

    def wrap(self, aw, ah):
        self.w = aw
        self.h = self.n * LINE_GAP + 1.2 * cm
        return aw, self.h

    def draw(self):
        c = self.canv
        c.saveState()
        # working space: blank
        y = 0.6 * cm
        c.setFont(FONTB, 10.5)
        label = "Answer"
        unit = self.unit
        uw = c.stringWidth(plain(unit), FONT, 10.5) + 6 if unit else 0
        bw = 4.2 * cm
        x0 = self.w - uw - bw
        c.drawString(x0 - c.stringWidth(label, FONTB, 10.5) - 8, y, label)
        c.setLineWidth(0.8)
        c.rect(x0, y - 4, bw, 0.8 * cm)
        if unit:
            c.setFont(FONT, 10.5)
            c.drawString(x0 + bw + 6, y, plain(unit))
        c.restoreState()


class MCQBoxes(Flowable):
    def __init__(self, options):
        super().__init__()
        self.options = options

    def wrap(self, aw, ah):
        self.w = aw
        self.h = len(self.options) * 0.75 * cm + 0.3 * cm
        return aw, self.h

    def draw(self):
        c = self.canv
        c.saveState()
        c.setFont(FONT, 10.5)
        y = self.h - 0.6 * cm
        for i, o in enumerate(self.options):
            c.drawString(0, y, f"{chr(65 + i)}   {plain(o)}")
            c.rect(self.w - 1.0 * cm, y - 2, 0.45 * cm, 0.45 * cm)
            y -= 0.75 * cm
        c.restoreState()


class TotalBox(Flowable):
    """Small boxed question total at the bottom-right of a question."""
    def __init__(self, total):
        super().__init__()
        self.total = total

    def wrap(self, aw, ah):
        self.w = aw
        return aw, 0.9 * cm

    def draw(self):
        c = self.canv
        c.saveState()
        c.setLineWidth(0.8)
        c.rect(self.w - 1.2 * cm, 0.1 * cm, 1.2 * cm, 0.7 * cm)
        c.setFont(FONTB, 10.5)
        c.drawCentredString(self.w - 0.6 * cm, 0.3 * cm, str(self.total))
        c.restoreState()


def qnum_cell(n, sub=None):
    """Boxed AQA-style question number: 0 1 . 2"""
    digits = list(f"{n:02d}")
    data = [digits + ([".", str(sub)] if sub is not None else [])]
    widths = [0.5 * cm] * len(data[0])
    t = Table(data, colWidths=widths, rowHeights=[0.55 * cm])
    style = [("FONT", (0, 0), (-1, -1), FONTB, 10.5),
             ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
             ("BOX", (0, 0), (0, 0), 0.8, colors.black), ("BOX", (1, 0), (1, 0), 0.8, colors.black),
             ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]
    if sub is not None:
        style.append(("BOX", (3, 0), (3, 0), 0.8, colors.black))
    t.setStyle(TableStyle(style))
    return t


def numbered_row(n, sub, content, avail_w):
    """[qnum | content flowables] table row"""
    nw = 2.6 * cm if sub is not None else 1.6 * cm
    t = Table([[qnum_cell(n, sub), content]], colWidths=[nw, avail_w - nw])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                           ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
    return t


# ---------- figures ----------
def render_table(tbl: QTable, avail_w, caption):
    data = [[Paragraph(esc(h), CELLB) for h in tbl.header]]
    for r in tbl.rows:
        data.append([Paragraph(esc(str(c)), CELL) for c in r])
    ncol = len(tbl.header)
    if tbl.col_widths:
        cw = [w * cm for w in tbl.col_widths]
    else:
        cw = [min(avail_w, 15 * cm) / ncol] * ncol
    t = Table(data, colWidths=cw, hAlign="CENTER", repeatRows=1)
    st = [("GRID", (0, 0), (-1, -1), 0.6, colors.black), ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (-1, -1), "CENTER")]
    if tbl.blank:
        st.append(("ROWHEIGHTS", (0, 1), (-1, -1), 0.9 * cm))
        t = Table(data, colWidths=cw, hAlign="CENTER", rowHeights=[None] + [0.9 * cm] * len(tbl.rows))
    t.setStyle(TableStyle(st))
    return [Paragraph(esc(caption), CAP), t, Spacer(1, 6)]


def render_chart(ch: Chart, avail_w, caption):
    w, h = min(avail_w, 15 * cm), 8.5 * cm
    d = Drawing(w, h)
    labels = list(ch.series.keys())
    if ch.kind == "bar":
        bc = VerticalBarChart()
        bc.x, bc.y, bc.width, bc.height = 55, 45, w - 90, h - 75
        bc.data = [[v for _, v in ch.series[k]] for k in labels]
        cats = ch.categories or [str(x) for x, _ in ch.series[labels[0]]]
        bc.categoryAxis.categoryNames = [plain(c) for c in cats]
        bc.categoryAxis.labels.fontName = FONT
        bc.valueAxis.labels.fontName = FONT
        bc.categoryAxis.labels.fontSize = 8
        bc.valueAxis.labels.fontSize = 8
        if ch.y_min is not None: bc.valueAxis.valueMin = ch.y_min
        if ch.y_max is not None: bc.valueAxis.valueMax = ch.y_max
        bc.groupSpacing = 8
        palette = [colors.HexColor("#4a6fa5"), colors.HexColor("#a5c16b"), colors.HexColor("#d98c3f"), colors.grey]
        for i in range(len(labels)):
            bc.bars[i].fillColor = palette[i % len(palette)]
        d.add(bc)
        plot = bc
    else:
        lp = LinePlot()
        lp.x, lp.y, lp.width, lp.height = 55, 45, w - 90, h - 75
        lp.data = [ch.series[k] for k in labels]
        lp.xValueAxis.labels.fontSize = 8
        lp.xValueAxis.labels.fontName = FONT
        lp.yValueAxis.labels.fontName = FONT
        lp.yValueAxis.labels.fontSize = 8
        if ch.y_min is not None: lp.yValueAxis.valueMin = ch.y_min
        if ch.y_max is not None: lp.yValueAxis.valueMax = ch.y_max
        lp.joinedLines = 1
        markers = ["FilledCircle", "FilledSquare", "FilledTriangle", "FilledDiamond"]
        for i in range(len(labels)):
            lp.lines[i].strokeWidth = 1.4
            lp.lines[i].strokeColor = colors.black if i == 0 else [colors.HexColor("#4a6fa5"), colors.HexColor("#8a8a8a"), colors.HexColor("#d98c3f")][(i - 1) % 3]
            lp.lines[i].symbol = makeMarker(markers[i % 4])
            lp.lines[i].symbol.size = 4
        d.add(lp)
        plot = lp
    # axis labels
    d.add(String(w / 2, 8, plain(ch.x_label), fontName=FONT, fontSize=9, textAnchor="middle"))
    ylab = String(0, 0, plain(ch.y_label), fontName=FONT, fontSize=9, textAnchor="middle")
    from reportlab.graphics.shapes import Group
    g = Group(ylab)
    g.translate(12, h / 2)
    g.rotate(90)
    d.add(g)
    if len(labels) > 1:
        lg = Legend()
        lg.x, lg.y = w - 30, h - 10
        lg.alignment = "right"
        lg.fontSize = 8
        lg.fontName = FONT
        lg.columnMaximum = 4
        if ch.kind == "bar":
            lg.colorNamePairs = [(plot.bars[i].fillColor, plain(labels[i])) for i in range(len(labels))]
        else:
            lg.colorNamePairs = [(plot.lines[i].strokeColor, plain(labels[i])) for i in range(len(labels))]
        d.add(lg)
    return [Paragraph(esc(caption), CAP), d, Spacer(1, 6)]


# ---------- question rendering ----------
def auto_lines(p: P):
    if p.lines is not None:
        return p.lines
    if p.essay:
        return 0
    if p.level:
        return 30
    if p.marks <= 1:
        return 2
    if p.marks <= 2:
        return 4
    if p.marks <= 4:
        return p.marks * 2 + 1
    return min(p.marks * 2 + 2, 20)


def question_flowables(qn, q: Q, avail_w, fig_counter, tab_counter):
    """Return flowables for one whole question (AQA style)."""
    out = []
    first = []
    if q.intro:
        first.append(Paragraph(esc(q.intro), BASE))
    for f in q.figures:
        if isinstance(f, QTable):
            tab_counter[0] += 1
            cap = f.caption or f"Table {tab_counter[0]}"
            first.extend(render_table(f, avail_w - 1.6 * cm, cap))
        else:
            fig_counter[0] += 1
            cap = f.caption or f"Figure {fig_counter[0]}"
            first.extend(render_chart(f, avail_w - 1.6 * cm, cap))
    if first:
        out.append(numbered_row(qn, None, first, avail_w))
        out.append(Spacer(1, 6))
    single = len(q.parts) == 1
    for i, p in enumerate(q.parts, 1):
        content = [Paragraph(esc(p.text), BASE)]
        content.append(Paragraph(f"[{p.marks} mark{'s' if p.marks != 1 else ''}]", MARKS))
        if p.table:
            tab_counter[0] += 1
            cap = p.table.caption or f"Table {tab_counter[0]}"
            content.extend(render_table(p.table, avail_w - 3 * cm, cap))
        if p.mcq:
            content.append(MCQBoxes(p.mcq))
        sub = None if (single and not q.intro and not q.figures) else i
        out.append(numbered_row(qn, sub, content, avail_w))
        # answer space (outside the numbered row so it can split across pages)
        after = []
        if p.mcq:
            pass
        elif p.calc:
            after.append(CalcSpace(p.unit, lines=max(4, p.marks * 2)))
        elif p.labels:
            after.append(LabelledLines(p.labels, lines_each=max(1, (auto_lines(p)) // len(p.labels))))
        elif p.items:
            after.append(LabelledLines([str(k) for k in range(1, p.items + 1)], lines_each=max(1, auto_lines(p) // p.items)))
        elif p.essay:
            pass
        else:
            n = auto_lines(p)
            if n:
                after.append(AnswerLines(n))
        if p.level:
            after.append(Paragraph("Extra space", SMALL))
            after.append(AnswerLines(12))
        out.extend(after)
        out.append(Spacer(1, 8))
    out.append(TotalBox(q.marks))
    out.append(Spacer(1, 10))
    return out


def essay_flowables(qn, pair, avail_w):
    out = [Paragraph("Write an essay on <b>one</b> of the following topics.", BOLD), Spacer(1, 10)]
    for k, e in enumerate(pair, 1):
        content = [Paragraph(esc(e.title), BASE), Paragraph("[25 marks]", MARKS)]
        out.append(numbered_row(qn, k, content, avail_w))
        if k == 1:
            out.append(Paragraph("<b>OR</b>", BASE))
            out.append(Spacer(1, 6))
    out.append(Spacer(1, 6))
    out.append(Paragraph("Indicate which question you have answered by writing its number, "
                         f"<b>{qn} . 1</b> or <b>{qn} . 2</b>, at the top of your answer.", SMALL))
    out.append(Spacer(1, 6))
    out.append(AnswerLines(120))
    out.append(Paragraph("<b>END OF QUESTIONS</b>", CENTER))
    return out


# ---------- documents ----------
class AQADoc(BaseDocTemplate):
    def __init__(self, path, code, **kw):
        super().__init__(path, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM, **kw)
        self.code = code
        frame = Frame(LM + 0.4 * cm, BM + 0.6 * cm, PAGE_W - LM - RM - 1.6 * cm, PAGE_H - TM - BM - 1.2 * cm,
                      id="main", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=self._decorate)])

    def _decorate(self, canv, doc):
        canv.saveState()
        canv.setLineWidth(0.6)
        canv.rect(LM, BM + 0.3 * cm, PAGE_W - LM - RM - 0.9 * cm, PAGE_H - TM - BM - 0.3 * cm)
        canv.setFont(FONT, 7.5)
        canv.saveState()
        canv.translate(PAGE_W - RM + 0.1 * cm, PAGE_H - TM - 0.5 * cm)
        canv.rotate(-90)
        canv.drawString(0, 0, "Do not write outside the box")
        canv.restoreState()
        canv.setFont(FONT, 8)
        canv.drawCentredString(PAGE_W / 2, BM - 0.2 * cm, str(doc.page))
        canv.drawRightString(PAGE_W - RM, BM - 0.2 * cm, self.code)
        canv.restoreState()


def cover_page(paper_no, title, subtitle, total, questions, essay=True):
    """AQA-style front page."""
    st = []
    st.append(Paragraph("A-level", ParagraphStyle("al", parent=BASE, fontSize=13)))
    st.append(Paragraph("<b>ENVIRONMENTAL SCIENCE</b>", TITLE))
    st.append(Paragraph(f"<b>{title}</b>", ParagraphStyle("pp", parent=BASE, fontSize=14, leading=18)))
    st.append(Spacer(1, 4))
    st.append(Paragraph(subtitle, BASE))
    st.append(Spacer(1, 10))
    st.append(Paragraph("<b>Time allowed: 3 hours</b>" if total == 120 else f"<b>Suggested time: {int(total * 1.5)} minutes</b>", BASE))
    st.append(Spacer(1, 12))
    # examiner's use table
    rows = [["Question", "Mark"]] + [[str(i), ""] for i in range(1, len(questions) + (2 if essay else 1))] + [["TOTAL", ""]]
    ex = Table(rows, colWidths=[2.2 * cm, 1.6 * cm], rowHeights=0.5 * cm)
    ex.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.black), ("FONT", (0, 0), (-1, -1), FONT, 8),
                            ("FONT", (0, 0), (-1, 0), FONTB, 8), ("ALIGN", (0, 0), (-1, -1), "CENTER")]))
    instr = [
        Paragraph("<b>Materials</b>", BASE),
        Paragraph("For this paper you may use:<br/>&nbsp;&nbsp;&bull; a calculator.", BASE), Spacer(1, 8),
        Paragraph("<b>Instructions</b>", BASE),
        Paragraph("&bull; Use black ink or black ball-point pen. Pencil should only be used for drawing.<br/>"
                  "&bull; Fill in the boxes at the top of this page.<br/>"
                  + (f"&bull; Answer <b>all</b> questions 1 to {len(questions)} and <b>one</b> essay from question {len(questions) + 1}.<br/>" if essay
                     else "&bull; Answer <b>all</b> questions.<br/>")
                  + "&bull; You must answer the questions in the spaces provided. Do not write outside the box around each page or on blank pages.<br/>"
                  "&bull; Do all rough work in this book. Cross through any work you do not want to be marked.", BASE), Spacer(1, 8),
        Paragraph("<b>Information</b>", BASE),
        Paragraph("&bull; The marks for questions are shown in brackets.<br/>"
                  f"&bull; The maximum mark for this paper is {total}.<br/>"
                  "&bull; All questions should be answered in continuous prose.<br/>"
                  "&bull; You will be assessed on your ability to:<br/>&nbsp;&nbsp;&nbsp;&nbsp;- use good English<br/>&nbsp;&nbsp;&nbsp;&nbsp;- organise information clearly<br/>&nbsp;&nbsp;&nbsp;&nbsp;- use specialist vocabulary where appropriate.", BASE),
    ]
    body = Table([[instr, [Paragraph("<b>For Examiner's Use</b>", SMALL), ex]]], colWidths=[11.5 * cm, 4.5 * cm])
    body.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    name_box = Table([["Please write clearly in block capitals.", "Centre number", "", "Candidate number", ""],
                      ["Surname", "", "", "", ""], ["Forename(s)", "", "", "", ""]],
                     colWidths=[5.2 * cm, 2.8 * cm, 2.2 * cm, 3.2 * cm, 2.6 * cm], rowHeights=0.7 * cm)
    name_box.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), FONT, 8), ("BOX", (2, 0), (2, 0), 0.5, colors.black),
                                  ("BOX", (4, 0), (4, 0), 0.5, colors.black), ("LINEBELOW", (1, 1), (-1, 1), 0.5, colors.black),
                                  ("LINEBELOW", (1, 2), (-1, 2), 0.5, colors.black), ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    return [name_box, Spacer(1, 10)] + st + [body, PageBreak()]


def build_question_paper(path, code, questions, essays=None, cover=None, heading=None):
    """questions: list[Q]; essays: (Essay, Essay) or None; cover: dict for cover page"""
    doc = AQADoc(path, code)
    avail_w = PAGE_W - LM - RM - 1.6 * cm
    story = []
    if cover:
        story += cover_page(cover.get("paper"), cover["title"], cover["subtitle"], cover["total"], questions, essay=bool(essays))
    if heading:
        story.append(Paragraph(esc(heading), H1))
        story.append(Spacer(1, 4))
    story.append(Paragraph("Answer <b>all</b> questions in the spaces provided.", BOLD))
    story.append(Spacer(1, 10))
    for i, q in enumerate(questions, 1):
        story.append(CondPageBreak(6 * cm))
        # figures / tables are numbered within each question (question texts refer to "Table 1", "Figure 1")
        story += question_flowables(i, q, avail_w, [0], [0])
    if essays:
        story.append(PageBreak())
        story += essay_flowables(len(questions) + 1, essays, avail_w)
    else:
        story.append(Paragraph("<b>END OF QUESTIONS</b>", CENTER))
    doc.build(story)


# ---------- mark scheme ----------
LEVELS_9 = [
    ("Level 3", "7-9", "Answer is comprehensive, relevant and logically structured. Shows detailed knowledge and understanding of the relevant scientific ideas and applies them accurately to the context. Evaluation/analysis is well supported by evidence and a clear judgement or conclusion is reached."),
    ("Level 2", "4-6", "Answer is mostly relevant and shows some structure. Knowledge and understanding of relevant ideas is sound but application to the context or evaluation may be incomplete or lack detail. A judgement may be made but is not fully supported."),
    ("Level 1", "1-3", "Answer is basic, with limited structure. Some relevant knowledge is shown but there are omissions or errors. Little application to the context and little or no evaluation."),
    ("", "0", "No relevant content."),
]
LEVELS_25 = [
    ("Level 5", "21-25", "Comprehensive and detailed knowledge and understanding drawn from across the specification, applied accurately to the question. Argument is coherent, well-structured and supported by a wide range of relevant, well-chosen examples and quantitative detail where appropriate. Interconnections between topics are made explicitly and a clear, justified conclusion is reached."),
    ("Level 4", "16-20", "Detailed knowledge and understanding with good application to the question. Argument is logically organised with relevant examples; some links between different areas of the specification are made. Conclusions are drawn but may be less fully justified."),
    ("Level 3", "11-15", "Sound knowledge and understanding, mostly applied to the question. Some structure and relevant examples, but coverage may be uneven or descriptive rather than analytical. Limited linking of topics."),
    ("Level 2", "6-10", "Basic knowledge and understanding with partial relevance. Answer is largely descriptive with few examples and limited structure; some errors or omissions."),
    ("Level 1", "1-5", "Limited, fragmented knowledge with little relevance to the question. Little structure; examples absent or inappropriate."),
    ("", "0", "No relevant content."),
]


def _html_paras(h, style):
    """Very small HTML -> Paragraph list: split on <p>, keep inline tags reportlab understands."""
    import re as _re
    out = []
    for part in _re.split(r"</?p>", h):
        part = part.strip()
        if part:
            part = _re.sub(r"</?(?!b|i|sub|sup|br)\w+[^>]*>", "", part)
            out.append(Paragraph(part, style))
    return out


def exemplar_flowables(ex):
    body = [Paragraph(f"<b>Model answer - {esc(ex['top_level'])}</b>", MSCELL)]
    body += _html_paras(ex["top"], MSCELL)
    if ex.get("low"):
        body.append(Spacer(1, 3))
        body.append(Paragraph(f"<b>Weaker answer - {esc(ex['low_level'])}</b>", MSCELL))
        body += _html_paras(ex["low"], MSCELL)
    body.append(Spacer(1, 3))
    body.append(Paragraph("<b>What makes the difference</b>", MSCELL))
    for n in ex["notes"]:
        body += _html_paras("<p>&bull; " + n + "</p>", MSCELL)
    return body


def ms_rows(qn, q: Q):
    rows = []
    single = len(q.parts) == 1 and not q.intro and not q.figures
    for i, p in enumerate(q.parts, 1):
        label = f"{qn:02d}" if single else f"{qn:02d}.{i}"
        body = []
        if p.level:
            body.append(Paragraph("<b>Levels of response</b>", MSCELL))
            for lv, rng, desc in LEVELS_9:
                body.append(Paragraph(f"<b>{lv} ({rng} marks)</b>: {esc(desc)}" if lv else f"<b>{rng} marks</b>: {esc(desc)}", MSCELL))
            body.append(Spacer(1, 4))
            body.append(Paragraph("<b>Indicative content</b> (credit other relevant, accurate points)", MSCELL))
            for m in p.ms:
                body.append(Paragraph("&bull; " + esc(m), MSCELL))
        else:
            rule, pts = mark_points(p)
            body.append(Paragraph(f"<i>{esc(rule)}</i>", MSCELL))
            for m, lab in pts:
                body.append(Paragraph("&bull; " + esc(m) + (f"  <b>({lab})</b>" if lab else ""), MSCELL))
        rows.append([Paragraph(label, CELLB), body, Paragraph(str(p.marks), CELL)])
        if p.level and q.id in EXEMPLARS:
            rows += exemplar_rows(EXEMPLARS[q.id])
    src = f"<b>Source:</b> {esc(BOOK)}, pp. {esc(q.pages)}; AQA spec {esc(q.spec)}."
    rows.append([Paragraph("", CELL), Paragraph(src, SMALL), Paragraph("", CELL)])
    return rows


def essay_ms_rows(qn, pair):
    rows = []
    for k, e in enumerate(pair, 1):
        body = [Paragraph(f"<b>{esc(e.title)}</b>", MSCELL), Spacer(1, 4), Paragraph("<b>Levels of response</b>", MSCELL)]
        for lv, rng, desc in LEVELS_25:
            body.append(Paragraph(f"<b>{lv} ({rng} marks)</b>: {esc(desc)}" if lv else f"<b>{rng} marks</b>: {esc(desc)}", MSCELL))
        body.append(Spacer(1, 4))
        body.append(Paragraph("<b>Indicative content</b> (students are not expected to cover all of these; credit other relevant material)", MSCELL))
        for m in e.indicative:
            body.append(Paragraph("&bull; " + esc(m), MSCELL))
        body.append(Paragraph(f"<b>Source:</b> {esc(BOOK)}, pp. {esc(e.pages)}; AQA spec {esc(e.spec)}.", SMALL))
        rows.append([Paragraph(f"{qn:02d}.{k}", CELLB), body, Paragraph("25", CELL)])
        if e.id in ESSAY_EXEMPLARS:
            rows += exemplar_rows(ESSAY_EXEMPLARS[e.id])
    return rows


def exemplar_rows(ex):
    """One table row per paragraph so the (long) model answer can break across pages."""
    return [[Paragraph("", CELL), [f], Paragraph("", CELL)] for f in exemplar_flowables(ex) if not isinstance(f, Spacer)]


def build_mark_scheme(path, code, title, questions, essays=None, subtitle=""):
    doc = AQADoc(path, code)
    avail_w = PAGE_W - LM - RM - 1.6 * cm
    story = [Paragraph("A-level", BASE), Paragraph("<b>ENVIRONMENTAL SCIENCE</b>", TITLE),
             Paragraph(f"<b>{esc(title)}</b>", H1), Paragraph("Mark scheme", H1)]
    if subtitle:
        story.append(Paragraph(esc(subtitle), BASE))
    story += [Spacer(1, 10), Paragraph("<b>Marking guidance</b>", H2),
              Paragraph("&bull; The number in brackets after each marking point is the mark it earns; the note above the points says how many are needed.<br/>"
                        "&bull; Where a question asks for a fixed number of points (eg <i>two</i> reasons), credit only the first points given.<br/>"
                        "&bull; Alternative correct wording and other relevant, accurate points are credited.<br/>"
                        "&bull; For levels-of-response questions, first determine the level using the descriptors, then position the mark within the level using the indicative content.<br/>"
                        "&bull; Calculations: credit correct working (method marks) even if the final answer is wrong; incorrect answers with no working score 0.", BASE),
              Spacer(1, 6),
              Paragraph(f"<b>Textbook references:</b> every question below cites the printed page numbers in {esc(BOOK)} from which the content is drawn, "
                        "together with the AQA 7447 specification reference.", SMALL), Spacer(1, 12)]
    rows = [[Paragraph("<b>Question</b>", CELLB), Paragraph("<b>Marking guidance</b>", CELLB), Paragraph("<b>Marks</b>", CELLB)]]
    for i, q in enumerate(questions, 1):
        rows += ms_rows(i, q)
    if essays:
        rows += essay_ms_rows(len(questions) + 1, essays)
    t = Table(rows, colWidths=[2.3 * cm, avail_w - 3.9 * cm, 1.6 * cm], repeatRows=1)
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, colors.black), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke)]))
    story.append(t)
    doc.build(story)
