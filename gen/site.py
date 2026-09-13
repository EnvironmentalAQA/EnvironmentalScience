"""Static site generator - environmental palette, topic hub pages, subtopic pages,
progress tracking, filtering / search, timed self-marked mock papers, dark mode,
print styles and a quick-fire random-question mode.  All state lives in the browser's
localStorage so the site still works as plain files with no server."""
import os, re, html, json
from bank.topics import PAPERS, subtopic_index, BOOK
from .model import Table as QTable, Chart
from .pdf import plain, LEVELS_9, LEVELS_25
from .marking import mark_points
from bank.official_index import OFFICIAL_INDEX
from bank.exemplars import EXEMPLARS, ESSAY_EXEMPLARS
from bank.terms import TERMS

EXAM_SECONDS = 3 * 60 * 60   # AQA 7447: each paper is 3 hours

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Source+Sans+3:wght@400;600;700&display=swap');
:root{--forest:#1f3d2b;--moss:#3f6b4a;--leaf:#7fb069;--leaf-light:#e6f0dc;--sand:#f6f3ec;--sand-dark:#ece6d8;--earth:#8b5e3c;--stone:#5c6660;--ink:#22302a;--line:#dcd6c8;
--p1:#2f5f73;--p1-light:#e2edf2;--p2:#3f6b4a;--p2-light:#e6f0dc;--card:#ffffff;--head:#1f3d2b;--ms-bg:#e6f0dc;--ms-line:#cfe0bf;--note-bg:#fff8e6;--note-line:#ecd9a3;--input:#fff;
--ok:#3f8f5a;--warn:#d9a441;--bad:#c0554a}
[data-theme=dark]{--forest:#0f1a13;--moss:#8fc17f;--leaf:#7fb069;--leaf-light:#22301f;--sand:#131a15;--sand-dark:#1c2620;--earth:#d6a878;--stone:#a6b0a8;--ink:#e4e8e2;--line:#2c3a31;
--p1-light:#1c3140;--p2-light:#22301f;--card:#192219;--head:#dfe9d9;--ms-bg:#1f2d21;--ms-line:#33513a;--note-bg:#2b2716;--note-line:#5a4c22;--input:#0f1611}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:'Source Sans 3',Segoe UI,Arial,sans-serif;font-size:17px;color:var(--ink);background:var(--sand);line-height:1.55}
h1,h2,h3,.brand{font-family:Fraunces,Georgia,'Times New Roman',serif;font-weight:700;letter-spacing:-.01em}
a{color:var(--moss)}code{background:var(--sand-dark);padding:1px 5px;border-radius:4px;font-size:.9em}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
header.top{background:var(--forest);color:#fff;position:sticky;top:0;z-index:20;box-shadow:0 2px 12px rgba(0,0,0,.18)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;min-height:62px}
header.top a{color:#fff;text-decoration:none}.brand{font-size:1.25rem;display:flex;align-items:center;gap:10px}.brand svg{width:30px;height:30px}
header.top nav{display:flex;align-items:center;flex-wrap:wrap}header.top nav a{margin-left:18px;font-size:.96rem;opacity:.9;padding:6px 0;border-bottom:2px solid transparent}header.top nav a:hover,header.top nav a.on{opacity:1;border-color:var(--leaf)}
button.icon-btn{margin-left:18px;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:8px;padding:5px 10px;cursor:pointer;font-size:.9rem;font-family:inherit}button.icon-btn:hover{background:rgba(255,255,255,.22)}
.hero{position:relative;overflow:hidden;background:linear-gradient(135deg,#1f3d2b 0%,#2f5a3f 55%,#3f6b4a 100%);color:#fff;padding:54px 0 48px}
.hero:before{content:"";position:absolute;inset:0;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400' viewBox='0 0 400 400'><g fill='none' stroke='rgba(255,255,255,0.10)' stroke-width='1.2'><path d='M0 300c60-40 120-40 180 0s120 40 220 0'/><path d='M0 240c60-40 120-40 180 0s120 40 220 0'/><path d='M0 180c60-40 120-40 180 0s120 40 220 0'/><path d='M0 120c60-40 120-40 180 0s120 40 220 0'/><path d='M0 60c60-40 120-40 180 0s120 40 220 0'/><path d='M0 360c60-40 120-40 180 0s120 40 220 0'/></g></svg>");opacity:.9}
.hero .wrap{position:relative}.hero h1{margin:0 0 10px;font-size:2.4rem;line-height:1.15}.hero p{margin:0;max-width:760px;color:rgba(255,255,255,.88);font-size:1.08rem}
.hero .crumbs{font-size:.9rem;margin-bottom:14px;color:rgba(255,255,255,.75)}.hero .crumbs a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.4)}.hero .crumbs span{margin:0 8px;opacity:.6}
.hero.p1{background:linear-gradient(135deg,#1e3f4d 0%,#2f5f73 60%,#3e7a90 100%)}.hero.p2{background:linear-gradient(135deg,#1f3d2b 0%,#3f6b4a 60%,#5e8f5a 100%)}
.hero.small{padding:34px 0 30px}.hero.small h1{font-size:1.9rem}
.pill{display:inline-block;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.35);border-radius:999px;padding:3px 12px;font-size:.82rem;margin-right:8px;margin-top:10px}
main{padding:30px 0 40px}
h2.sec{font-size:1.55rem;color:var(--head);margin:34px 0 14px;display:flex;align-items:center;gap:12px}h2.sec:after{content:"";flex:1;height:1px;background:var(--line)}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}@media(max-width:860px){.grid3{grid-template-columns:1fr}}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}@media(max-width:900px){.grid4{grid-template-columns:1fr 1fr}}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 24px;box-shadow:0 1px 3px rgba(31,61,43,.06)}
.card h3{margin:0 0 8px;font-size:1.25rem;color:var(--head)}.card p{margin:0 0 10px;color:var(--stone)}
.stat{font-family:Fraunces,serif;font-size:2.2rem;color:var(--moss);line-height:1}
a.btn,button.btn{display:inline-block;background:var(--moss);color:#fff;text-decoration:none;padding:9px 16px;border-radius:8px;font-weight:600;font-size:.95rem;border:0;cursor:pointer;font-family:inherit}a.btn:hover,button.btn:hover{background:var(--forest)}
[data-theme=dark] a.btn:hover,[data-theme=dark] button.btn:hover{background:#6fa562}
a.btn.ghost,button.btn.ghost{background:transparent;color:var(--moss);border:1.5px solid var(--moss)}a.btn.ghost:hover,button.btn.ghost:hover{background:var(--leaf-light)}
.paper-head{display:flex;align-items:center;gap:14px;margin:8px 0 14px}.paper-head .tag{white-space:nowrap;font-family:Fraunces,serif;font-size:1.05rem;font-weight:700;color:#fff;border-radius:8px;padding:4px 12px}
.tag.p1{background:var(--p1)}.tag.p2{background:var(--p2)}.paper-head span.assessed{color:var(--stone);font-size:.95rem}
.topic-card{display:flex;gap:16px;text-decoration:none;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;transition:transform .12s,box-shadow .12s}
.topic-card:hover{transform:translateY(-2px);box-shadow:0 6px 18px rgba(31,61,43,.12)}
.topic-card .icon{flex:0 0 52px;height:52px;border-radius:12px;display:flex;align-items:center;justify-content:center}.topic-card .icon svg{width:30px;height:30px}
.icon.p1{background:var(--p1-light);color:var(--p1)}.icon.p2{background:var(--p2-light);color:var(--p2)}[data-theme=dark] .icon.p1{color:#8fc3d8}[data-theme=dark] .icon.p2{color:#9fd08f}
.topic-card>div:last-child{flex:1}.topic-card h3{margin:0 0 4px;font-size:1.2rem;color:var(--head)}.topic-card .meta{color:var(--stone);font-size:.9rem}.topic-card .subs{margin:8px 0 0;color:var(--stone);font-size:.9rem;line-height:1.4}
.sub-list{list-style:none;padding:0;margin:0}
.sub-item{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin:12px 0;display:flex;justify-content:space-between;gap:16px;align-items:center;flex-wrap:wrap}
.sub-item .t{flex:1 1 380px}.sub-item .t a.name{font-family:Fraunces,serif;font-size:1.15rem;font-weight:700;color:var(--head);text-decoration:none}.sub-item .t a.name:hover{color:var(--moss)}
.sub-item .meta{color:var(--stone);font-size:.88rem;margin-top:2px}
.links{display:flex;flex-wrap:wrap;gap:6px}.links a{font-size:.82rem;padding:4px 11px;border-radius:999px;text-decoration:none;border:1px solid var(--line);background:var(--sand);color:var(--moss);font-weight:600}
.links a:hover{background:var(--leaf-light);border-color:var(--leaf)}.links a.qp{background:var(--leaf-light)}
table.list{border-collapse:collapse;width:100%;margin:10px 0 24px;background:var(--card);border-radius:12px;overflow:hidden;border:1px solid var(--line)}
table.list th,table.list td{padding:10px 14px;text-align:left;font-size:.95rem;vertical-align:top;border-bottom:1px solid var(--line)}table.list th{background:var(--sand-dark);color:var(--head)}table.list tr:last-child td{border-bottom:0}
.q{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 24px;margin:20px 0;box-shadow:0 1px 3px rgba(31,61,43,.05);border-left-width:5px}
.q[data-status="1"]{border-left-color:var(--warn)}.q[data-status="2"]{border-left-color:var(--ok)}
.q .qh{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8px;border-bottom:1px solid var(--line);padding-bottom:8px;margin-bottom:8px}
.q .qh .num{font-family:Fraunces,serif;font-weight:700;color:var(--head);font-size:1.15rem}.q .meta{font-size:.82rem;color:var(--stone)}
.q .part{margin:12px 0 6px;padding:8px 0 8px 12px;border-left:3px solid var(--leaf)}.q .part .pn{font-weight:700;color:var(--moss);margin-right:8px;font-family:Fraunces,serif}.q .marks{float:right;font-weight:700;color:var(--earth);font-size:.9rem}
.q table.data{border-collapse:collapse;margin:12px auto;background:var(--card)}.q table.data th,.q table.data td{border:1px solid var(--stone);padding:5px 12px;text-align:center;font-size:.92rem}.q table.data th{background:var(--sand-dark)}
.q .cap{text-align:center;font-weight:700;margin:10px 0 2px;font-family:Fraunces,serif;color:var(--head)}
.q ul.mcq{list-style:none;padding-left:10px}.q ul.mcq li:before{content:"\\2610  ";}
svg.chart{max-width:100%;height:auto;display:block;margin:6px auto;background:#fff;border-radius:8px}
details.ms{margin-top:12px;background:var(--ms-bg);border:1px solid var(--ms-line);border-radius:10px;padding:10px 14px}details.ms summary{cursor:pointer;font-weight:700;color:var(--moss)}
details.ms ul{margin:6px 0 8px 18px;padding:0}details.ms .lvl{font-size:.88rem;margin:4px 0;color:var(--stone)}details.ms .src{font-size:.85rem;color:var(--earth);margin-top:8px;border-top:1px dashed var(--ms-line);padding-top:6px}
.note{background:var(--note-bg);border:1px solid var(--note-line);border-radius:10px;padding:12px 16px;font-size:.95rem}
footer{background:var(--forest);color:rgba(255,255,255,.75);padding:26px 0;font-size:.88rem;margin-top:40px}footer a{color:#fff}
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px}@media(max-width:860px){.two{grid-template-columns:1fr}}
/* progress */
.st{display:inline-flex;gap:4px;margin-left:auto}.st button{font-family:inherit;font-size:.78rem;border:1px solid var(--line);background:var(--sand);color:var(--stone);border-radius:999px;padding:2px 10px;cursor:pointer}
.st button:hover{border-color:var(--moss)}.st button.on[data-s="1"]{background:var(--warn);color:#222;border-color:var(--warn)}.st button.on[data-s="2"]{background:var(--ok);color:#fff;border-color:var(--ok)}
.prog{display:flex;align-items:center;gap:10px;font-size:.82rem;color:var(--stone);margin-top:8px}.prog .bar{flex:1;height:8px;background:var(--sand-dark);border-radius:999px;overflow:hidden;display:flex;max-width:260px}
.prog .bar .ok{background:var(--ok);height:100%}.prog .bar .wk{background:var(--warn);height:100%}.prog .pl{white-space:nowrap;min-width:90px}
.hero .prog{color:rgba(255,255,255,.85)}.hero .prog .bar{background:rgba(255,255,255,.25)}
/* filter bar & tools */
.filterbar{position:sticky;top:var(--hdr,62px);z-index:10;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px;margin:10px 0 6px;display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.filterbar input[type=search]{flex:1 1 220px;font:inherit;padding:7px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink)}
.filterbar label{font-size:.85rem;color:var(--stone);display:inline-flex;align-items:center;gap:4px;cursor:pointer}.filterbar .chip{border:1px solid var(--line);border-radius:999px;padding:2px 10px;background:var(--sand);color:var(--stone);font-size:.82rem;cursor:pointer;font-family:inherit}
.filterbar .chip.on{background:var(--moss);color:#fff;border-color:var(--moss)}.filterbar .cnt{font-size:.85rem;color:var(--stone);margin-left:auto}
.filterbar select{font:inherit;font-size:.88rem;padding:5px 8px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink)}
.tools{position:sticky;top:var(--hdr,62px);z-index:10;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 16px;margin:10px 0;display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.tools .time{font-family:Fraunces,serif;font-size:1.6rem;font-weight:700;color:var(--head);min-width:120px}.tools .time.low{color:var(--bad)}
.tools .score{font-weight:700;color:var(--moss)}.tools .score b{font-family:Fraunces,serif;font-size:1.3rem}.tools .pct{font-size:.85rem;color:var(--stone)}
.tools button{font-family:inherit;font-size:.88rem;padding:6px 12px;border-radius:8px;border:1px solid var(--moss);background:transparent;color:var(--moss);cursor:pointer}.tools button.primary{background:var(--moss);color:#fff}
.aw{display:flex;align-items:center;gap:8px;margin:4px 0 8px;font-size:.88rem;color:var(--stone)}.aw input{width:64px;font:inherit;padding:3px 6px;border:1px solid var(--line);border-radius:6px;background:var(--input);color:var(--ink)}
.q.hide{display:none}
/* quick-fire & search */
.qf-controls{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin:10px 0 16px}.qf-controls label{font-size:.9rem;color:var(--stone);display:inline-flex;gap:5px;align-items:center}
.qf-controls select,.qf-controls input[type=search]{font:inherit;padding:6px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink)}
.kbd{font-size:.8rem;color:var(--stone)}.kbd kbd{border:1px solid var(--line);border-radius:4px;padding:0 5px;background:var(--sand-dark);font-family:inherit}
.res{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:10px 0;text-decoration:none;color:inherit}.res:hover{border-color:var(--moss)}
.res .t{font-weight:700;color:var(--head)}.res .m{font-size:.82rem;color:var(--stone)}.res .s{font-size:.92rem;margin-top:4px}.res mark{background:#ffe58a;color:#222;border-radius:3px;padding:0 2px}
.empty{color:var(--stone);font-style:italic}
/* mark scheme points, levels, links */
.mspart{margin:8px 0 12px}.msh{display:flex;align-items:baseline;gap:8px;margin-bottom:2px}.msh .mtot{font-size:.8rem;color:var(--earth);font-weight:700}
ul.pts{list-style:none;margin:4px 0 6px 0!important;padding:0}ul.pts li{display:flex;gap:10px;align-items:flex-start;padding:4px 0;border-top:1px dashed var(--ms-line)}ul.pts li:first-child{border-top:0}
.mk{flex:0 0 auto;min-width:26px;text-align:center;font-size:.75rem;font-weight:700;color:#fff;background:var(--ok);border-radius:6px;padding:2px 6px;margin-top:3px}
table.levels{border-collapse:collapse;width:100%;margin:6px 0 10px;font-size:.86rem;background:var(--card)}table.levels th,table.levels td{border:1px solid var(--ms-line);padding:5px 8px;text-align:left;vertical-align:top}table.levels th{background:var(--sand-dark)}table.levels td.r{white-space:nowrap;font-weight:700;color:var(--earth)}
ul.ind{margin:4px 0 8px 18px}
.st button.lnk{padding:2px 7px}
#totop{position:fixed;right:18px;bottom:18px;z-index:15;background:var(--moss);color:#fff;border:0;border-radius:50%;width:42px;height:42px;font-size:1.2rem;cursor:pointer;box-shadow:0 3px 10px rgba(0,0,0,.25);opacity:0;pointer-events:none;transition:opacity .2s}#totop.show{opacity:1;pointer-events:auto}
.jump{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 4px}.jump a{font-size:.82rem;padding:3px 10px;border-radius:999px;border:1px solid var(--line);background:var(--sand);color:var(--moss);text-decoration:none;font-weight:600}.jump a:hover{background:var(--leaf-light)}
.real .row{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap;padding:8px 0;border-bottom:1px dashed var(--line);font-size:.95rem}.real .row .ser{font-weight:700;color:var(--head);min-width:150px}.real .row .qn{color:var(--stone);min-width:70px}.real .row .t{flex:1 1 300px}
.real .row a{font-size:.82rem;padding:2px 9px;border-radius:999px;border:1px solid var(--line);background:var(--sand);text-decoration:none;font-weight:600}
.plan input[type=date]{font:inherit;padding:6px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink)}.plan .big{font-family:Fraunces,serif;font-size:2rem;color:var(--moss)}
table.list td .bar{height:8px;background:var(--sand-dark);border-radius:999px;overflow:hidden;display:flex;width:140px}table.list td .bar .ok{background:var(--ok)}table.list td .bar .wk{background:var(--warn)}
@media(max-width:720px){header.top{position:static}header.top nav a{margin-left:12px;font-size:.88rem}.filterbar,.tools{top:0}.hero h1{font-size:1.8rem}.hero{padding:34px 0 28px}.sub-item .t{flex-basis:100%}}
/* write-first mode, exemplars, drills */
.modew{font-size:.85rem;color:var(--stone);display:inline-flex;align-items:center;gap:5px;cursor:pointer;border:1px solid var(--line);border-radius:999px;padding:2px 10px;background:var(--sand)}
body.wmode .q:not(.revealed) details.ms{display:none}
.wa{display:block;width:100%;min-height:70px;font:inherit;font-size:.95rem;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink);margin:6px 0 2px;resize:vertical}
.wctl{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0 4px}.wctl .hint{font-size:.82rem;color:var(--stone)}
.sm{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;margin:8px 0;padding:8px 12px;border:1px dashed var(--ms-line);border-radius:8px;font-size:.88rem}.sm input{width:60px;font:inherit;padding:3px 6px;border:1px solid var(--line);border-radius:6px;background:var(--input);color:var(--ink)}
.sm .res{font-weight:700}.sm .res.ok{color:var(--ok)}.sm .res.wk{color:var(--warn)}
details.ex{margin:10px 0 4px;background:var(--card);border:1px solid var(--ms-line);border-radius:8px;padding:8px 12px}details.ex summary{cursor:pointer;font-weight:700;color:var(--earth)}
.exwrap{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:8px}@media(max-width:860px){.exwrap{grid-template-columns:1fr}}
.exa{border-radius:8px;padding:10px 14px;font-size:.93rem;line-height:1.5}.exa p{margin:0 0 8px}.exa.top{background:var(--leaf-light);border-left:4px solid var(--ok)}.exa.low{background:var(--note-bg);border-left:4px solid var(--warn)}
.exh{font-weight:700;font-size:.85rem;margin-bottom:6px;color:var(--head)}.exn{margin-top:10px;font-size:.9rem}.exn ul{margin:4px 0 0 18px}
.drill{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px 26px;margin:14px 0;min-height:160px}
.drill .term{font-family:Fraunces,serif;font-size:1.6rem;color:var(--head);margin:0 0 6px}.drill .def{font-size:1.05rem;margin:8px 0}.drill .src{font-size:.82rem;color:var(--stone)}
.drill .btns{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}.drill input.ans{font:inherit;padding:8px 10px;border:1px solid var(--line);border-radius:8px;background:var(--input);color:var(--ink);width:100%;max-width:520px}
.drill .fb{margin-top:8px;font-weight:700}.drill .fb.ok{color:var(--ok)}.drill .fb.bad{color:var(--bad)}
.drill .work{white-space:pre-line;background:var(--sand-dark);border-radius:8px;padding:10px 14px;font-size:.92rem;margin-top:8px}
.modecard{display:flex;gap:16px;align-items:flex-start;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin-bottom:14px}.modecard .mi{font-size:1.6rem;flex:0 0 40px;text-align:center}.modecard h3{margin:0 0 4px;color:var(--head)}.modecard p{margin:0 0 8px;color:var(--stone)}
.due{font-size:.85rem;color:var(--stone)}
/* print */
@media print{header.top,footer,.tools,.filterbar,.st,.pill,.aw,.hero .crumbs,.prog,.noprint{display:none!important}
body{background:#fff;color:#000;font-size:12pt}.hero{background:#fff!important;color:#000;padding:10px 0}.hero p,.hero h1{color:#000}.hero:before{display:none}
.q{break-inside:avoid;box-shadow:none;border:1px solid #999;page-break-inside:avoid}details.ms{display:none}body.print-ms details.ms{display:block;background:#f3f3f3}body.print-ms details.ms summary{display:none}
svg.chart{max-width:420px}a{color:#000;text-decoration:none}}
"""

ICONS = {
    "physical": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 18a4 4 0 0 1-.8-7.9A6 6 0 0 1 17.7 8.6 4 4 0 0 1 17 18H7z"/><path d="M8 21h8"/></svg>',
    "energy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/></svg>',
    "pollution": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6"/><path d="M10 3v6L4.5 18a2 2 0 0 0 1.7 3h11.6a2 2 0 0 0 1.7-3L14 9V3"/><path d="M7 15h10"/></svg>',
    "research": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m21 21-5.5-5.5"/><path d="M8 10.5h5M10.5 8v5"/></svg>',
    "living": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 4c-8 0-14 4-14 12 0 1.5.3 3 1 4 2-6 6-9 11-11-4 3-7 6-8 12 8 0 12-6 10-17z"/></svg>',
    "bioresources": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22V9"/><path d="M12 9c-3 0-5-2-5-5 3 0 5 2 5 5zM12 9c3 0 5-2 5-5-3 0-5 2-5 5zM12 15c-3 0-5-2-5-5 3 0 5 2 5 5zM12 15c3 0 5-2 5-5-3 0-5 2-5 5z"/></svg>',
    "sustainability": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 0 1-15.5 6.2"/><path d="M3 12a9 9 0 0 1 15.5-6.2"/><path d="m18.5 2.8.2 4-4-.2"/><path d="m5.5 21.2-.2-4 4 .2"/></svg>',
}
LEAF = '<svg viewBox="0 0 24 24" fill="none" stroke="#7fb069" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 4c-8 0-14 4-14 12 0 1.5.3 3 1 4 2-6 6-9 11-11-4 3-7 6-8 12 8 0 12-6 10-17z"/></svg>'

# Shared JavaScript: theme, progress tracking, filtering, print helpers.  Runs on every page.
JS = r"""
(function(){
const LS=k=>{try{return JSON.parse(localStorage.getItem(k)||'null')}catch(e){return null}};
const SV=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
window.ES={LS,SV};
/* ---- theme ---- */
const root=document.documentElement;
function applyTheme(t){if(t==='dark')root.dataset.theme='dark';else delete root.dataset.theme;const b=document.getElementById('themeBtn');if(b)b.textContent=t==='dark'?'\u2600 Light':'\u263E Dark';}
applyTheme(LS('envsci.theme')||'light');
const tb=document.getElementById('themeBtn');if(tb)tb.onclick=()=>{const t=root.dataset.theme==='dark'?'light':'dark';SV('envsci.theme',t);applyTheme(t);};
/* ---- progress ---- */
let prog=LS('envsci.progress')||{};
window.ES.prog=()=>prog;
function paint(){
  document.querySelectorAll('.q[data-qid]').forEach(el=>{const s=prog[el.dataset.qid]||0;el.dataset.status=s;el.querySelectorAll('.st button[data-s]').forEach(b=>b.classList.toggle('on',+b.dataset.s===s&&s>0));});
  document.querySelectorAll('[data-qids]').forEach(el=>{const ids=el.dataset.qids.split(',').filter(Boolean);const n=ids.length;if(!n)return;
    const ok=ids.filter(i=>prog[i]===2).length,wk=ids.filter(i=>prog[i]===1).length;
    const o=el.querySelector('.bar .ok'),w=el.querySelector('.bar .wk'),p=el.querySelector('.pl');
    if(o)o.style.width=(100*ok/n)+'%';if(w)w.style.width=(100*wk/n)+'%';if(p)p.textContent=ok+'/'+n+' secure'+(wk?' \u00b7 '+wk+' to revisit':'');});
  const ov=document.getElementById('overall');if(ov){const all=(ov.dataset.qids||'').split(',').filter(Boolean);const ok=all.filter(i=>prog[i]===2).length,wk=all.filter(i=>prog[i]===1).length;ov.querySelector('.stat').textContent=Math.round(100*ok/all.length)+'%';ov.querySelector('.detail').textContent=ok+' secure, '+wk+' to revisit, '+(all.length-ok-wk)+' not attempted of '+all.length+' questions.';}
}
window.ES.paint=paint;
document.addEventListener('click',e=>{const b=e.target.closest('.st button[data-s]');if(!b)return;const q=b.closest('.q');const s=+b.dataset.s;const cur=prog[q.dataset.qid]||0;if(s===cur||s===0)delete prog[q.dataset.qid];else prog[q.dataset.qid]=s;SV('envsci.progress',prog);window.ES.schedule(q.dataset.qid,prog[q.dataset.qid]||0);paint();if(window.ES.onFilter)window.ES.onFilter();});
const rs=document.getElementById('resetProg');if(rs)rs.onclick=()=>{if(confirm('Clear all saved progress on this browser?')){prog={};SV('envsci.progress',prog);paint();}};
paint();
/* ---- spaced repetition: secure questions come back after 1, 3, 7, 14, 30 days ---- */
const IVL=[1,3,7,14,30];let srs=LS('envsci.srs')||{};
window.ES.srs=()=>srs;window.ES.isDue=id=>{const r=srs[id];return !r||!r.due||r.due<=Date.now();};
window.ES.schedule=(id,s)=>{if(s===2){const prev=srs[id]&&srs[id].ivl||0;const i=IVL[Math.min(IVL.indexOf(prev)+1,IVL.length-1)]||1;srs[id]={ivl:i,due:Date.now()+i*86400000};}else delete srs[id];SV('envsci.srs',srs);};
/* ---- write-first mode (opt-in): answer boxes first, mark scheme after reveal ---- */
let mode=LS('envsci.mode')||'read';
function applyMode(){document.body.classList.toggle('wmode',mode==='write');document.querySelectorAll('input.modeW').forEach(c=>c.checked=mode==='write');
  document.querySelectorAll('.q[data-qid]').forEach(setupW);}
function setupW(q){if(mode!=='write'){q.querySelectorAll('.wbox').forEach(e=>e.remove());q.classList.remove('revealed');return;}
  if(q.querySelector('.wbox'))return;const id=q.dataset.qid;const ans=LS('envsci.answers')||{};
  q.querySelectorAll('.part').forEach((part,i)=>{const w=document.createElement('div');w.className='wbox';const ta=document.createElement('textarea');ta.className='wa';ta.placeholder='Write your answer here before revealing the mark scheme...';ta.value=ans[id+'.'+(i+1)]||'';
    ta.addEventListener('input',()=>{const a=LS('envsci.answers')||{};a[id+'.'+(i+1)]=ta.value;SV('envsci.answers',a);});w.appendChild(ta);part.after(w);});
  const ctl=document.createElement('div');ctl.className='wbox wctl';ctl.innerHTML='<button type="button" class="btn reveal">Reveal mark scheme &amp; self-mark</button><span class="hint">Your answers are saved in this browser.</span>';
  const ms=q.querySelector('details.ms');if(ms)ms.before(ctl);
  ctl.querySelector('.reveal').onclick=()=>{q.classList.add('revealed');if(ms)ms.open=true;ctl.remove();buildSelfMark(q);};}
function buildSelfMark(q){if(q.querySelector('.sm'))return;const pm=(q.dataset.pm||'').split(',').map(Number);const max=pm.reduce((a,b)=>a+b,0);
  const sm=document.createElement('div');sm.className='sm wbox';sm.innerHTML='<b>Self-mark:</b> '+pm.map((m,i)=>'<label>Part '+(i+1)+' <input type="number" min="0" max="'+m+'" data-i="'+i+'"> / '+m+'</label>').join('')+'<button type="button" class="chip save">Save &amp; set status</button><span class="res"></span>';
  const ms=q.querySelector('details.ms');ms.appendChild(sm);
  sm.querySelector('.save').onclick=()=>{let t=0;sm.querySelectorAll('input').forEach(i=>t+=Math.min(+i.max,+i.value||0));const pc=t/max;const s=pc>=0.7?2:1;
    const id=q.dataset.qid;if(s===2)prog[id]=2;else prog[id]=1;SV('envsci.progress',prog);window.ES.schedule(id,s);paint();
    const r=sm.querySelector('.res');r.textContent=t+'/'+max+' ('+Math.round(pc*100)+'%) - marked '+(s===2?'secure':'needs work');r.className='res '+(s===2?'ok':'wk');if(window.ES.onFilter)window.ES.onFilter();};}
window.ES.applyMode=applyMode;
document.addEventListener('change',e=>{if(!e.target.matches('input.modeW'))return;mode=e.target.checked?'write':'read';SV('envsci.mode',mode);applyMode();});
applyMode();
/* ---- filter bar ---- */
const fb=document.querySelector('.filterbar');
if(fb){
  const qs=[...document.querySelectorAll('.q[data-qid]')];
  const txt=fb.querySelector('input[type=search]');const cnt=fb.querySelector('.cnt');
  function run(){const words=(txt.value||'').toLowerCase().split(/\s+/).filter(Boolean);
    const marks=[...fb.querySelectorAll('.chip.mk.on')].map(c=>c.dataset.v);const flags=[...fb.querySelectorAll('.chip.fl.on')].map(c=>c.dataset.v);
    const st=fb.querySelector('select.status').value;let shown=0;
    qs.forEach(el=>{let ok=true;const t=el.textContent.toLowerCase();
      if(words.length&&!words.every(w=>t.includes(w)))ok=false;
      if(marks.length&&!marks.includes(el.dataset.marks))ok=false;
      if(flags.length&&!flags.every(f=>(' '+el.dataset.flags+' ').includes(' '+f+' ')))ok=false;
      const s=prog[el.dataset.qid]||0;if(st==='todo'&&s!==0)ok=false;if(st==='work'&&s!==1)ok=false;if(st==='secure'&&s!==2)ok=false;if(st==='notsecure'&&s===2)ok=false;
      el.classList.toggle('hide',!ok);if(ok)shown++;});
    cnt.textContent='Showing '+shown+' of '+qs.length;
    document.querySelectorAll('h2.sec.set').forEach(h=>{let n=h.nextElementSibling,any=false;while(n&&!n.classList.contains('set')){if(n.classList.contains('q')&&!n.classList.contains('hide'))any=true;n=n.nextElementSibling;}h.style.display=any?'':'none';});}
  window.ES.onFilter=run;
  txt.addEventListener('input',run);fb.querySelectorAll('.chip').forEach(c=>c.onclick=()=>{c.classList.toggle('on');run();});fb.querySelector('select.status').onchange=run;
  const clr=fb.querySelector('.clear');if(clr)clr.onclick=()=>{txt.value='';fb.querySelectorAll('.chip').forEach(c=>c.classList.remove('on'));fb.querySelector('select.status').value='all';run();};
  run();}
/* ---- sticky offset = real header height (nav can wrap) ---- */
const hd=document.querySelector('header.top');const setH=()=>root.style.setProperty('--hdr',(getComputedStyle(hd).position==='sticky'?hd.offsetHeight:0)+'px');setH();window.addEventListener('resize',setH);
/* ---- copy link, back to top ---- */
document.addEventListener('click',e=>{const b=e.target.closest('[data-copy]');if(!b)return;const q=b.closest('.q');const url=location.href.split('#')[0]+'#'+q.id;
  (navigator.clipboard?navigator.clipboard.writeText(url):Promise.reject()).then(()=>{b.textContent='\u2713';setTimeout(()=>b.innerHTML='&#128279;',1200);}).catch(()=>prompt('Copy this link:',url));});
const tt=document.createElement('button');tt.id='totop';tt.title='Back to top';tt.innerHTML='&uarr;';tt.className='noprint';document.body.appendChild(tt);tt.onclick=()=>window.scrollTo({top:0,behavior:'smooth'});
window.addEventListener('scroll',()=>tt.classList.toggle('show',window.scrollY>600),{passive:true});
/* ---- print & reveal ---- */
document.querySelectorAll('[data-print]').forEach(b=>b.onclick=()=>{const ms=b.dataset.print==='ms';document.body.classList.toggle('print-ms',ms);document.querySelectorAll('details.ms').forEach(d=>d.open=ms);window.print();});
document.querySelectorAll('[data-reveal]').forEach(b=>b.onclick=()=>{const open=b.dataset.reveal==='1';document.querySelectorAll('details.ms').forEach(d=>d.open=open);b.dataset.reveal=open?'0':'1';b.textContent=open?'Hide all mark schemes':'Show all mark schemes';});
})();
"""

# Mock-paper page: exam timer + self-marking score (state saved per paper in localStorage)
PAPER_JS = r"""
(function(){
const file=document.body.dataset.paper,LS=window.ES.LS,SV=window.ES.SV;const TOTAL=%d;
let sc=LS('envsci.scores')||{};let mine=sc[file]||{parts:{},essay:{}};
const inputs=[...document.querySelectorAll('input.aw-in')];
function total(){let t=0;inputs.forEach(i=>{if(i.dataset.kind==='part')t+=+i.value||0;});const ev=Object.values(mine.essay).map(Number);if(ev.length)t+=Math.max(...ev,0);return t;}
function paintScore(){const t=total();const max=+document.body.dataset.max;document.getElementById('scoreN').textContent=t;document.getElementById('scorePct').textContent=Math.round(100*t/max)+'%%';}
inputs.forEach(i=>{const key=i.dataset.key;const stored=i.dataset.kind==='part'?mine.parts[key]:mine.essay[key];if(stored!==undefined)i.value=stored;
  i.addEventListener('input',()=>{let v=Math.max(0,Math.min(+i.max,+i.value||0));if(i.value!=='')i.value=v;if(i.dataset.kind==='part')mine.parts[key]=v;else mine.essay[key]=v;mine.total=total();mine.max=+document.body.dataset.max;mine.when=Date.now();sc[file]=mine;SV('envsci.scores',sc);paintScore();});});
paintScore();
document.getElementById('clearScore').onclick=()=>{if(!confirm('Clear the marks you entered for this paper?'))return;inputs.forEach(i=>i.value='');mine={parts:{},essay:{}};delete sc[file];SV('envsci.scores',sc);paintScore();};
/* timer */
let tm=(LS('envsci.timers')||{})[file]||{left:TOTAL,running:false,at:0};
const disp=document.getElementById('clock'),btn=document.getElementById('startBtn');
function left(){return tm.running?Math.max(0,tm.left-Math.floor((Date.now()-tm.at)/1000)):tm.left;}
function save(){const all=LS('envsci.timers')||{};all[file]=tm;SV('envsci.timers',all);}
function fmt(s){const h=Math.floor(s/3600),m=Math.floor(s%%3600/60),x=s%%60;return h+':'+String(m).padStart(2,'0')+':'+String(x).padStart(2,'0');}
function tick(){const l=left();disp.textContent=fmt(l);disp.classList.toggle('low',l<15*60);btn.textContent=tm.running?'Pause':(l===TOTAL?'Start exam':'Resume');if(tm.running&&l===0){tm.running=false;tm.left=0;save();alert('Time is up - pens down!');}}
btn.onclick=()=>{if(tm.running){tm.left=left();tm.running=false;}else{if(tm.left===0)return;tm.running=true;tm.at=Date.now();}save();tick();};
document.getElementById('resetBtn').onclick=()=>{tm={left:TOTAL,running:false,at:0};save();tick();};
tick();setInterval(tick,1000);
})();
"""

# papers.html: fill the "your score" column from localStorage
PAPERS_JS = r"""
(function(){const sc=window.ES.LS('envsci.scores')||{};document.querySelectorAll('td.yours').forEach(td=>{const s=sc[td.dataset.file];if(s&&s.total!==undefined){const p=Math.round(100*s.total/s.max);td.innerHTML='<b>'+s.total+'</b>/'+s.max+' <span style="color:var(--stone)">('+p+'%)</span>';}else td.innerHTML='<span style="color:var(--stone)">&ndash;</span>';});})();
"""


def page(title, body, root="", active="", extra_js="", body_attrs=""):
    nav = "".join(f'<a href="{root}{h}" class="{"on" if active == h else ""}">{t}</a>' for h, t in
                  [("index.html", "Topics"), ("papers.html", "Mock papers"), ("official.html", "Past papers"), ("practice.html", "Practice modes"),
                   ("planner.html", "Planner"), ("search.html", "Search")])
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} - AQA Environmental Science</title><style>{CSS}</style>
<script>try{{if(localStorage.getItem('envsci.theme')==='"dark"')document.documentElement.dataset.theme='dark';}}catch(e){{}}</script></head><body {body_attrs}>
<header class="top"><div class="wrap"><a class="brand" href="{root}index.html">{LEAF}<span>AQA Environmental Science</span></a><nav>{nav}<button class="icon-btn" id="themeBtn" type="button" title="Toggle dark mode">&#9790; Dark</button></nav></div></header>
{body}
<footer><div class="wrap">Original practice questions and mark schemes written to the AQA A-level Environmental Science (7447) specification. Every question cites the printed page numbers of {html.escape(BOOK)}. AQA past papers are &copy; AQA. Progress, scores and timers are saved only in this browser. &nbsp;&middot;&nbsp; <a href="{root}index.html">Topics</a> &middot; <a href="{root}papers.html">Mock papers</a> &middot; <a href="{root}official.html">Past papers</a> &middot; <a href="{root}essays.html">Essay bank</a> &middot; <a href="{root}practice.html">Practice modes</a> &middot; <a href="{root}essays.html">Essay bank</a> &middot; <a href="{root}pastq.html">Real questions by topic</a> &middot; <a href="{root}planner.html">Planner</a> &middot; <a href="{root}search.html">Search</a></div></footer>
<script>{JS}</script>{extra_js}</body></html>"""


def hero(title, sub, crumbs=None, cls="", pills=None, extra=""):
    c = ""
    if crumbs:
        c = '<div class="crumbs">' + '<span>&rsaquo;</span>'.join(f'<a href="{h}">{html.escape(t)}</a>' if h else html.escape(t) for h, t in crumbs) + "</div>"
    p = "".join(f'<span class="pill">{x}</span>' for x in (pills or []))
    return f'<section class="hero {cls}"><div class="wrap">{c}<h1>{title}</h1><p>{sub}</p>{p}{extra}</div></section>'


def progress_bar(ids):
    return f'<div class="prog" data-qids="{",".join(ids)}"><div class="bar"><div class="ok"></div><div class="wk"></div></div><span class="pl"></span></div>'


def fmt(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"&amp;(#?\w+);", r"&\1;", s)
    for tag in ("b", "i", "sub", "sup", "u"):
        s = s.replace(f"&lt;{tag}&gt;", f"<{tag}>").replace(f"&lt;/{tag}&gt;", f"</{tag}>")
    s = s.replace("&lt;br/&gt;", "<br>")
    s = re.sub(r"_(\d+)", r"<sub>\1</sub>", s)
    s = re.sub(r"\^(-?\d+)", r"<sup>\1</sup>", s)
    return s


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", html.unescape(fmt(s)))


# ---------- charts as inline SVG ----------
def svg_chart(ch: Chart, caption):
    W, H = 560, 320
    ml, mr, mt, mb = 60, 20, 20, 50
    pw, ph = W - ml - mr, H - mt - mb
    labels = list(ch.series.keys())
    cols = ["#22302a", "#2f5f73", "#8b5e3c", "#7fb069"]
    out = [f'<div class="cap">{html.escape(caption)}</div>',
           f'<svg class="chart" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial" font-size="11">']
    if ch.kind == "bar":
        cats = ch.categories or [str(x) for x, _ in ch.series[labels[0]]]
        vals = [v for k in labels for _, v in ch.series[k]]
        ymin = ch.y_min if ch.y_min is not None else min(0, min(vals))
        ymax = ch.y_max if ch.y_max is not None else max(vals) * 1.1
        ng = len(cats); ns = len(labels)
        gw = pw / ng; bw = gw * 0.7 / ns
        def ypix(v): return mt + ph - (v - ymin) / (ymax - ymin) * ph
        for gi, cat in enumerate(cats):
            for si, k in enumerate(labels):
                v = ch.series[k][gi][1]
                x = ml + gi * gw + gw * 0.15 + si * bw
                out.append(f'<rect x="{x:.1f}" y="{ypix(v):.1f}" width="{bw:.1f}" height="{(ypix(ymin)-ypix(v)):.1f}" fill="{cols[(si+1)%4] if ns>1 else "#3f6b4a"}"/>')
            out.append(f'<text x="{ml+gi*gw+gw/2:.1f}" y="{mt+ph+16}" text-anchor="middle">{html.escape(plain(cat))}</text>')
        for t in range(6):
            v = ymin + (ymax - ymin) * t / 5
            out.append(f'<line x1="{ml-4}" y1="{ypix(v):.1f}" x2="{ml}" y2="{ypix(v):.1f}" stroke="#000"/><text x="{ml-8}" y="{ypix(v)+4:.1f}" text-anchor="end">{v:g}</text>')
    else:
        xs = [x for k in labels for x, _ in ch.series[k]]; ys = [y for k in labels for _, y in ch.series[k]]
        xmin, xmax = min(xs), max(xs)
        ymin = ch.y_min if ch.y_min is not None else min(ys) - (max(ys) - min(ys)) * 0.05
        ymax = ch.y_max if ch.y_max is not None else max(ys) + (max(ys) - min(ys)) * 0.1
        if ymax == ymin: ymax = ymin + 1
        if xmax == xmin: xmax = xmin + 1
        def xpix(v): return ml + (v - xmin) / (xmax - xmin) * pw
        def ypix(v): return mt + ph - (v - ymin) / (ymax - ymin) * ph
        for si, k in enumerate(labels):
            pts = " ".join(f"{xpix(x):.1f},{ypix(y):.1f}" for x, y in ch.series[k])
            out.append(f'<polyline points="{pts}" fill="none" stroke="{cols[si%4]}" stroke-width="1.8"/>')
            for x, y in ch.series[k]:
                out.append(f'<circle cx="{xpix(x):.1f}" cy="{ypix(y):.1f}" r="2.6" fill="{cols[si%4]}"/>')
        for t in range(6):
            v = xmin + (xmax - xmin) * t / 5
            out.append(f'<line x1="{xpix(v):.1f}" y1="{mt+ph}" x2="{xpix(v):.1f}" y2="{mt+ph+4}" stroke="#000"/><text x="{xpix(v):.1f}" y="{mt+ph+16}" text-anchor="middle">{v:g}</text>')
            v = ymin + (ymax - ymin) * t / 5
            out.append(f'<line x1="{ml-4}" y1="{ypix(v):.1f}" x2="{ml}" y2="{ypix(v):.1f}" stroke="#000"/><text x="{ml-8}" y="{ypix(v)+4:.1f}" text-anchor="end">{v:.3g}</text>')
    out.append(f'<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt+ph}" stroke="#000"/><line x1="{ml}" y1="{mt+ph}" x2="{ml+pw}" y2="{mt+ph}" stroke="#000"/>')
    out.append(f'<text x="{ml+pw/2}" y="{H-8}" text-anchor="middle" font-weight="bold">{html.escape(plain(ch.x_label))}</text>')
    out.append(f'<text transform="translate(14,{mt+ph/2}) rotate(-90)" text-anchor="middle" font-weight="bold">{html.escape(plain(ch.y_label))}</text>')
    if len(labels) > 1:
        for si, k in enumerate(labels):
            out.append(f'<rect x="{ml+10}" y="{mt+4+si*14}" width="10" height="10" fill="{cols[si%4] if ch.kind=="line" else cols[(si+1)%4]}"/><text x="{ml+24}" y="{mt+13+si*14}">{html.escape(plain(k))}</text>')
    out.append("</svg>")
    return "\n".join(out)


def html_table(t: QTable, caption):
    s = [f'<div class="cap">{html.escape(caption)}</div><table class="data"><tr>' + "".join(f"<th>{fmt(h)}</th>" for h in t.header) + "</tr>"]
    for r in t.rows:
        s.append("<tr>" + "".join(f"<td>{fmt(str(c))}</td>" for c in r) + "</tr>")
    s.append("</table>")
    return "".join(s)


def q_flags(q):
    """Question-type tags used by the filter bar and search."""
    f = []
    if any(p.calc for p in q.parts): f.append("calc")
    if q.figures or any(p.table for p in q.parts): f.append("data")
    if q.has_extended: f.append("ext")
    if any(p.mcq for p in q.parts): f.append("mcq")
    if any(p.table for p in q.parts): f.append("table")
    return f


def exemplar_html(ex, essay=False):
    """Model answers (Level 3 / weaker) with annotated differences, shown inside the mark scheme."""
    if not ex:
        return ""
    low = f'<div class="exa low"><div class="exh">Weaker answer &middot; {html.escape(ex["low_level"])}</div>{ex["low"]}</div>' if ex.get("low") else ""
    return (f'<details class="ex"><summary>Model answers: what a {html.escape(ex["top_level"].split(" (")[0])} answer looks like</summary><div class="exwrap">'
            f'<div class="exa top"><div class="exh">Model answer &middot; {html.escape(ex["top_level"])}</div>{ex["top"]}</div>{low}</div>'
            '<div class="exn"><b>What makes the difference</b><ul>' + "".join(f"<li>{n}</li>" for n in ex["notes"]) + "</ul></div></details>")


def levels_table(levels):
    rows = "".join(f'<tr><td><b>{html.escape(lv) if lv else "&nbsp;"}</b></td><td class="r">{html.escape(rng)}</td><td>{html.escape(desc)}</td></tr>' for lv, rng, desc in levels)
    return f'<table class="levels"><tr><th>Level</th><th>Marks</th><th>What the answer must show</th></tr>{rows}</table>'


FLAG_NAMES = {"calc": "Calculation", "data": "Data / figure", "ext": "9-mark extended", "mcq": "Multiple choice", "table": "Complete a table"}
STATUS_BTNS = '<span class="st noprint"><button type="button" class="lnk" data-copy title="Copy a link to this question">&#128279;</button><button type="button" data-s="1" title="Attempted but needs more work">Needs work</button><button type="button" data-s="2" title="Confident with this question">Secure</button></span>'


def html_question(qn, q, marking=False):
    """One question card.  marking=True adds 'marks awarded' inputs (mock-paper self-marking)."""
    idx = subtopic_index()
    fig, tab = [0], [0]
    out = [f'<div class="q" id="{q.id}" data-qid="{q.id}" data-marks="{q.marks}" data-pm="{",".join(str(p.marks) for p in q.parts)}" data-flags="{" ".join(q_flags(q))}"><div class="qh"><span class="num">Question {qn}</span>'
           f'<span class="meta">{q.marks} marks &middot; <a href="../subtopic/{q.topic}.html">{html.escape(idx[q.topic]["name"])}</a> &middot; spec {html.escape(q.spec)} &middot; Genn pp. {html.escape(q.pages)} &middot; {q.id}</span>{STATUS_BTNS}</div>']
    if q.intro:
        out.append(f"<p>{fmt(q.intro)}</p>")
    for f in q.figures:
        if isinstance(f, QTable):
            tab[0] += 1; out.append(html_table(f, f.caption or f"Table {tab[0]}"))
        else:
            fig[0] += 1; out.append(svg_chart(f, f.caption or f"Figure {fig[0]}"))
    single = len(q.parts) == 1 and not q.intro and not q.figures
    for i, p in enumerate(q.parts, 1):
        lab = f"{qn:02d}" if single else f"{qn:02d}.{i}"
        out.append(f'<div class="part"><span class="marks">[{p.marks} mark{"s" if p.marks != 1 else ""}]</span><span class="pn">{lab}</span>{fmt(p.text)}')
        if p.table:
            tab[0] += 1; out.append(html_table(p.table, p.table.caption or f"Table {tab[0]}"))
        if p.mcq:
            out.append('<ul class="mcq">' + "".join(f"<li>{chr(65+k)}&nbsp; {fmt(o)}</li>" for k, o in enumerate(p.mcq)) + "</ul>")
        out.append("</div>")
    out.append('<details class="ms"><summary>Show mark scheme</summary>')
    for i, p in enumerate(q.parts, 1):
        lab = f"{qn:02d}" if single else f"{qn:02d}.{i}"
        out.append(f'<div class="mspart"><div class="msh"><b>{lab}</b> <span class="mtot">{p.marks} mark{"s" if p.marks != 1 else ""}</span></div>')
        rule, pts = mark_points(p)
        if p.level:
            out.append(levels_table(LEVELS_9) + '<div class="lvl"><b>Indicative content</b> - credit any of the following (and other relevant, accurate points):</div>')
            out.append('<ul class="ind">' + "".join(f"<li>{fmt(m)}</li>" for m in p.ms) + "</ul>")
            out.append(exemplar_html(EXEMPLARS.get(q.id)))
        elif p.mcq:
            letter = chr(65 + p.mcq.index(p.ms[0])) if p.ms and p.ms[0] in p.mcq else ""
            out.append(f'<div class="lvl">{fmt(rule)}</div><ul class="pts"><li><span class="mk">1</span><span><b>{letter}</b>&nbsp; {fmt(p.ms[0]) if p.ms else ""}</span></li></ul>')
        else:
            out.append(f'<div class="lvl">{fmt(rule)}</div><ul class="pts">' + "".join(f'<li><span class="mk">{lab_}</span><span>{fmt(m)}</span></li>' for m, lab_ in pts) + "</ul>")
        if marking:
            out.append(f'<div class="aw"><label>Marks awarded <input class="aw-in" type="number" min="0" max="{p.marks}" step="1" data-kind="part" data-key="{q.id}.{i}"></label> / {p.marks}</div>')
        out.append("</div>")
    out.append(f'<div class="src">Source: {html.escape(BOOK)}, pp. {html.escape(q.pages)}; AQA spec {html.escape(q.spec)}.</div></details></div>')
    return "\n".join(out)


def filter_bar(show_status=True):
    chips = "".join(f'<button type="button" class="chip mk" data-v="{m}">{m} marks</button>' for m in (5, 10, 15))
    chips += "".join(f'<button type="button" class="chip fl" data-v="{k}">{v}</button>' for k, v in FLAG_NAMES.items())
    status = ('<select class="status" title="Filter by your progress"><option value="all">All progress</option><option value="todo">Not attempted</option>'
              '<option value="work">Needs work</option><option value="secure">Secure</option><option value="notsecure">Not yet secure</option></select>')
    return (f'<div class="filterbar noprint"><input type="search" placeholder="Filter questions by keyword (e.g. albedo, quota, Simpson)">{chips}{status}'
            '<button type="button" class="chip clear">Clear</button><label class="modew" title="Type your answer before the mark scheme can be opened"><input type="checkbox" class="modeW"> Write-first mode</label><span class="cnt"></span>'
            '<button type="button" class="chip" data-reveal="1">Show all mark schemes</button>'
            '<button type="button" class="chip" data-print="qp" title="Print the questions only">Print</button><button type="button" class="chip" data-print="ms" title="Print questions with mark schemes">Print + MS</button></div>')


def sub_links(slug, sets, root=""):
    links = [f'<a href="{root}subtopic/{slug}.html">View online</a>']
    for k in range(1, len(sets) + 1):
        links.append(f'<a class="qp" href="{root}pdf/topic/{slug}-set{k}-QP.pdf">Set {k} QP</a><a href="{root}pdf/topic/{slug}-set{k}-MS.pdf">Set {k} MS</a>')
    return '<span class="links">' + "".join(links) + "</span>"


def topic_ids(t, sets_by_sub):
    return [q.id for slug, *_ in t["subtopics"] for s in sets_by_sub.get(slug, []) for q in s]


# ---------- pages ----------
def index_page(sets_by_sub, counts):
    all_ids = sorted({q.id for sets in sets_by_sub.values() for s in sets for q in s})
    body = [hero("Environmental Science A-level revision",
                 f"Questions by topic, full mock papers and official past papers for AQA 7447, organised exactly as the specification. Every question is referenced to the page of the approved textbook ({html.escape(BOOK)}).")]
    body.append('<main><div class="wrap">')
    body.append('<div class="grid4">'
                f'<div class="card"><div class="stat">{counts["questions"]}</div><h3>Questions by topic</h3><p>Across {counts["subtopics"]} subtopics, each with an AQA-format question paper PDF and a separate mark-scheme PDF.</p><a class="btn" href="#topics">Browse topics</a></div>'
                f'<div class="card"><div class="stat">{counts["papers"]}</div><h3>Mock papers</h3><p>Full 3-hour papers (120 marks) with an exam timer and self-marking scorecard.</p><a class="btn" href="papers.html">Open mock papers</a></div>'
                '<div class="card"><div class="stat">{counts["official"]}</div><h3>Official AQA papers</h3><p>Real question papers and mark schemes for every series so far (plus the specimen papers), grouped by year and paper.</p><a class="btn ghost" href="official.html">Open past papers</a></div>'
                f'<div class="card" id="overall" data-qids="{",".join(all_ids)}"><div class="stat">0%</div><h3>Your progress</h3><p class="detail"></p><a class="btn ghost" href="quickfire.html">Quick-fire practice</a> <button type="button" class="chip" id="resetProg" style="margin-top:8px;font-family:inherit;font-size:.8rem;border:1px solid var(--line);background:var(--sand);color:var(--stone);border-radius:999px;padding:3px 10px;cursor:pointer">Reset</button></div></div>')
    body.append('<h2 class="sec" id="topics">Topics by paper</h2><div class="two">')
    for pno, paper in PAPERS.items():
        body.append(f'<div><div class="paper-head"><span class="tag p{pno}">{paper["name"]}</span><span class="assessed">{html.escape(paper["assessed"])} &middot; 3 h &middot; 120 marks</span></div>')
        for t in paper["topics"]:
            ids = topic_ids(t, sets_by_sub)
            subs = " &middot; ".join(html.escape(name) for _, name, *_ in t["subtopics"])
            body.append(f'<a class="topic-card" href="topic/{t["slug"]}.html" style="margin-bottom:14px"><div class="icon p{pno}">{ICONS.get(t["slug"], ICONS["living"])}</div><div><h3>{html.escape(t["name"])}</h3>'
                        f'<div class="meta">Spec {t["spec"]} &middot; {len(t["subtopics"])} subtopics &middot; {len(ids)} questions</div><div class="subs">{subs}</div>{progress_bar(ids)}</div></a>')
        body.append("</div>")
    body.append('</div><p class="note" style="margin-top:26px">Mark each question <b>Needs work</b> or <b>Secure</b> as you go: the bars above, the topic pages and the Quick-fire mode all use these marks so you can focus on what you have not yet mastered. Everything is stored in this browser only.</p>')
    body.append("</div></main>")
    return page("Topics", "\n".join(body), active="index.html")


def topic_hub_page(t, pnos, sets_by_sub):
    """One page per spec topic (Pollution, Energy resources ...) listing its subtopics."""
    pno = pnos[0]
    cls = f"p{pno}" if len(pnos) == 1 else ""
    papers = " and ".join(PAPERS[p]["name"] for p in pnos)
    ids = topic_ids(t, sets_by_sub)
    pages_all = ", ".join(sorted({pg for _, _, _, pg in t["subtopics"]}, key=lambda s: int(re.match(r"\d+", s).group())))
    body = [hero(html.escape(t["name"]), f"Specification section {t['spec']} &middot; examined in {papers}. {len(t['subtopics'])} subtopics, {len(ids)} questions.",
                 crumbs=[("../index.html", "Topics"), (None, t["name"])], cls=cls, pills=[f"Spec {t['spec']}", f"Genn pp. {pages_all}", papers], extra=progress_bar(ids))]
    body.append('<main><div class="wrap"><h2 class="sec">Subtopics</h2><ul class="sub-list">')
    for slug, name, spec, pages in t["subtopics"]:
        sets = sets_by_sub.get(slug, [])
        sids = [q.id for s in sets for q in s]
        body.append(f'<li class="sub-item"><div class="t"><a class="name" href="../subtopic/{slug}.html">{html.escape(name)}</a><div class="meta">Spec {spec} &middot; Genn pp. {pages} &middot; {len(sids)} questions in {len(sets)} set{"s" if len(sets) != 1 else ""}</div>{progress_bar(sids)}</div>{sub_links(slug, sets, root="../")}</li>')
    body.append("</ul>")
    body.append(f'<p class="note">Each set is a printable question paper in AQA format with its own mark scheme. The online view shows every question with a click-to-reveal mark scheme and its textbook page reference. Try <a href="../quickfire.html?topic={t["slug"]}">Quick-fire on this topic</a>.</p>')
    body.append("</div></main>")
    return page(t["name"], "\n".join(body), root="../")


def subtopic_page(slug, sets):
    idx = subtopic_index()[slug]
    ids = [q.id for s in sets for q in s]
    pno = idx["papers"][0]
    cls = f"p{pno}" if len(idx["papers"]) == 1 else ""
    body = [hero(html.escape(idx["name"]), f'{html.escape(idx["topic"])} &middot; AQA spec {html.escape(idx["spec"])} &middot; {html.escape(BOOK)}, pp. {html.escape(idx["pages"])}',
                 crumbs=[("../index.html", "Topics"), (f"../topic/{idx['topic_slug']}.html", idx["topic"]), (None, idx["name"])], cls=cls + " small",
                 pills=[" and ".join("Paper " + str(p) for p in idx["papers"]), f"{len(ids)} questions"], extra=progress_bar(ids))]
    body.append('<main><div class="wrap"><h2 class="sec">Question sets</h2><table class="list"><tr><th>Set</th><th>Questions</th><th>Marks</th><th>Question paper</th><th>Mark scheme</th></tr>')
    for k, s in enumerate(sets, 1):
        body.append(f'<tr><td>Set {k}</td><td>{len(s)}</td><td>{sum(q.marks for q in s)}</td><td><a href="../pdf/topic/{slug}-set{k}-QP.pdf">Download QP (PDF)</a></td><td><a href="../pdf/topic/{slug}-set{k}-MS.pdf">Download MS (PDF)</a></td></tr>')
    body.append("</table>")
    real = official_rows(slug)
    if real:
        body.append(f'<h2 class="sec">Real AQA questions on this topic ({len(real)})</h2><div class="real">' + "".join(real) + "</div>")
    body.append(f'<p class="note noprint">Practise this subtopic one question at a time: <a href="../quickfire.html?sub={slug}">Quick-fire &rarr;</a></p>')
    body.append(filter_bar())
    qn = 0
    for k, s in enumerate(sets, 1):
        body.append(f'<h2 class="sec set">Set {k}</h2>')
        for q in s:
            qn += 1
            body.append(html_question(qn, q))
    body.append("</div></main>")
    return page(idx["name"], "\n".join(body), root="../")


def papers_page(generated):
    idx = subtopic_index()
    body = [hero("Generated mock papers", "Full-length papers in exact AQA 7447 format: 10 questions (5, 10 or 15 marks; 95 marks) plus one 25-mark essay chosen from two. Each set is assembled from the topic bank, so topics recur across sets deliberately to consolidate memory. Open a paper online for a 3-hour exam timer and a self-marking scorecard; your scores appear in the table.")]
    body.append('<main><div class="wrap">')
    for pno in (1, 2):
        body.append(f'<div class="paper-head"><span class="tag p{pno}">{PAPERS[pno]["name"]}</span><span class="assessed">{html.escape(PAPERS[pno]["assessed"])}</span></div><table class="list"><tr><th>Set</th><th>Question paper</th><th>Mark scheme</th><th>Your score</th><th>Topics covered (Q1&ndash;Q10) and essays</th></tr>')
        for g in generated:
            if g["paper"] != pno:
                continue
            tl = "; ".join(f'Q{i} {html.escape(idx[q.topic]["name"])} ({q.marks})' for i, q in enumerate(g["questions"], 1))
            es = " / ".join(html.escape(e.title) for e in g["essays"]) if g["essays"] else ""
            body.append(f'<tr><td><b>Set {g["set"]:02d}</b></td><td><a href="pdf/papers/{g["file"]}-QP.pdf">QP (PDF)</a><br><a href="paper/{g["file"]}.html">Sit online</a></td><td><a href="pdf/papers/{g["file"]}-MS.pdf">MS (PDF)</a></td><td class="yours" data-file="{g["file"]}"></td><td style="font-size:.88rem">{tl}<br><i style="color:var(--stone)">Essay: {es}</i></td></tr>')
        body.append("</table>")
    body.append("</div></main>")
    return page("Mock papers", "\n".join(body), active="papers.html", extra_js=f"<script>{PAPERS_JS}</script>")


def paper_online_page(g):
    pno = g["paper"]
    total = sum(q.marks for q in g["questions"]) + (25 if g["essays"] else 0)
    body = [hero(f'{PAPERS[pno]["name"]} &mdash; Generated Set {g["set"]:02d}', f'{total} marks &middot; 3 hours &middot; <a style="color:#fff" href="../pdf/papers/{g["file"]}-QP.pdf">Question paper PDF</a> &middot; <a style="color:#fff" href="../pdf/papers/{g["file"]}-MS.pdf">Mark scheme PDF</a>',
                 crumbs=[("../papers.html", "Mock papers"), (None, f"Set {g['set']:02d}")], cls=f"p{pno} small")]
    body.append('<main><div class="wrap">')
    body.append('<div class="tools noprint"><span class="time" id="clock">3:00:00</span><button type="button" class="primary" id="startBtn">Start exam</button><button type="button" id="resetBtn">Reset timer</button>'
                f'<span class="score">Score <b id="scoreN">0</b>/{total} <span class="pct" id="scorePct">0%</span></span><button type="button" id="clearScore">Clear marks</button>'
                '<button type="button" data-reveal="1">Show all mark schemes</button><button type="button" data-print="qp">Print</button><button type="button" data-print="ms">Print + MS</button>'
                '<label class="modew"><input type="checkbox" class="modeW"> Write-first mode</label>'
                '<span class="kbd">Enter the marks you award yourself inside each mark scheme; the score is saved for this paper.</span></div>')
    body.append('<div class="jump noprint">' + "".join(f'<a href="#{q.id}">Q{i} &middot; {q.marks}</a>' for i, q in enumerate(g["questions"], 1)) + (f'<a href="#essay">Q{len(g["questions"]) + 1} &middot; essay</a>' if g["essays"] else "") + "</div>")
    for i, q in enumerate(g["questions"], 1):
        body.append(html_question(i, q, marking=True))
    if g["essays"]:
        n = len(g["questions"]) + 1
        body.append(f'<div class="q" id="essay"><div class="qh"><span class="num">Question {n} &mdash; Essay (answer ONE)</span><span class="meta">25 marks</span></div>')
        for k, e in enumerate(g["essays"], 1):
            body.append(f'<div class="part"><span class="marks">[25 marks]</span><span class="pn">{n:02d}.{k}</span>{fmt(e.title)}</div>')
            body.append('<details class="ms"><summary>Indicative content</summary>' + levels_table(LEVELS_25) + '<div class="lvl"><b>Indicative content</b> - students are not expected to cover all of these:</div><ul class="ind">' + "".join(f"<li>{fmt(m)}</li>" for m in e.indicative) +
                        f'</ul>' + exemplar_html(ESSAY_EXEMPLARS.get(e.id), essay=True) + f'<div class="aw"><label>Marks awarded <input class="aw-in" type="number" min="0" max="25" step="1" data-kind="essay" data-key="{e.id}"></label> / 25 (only the higher of the two essays counts)</div><div class="src">Source: {html.escape(BOOK)}, pp. {html.escape(e.pages)}; spec {html.escape(e.spec)}.</div></details>')
        body.append("</div>")
    body.append("</div></main>")
    return page(f"Generated Set {g['set']:02d}", "\n".join(body), root="../", extra_js=f"<script>{PAPER_JS % EXAM_SECONDS}</script>",
                body_attrs=f'data-paper="{g["file"]}" data-max="{total}"')


def essays_page(essays):
    body = [hero("Essay bank", "25-mark essay titles in the style of Question 11. Essays are marked with levels of response (L5 21&ndash;25 down to L1 1&ndash;5) and reward synoptic links across the specification.")]
    body.append('<main><div class="wrap">')
    for pno in (1, 2):
        body.append(f'<div class="paper-head"><span class="tag p{pno}">{PAPERS[pno]["name"]}</span><span class="assessed">{html.escape(PAPERS[pno]["assessed"])}</span></div>')
        for e in [x for x in essays if x.paper == pno]:
            body.append(f'<div class="q"><div class="qh"><span class="num">{fmt(e.title)}</span><span class="meta">spec {html.escape(e.spec)} &middot; Genn pp. {html.escape(e.pages)} &middot; {e.id}</span></div>'
                        '<details class="ms"><summary>Mark scheme and indicative content</summary>' + levels_table(LEVELS_25) + '<div class="lvl"><b>Indicative content</b> - students are not expected to cover all of these:</div><ul class="ind">' + "".join(f"<li>{fmt(m)}</li>" for m in e.indicative) + "</ul>" + exemplar_html(ESSAY_EXEMPLARS.get(e.id), essay=True) + "</details></div>")
    body.append("</div></main>")
    return page("Essay bank", "\n".join(body), active="essays.html")


def official_page(files):
    body = [hero("Official AQA past papers", "Every real AQA 7447 question paper and mark scheme published so far, plus the specimen papers, grouped by series. Sit them under timed conditions (3 hours, 120 marks) and mark with the official mark scheme. &copy; AQA.")]
    body.append('<main><div class="wrap">')
    if not files:
        body.append('<p class="note">No official papers found yet. Copy AQA PDFs into <code>official-papers/</code> and rebuild.</p>')
    series = {}
    for f in files:
        series.setdefault(f["series"], []).append(f)
    order = sorted(series, key=lambda s: ("00" if s == "SPECIMEN" else s[-2:], {"JUN": 1, "NOV": 2}.get(s[:3], 0)), reverse=True)
    for s in order:
        label = "Specimen papers" if s == "SPECIMEN" else {"JUN": "June 20", "NOV": "November 20"}.get(s[:3], "") + s[3:]
        body.append(f'<h2 class="sec">{html.escape(label)}</h2><table class="list"><tr><th>Paper</th><th>Document</th><th>File</th></tr>')
        for f in sorted(series[s], key=lambda f: (f["paper"], f["kind"])):
            body.append(f'<tr><td>{html.escape(f["paper"])}</td><td>{html.escape(f["kind"])}</td><td><a href="official/{html.escape(f["name"])}">{html.escape(f["name"])}</a></td></tr>')
        body.append("</table>")
    body.append("</div></main>")
    return page("Past papers", "\n".join(body), active="official.html")


# ---------- question data file (used by quick-fire and search) ----------
def qdata_js(sets_by_sub):
    idx = subtopic_index()
    rows = []
    for slug, sets in sets_by_sub.items():
        info = idx[slug]
        qn = 0
        for s in sets:
            for q in s:
                qn += 1
                text = " ".join([q.intro] + [p.text for p in q.parts] + [m for p in q.parts for m in p.ms])
                snippet = strip_tags(q.intro or q.parts[0].text)
                rows.append({"id": q.id, "sub": slug, "subname": info["name"], "topic": info["topic"], "tslug": info["topic_slug"], "papers": info["papers"],
                             "marks": q.marks, "flags": q_flags(q), "spec": q.spec, "pages": q.pages, "url": f"subtopic/{slug}.html#{q.id}",
                             "snippet": snippet[:180], "text": strip_tags(text).lower(), "html": html_question(qn, q)})
    # a relative link inside html_question points to ../subtopic/...; quick-fire lives at the site root
    for r in rows:
        r["html"] = r["html"].replace('href="../subtopic/', 'href="subtopic/')
    topics = [{"slug": t["slug"], "name": t["name"], "paper": pno} for pno, paper in PAPERS.items() for t in paper["topics"]]
    return "window.QBANK=" + json.dumps(rows, ensure_ascii=False) + ";\nwindow.QTOPICS=" + json.dumps(topics, ensure_ascii=False) + ";\n"


QUICKFIRE_JS = r"""
(function(){
const bank=window.QBANK,prog=window.ES.prog;const $=s=>document.querySelector(s);
const paperSel=$('#qfPaper'),topicSel=$('#qfTopic'),marksSel=$('#qfMarks'),skip=$('#qfSkip'),host=$('#qfHost'),stat=$('#qfStat');
const params=new URLSearchParams(location.search);
window.QTOPICS.forEach(t=>{const o=document.createElement('option');o.value=t.slug;o.textContent='Paper '+t.paper+' \u00b7 '+t.name;topicSel.appendChild(o);});
if(params.get('topic'))topicSel.value=params.get('topic');
if(params.get('sub')){const o=document.createElement('option');o.value='__sub';o.textContent='Selected subtopic only';topicSel.appendChild(o);topicSel.value='__sub';topicSel.disabled=true;}
let seen=[],cur=null,n=0;
const subParam=params.get('sub');
const dueOnly=params.get('due')==='1';
function pool(){const p=prog();return bank.filter(q=>(paperSel.value==='any'||q.papers.includes(+paperSel.value))&&(topicSel.value==='any'||topicSel.value==='__sub'||topicSel.value==='__due'||q.tslug===topicSel.value)&&(!subParam||q.sub===subParam)&&(marksSel.value==='any'||q.marks===+marksSel.value)
  &&!(skip.checked&&p[q.id]===2&&!window.ES.isDue(q.id))&&(!dueOnly||(p[q.id]===1||(p[q.id]===2&&window.ES.isDue(q.id)))));}
function next(){const p=pool();if(!p.length){host.innerHTML='<p class="empty">No questions match these filters (or you have marked them all secure - untick "skip secure").</p>';return;}
  let c=p.filter(q=>!seen.includes(q.id));if(!c.length){seen=[];c=p;}
  /* questions marked "needs work" are three times as likely to come up as untried ones */
  const pr=prog();const w=c.map(q=>pr[q.id]===1?3:(pr[q.id]===2?2:1));let r=Math.random()*w.reduce((a,b)=>a+b,0);cur=c[c.length-1];for(let i=0;i<c.length;i++){r-=w[i];if(r<0){cur=c[i];break;}}
  seen.push(cur.id);n++;
  host.innerHTML=cur.html;window.ES.paint();window.ES.applyMode();stat.textContent='Question '+n+' this session \u00b7 '+p.length+' in the pool';window.scrollTo({top:host.offsetTop-90,behavior:'smooth'});}
$('#qfNext').onclick=next;[paperSel,topicSel,marksSel,skip].forEach(e=>e.onchange=()=>{seen=[];stat.textContent=pool().length+' questions in the pool';});
document.addEventListener('keydown',e=>{if(e.target.matches('input,select,textarea'))return;if(e.key==='n'||e.key==='N'||e.key===' '){e.preventDefault();next();}
  if(e.key==='m'||e.key==='M'){const d=host.querySelector('details.ms');if(d)d.open=!d.open;}
  if(e.key==='1'||e.key==='2'){const b=host.querySelector('.st button[data-s="'+e.key+'"]');if(b)b.click();}});
stat.textContent=pool().length+' questions in the pool';
if(params.get('topic')||params.get('sub')||dueOnly)next();
if(dueOnly){const o=document.createElement('option');o.value='__due';o.textContent='Due for review only';topicSel.appendChild(o);topicSel.value='__due';topicSel.disabled=true;}
})();
"""

SEARCH_JS = r"""
(function(){
const bank=window.QBANK,$=s=>document.querySelector(s);const box=$('#sq'),out=$('#results'),paperSel=$('#sPaper'),marksSel=$('#sMarks'),flagSel=$('#sFlag');
const params=new URLSearchParams(location.search);if(params.get('q'))box.value=params.get('q');
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function hl(s,words){let e=esc(s);words.forEach(w=>{e=e.replace(new RegExp('('+w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig'),'<mark>$1</mark>');});return e;}
function run(){const words=box.value.toLowerCase().split(/\s+/).filter(Boolean);
  const res=bank.filter(q=>(paperSel.value==='any'||q.papers.includes(+paperSel.value))&&(marksSel.value==='any'||q.marks===+marksSel.value)&&(flagSel.value==='any'||q.flags.includes(flagSel.value))&&words.every(w=>q.text.includes(w)));
  if(!words.length&&paperSel.value==='any'&&marksSel.value==='any'&&flagSel.value==='any'){out.innerHTML='<p class="empty">Type a keyword (e.g. <i>eutrophication</i>, <i>albedo</i>, <i>Lincoln index</i>) to search every question and mark scheme.</p>';return;}
  if(!res.length){out.innerHTML='<p class="empty">Nothing found.</p>';return;}
  const p=window.ES.prog();
  out.innerHTML='<p class="kbd">'+res.length+' question'+(res.length===1?'':'s')+' found</p>'+res.slice(0,150).map(q=>{const s=p[q.id]===2?' \u00b7 <span style="color:var(--ok)">secure</span>':p[q.id]===1?' \u00b7 <span style="color:var(--warn)">needs work</span>':'';
    return '<a class="res" href="'+q.url+'"><div class="t">'+esc(q.subname)+' <span style="color:var(--stone);font-weight:400">('+q.id+', '+q.marks+' marks)</span></div><div class="m">Paper '+q.papers.join(' & ')+' \u00b7 '+esc(q.topic)+' \u00b7 spec '+esc(q.spec)+' \u00b7 Genn pp. '+esc(q.pages)+s+'</div><div class="s">'+hl(q.snippet,words)+'</div></a>';}).join('');}
box.addEventListener('input',run);[paperSel,marksSel,flagSel].forEach(e=>e.onchange=run);run();box.focus();
})();
"""


def quickfire_page():
    body = [hero("Quick-fire practice", "One random question at a time from the whole bank. Filter by paper, topic or mark size, reveal the mark scheme, then mark yourself <b>Needs work</b> or <b>Secure</b> - questions you have marked secure can be skipped so you spend time where it counts.")]
    body.append('<main><div class="wrap"><div class="qf-controls">'
                '<label>Paper <select id="qfPaper"><option value="any">Both papers</option><option value="1">Paper 1</option><option value="2">Paper 2</option></select></label>'
                '<label>Topic <select id="qfTopic"><option value="any">All topics</option></select></label>'
                '<label>Marks <select id="qfMarks"><option value="any">Any</option><option value="5">5</option><option value="10">10</option><option value="15">15</option></select></label>'
                '<label><input type="checkbox" id="qfSkip" checked> Skip secure questions until they are due for review</label><label class="modew"><input type="checkbox" class="modeW"> Write-first mode</label>'
                '<button type="button" class="btn" id="qfNext">Next question &rarr;</button><span class="kbd" id="qfStat"></span></div>'
                '<p class="kbd">Shortcuts: <kbd>N</kbd> or <kbd>space</kbd> next question &middot; <kbd>M</kbd> toggle mark scheme &middot; <kbd>1</kbd> needs work &middot; <kbd>2</kbd> secure</p>'
                '<div id="qfHost"><p class="empty">Press <b>Next question</b> to begin.</p></div></div></main>')
    return page("Quick-fire", "\n".join(body), active="quickfire.html", extra_js=f'<script src="qdata.js"></script><script>{QUICKFIRE_JS}</script>')


def search_page():
    body = [hero("Search the question bank", "Search every question, figure and mark scheme by keyword. Results link straight to the question on its subtopic page.")]
    body.append('<main><div class="wrap"><div class="qf-controls"><input type="search" id="sq" placeholder="e.g. Simpson, catalytic converter, tipping point" style="flex:1 1 320px">'
                '<label>Paper <select id="sPaper"><option value="any">Both</option><option value="1">Paper 1</option><option value="2">Paper 2</option></select></label>'
                '<label>Marks <select id="sMarks"><option value="any">Any</option><option value="5">5</option><option value="10">10</option><option value="15">15</option></select></label>'
                '<label>Type <select id="sFlag"><option value="any">Any</option>' + "".join(f'<option value="{k}">{v}</option>' for k, v in FLAG_NAMES.items()) + '</select></label></div>'
                '<div id="results"></div></div></main>')
    return page("Search", "\n".join(body), active="search.html", extra_js=f'<script src="qdata.js"></script><script>{SEARCH_JS}</script>')


# ---------- real AQA past-paper questions by topic ----------
def _series_label(name):
    m = re.search(r"-(JUN|NOV)(\d\d)", name)
    if m:
        return ("June " if m.group(1) == "JUN" else "November ") + "20" + m.group(2)
    return "Specimen"


def _ms_for(qp_name, official):
    """Find the mark-scheme file for a question paper (same paper number and series)."""
    m = re.match(r"AQA-(7447\d)-(?:QP-(\w{5})|SQP)", qp_name)
    if not m:
        return None
    code, series = m.group(1), m.group(2)
    for f in official:
        n = f["name"].upper()
        if series and re.match(rf"AQA-{code}-(W-)?MS-{series}", n):
            return f["name"]
        if not series and n.startswith(f"AQA-{code}-SMS"):
            return f["name"]
    return None


OFFICIAL_FILES = []   # set by build.py before pages are rendered


def official_rows(slug, root="../"):
    idx = subtopic_index()
    rows = []
    for fname, entries in OFFICIAL_INDEX.items():
        pno = fname[8]
        ms = _ms_for(fname, OFFICIAL_FILES)
        for qn, page, marks, sub, title in entries:
            if sub != slug:
                continue
            kind = "Essay" if qn == 11 else f"Q{qn}"
            links = f'<a href="{root}official/{fname}#page={page}">Question (p.{page})</a>'
            if ms:
                links += f' <a href="{root}official/{ms}">Mark scheme</a>'
            rows.append((fname, qn, f'<div class="row"><span class="ser">{_series_label(fname)} &middot; Paper {pno}</span><span class="qn">{kind} &middot; {marks} marks</span><span class="t">{html.escape(title)}</span>{links}</div>'))
    def key(r):
        m = re.search(r"-(JUN|NOV)(\d\d)", r[0])
        return ((int(m.group(2)), 1 if m.group(1) == "JUN" else 2) if m else (0, 0), r[1])
    rows.sort(key=key, reverse=True)
    return [r[2] for r in rows]


def official_counts():
    c = {}
    for entries in OFFICIAL_INDEX.values():
        for qn, page, marks, sub, title in entries:
            c[sub] = c.get(sub, 0) + 1
    return c


def pastq_page():
    idx = subtopic_index()
    counts = official_counts()
    total = sum(len(v) for v in OFFICIAL_INDEX.values())
    body = [hero("Real AQA questions by topic", f"Every question from the {len(OFFICIAL_INDEX)} published AQA 7447 papers ({total} questions and essay titles), sorted by specification topic. Each link opens the official paper at the right page; the mark scheme link opens AQA's mark scheme for that paper. Use it to see how a topic is really examined, then compare with the practice sets.")]
    body.append('<main><div class="wrap">')
    body.append('<div class="jump noprint">' + "".join(f'<a href="#{t["slug"]}">{html.escape(t["name"])}</a>' for pno, paper in PAPERS.items() for t in paper["topics"] if not (pno == 2 and t["slug"] == "research")) + "</div>")
    seen = set()
    for pno, paper in PAPERS.items():
        for t in paper["topics"]:
            if t["slug"] in seen:
                continue
            seen.add(t["slug"])
            body.append(f'<h2 class="sec" id="{t["slug"]}">{html.escape(t["name"])}</h2>')
            for slug, name, spec, pages in t["subtopics"]:
                rows = official_rows(slug, root="")
                body.append(f'<h3 style="margin:16px 0 4px;color:var(--head)"><a href="subtopic/{slug}.html" style="text-decoration:none;color:inherit">{html.escape(name)}</a> <span style="font-size:.85rem;color:var(--stone);font-weight:400">spec {spec} &middot; {len(rows)} question{"s" if len(rows) != 1 else ""}</span></h3>')
                body.append('<div class="real">' + ("".join(rows) if rows else '<div class="row empty">Not yet examined in a published paper - a likely candidate for future series.</div>') + "</div>")
    body.append("</div></main>")
    return page("Real AQA questions by topic", "\n".join(body), active="pastq.html")


# ---------- revision planner ----------
PLANNER_JS = r"""
(function(){
const LS=window.ES.LS,SV=window.ES.SV,prog=window.ES.prog();const subs=window.PSUBS;
/* exam countdown */
const dIn=document.getElementById('examDate'),out=document.getElementById('countdown');
const saved=LS('envsci.examdate');if(saved)dIn.value=saved;
function cd(){if(!dIn.value){out.textContent='Set your first exam date to see the countdown.';return;}const d=Math.ceil((new Date(dIn.value)-new Date())/86400000);
  out.innerHTML=d<0?'Exam date has passed.':'<span class="big">'+d+'</span> day'+(d===1?'':'s')+' to go'+(d>0?' &middot; about '+Math.max(1,Math.round(d/7))+' week'+(Math.round(d/7)===1?'':'s'):'');}
dIn.onchange=()=>{SV('envsci.examdate',dIn.value);cd();};cd();
/* due for review */
const allIds=subs.flatMap(s=>s.ids);const due=allIds.filter(i=>prog[i]===2&&window.ES.isDue(i)).length,work=allIds.filter(i=>prog[i]===1).length;
document.getElementById('due').innerHTML=(due+work)?'<span class="big">'+(due+work)+'</span> to review today: '+work+' marked needs work, '+due+' secure questions due for a spaced review. <a class="btn" href="quickfire.html?due=1">Review now</a>':'<span class="big">0</span> due today - nothing is waiting for review.';
/* weakest subtopics */
const rows=subs.map(s=>{const ok=s.ids.filter(i=>prog[i]===2).length,wk=s.ids.filter(i=>prog[i]===1).length;return {...s,ok,wk,pct:s.ids.length?ok/s.ids.length:0};});
rows.sort((a,b)=>a.pct-b.pct||b.real-a.real);
document.getElementById('weak').innerHTML=rows.map(s=>'<tr><td><a href="subtopic/'+s.slug+'.html">'+s.name+'</a><br><span style="font-size:.8rem;color:var(--stone)">'+s.topic+' &middot; Paper '+s.papers.join(' & ')+'</span></td>'+
  '<td><div class="bar"><div class="ok" style="width:'+(100*s.ok/s.ids.length)+'%"></div><div class="wk" style="width:'+(100*s.wk/s.ids.length)+'%"></div></div><span style="font-size:.8rem;color:var(--stone)">'+s.ok+'/'+s.ids.length+' secure'+(s.wk?', '+s.wk+' to revisit':'')+'</span></td>'+
  '<td>'+s.real+'</td><td><a class="btn ghost" style="padding:4px 10px;font-size:.82rem" href="quickfire.html?sub='+s.slug+'">Practise</a></td></tr>').join('');
/* mock scores */
const sc=LS('envsci.scores')||{};const keys=Object.keys(sc).filter(k=>sc[k].total!==undefined).sort((a,b)=>(sc[b].when||0)-(sc[a].when||0));
const mock=document.getElementById('mocks');
if(!keys.length)mock.innerHTML='<p class="empty">No mock papers marked yet - open a paper from <a href="papers.html">Mock papers</a>, sit it with the timer and enter your marks.</p>';
else{const avg=p=>{const k=keys.filter(x=>x.startsWith('P'+p));return k.length?Math.round(100*k.reduce((a,x)=>a+sc[x].total/sc[x].max,0)/k.length):null;};
  mock.innerHTML='<p><b>Average:</b> Paper 1 '+(avg(1)===null?'&ndash;':avg(1)+'%')+' &middot; Paper 2 '+(avg(2)===null?'&ndash;':avg(2)+'%')+'</p><table class="list"><tr><th>Paper</th><th>Score</th><th>When</th></tr>'+
  keys.map(k=>{const s=sc[k];const pc=Math.round(100*s.total/s.max);return '<tr><td><a href="paper/'+k+'.html">'+k.replace('P','Paper ').replace('-Set',' - Set ')+'</a></td><td><b>'+s.total+'</b>/'+s.max+' ('+pc+'%)</td><td>'+(s.when?new Date(s.when).toLocaleDateString():'')+'</td></tr>';}).join('')+'</table>';}
/* suggestions */
const sug=document.getElementById('sug');const weakest=rows.filter(s=>s.pct<0.5).slice(0,3);
sug.innerHTML='<ol>'+(weakest.length?weakest.map(s=>'<li>Work through <a href="subtopic/'+s.slug+'.html">'+s.name+'</a>'+(s.real?' - examined '+s.real+' time'+(s.real===1?'':'s')+' in real papers':'')+'.</li>').join(''):'<li>Every subtopic is at least half secure - sit a full timed mock next.</li>')+
  '<li>Do a 15-minute <a href="quickfire.html">Quick-fire</a> session; questions you marked <i>needs work</i> come up three times as often.</li><li>Sit one full <a href="papers.html">mock paper</a> a week under timed conditions and enter your marks.</li></ol>';
})();
"""


def planner_page(sets_by_sub, counts_real):
    idx = subtopic_index()
    subs = [{"slug": slug, "name": idx[slug]["name"], "topic": idx[slug]["topic"], "papers": idx[slug]["papers"], "ids": [q.id for s in sets for q in s], "real": counts_real.get(slug, 0)}
            for slug, sets in sets_by_sub.items()]
    body = [hero("Revision planner", "Your weakest subtopics first, how often each has come up in real AQA papers, your mock-paper scores and a countdown to the exam. Everything here is built from the progress you mark on the site.")]
    body.append('<main><div class="wrap plan"><div class="grid3">'
                '<div class="card"><h3>Exam countdown</h3><p><label>First exam date <input type="date" id="examDate"></label></p><p id="countdown"></p></div>'
                '<div class="card"><h3>Spaced review</h3><p id="due"></p><p class="due">Secure questions come back after 1, 3, 7, 14 and 30 days; get them right each time and the gap grows.</p></div>'
                '<div class="card"><h3>What to do next</h3><div id="sug"></div></div></div>')
    body.append('<h2 class="sec">Subtopics, weakest first</h2><table class="list"><tr><th>Subtopic</th><th>Your progress</th><th>Times in real papers</th><th></th></tr><tbody id="weak"></tbody></table>')
    body.append('<h2 class="sec">Mock-paper scores</h2><div id="mocks"></div>')
    body.append("</div></main>")
    return page("Revision planner", "\n".join(body), active="planner.html", extra_js="<script>window.PSUBS=" + json.dumps(subs) + ";" + PLANNER_JS + "</script>")


# ---------- practice hub ----------
def practice_page(counts):
    modes = [
        ("&#9889;", "Quick-fire", "quickfire.html", "One random question at a time from the whole bank, filtered by paper, topic or marks. Questions you mark <i>needs work</i> come up three times as often, and secure questions return after 1, 3, 7, 14 and 30 days."),
        ("&#9998;", "Write-first mode", "quickfire.html", "Tick <b>Write-first mode</b> on any question page (quick-fire, subtopic pages, mock papers). Answer boxes appear under every part and the mark scheme stays hidden until you reveal it; then you self-mark against the point-by-point scheme and your status is set automatically."),
        ("&#128203;", "Definitions drill", "terms.html", f"Question 1 of every real paper is a 5-mark table of terms and definitions. Flashcards and a timed table test on {counts['terms']} key terms from every subtopic, with spaced repetition."),
        ("&#128290;", "Calculations", "calc.html", "Fresh numbers every time: percentage change, standard form, Lincoln index, energy ratios, Simpson's index, residence time, USLE, half-lives, decibels and more, each with worked solutions."),
        ("&#128214;", "Model answers", "essays.html", "Every 9-mark question has a Level 3 model answer beside a weaker one, with notes on what makes the difference - open <i>Model answers</i> inside its mark scheme. Two full Level 5 essays are in the essay bank."),
        ("&#127891;", "Real questions by topic", "pastq.html", "All 132 questions from the published AQA papers indexed by subtopic, each linking to the official paper and mark scheme."),
        ("&#9203;", "Timed mock papers", "papers.html", f"{counts['papers']} generated papers in exact AQA format with a 3-hour timer and a self-marking scorecard."),
    ]
    body = [hero("Practice modes", "Different ways to use the same question bank. Read-and-check is the default everywhere; the modes below are there when you want retrieval practice, drills or timed conditions.")]
    body.append('<main><div class="wrap">' + "".join(f'<a class="modecard" href="{h}" style="text-decoration:none;color:inherit"><div class="mi">{i}</div><div><h3>{t}</h3><p>{d}</p></div></a>' for i, t, h, d in modes) + "</div></main>")
    return page("Practice modes", "\n".join(body), active="practice.html")


# ---------- definitions drill ----------
TERMS_JS = r"""
(function(){
const T=window.TERMS,LS=window.ES.LS,SV=window.ES.SV,$=s=>document.querySelector(s);
const paperSel=$('#tPaper'),topicSel=$('#tTopic'),host=$('#tHost'),stat=$('#tStat');
window.QTOPICS.forEach(t=>{const o=document.createElement('option');o.value=t.slug;o.textContent='Paper '+t.paper+' \u00b7 '+t.name;topicSel.appendChild(o);});
const params=new URLSearchParams(location.search);if(params.get('topic'))topicSel.value=params.get('topic');
let box=LS('envsci.terms')||{};   /* key -> {lvl 0-4, due} */
const IVL=[0,1,3,7,14];
function pool(){return T.filter(t=>(paperSel.value==='any'||t.papers.includes(+paperSel.value))&&(topicSel.value==='any'||t.tslug===topicSel.value));}
function dueList(p){const now=Date.now();return p.filter(t=>{const b=box[t.key];return !b||b.due<=now;});}
function norm(s){return s.toLowerCase().replace(/\(.*?\)/g,'').replace(/[^a-z0-9 ]/g,' ').replace(/\s+/g,' ').trim();}
function match(typed,term){const a=norm(typed),b=norm(term);if(!a)return false;if(a===b)return true;const alts=term.split('/').map(norm);if(alts.some(x=>x&&x===a))return true;
  const kw=b.split(' ').filter(w=>w.length>3);return kw.length>0&&kw.every(w=>a.includes(w.slice(0,Math.max(4,w.length-2))));}
let mode='cards',cur=null,n=0,right=0,test=[];
function grade(t,ok){const b=box[t.key]||{lvl:0};b.lvl=ok?Math.min(4,b.lvl+1):0;b.due=Date.now()+IVL[b.lvl]*86400000;box[t.key]=b;SV('envsci.terms',box);}
function card(){const p=pool();let c=dueList(p);if(!c.length)c=p;if(!c.length){host.innerHTML='<p class="empty">No terms match.</p>';return;}
  cur=c[Math.floor(Math.random()*c.length)];n++;
  host.innerHTML='<div class="drill"><div class="src">'+cur.subname+' \u00b7 Paper '+cur.papers.join(' & ')+' \u00b7 Genn pp. '+cur.pages+'</div><div class="term">'+cur.term+'</div><div class="def" id="def" hidden>'+cur.def+'</div>'+
    '<div class="btns"><button type="button" class="btn" id="show">Show definition</button><span id="grade" hidden><button type="button" class="btn ghost" id="again">Again</button> <button type="button" class="btn" id="got">Got it</button></span></div></div>';
  $('#show').onclick=()=>{$('#def').hidden=false;$('#show').hidden=true;$('#grade').hidden=false;};
  $('#again').onclick=()=>{grade(cur,false);card();};$('#got').onclick=()=>{grade(cur,true);right++;card();};
  stat.textContent=n+' seen this session \u00b7 '+dueList(p).length+' due of '+p.length;}
function table(){const p=pool();if(p.length<5){host.innerHTML='<p class="empty">Not enough terms in this filter.</p>';return;}
  test=[...p].sort(()=>Math.random()-0.5).slice(0,5);
  host.innerHTML='<div class="drill"><p><b>Complete the table</b> - write the term that matches each definition (5 marks, as in Question 1 of the real papers).</p><table class="list">'+
    test.map((t,i)=>'<tr><td style="width:60%">'+t.def+'</td><td><input class="ans" data-i="'+i+'" placeholder="Term"></td></tr>').join('')+'</table><div class="btns"><button type="button" class="btn" id="check">Check answers</button></div><div id="tres"></div></div>';
  $('#check').onclick=()=>{let sc=0;host.querySelectorAll('input.ans').forEach(inp=>{const t=test[+inp.dataset.i];const ok=match(inp.value,t.term);if(ok)sc++;grade(t,ok);inp.style.borderColor=ok?'var(--ok)':'var(--bad)';inp.insertAdjacentHTML('afterend','<div class="fb '+(ok?'ok':'bad')+'">'+(ok?'\u2713 ':'\u2717 ')+t.term+'</div>');});
    $('#tres').innerHTML='<p class="fb '+(sc>=4?'ok':'bad')+'">'+sc+' / 5</p><button type="button" class="btn" id="again2">Another table</button>';$('#again2').onclick=table;$('#check').disabled=true;};}
document.querySelectorAll('[data-tmode]').forEach(b=>b.onclick=()=>{mode=b.dataset.tmode;document.querySelectorAll('[data-tmode]').forEach(x=>x.classList.toggle('on',x===b));mode==='cards'?card():table();});
[paperSel,topicSel].forEach(e=>e.onchange=()=>{mode==='cards'?card():table();});
document.addEventListener('keydown',e=>{if(mode!=='cards'||e.target.matches('input,textarea'))return;if(e.key===' '){e.preventDefault();const s=$('#show');if(s&&!s.hidden)s.click();}if(e.key==='1'){const a=$('#again');if(a&&!$('#grade').hidden)a.click();}if(e.key==='2'){const g=$('#got');if(g&&!$('#grade').hidden)g.click();}});
card();
})();
"""


def terms_page():
    idx = subtopic_index()
    rows = []
    for slug, items in TERMS.items():
        info = idx[slug]
        for term, d in items:
            rows.append({"key": f"{slug}|{term}", "term": term, "def": d, "sub": slug, "subname": info["name"], "tslug": info["topic_slug"], "papers": info["papers"], "pages": info["pages"]})
    topics = [{"slug": t["slug"], "name": t["name"], "paper": pno} for pno, paper in PAPERS.items() for t in paper["topics"]]
    body = [hero("Definitions drill", f"{len(rows)} key terms from every subtopic, defined from the textbook. Flashcards use spaced repetition (a term you get right comes back after 1, 3, 7 then 14 days); the table test copies Question 1 of the real papers.")]
    body.append('<main><div class="wrap"><div class="qf-controls">'
                '<button type="button" class="chip on" data-tmode="cards">Flashcards</button><button type="button" class="chip" data-tmode="table">Table test (5 marks)</button>'
                '<label>Paper <select id="tPaper"><option value="any">Both</option><option value="1">Paper 1</option><option value="2">Paper 2</option></select></label>'
                '<label>Topic <select id="tTopic"><option value="any">All topics</option></select></label><span class="kbd" id="tStat"></span></div>'
                '<p class="kbd">Flashcards: <kbd>space</kbd> show definition &middot; <kbd>1</kbd> again &middot; <kbd>2</kbd> got it</p><div id="tHost"></div></div></main>')
    return page("Definitions drill", "\n".join(body), active="practice.html",
                extra_js="<script>window.TERMS=" + json.dumps(rows, ensure_ascii=False) + ";window.QTOPICS=" + json.dumps(topics) + ";" + TERMS_JS + "</script>")


def terms_count():
    return sum(len(v) for v in TERMS.values())


# ---------- calculations drill ----------
CALC_JS = r"""
(function(){
const $=s=>document.querySelector(s);const R=(a,b)=>a+Math.random()*(b-a);const ri=(a,b)=>Math.floor(R(a,b+1));const r1=x=>Math.round(x*10)/10,r2=x=>Math.round(x*100)/100,sf3=x=>+x.toPrecision(3);
const G={
 pct:{name:'Percentage change',pages:'89-103',make(){const a=ri(280,330),b=a+ri(60,140);return {q:'Atmospheric CO<sub>2</sub> concentration rose from '+a+' ppm to '+b+' ppm. Calculate the percentage increase. Give your answer to one decimal place.',unit:'%',ans:r1((b-a)/a*100),tol:0.15,work:'Increase = '+b+' - '+a+' = '+(b-a)+' ppm\n% increase = '+(b-a)+' / '+a+' x 100 = '+r1((b-a)/a*100)+'%'};}},
 pctdec:{name:'Percentage decrease',pages:'275-277',make(){const a=ri(12,20),b=r1(R(1.5,4));return {q:'Mean blood lead concentration in children fell from '+a+' &micro;g dl<sup>-1</sup> to '+b+' &micro;g dl<sup>-1</sup> after lead was removed from petrol. Calculate the percentage decrease.',unit:'%',ans:r1((a-b)/a*100),tol:0.15,work:'Decrease = '+a+' - '+b+' = '+r1(a-b)+'\n% decrease = '+r1(a-b)+' / '+a+' x 100 = '+r1((a-b)/a*100)+'%'};}},
 sf:{name:'Standard form',pages:'148-151',make(){const gt=ri(600,900);return {q:'The atmosphere holds about '+gt+' Gt (gigatonnes) of carbon. 1 Gt = 10<sup>9</sup> tonnes. Give this mass in tonnes in standard form (enter as e.g. 7.5e11).',unit:'tonnes',ans:gt*1e9,tol:0.005,work:gt+' x 10^9 = '+(gt/100).toFixed(2)+' x 10^11 tonnes = '+sf3(gt*1e9).toExponential(2)};}},
 lincoln:{name:'Lincoln index',pages:'401-402',make(){const m=ri(20,60),c=ri(25,70),r=ri(4,Math.min(m,c)-2);return {q:'In a mark-release-recapture study '+m+' woodlice were caught, marked and released. Later '+c+' were caught, of which '+r+' were marked. Estimate the population size.',unit:'',ans:Math.round(m*c/r),tol:0.02,work:'N = (M x C) / R = ('+m+' x '+c+') / '+r+' = '+r1(m*c/r)+' \u2248 '+Math.round(m*c/r)};}},
 eratio:{name:'Energy ratio',pages:'325-326',make(){const inp=ri(8,40),out=r1(inp*R(0.2,4));return {q:'A farming system uses '+inp+' GJ ha<sup>-1</sup> of energy inputs and produces '+out+' GJ ha<sup>-1</sup> of food energy. Calculate the energy ratio to two decimal places.',unit:'',ans:r2(out/inp),tol:0.02,work:'Energy ratio = output / input = '+out+' / '+inp+' = '+r2(out/inp)+(out/inp<1?'\nLess than 1: more energy is put in than comes out (typical of intensive livestock systems)':'')};}},
 fcr:{name:'Food conversion ratio',pages:'326',make(){const feed=ri(40,200),gain=r1(feed/R(1.2,8));return {q:'Farmed fish were fed '+feed+' kg of feed and gained '+gain+' kg in mass. Calculate the food conversion ratio to one decimal place.',unit:'',ans:r1(feed/gain),tol:0.03,work:'FCR = feed mass / mass gained = '+feed+' / '+gain+' = '+r1(feed/gain)+'\n(the lower the FCR, the better the conversion)'};}},
 simpson:{name:"Simpson's index of diversity",pages:'402',make(){const ns=[ri(20,50),ri(10,40),ri(5,30),ri(2,20)];const N=ns.reduce((a,b)=>a+b,0);const sum=ns.reduce((a,n)=>a+n*(n-1),0);const D=N*(N-1)/sum;return {q:'A quadrat survey found four species with '+ns.join(', ')+' individuals (total N = '+N+'). Using D = N(N-1) / &Sigma;n(n-1), calculate Simpson\'s index of diversity to two decimal places.',unit:'',ans:r2(D),tol:0.02,work:'\u03a3n(n-1) = '+ns.map(n=>n+'x'+(n-1)).join(' + ')+' = '+sum+'\nN(N-1) = '+N+' x '+(N-1)+' = '+N*(N-1)+'\nD = '+N*(N-1)+' / '+sum+' = '+r2(D)};}},
 res:{name:'Residence time',pages:'116-117',make(){const vol=ri(8,20)*1000,flow=ri(300,600);return {q:'A lake holds '+vol+' x 10<sup>6</sup> m<sup>3</sup> of water and the river flowing out of it carries '+flow+' x 10<sup>6</sup> m<sup>3</sup> per year. Calculate the mean residence time of water in the lake to one decimal place.',unit:'years',ans:r1(vol/flow),tol:0.03,work:'Residence time = volume / flow rate = '+vol+' / '+flow+' = '+r1(vol/flow)+' years'};}},
 usle:{name:'Universal Soil Loss Equation',pages:'162-164',make(){const Rf=ri(80,300),K=r2(R(0.1,0.5)),LS_=r1(R(0.5,3)),C=r2(R(0.05,0.6)),P=[1,0.5,0.25][ri(0,2)];const A=Rf*K*LS_*C*P;return {q:'Use the USLE, A = R x K x LS x C x P, with R = '+Rf+', K = '+K+', LS = '+LS_+', C = '+C+' and P = '+P+'. Calculate the predicted soil loss A to one decimal place.',unit:'t ha<sup>-1</sup> yr<sup>-1</sup>',ans:r1(A),tol:0.03,work:'A = '+Rf+' x '+K+' x '+LS_+' x '+C+' x '+P+' = '+r1(A)+' t/ha/yr'+(P<1?'\n(P below 1 shows that contour ploughing / terracing reduces the loss)':'')};}},
 edens:{name:'Energy density',pages:'175-177',make(){const mass=ri(2,12),e=ri(60,500);return {q:'A '+mass+' kg sample of biomass fuel releases '+e+' MJ when burnt. Calculate its energy density in MJ kg<sup>-1</sup> to one decimal place.',unit:'MJ kg<sup>-1</sup>',ans:r1(e/mass),tol:0.03,work:'Energy density = energy / mass = '+e+' / '+mass+' = '+r1(e/mass)+' MJ/kg'};}},
 half:{name:'Radioactive half-life',pages:'296-299',make(){const n=ri(2,5),hl=[8,30,5.3,28][ri(0,3)],start=ri(200,900);return {q:'A sample contains '+start+' Bq of an isotope with a half-life of '+hl+' years. What activity remains after '+(n*hl)+' years?',unit:'Bq',ans:r1(start/Math.pow(2,n)),tol:0.03,work:(n*hl)+' / '+hl+' = '+n+' half-lives\nRemaining = '+start+' / 2^'+n+' = '+start+' / '+Math.pow(2,n)+' = '+r1(start/Math.pow(2,n))+' Bq'};}},
 db:{name:'Decibel scale',pages:'286-288',make(){const d=[10,20,30][ri(0,2)];const a=ri(50,80);return {q:'Road noise at a house is '+(a+d)+' dB. An acoustic barrier reduces it to '+a+' dB. By what factor has the sound intensity been reduced? (Every 10 dB is a factor of 10.)',unit:'times',ans:Math.pow(10,d/10),tol:0.01,work:'Reduction = '+d+' dB = '+(d/10)+' x 10 dB\nIntensity factor = 10^'+(d/10)+' = '+Math.pow(10,d/10)};}},
 eff:{name:'Efficiency',pages:'178-179',make(){const inp=ri(200,900),out=Math.round(inp*R(0.3,0.6));return {q:'A power station uses fuel with an energy content of '+inp+' MJ to generate '+out+' MJ of electricity. Calculate its efficiency to one decimal place.',unit:'%',ans:r1(out/inp*100),tol:0.15,work:'Efficiency = useful output / input x 100 = '+out+' / '+inp+' x 100 = '+r1(out/inp*100)+'%'};}},
 ap:{name:'Area : perimeter ratio',pages:'41-42',make(){const w=ri(40,120),h=ri(40,120);const ap=(w*h)/(2*(w+h));return {q:'A rectangular nature reserve is '+w+' m by '+h+' m. Calculate its area : perimeter ratio to one decimal place (as a value : 1).',unit:': 1',ans:r1(ap),tol:0.03,work:'Area = '+w+' x '+h+' = '+w*h+' m\u00b2\nPerimeter = 2 x ('+w+' + '+h+') = '+2*(w+h)+' m\nRatio = '+w*h+' / '+2*(w+h)+' = '+r1(ap)+' : 1\n(a larger ratio means less edge effect)'};}},
 growth:{name:'Population growth rate',pages:'78-80',make(){const b=ri(18,45),d=ri(5,20),pop=ri(2,9)*1000;return {q:'A population of '+pop+' has a birth rate of '+b+' per 1000 per year and a death rate of '+d+' per 1000 per year. Calculate the population after one year.',unit:'',ans:Math.round(pop*(1+(b-d)/1000)),tol:0.005,work:'Growth rate = '+b+' - '+d+' = '+(b-d)+' per 1000 = '+((b-d)/10)+'%\nIncrease = '+pop+' x '+(b-d)+'/1000 = '+pop*(b-d)/1000+'\nPopulation = '+Math.round(pop*(1+(b-d)/1000))};}},
 mean:{name:'Mean and standard deviation check',pages:'420',make(){const v=[ri(10,30),ri(10,30),ri(10,30),ri(10,30),ri(10,30)];const m=v.reduce((a,b)=>a+b,0)/5;return {q:'Five quadrats gave counts of '+v.join(', ')+'. Calculate the mean to one decimal place.',unit:'',ans:r1(m),tol:0.03,work:'Mean = ('+v.join(' + ')+') / 5 = '+v.reduce((a,b)=>a+b,0)+' / 5 = '+r1(m)};}},
};
const keys=Object.keys(G);const sel=$('#cType');keys.forEach(k=>{const o=document.createElement('option');o.value=k;o.textContent=G[k].name;sel.appendChild(o);});
const host=$('#cHost'),stat=$('#cStat');let cur=null,n=0,right=0,answered=0;let hist=window.ES.LS('envsci.calc')||{};
function next(){const k=sel.value==='any'?keys[Math.floor(Math.random()*keys.length)]:sel.value;cur=G[k].make();cur.k=k;n++;
  host.innerHTML='<div class="drill"><div class="src">'+G[k].name+' \u00b7 Genn pp. '+G[k].pages+'</div><p class="def">'+cur.q+'</p><div class="btns"><input class="ans" id="cAns" placeholder="Your answer" autocomplete="off"> <span>'+cur.unit+'</span></div><div class="btns"><button type="button" class="btn" id="cCheck">Check</button><button type="button" class="btn ghost" id="cShow">Show working</button><button type="button" class="btn ghost" id="cNext">Next &rarr;</button></div><div id="cFb"></div></div>';
  $('#cAns').focus();$('#cCheck').onclick=check;$('#cShow').onclick=()=>show(false);$('#cNext').onclick=next;$('#cAns').addEventListener('keydown',e=>{if(e.key==='Enter')check();});
  stat.textContent=right+' / '+answered+' correct this session';}
function show(ok){const fb=$('#cFb');fb.innerHTML=(ok===true?'<div class="fb ok">\u2713 Correct: '+cur.ans+' '+cur.unit+'</div>':ok===false?'<div class="fb bad">\u2717 Answer: '+cur.ans+' '+cur.unit+'</div>':'')+'<div class="work">'+cur.work+'</div>';}
function check(){const v=parseFloat(($('#cAns').value||'').replace(/,/g,'').replace(/x ?10\^/i,'e'));if(isNaN(v)){$('#cFb').innerHTML='<div class="fb bad">Enter a number</div>';return;}
  const ok=Math.abs(v-cur.ans)<=Math.max(Math.abs(cur.ans)*cur.tol,0.051);if(ok)right++;answered++;const h=hist[cur.k]||{n:0,ok:0};h.n++;if(ok)h.ok++;hist[cur.k]=h;window.ES.SV('envsci.calc',hist);show(ok);$('#cCheck').disabled=true;stat.textContent=right+' / '+answered+' correct this session';
  $('#cHist').innerHTML=keys.filter(k=>hist[k]).map(k=>G[k].name+': '+hist[k].ok+'/'+hist[k].n).join(' \u00b7 ');}
sel.onchange=next;$('#cHist').innerHTML=keys.filter(k=>hist[k]).map(k=>G[k].name+': '+hist[k].ok+'/'+hist[k].n).join(' \u00b7 ');next();
})();
"""


def calc_page():
    body = [hero("Calculations", "The real papers are heavier on maths than most students expect. Every question here is generated with fresh numbers, so you can practise the method until the working is automatic. Answers are checked with a small tolerance; each shows the worked solution and the textbook pages the method comes from.")]
    body.append('<main><div class="wrap"><div class="qf-controls"><label>Type <select id="cType"><option value="any">Random mix</option></select></label><span class="kbd" id="cStat"></span></div>'
                '<p class="kbd">Type the answer and press <kbd>Enter</kbd>. Standard form can be entered as 7.5e11.</p><div id="cHost"></div><p class="kbd" id="cHist"></p></div></main>')
    return page("Calculations", "\n".join(body), active="practice.html", extra_js=f"<script>{CALC_JS}</script>")
