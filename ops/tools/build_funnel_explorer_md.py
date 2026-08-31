#!/usr/bin/env python3
"""Build ops/data/FUNNEL_EXPLORER.md — the funnel explorer as GitHub-rendered Markdown.
Same law as the HTML: whole funnel + every name at the top (as jump links),
expandable <details> per person below, every claim linked to proof. No downloads."""
import json, re, os, csv

BASE = os.path.dirname(__file__)
D = json.load(open(os.path.join(BASE, '..', 'data', 'funnel_explorer_data.json')))
G, O, P = D['G'], D['O'], D['P']
_csvp = os.path.join(BASE, '..', 'archive', 'ghl', '2026-08-30', 'contacts_2026-08-30.csv')
TAGS = {c['id']: (c['tags'] or '') for c in csv.DictReader(open(_csvp, encoding='utf-8-sig'))}

def anchor(n):
    return re.sub(r'[^a-z0-9]+', '-', n.lower()).strip('-')

OC = {"showed": "✅ SHOWED", "noshow": "❌ NO-SHOW", "cancelled": "🚫 CANCELLED",
      "unresolved": "❓ UNRESOLVED", "optin": "📥 NEVER BOOKED"}
PC = {"direct": "⚡ Direct to Booking", "later": "📞 Triage → Call Booked",
      "never": "Opt-in only", "referral": "➕ Referral"}
TR = {"tag": "Lynn's `triaged` tag [V]", "attested": "Alan-attested triage",
      "tag+attested": "Lynn's tag [V] + Alan-attested", "": "no triage recorded"}

by = {p[0]: p for p in P}
def links_of(names, mark_show=True):
    out = []
    for n in names:
        showed = by[n][1] == 'showed'
        m = ' ✓' if (mark_show and showed) else ''
        out.append(f'[{n}{m}](#{anchor(n)})')
    return ' · '.join(out)

direct = [p[0] for p in P if p[2] == 'direct']
later = [p[0] for p in P if p[2] == 'later']
never = [p[0] for p in P if p[2] == 'never']
d_tri = [n for n in direct if by[n][3]]
d_untri = [n for n in direct if not by[n][3]]

def person_md(p):
    n, o, path, tr, arr, bk, q, links = p
    lk = ' · '.join(f'[{l} ↗]({u if u.startswith("http") else G + u})' for l, u in links)
    cid = next((u for l, u in links if not u.startswith('http')), None)
    rows = [f'📅 Opted in **{arr}** — {bk}', f'🎯 {TR[tr]}']
    if cid and TAGS.get(cid):
        rows.append('🏷️ GHL tags [V]: ' + ' '.join(f'`{t.strip()}`' for t in TAGS[cid].split('|')))
    if n in O:
        att, conn, longest, smo, smi, v = O[n]
        lg = f"{longest // 60}m{longest % 60:02d}s" if longest >= 60 else f"{longest}s"
        rows.append(f'📞 Outreach: speed to lead ≤1 min ✓ · {att} call attempts · **{conn} connected** (longest {lg}) · {smo} texts out / **{smi} replies**')
        rows.append(f'⚖️ **{v}**')
    rows.append(f'Qualification: {q}')
    rows.append(f'🔗 {lk}')
    body = '\n'.join(f'> {r}' for r in rows)
    return (f'<a id="{anchor(n)}"></a>\n<details><summary><b>{n}</b> — {OC[o]} · {PC[path]}</summary>\n\n'
            f'{body}\n</details>\n')

sections = [
    ('✅ SHOWED — 9 (+1 referral)', [p for p in P if p[1] == 'showed']),
    ('❌ NO-SHOW — 17', [p for p in P if p[1] == 'noshow']),
    ('🚫 CANCELLED — 2', [p for p in P if p[1] == 'cancelled']),
    ('❓ UNRESOLVED — 1', [p for p in P if p[1] == 'unresolved']),
    ('📥 OPTED IN, NEVER BOOKED — 9', [p for p in P if p[1] == 'optin']),
]

md = f'''# 🎯 APW True Funnel — Jul 28 → Aug 26 (click any name to jump)

**How to read (no context needed):** every ad lead fills the **application opt-in**. Most keep going and grab a slot the same minute — **⚡ Direct to Booking**. **Speed to lead** = instant automatic first touch (everyone got it, ≤1 min). **Connected** = an answered call (60s+). **Triaged** = Lynn got them in a real conversation. **Unresponsive** = we kept dialing/texting, they never engaged.

## ⬇️ THE WHOLE FUNNEL — one glance

**$6,100 spend → 38 new leads** ($160/lead · zero skipped the opt-in)

### ⚡ DIRECT TO BOOKING — 25 (booked within minutes of opting in)
- **🎯 Triaged / connected first — 13 → 6 showed (50%)** · 6 no-show · 1 unrecorded
  {links_of(d_tri)}
- **🚷 Never triaged (dialed & texted, no pickup) — 12 → 1 showed (8%)** · 9 no-show · 2 cancelled
  {links_of(d_untri)}

### 📞 TRIAGE → CALL BOOKED — 4 (connected live FIRST, then booked) → 2 showed (50%), incl. the only qualified
  {links_of(later)}

### 📥 OPT-IN ONLY, NEVER BOOKED — 9 (chased 6–22× each, unresponsive)
  {links_of(never, mark_show=False)}

### 🏁 END OF FUNNEL
**9 SHOWED (31% of 29 booked) → 1 QUALIFIED — [Karl](#{anchor("Karl Krummenacher")}) (11% of shows · $6,100/qualified) → $0 collected** (Karl's $7.5K agreed, unsigned)
➕ Referral outside funnel: [Chris Mclean](#{anchor("Chris Mclean")}) · ❓ unrecorded: [Robert Morawitz](#{anchor("Robert Morawitz")})

> **Headline: a booking with a live triage shows ~50%. A self-booked slot nobody connected with shows 8%.** The only qualified lead came through follow-up + triage, not self-serve.

---

## Every person — tap to expand (status · path · tags · outreach proof · links)

'''
for title, people in sections:
    md += f'\n### {title}\n\n'
    for p in people:
        md += person_md(p) + '\n'

md += '''---
⚖️ **Definitions & sources:** connected = answered call ≥60s from [raw call logs](https://github.com/Awake999/awake/tree/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/raw) · arrivals/tags from [contacts CSV](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/contacts_2026-08-30.csv) · slots from [appointments CSV](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/appointments_2026-08-30.csv) · outcomes/qualifications from [Alan's 8/31 review](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/prompts/2026-08-31-alan-review-attestations.md) · per-person proof: [verification file](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/KAI_VERIFICATION_LINKS_2026-08-31.md). Alan's TRUE-triage bar (live convo + all questions + confirmed booking) was documented ZERO times this window — Sep 1 fields capture it.
'''
out = os.path.join(BASE, '..', 'data', 'FUNNEL_EXPLORER.md')
open(out, 'w').write(md)
print('built', out, len(md), 'bytes')
