"""Data model for the question bank.

Every question cites the pages of Genn, *Environmental Science A level AQA*
(Insight & Perspective, 2018) that it is drawn from, plus the AQA 7447 spec
reference.  Printed page numbers are used (PDF page = printed page + 2).
"""
from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class Table:
    """A data table shown in the question (Table 1, Table 2 ...)."""
    header: List[str]
    rows: List[List[str]]
    caption: str = ""          # e.g. "Table 1" (auto-numbered if blank)
    col_widths: Optional[List[float]] = None   # in cm, optional
    blank: bool = False        # True = it is an answer table the student fills in


@dataclass
class Chart:
    """A simple line or bar chart shown in the question (Figure 1 ...)."""
    kind: str                      # 'line' | 'bar'
    x_label: str
    y_label: str
    series: dict                   # {"label": [(x, y), ...]}  (bar: [(category, value), ...])
    caption: str = ""              # e.g. "Figure 1"
    categories: Optional[List[str]] = None   # for bar charts
    y_min: Optional[float] = None
    y_max: Optional[float] = None


@dataclass
class P:
    """One question part, e.g. 0 3 . 2"""
    text: str
    marks: int
    ms: List[str] = field(default_factory=list)   # marking points / indicative content
    lines: Optional[int] = None    # answer lines (auto if None)
    items: int = 0                 # numbered answer slots ("1 ....", "2 ....")
    labels: Optional[List[str]] = None   # labelled answer slots, e.g. ["Advantage", "Disadvantage"]
    calc: bool = False             # working space + answer box
    unit: str = ""                 # unit printed after the answer box
    level: bool = False            # 9-mark levels-of-response question
    essay: bool = False            # 25-mark essay
    table: Optional[Table] = None  # answer table to complete
    mcq: Optional[List[str]] = None   # multiple-choice options (tick one box)
    ms_note: str = ""              # e.g. "Accept converse", "Any 3 from"
    ao: str = ""                   # optional AO tag


@dataclass
class Q:
    id: str
    topic: str                     # subtopic slug (see bank/topics.py)
    spec: str                      # e.g. "3.4.3.2.8"
    pages: str                     # Genn printed pages, e.g. "262-266" or "89, 103-104"
    parts: List[P]
    intro: str = ""                # context / stem shown before the first part
    figures: List[Union[Table, Chart]] = field(default_factory=list)
    title: str = ""                # short label for the site listing

    @property
    def marks(self) -> int:
        return sum(p.marks for p in self.parts)

    @property
    def has_extended(self) -> bool:
        return any(p.level for p in self.parts)


@dataclass
class Essay:
    id: str
    paper: int                     # 1 or 2
    title: str                     # the essay question
    spec: str
    pages: str
    indicative: List[str]          # indicative content bullets
