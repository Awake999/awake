#!/usr/bin/env python3
"""Build ops/data/funnel_explorer_2026-08-31.html from funnel_explorer_data.json.
Layout law (Alan 8/31): the ENTIRE funnel — every stage, every segment, every NAME —
sits at the very top on one screen; details + proof links live below via anchors."""
import json, re, os

D = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'data', 'funnel_explorer_data.json')))
G, O, P = D['G'], D['O'], D['P']

def slug(n): return re.sub(r'[^a-z]+', '-', n.lower()).strip('-')

OC = {"showed": ("✅ SHOWED", "#16a34a"), "noshow": ("❌ NO-SHOW", "#dc2626"),
      "cancelled": ("🚫 CANCELLED", "#d97706"), "unresolved": ("❓ UNRESOLVED", "#7c3aed"),
      "optin": ("📥 NEVER BOOKED", "#64748b")}
PC = {"direct": "⚡ Direct to Booking", "later": "📞 Triage → Call Booked",
      "never": "Opt-in only", "referral": "➕ Referral"}
TR = {"tag": "Lynn's 'triaged' tag [V]", "attested": "Alan-attested triage",
      "tag+attested": "Lynn's tag [V] + Alan-attested", "": ""}

by = {p[0]: p for p in P}
def chips(names, mark=None):
    out = []
    for n in names:
        col = OC[by[n][1]][1]
        star = mark(n) if mark else ''
        out.append(f'<a class="chip" style="border-color:{col};color:{col}" href="#{slug(n)}">{n}{star}</a>')
    return ''.join(out)

# segment name lists (derived from data)
direct = [p[0] for p in P if p[2] == 'direct']
later = [p[0] for p in P if p[2] == 'later']
never = [p[0] for p in P if p[2] == 'never']
d_tri = [n for n in direct if by[n][3]]            # triaged (tag/attested)
d_untri = [n for n in direct if not by[n][3]]      # never got a triage
showed = [p[0] for p in P if p[1] == 'showed' and p[2] != 'referral']

card_html = []
for n, o, path, tr, arr, bk, q, links in P:
    ol, col = OC[o]
    tri = TR[tr]
    tribadge = f'<span class="b btri">🎯 {tri}</span>' if tri else '<span class="b bnone">no triage recorded</span>'
    lk = ' '.join(f'<a href="{u if u.startswith("http") else G + u}" target="_blank">{l} ↗</a>' for l, u in links)
    oline = ''
    if n in O:
        att, conn, longest, smo, smi, v = O[n]
        lg = f"{longest // 60}m{longest % 60:02d}s" if longest >= 60 else f"{longest}s"
        oline = (f'<div class="row">📞 <b>Outreach:</b> speed to lead ≤1 min ✓ · {att} call attempts · '
                 f'<b>{conn} connected</b> (longest {lg}) · {smo} texts out / <b>{smi} replies</b>'
                 f'<br>⚖️ <b>{v}</b></div>')
    card_html.append(f'''<details class="card" id="{slug(n)}" data-o="{o}" data-p="{path}" data-t="{'y' if tr else 'n'}" style="border-left-color:{col}">
<summary><b>{n}</b> <span class="b" style="background:{col}1a;color:{col}">{ol}</span> <span class="b bpath">{PC[path]}</span></summary>
<div class="body">
<div class="row">📅 Opted in <b>{arr}</b> · {bk}</div>
<div class="row">{tribadge}</div>{oline}
<div class="row">🏷 {q}</div>
<div class="row links">🔗 {lk}</div>
</div></details>''')

html = f'''<title>APW True Funnel Explorer</title>
<style>
:root{{--bg:#f8fafc;--card:#fff;--tx:#0f172a;--mut:#64748b;--bd:#e2e8f0;--ac:#2563eb;--ok:#16a34a;--bad:#dc2626}}
@media(prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0b1220;--card:#131c2e;--tx:#e2e8f0;--mut:#94a3b8;--bd:#243146}}}}
body{{background:var(--bg);color:var(--tx);font:14px/1.5 -apple-system,Segoe UI,sans-serif;margin:0 auto;padding:16px;max-width:900px}}
h1{{font-size:19px;margin:6px 0 10px}}
.map{{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:14px 16px;margin-bottom:14px}}
.mrow{{padding:8px 0;border-bottom:1px dashed var(--bd)}} .mrow:last-child{{border:none}}
.mhead{{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}}
.mnum{{font-size:20px;font-weight:800}}
.msub{{margin:6px 0 2px 16px;padding-left:10px;border-left:3px solid var(--bd)}}
.rate{{font-weight:700}} .good{{color:var(--ok)}} .bad{{color:var(--bad)}}
.chip{{display:inline-block;font-size:11px;border:1px solid;border-radius:11px;padding:1px 7px;margin:2px 3px 0 0;text-decoration:none}}
.mut{{color:var(--mut);font-size:12px}}
.filters{{position:sticky;top:0;background:var(--bg);padding:8px 0;display:flex;flex-wrap:wrap;gap:6px;z-index:5}}
.filters button{{border:1px solid var(--bd);background:var(--card);color:var(--tx);border-radius:20px;padding:5px 12px;cursor:pointer;font-size:12.5px}}
.filters button.on{{background:var(--ac);border-color:var(--ac);color:#fff}}
.card{{background:var(--card);border:1px solid var(--bd);border-left:4px solid;border-radius:10px;margin:8px 0;scroll-margin-top:60px}}
summary{{padding:10px 14px;cursor:pointer;list-style:none;display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
summary::-webkit-details-marker{{display:none}} summary::after{{content:"▾";margin-left:auto;color:var(--mut)}}
details[open] summary::after{{content:"▴"}}
.body{{padding:2px 14px 12px;border-top:1px dashed var(--bd)}}
.row{{padding:4px 0}} .links a{{color:var(--ac);text-decoration:none;margin-right:12px}}
.b{{font-size:11.5px;padding:2px 9px;border-radius:12px;background:var(--bd)}}
.btri{{background:#2563eb1a;color:#2563eb}} .bnone{{background:var(--bd);color:var(--mut)}} .bpath{{background:var(--bd);color:var(--mut)}}
.note{{color:var(--mut);font-size:12.5px;margin:12px 0}}
h2{{font-size:15px;margin:18px 0 4px}}
</style>
<h1>🎯 APW True Funnel — Jul 28 → Aug 26 · the WHOLE picture, top of page</h1>

<div class="map">
<div class="mrow mhead"><span class="mnum">$6,100</span> ad spend → <span class="mnum">38</span> <b>new leads</b> <span class="mut">($160/lead · every lead got speed-to-lead ≤1 min · zero skipped the application opt-in)</span></div>

<div class="mrow">
<div class="mhead"><span class="mnum">25</span> <b>⚡ DIRECT TO BOOKING</b> <span class="mut">— booked a slot within minutes of opting in</span></div>
<div class="msub"><b>🎯 Triaged / connected first — 13</b> → <span class="rate good">6 showed (50%)</span> · 6 no-show · 1 unrecorded<br>
{chips(d_tri, lambda n: ' ✓' if n in showed else '')}</div>
<div class="msub"><b>🚷 Never triaged (dialed &amp; texted, no pickup) — 12</b> → <span class="rate bad">1 showed (8%)</span> · 9 no-show · 2 cancelled<br>
{chips(d_untri, lambda n: ' ✓' if n in showed else '')}</div>
</div>

<div class="mrow">
<div class="mhead"><span class="mnum">4</span> <b>📞 TRIAGE → CALL BOOKED</b> <span class="mut">— connected live FIRST, then booked</span> → <span class="rate good">2 showed (50%)</span>, incl. the only qualified</div>
<div class="msub">{chips(later, lambda n: ' ✓' if n in showed else '')}</div>
</div>

<div class="mrow">
<div class="mhead"><span class="mnum">9</span> <b>📥 OPT-IN ONLY, NEVER BOOKED</b> <span class="mut">— chased 6–22× each, unresponsive (we did reach out — proof in each card)</span></div>
<div class="msub">{chips(never)}</div>
</div>

<div class="mrow mhead"><span class="mnum">9</span> <b>✅ SHOWED</b> <span class="mut">(31% of 29 booked)</span> → <span class="mnum">1</span> <b>🟢 QUALIFIED — Karl</b> <span class="mut">(11% of shows · $6,100/qualified)</span> → <span class="mnum">$0</span> <b>collected</b> <span class="mut">(Karl's $7.5K agreed, unsigned)</span></div>

<div class="mrow mut">➕ Referral outside the funnel: {chips(['Chris Mclean'])} · ❓ unrecorded outcome: {chips(['Robert Morawitz'])} · Headline: <b>a booking with a live triage shows ~50%; a self-booked slot nobody connected with shows 8%.</b></div>
</div>

<div class="filters">
<button class="on" data-f="all">All 39</button>
<button data-f="o:showed">✅ Showed</button>
<button data-f="o:noshow">❌ No-show</button>
<button data-f="o:cancelled">🚫 Cancelled</button>
<button data-f="o:optin">📥 Never booked</button>
<button data-f="p:direct">⚡ Direct to Booking</button>
<button data-f="p:later">📞 Triage → Booked</button>
<button data-f="t:y">🎯 Triaged</button>
<button data-f="t:n">Not triaged</button>
</div>
<h2>Every person — tap to expand (status · path · outreach proof · links)</h2>
{''.join(card_html)}
<div class="note">⚖️ <b>Definitions (APW language):</b> speed to lead = instant automatic first touch · connected = answered call ≥60s (raw call logs) · triaged = live conversation with Lynn (tag [V] and/or Alan-attested) · unresponsive = repeated dials/texts, no engagement. Alan's TRUE-triage bar (live convo + all questions + confirmed booking) was documented ZERO times this window — Sep 1 fields fix that. Raw proof: <a style="color:var(--ac)" target="_blank" href="https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/contacts_2026-08-30.csv">contacts</a> · <a style="color:var(--ac)" target="_blank" href="https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/appointments_2026-08-30.csv">appointments</a> · <a style="color:var(--ac)" target="_blank" href="https://github.com/Awake999/awake/tree/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/raw">messages/calls raw</a> · <a style="color:var(--ac)" target="_blank" href="https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/KAI_VERIFICATION_LINKS_2026-08-31.md">per-person verification file</a></div>
<script>
document.querySelectorAll('.filters button').forEach(b=>b.onclick=()=>{{
 document.querySelectorAll('.filters button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
 const f=b.dataset.f;document.querySelectorAll('.card').forEach(c=>{{
  if(f==='all'){{c.hidden=false;return}}
  const[k,v]=f.split(':');c.hidden=c.dataset[k]!==v;
 }});
}});
document.querySelectorAll('.chip').forEach(a=>a.onclick=()=>{{const el=document.getElementById(a.getAttribute('href').slice(1));if(el)el.open=true;}});
</script>'''

out = os.path.join(os.path.dirname(__file__), '..', 'data', 'funnel_explorer_2026-08-31.html')
open(out, 'w').write(html)
print("built", out, len(html), "bytes")
