"""Small SVG diagram generators for the revision notes.

Diagram specs are plain dicts so the notes files stay readable:
  {"type": "flow",   "title": ..., "nodes": [(id, label, col, row), ...], "edges": [(a, b, label), ...], "caption": ...}
  {"type": "cycle",  "title": ..., "nodes": [label, ...], "edges": [(i, j, label), ...] (indices, default = ring), "centre": "..."}
  {"type": "layers", "title": ..., "layers": [(label, note), ...] (bottom first), "side": "Altitude"}
  {"type": "chart",  ... same fields as gen.model.Chart ... }
Node ids in flow diagrams are short strings; labels may contain '\\n' for line breaks.
"""
import html, math
from .model import Chart

CW, CH = 200, 96          # grid cell size for flow diagrams
BW, BH = 164, 54          # box size
INK, MOSS, LEAF, EARTH, SAND = "#22302a", "#3f6b4a", "#7fb069", "#8b5e3c", "#f6f3ec"


def _text(x, y, label, size=12, anchor="middle", weight="normal", fill=INK):
    lines = label.split("\n")
    dy = -(len(lines) - 1) * size * 0.6
    out = [f'<text x="{x}" y="{y + dy:.1f}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}">']
    for i, ln in enumerate(lines):
        out.append(f'<tspan x="{x}" dy="{0 if i == 0 else size * 1.2:.1f}">{html.escape(ln)}</tspan>')
    out.append("</text>")
    return "".join(out)


def _wrap(title, body, w, h, caption):
    cap = f'<div class="dcap">{html.escape(caption)}</div>' if caption else ""
    return (f'<figure class="diag"><figcaption>{html.escape(title)}</figcaption>'
            f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Source Sans 3, Segoe UI, Arial, sans-serif">'
            '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10z" fill="{MOSS}"/></marker></defs>{body}</svg>{cap}</figure>')


def flow(spec):
    nodes = {n[0]: n for n in spec["nodes"]}
    cols = max(n[2] for n in spec["nodes"]) + 1
    rows = max(n[3] for n in spec["nodes"]) + 1
    W, H = cols * CW + 20, rows * CH + 20
    body = []
    pos = {}
    for nid, label, c, r in spec["nodes"]:
        x, y = 10 + c * CW + (CW - BW) / 2, 10 + r * CH + (CH - BH) / 2
        pos[nid] = (x + BW / 2, y + BH / 2)
        kind = spec.get("kinds", {}).get(nid, "box")
        fill = {"box": "#ffffff", "hi": "#e6f0dc", "warn": "#fff3d6", "plain": "none"}[kind]
        stroke = "none" if kind == "plain" else MOSS
        body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{BW}" height="{BH}" rx="9" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')
        body.append(_text(x + BW / 2, y + BH / 2 + 4, label, 12, weight="600" if kind == "hi" else "normal"))
    for e in spec.get("edges", []):
        a, b = e[0], e[1]
        lab = e[2] if len(e) > 2 else ""
        (x1, y1), (x2, y2) = pos[a], pos[b]
        dx, dy = x2 - x1, y2 - y1
        d = math.hypot(dx, dy) or 1
        ux, uy = dx / d, dy / d
        t = min(BW / 2 / abs(ux) if ux else 1e9, BH / 2 / abs(uy) if uy else 1e9) + 3
        sx, sy, ex, ey = x1 + ux * t, y1 + uy * t, x2 - ux * t, y2 - uy * t
        body.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{MOSS}" stroke-width="1.6" marker-end="url(#ah)"/>')
        if lab:
            mx, my = (sx + ex) / 2, (sy + ey) / 2
            body.append(f'<rect x="{mx - 4 - len(lab) * 3.1:.1f}" y="{my - 9:.1f}" width="{len(lab) * 6.2 + 8:.1f}" height="16" rx="4" fill="{SAND}"/>')
            body.append(_text(mx, my + 4, lab, 10.5, fill=EARTH))
    return _wrap(spec["title"], "".join(body), W, H, spec.get("caption", ""))


def cycle(spec):
    labels = spec["nodes"]
    n = len(labels)
    R = 150 if n <= 6 else 175
    W = H = 2 * R + 220
    cx, cy = W / 2, H / 2
    pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + R * math.cos(a), cy + R * math.sin(a)))
    body, labels_out = [], []
    edges = spec.get("edges") or [(i, (i + 1) % n, "") for i in range(n)]
    for e in edges:
        (x1, y1), (x2, y2) = pts[e[0]], pts[e[1]]
        lab = e[2] if len(e) > 2 else ""
        dx, dy = x2 - x1, y2 - y1
        d = math.hypot(dx, dy)
        ux, uy = dx / d, dy / d
        # leave / enter each box exactly at its edge (boxes are 164 x 52)
        t = min(82 / abs(ux) if ux else 1e9, 26 / abs(uy) if uy else 1e9) + 4
        sx, sy, ex, ey = x1 + ux * t, y1 + uy * t, x2 - ux * t, y2 - uy * t
        body.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{MOSS}" stroke-width="1.6" marker-end="url(#ah)"/>')
        if lab:
            mx, my = (sx + ex) / 2, (sy + ey) / 2
            # push the label outwards from the centre
            ox, oy = mx - cx, my - cy
            od = math.hypot(ox, oy) or 1
            mx, my = mx + ox / od * 16, my + oy / od * 16
            labels_out.append(f'<rect x="{mx - 4 - len(lab) * 3.1:.1f}" y="{my - 9:.1f}" width="{len(lab) * 6.2 + 8:.1f}" height="16" rx="4" fill="{SAND}" stroke="{MOSS}" stroke-width="0.6"/>')
            labels_out.append(_text(mx, my + 4, lab, 10.5, fill=EARTH))
    for (x, y), lab in zip(pts, labels):
        body.append(f'<rect x="{x - 82:.1f}" y="{y - 26:.1f}" width="164" height="52" rx="9" fill="#ffffff" stroke="{MOSS}" stroke-width="1.5"/>')
        body.append(_text(x, y + 4, lab, 12))
    body += labels_out
    if spec.get("centre"):
        body.append(_text(cx, cy + 4, spec["centre"], 13, weight="700", fill=MOSS))
    return _wrap(spec["title"], "".join(body), W, H, spec.get("caption", ""))


def layers(spec):
    ls = spec["layers"]
    W, LH = 560, 58
    H = len(ls) * LH + 30
    body = []
    for i, (lab, note) in enumerate(reversed(ls)):
        y = 10 + i * LH
        shade = ["#dbe8f3", "#e6f0dc", "#f3ecd8", "#fbe3d3", "#f6f3ec"][i % 5]
        body.append(f'<rect x="10" y="{y}" width="{W - 20}" height="{LH}" fill="{shade}" stroke="#ffffff" stroke-width="2"/>')
        body.append(_text(120, y + LH / 2 + 4, lab, 13, weight="700"))
        body.append(_text(360, y + LH / 2 + 4, note, 11))
    if spec.get("side"):
        body.append(f'<line x1="{W - 6}" y1="{H - 20}" x2="{W - 6}" y2="14" stroke="{EARTH}" stroke-width="1.5" marker-end="url(#ah)"/>')
        body.append(f'<text transform="translate({W - 12},{H / 2}) rotate(-90)" text-anchor="middle" font-size="10" fill="{EARTH}">{html.escape(spec["side"])}</text>')
    return _wrap(spec["title"], "".join(body), W, H, spec.get("caption", ""))


def render(spec, chart_fn):
    t = spec["type"]
    if t == "flow":
        return flow(spec)
    if t == "cycle":
        return cycle(spec)
    if t == "layers":
        return layers(spec)
    if t == "chart":
        ch = Chart(spec["kind"], spec["x_label"], spec["y_label"], spec["series"], y_min=spec.get("y_min"), y_max=spec.get("y_max"), categories=spec.get("categories"))
        cap = f'<div class="dcap">{html.escape(spec.get("caption", ""))}</div>' if spec.get("caption") else ""
        return f'<figure class="diag"><figcaption>{html.escape(spec["title"])}</figcaption>{chart_fn(ch, "")}{cap}</figure>'
    raise ValueError(t)
