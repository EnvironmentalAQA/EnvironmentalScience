# AQA A-level Environmental Science (7447) — past-paper website

A self-contained, data-driven revision site: questions by topic (with AQA-format PDFs and
separate mark-scheme PDFs), generated full mock papers in exact AQA format, an essay bank,
and a page listing real AQA past papers.

**Open the site:** `site/index.html` (double-click; no server needed).

Every question cites the printed page numbers of the source textbook —
*R. Genn, Environmental Science A level AQA (Insight & Perspective, 2018)* — and the AQA
specification reference. Printed page = PDF page − 2 in the compressed PDF.

## Layout

```
build.py            rebuilds everything (site/ is output — never edit it by hand)
bank/official_index.py  which subtopic each question in the real AQA papers covers (edit when a new series is added)
bank/notes_*.py     revision notes per subtopic (sections under the book's headings with page refs, diagram specs, key numbers, exam pointers)
gen/diagrams.py     SVG diagram generators (flow / cycle / layers / chart) used by the notes
bank/exemplars.py   model answers (Level 3 vs weaker) for the 9-mark questions and two essays
bank/terms.py       key terms and definitions per subtopic for the definitions drill
bank/topics.py      the topic tree: Paper 1 / Paper 2 → topic → subtopic (slug, spec ref, book pages)
bank/p1_*.py        Paper 1 question bank (physical environment, energy, pollution)
bank/p2_*.py        Paper 2 question bank (living environment, biological resources, sustainability)
bank/rm_methods.py  research methods (examined in both papers)
gen/model.py        Q / P / Table / Chart / Essay data classes
gen/pdf.py          AQA-style PDF renderer (reportlab; uses Arial from C:\Windows\Fonts)
gen/papers.py       assembles 10-question / 95-mark mock papers + essay pair (120 marks)
gen/site.py         static HTML generator (PMT-style layout)
official-papers/    drop real AQA PDFs here (keep AQA names e.g. AQA-74471-QP-JUN23.PDF)
site/               OUTPUT: index.html, notes.html + notes/<slug>.html, topic/<topic>.html (hub per spec topic), subtopic/<slug>.html, paper/*.html,
                    quickfire.html, search.html, qdata.js (question data for those two), pdf/topic/*, pdf/papers/*
```

## Rebuild

```bash
python build.py               # 30 mock papers per paper (default) + all topic PDFs
python build.py --papers 60   # more mock papers
python build.py --no-pdf      # HTML only (fast, for checking new questions)
```

Requirements: Python 3.12 with `reportlab` (already installed with `python -m pip install reportlab`).

## Adding questions

Add a `Q(...)` to the `QUESTIONS` list in the relevant `bank/*.py` file (or create a new
file — any `bank/*.py` exporting `QUESTIONS` / `ESSAYS` is picked up automatically).

```python
Q("PEST-09", "pesticides", "3.4.3.2.8", "263-265",
  intro="Table 1 shows ...",                       # optional context
  figures=[Table([...header...], [[...rows...]]),  # or Chart("line"/"bar", x_label, y_label, {"series": [(x, y), ...]})
  parts=[
      P("Explain ...", 3, ms=["point 1", "point 2", "point 3", "extra point"]),   # >marks points = "Any 3 from"
      P("Calculate ...", 2, calc=True, unit="%", ms=["working", "answer"]),
      P("Give two ...", 2, items=2, ms=[...]),        # numbered answer slots
      P("Compare ...", 4, labels=["Advantage", "Disadvantage"], ms=[...]),
      P("Which ...? Tick one box.", 1, mcq=["A", "B", "C", "D"], ms=["B"]),
      P("Evaluate ...", 9, level=True, ms=[...indicative content...]),   # levels-of-response
  ])
```

Rules enforced by `build.py`:
- every question must total **5, 10 or 15 marks** (so mock papers always sum to 95 + 25 essay);
- ids must be unique; `topic` must be a slug from `bank/topics.py`; every part needs `ms`;
- a `level=True` part must be 9 marks.

Text supports `<b>`, `<i>`, `<sub>`, `<sup>`, HTML entities (`&deg;`, `&pound;`), and
shortcuts `CO_2` → CO₂ and `m^-3` → m⁻³.

Topic sets are split into PDFs of 8 questions each (`SET_SIZE` in build.py).
Mock papers rotate through the bank so each set is different; questions are reused
across sets deliberately (the assembler always spreads reuse as evenly as possible and
guarantees one 9-mark extended-response question per paper).

## Adding official past papers

Copy AQA PDFs into `official-papers/` using AQA's file names
(`AQA-74471-QP-JUN23.PDF`, `AQA-74471-W-MS-JUN23.PDF`, `AQA-74472-QP-JUN22.PDF` …) and rebuild.
They are grouped by series and paper on `site/official.html`.

## Site features (all state is kept in the browser's localStorage - no server needed)

- **Progress tracking** - every question has *Needs work* / *Secure* buttons; progress bars appear on the
  home page, topic hubs and subtopic pages, and the home page has an overall percentage and a reset button.
- **Filter bar** on subtopic pages: keyword, mark size (5/10/15), question type (calculation, data/figure,
  9-mark extended, multiple choice, complete-a-table) and your progress status; plus *Show all mark
  schemes*, *Print* and *Print + MS* (questions with mark schemes) buttons.
- **Search** (`search.html`) - full-text search of every question, figure and mark scheme; results link to
  the question on its subtopic page.
- **Quick-fire** (`quickfire.html`) - one random question at a time filtered by paper / topic / marks, skipping
  questions already marked secure. Keyboard: N or space = next, M = mark scheme, 1 = needs work, 2 = secure.
  Topic hub pages link straight into quick-fire for that topic (`quickfire.html?topic=pollution`).
- **Timed mock papers with self-marking** - *Sit online* on the mock-papers page gives a 3-hour countdown
  (pause / resume / reset, survives reloads) and a *Marks awarded* box under every mark-scheme part
  (essay: higher of the two counts). The score is saved per paper and shown in the *Your score* column.
- **Dark mode** toggle in the header (remembered) and a print stylesheet that hides navigation and tools.
- **Real AQA questions by topic** (`pastq.html`) - every question in the published AQA papers indexed by
  subtopic (`bank/official_index.py`), linking to the official PDF at the right page and to its mark scheme;
  each subtopic page also lists the real questions on that topic.
- **Revision planner** (`planner.html`) - exam countdown, subtopics sorted weakest-first with how often each
  has been examined, mock-paper score history and suggested next steps.
- **Explicit mark schemes** - every marking point shows the mark it earns and a rule line ("Any 3 from",
  "2 marks for each point", calculation rules); levels-of-response questions show the full level
  descriptor table (`gen/marking.py`, shared by the PDFs and the site).
- **Revision notes** (`notes.html`, `notes/<slug>.html`) - full notes for all 43 subtopics, each organised under the
  textbook's own headings with the printed pages to read alongside, redrawn diagrams, key numbers and a list of how
  the subtopic has been examined (linked to the real papers). Written in `bank/notes_*.py`.
- **Practice modes** (`practice.html` hub): **Write-first mode** (opt-in tick box on any question page -
  answer boxes appear, the mark scheme stays hidden until revealed, then you self-mark and your status is set);
  **Definitions drill** (`terms.html`, flashcards with spaced repetition and a Question-1-style table test,
  from `bank/terms.py`); **Calculations** (`calc.html`, generated questions with fresh numbers and worked
  solutions); **Model answers** for every 9-mark question and two essays (`bank/exemplars.py`, shown inside
  mark schemes online and in the MS PDFs); **Spaced repetition** - secure questions return in quick-fire after
  1, 3, 7, 14, 30 days and the planner shows what is due (`quickfire.html?due=1`).
- Quick-fire weights questions marked *needs work* three times more heavily; `quickfire.html?sub=<slug>`
  practises one subtopic. Copy-link button on every question; jump list on mock papers; back-to-top.

## Current contents

301 questions across all 43 spec subtopics (33 five-markers, 13 fifteen-markers), 31 essay titles,
40 mock papers per paper. Adding more 15-mark questions is the main lever for making the assembler
use the real AQA (2 x 15, 5 x 10, 3 x 5) pattern more often.
