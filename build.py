"""Build the whole site: topic question-set PDFs, mark schemes, mock papers and HTML.

Usage:  python build.py            (defaults: 30 mock papers per paper)
        python build.py --papers 50
        python build.py --no-pdf    (HTML only, fast)
"""
import argparse, importlib, os, pkgutil, re, shutil, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bank
from bank.topics import PAPERS, subtopic_index
from gen import pdf, site, papers as paper_gen
from gen.model import Q, Essay

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
SET_SIZE = 8   # questions per topic set PDF


def load_bank():
    questions, essays = [], []
    for m in pkgutil.iter_modules(bank.__path__):
        if m.name == "topics":
            continue
        mod = importlib.import_module(f"bank.{m.name}")
        questions += getattr(mod, "QUESTIONS", [])
        essays += getattr(mod, "ESSAYS", [])
    return questions, essays


def validate(questions, essays):
    idx = subtopic_index()
    ids = Counter(q.id for q in questions)
    errs = []
    for q in questions:
        if ids[q.id] > 1:
            errs.append(f"duplicate id {q.id}")
        if q.topic not in idx:
            errs.append(f"{q.id}: unknown topic '{q.topic}'")
        if q.marks not in (5, 10, 15):
            errs.append(f"{q.id}: total marks {q.marks} (must be 5, 10 or 15 to fit AQA paper structure)")
        for i, p in enumerate(q.parts, 1):
            if not p.ms:
                errs.append(f"{q.id} part {i}: no mark scheme")
            if p.level and p.marks != 9:
                errs.append(f"{q.id} part {i}: level-marked part must be 9 marks")
    eids = Counter(e.id for e in essays)
    for e in essays:
        if eids[e.id] > 1:
            errs.append(f"duplicate essay id {e.id}")
    if errs:
        print("VALIDATION ERRORS:")
        for e in errs:
            print("  -", e)
        sys.exit(1)


def official_files():
    out = []
    src = os.path.join(ROOT, "official-papers")
    for name in sorted(os.listdir(src)):
        if not name.lower().endswith(".pdf"):
            continue
        m = re.match(r"AQA-7447(\d)-(QP|MS|W-MS|ER|WRE|RE)-([A-Z]{3}\d{2})", name.upper())
        sp = re.match(r"AQA-7447(\d)-(SQP|SMS)", name.upper())
        kinds = {"QP": "Question paper", "MS": "Mark scheme", "W-MS": "Mark scheme", "ER": "Examiner report", "WRE": "Examiner report", "RE": "Examiner report",
                 "SQP": "Specimen question paper", "SMS": "Specimen mark scheme"}
        if m:
            paper, kind, series = f"Paper {m.group(1)}", kinds[m.group(2)], m.group(3)
        elif sp:   # specimen papers (AQA-74471-SQP-CR.PDF, AQA-74471-SMS.PDF)
            paper, kind, series = f"Paper {sp.group(1)}", kinds[sp.group(2)], "SPECIMEN"
        else:
            paper, kind, series = "Unknown", "Document", "Other"
        out.append({"name": name, "paper": paper, "kind": kind, "series": series})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", type=int, default=30, help="mock papers per paper")
    ap.add_argument("--no-pdf", action="store_true")
    args = ap.parse_args()

    questions, essays = load_bank()
    validate(questions, essays)
    idx = subtopic_index()
    print(f"Bank: {len(questions)} questions, {len(essays)} essays")

    for d in ("pdf/topic", "pdf/papers", "topic", "subtopic", "paper", "official"):
        os.makedirs(os.path.join(SITE, d), exist_ok=True)

    site.OFFICIAL_FILES = official_files()   # needed for the real-question links on subtopic pages

    # ---- topic sets ----
    by_sub = {}
    for q in questions:
        by_sub.setdefault(q.topic, []).append(q)
    sets_by_sub = {}
    for slug, qs in by_sub.items():
        qs = sorted(qs, key=lambda q: q.id)
        sets_by_sub[slug] = [qs[i:i + SET_SIZE] for i in range(0, len(qs), SET_SIZE)]
    for slug, sets in sets_by_sub.items():
        info = idx[slug]
        for k, s in enumerate(sets, 1):
            base = os.path.join(SITE, "pdf", "topic", f"{slug}-set{k}")
            code = f"ESP/{slug.upper()}/SET{k}"
            heading = f"Questions by topic: {info['name']} - Set {k}   ({sum(q.marks for q in s)} marks)"
            if not args.no_pdf:
                pdf.build_question_paper(base + "-QP.pdf", code, s, heading=heading)
                pdf.build_mark_scheme(base + "-MS.pdf", code, f"Questions by topic: {info['name']} - Set {k}", s,
                                      subtitle=f"AQA spec {info['spec']}; {info['topic']}; textbook pp. {info['pages']}")
        with open(os.path.join(SITE, "subtopic", f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(site.subtopic_page(slug, sets))
        print(f"  {slug}: {len(by_sub[slug])} questions in {len(sets)} set(s)")

    # ---- topic hub pages (one per spec topic) ----
    seen = {}
    for pno, paper in PAPERS.items():
        for t in paper["topics"]:
            seen.setdefault(t["slug"], (t, []))[1].append(pno)
    for slug, (t, pnos) in seen.items():
        with open(os.path.join(SITE, "topic", f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(site.topic_hub_page(t, pnos, sets_by_sub))

    # ---- mock papers ----
    generated = []
    used = Counter()
    for pno in (1, 2):
        for n in range(1, args.papers + 1):
            qs, pair = paper_gen.assemble_paper(pno, n, questions, essays, used)
            if len(qs) < 10:
                print(f"  ! Paper {pno} set {n}: only {len(qs)} questions available (bank too small)")
            fname = f"P{pno}-Set{n:02d}"
            g = {"paper": pno, "set": n, "questions": qs, "essays": pair, "file": fname}
            generated.append(g)
            base = os.path.join(SITE, "pdf", "papers", fname)
            code = f"ESP/7447/{pno}/SET{n:02d}"
            if not args.no_pdf:
                cover = {"paper": pno, "title": f"Paper {pno}  (Generated practice paper - Set {n:02d})",
                         "subtitle": f"Assessed: {PAPERS[pno]['assessed']}", "total": 120}
                pdf.build_question_paper(base + "-QP.pdf", code, qs, essays=pair, cover=cover)
                pdf.build_mark_scheme(base + "-MS.pdf", code, f"Paper {pno} - Generated practice paper Set {n:02d}", qs, essays=pair,
                                      subtitle="120 marks: Questions 1-10 (95 marks) plus one essay from Question 11 (25 marks).")
            with open(os.path.join(SITE, "paper", fname + ".html"), "w", encoding="utf-8") as f:
                f.write(site.paper_online_page(g))
        print(f"  Paper {pno}: {args.papers} mock papers")

    # ---- official papers ----
    files = official_files()
    for f in files:
        shutil.copy2(os.path.join(ROOT, "official-papers", f["name"]), os.path.join(SITE, "official", f["name"]))

    counts = {"questions": len(questions), "subtopics": len(sets_by_sub), "papers": len(generated), "official": len(files)}
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(site.index_page(sets_by_sub, counts))
    with open(os.path.join(SITE, "papers.html"), "w", encoding="utf-8") as f:
        f.write(site.papers_page(generated))
    with open(os.path.join(SITE, "essays.html"), "w", encoding="utf-8") as f:
        f.write(site.essays_page(essays))
    with open(os.path.join(SITE, "official.html"), "w", encoding="utf-8") as f:
        f.write(site.official_page(files))
    # question data for the quick-fire and search pages (plain JS so it works from file://)
    with open(os.path.join(SITE, "qdata.js"), "w", encoding="utf-8") as f:
        f.write(site.qdata_js(sets_by_sub))
    with open(os.path.join(SITE, "quickfire.html"), "w", encoding="utf-8") as f:
        f.write(site.quickfire_page())
    with open(os.path.join(SITE, "search.html"), "w", encoding="utf-8") as f:
        f.write(site.search_page())
    with open(os.path.join(SITE, "pastq.html"), "w", encoding="utf-8") as f:
        f.write(site.pastq_page())
    with open(os.path.join(SITE, "planner.html"), "w", encoding="utf-8") as f:
        f.write(site.planner_page(sets_by_sub, site.official_counts()))
    print(f"Done -> {os.path.join(SITE, 'index.html')}")


if __name__ == "__main__":
    main()
