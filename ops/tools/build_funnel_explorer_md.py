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

noshow_names = [p[0] for p in P if p[1] == 'noshow']
cancel_names = [p[0] for p in P if p[1] == 'cancelled']
show_names = [p[0] for p in P if p[1] == 'showed' and p[2] != 'referral']
unq_names = [n for n in show_names if n != 'Karl Krummenacher']
all_leads = [p[0] for p in P if p[2] != 'referral']
not_instant = later + never

md = f'''# 🎯 APW True Funnel — Jul 28 → Aug 26 · chronological, every number with its names

**How to read:** every layer's numbers add up to the layer above it. ✓ after a name = they showed. Click any name for their full card (status · tags · outreach · proof links). Terms: **speed to lead** = instant automatic first touch (everyone got one, ≤1 min) · **direct to booking** = grabbed a slot within minutes of opting in · **connected** = answered call 60s+ · **triaged** = live conversation with Lynn · **unresponsive** = repeated dials/texts, no engagement.

## LAYER 1 — 💵 $6,100 spend → 38 NEW LEADS came in ($160/lead, all via the application opt-in)
{links_of(all_leads)}

## LAYER 2 — what the 38 did next: **38 = 25 + 13**
**⚡ 25 booked INSTANTLY (direct to booking):**
{links_of(direct)}

**⏳ 13 did NOT book right away (opt-in only at first):**
{links_of(not_instant)}

## LAYER 3 — what happened to those 13: **13 = 4 + 9**
**📞 4 booked LATER, after triage/follow-up** (Jennifer +5h · Behnad +15h · Connor +7d · Karl +14d):
{links_of(later)}

**📥 9 NEVER booked** (chased 6–22× each — unresponsive):
{links_of(never, mark_show=False)}

## LAYER 4 — everyone who booked: **25 + 4 = 29 → outcomes: 9 + 17 + 2 + 1**
**✅ 9 SHOWED (31%):**
{links_of(show_names, mark_show=False)}

**❌ 17 NO-SHOW:**
{links_of(noshow_names, mark_show=False)}

**🚫 2 CANCELLED:** {links_of(cancel_names, mark_show=False)} · **❓ 1 unrecorded:** [Robert Morawitz](#{anchor("Robert Morawitz")})

## LAYER 5 — of the 9 who showed: **9 = 1 + 8**
**🟢 1 QUALIFIED:** [Karl Krummenacher](#{anchor("Karl Krummenacher")}) (11% of shows · $6,100/qualified)
**🔴 8 unqualified** (4 no money · 1 credit too weak · 1 needs PG · 1 offer mismatch · 1 fake):
{links_of(unq_names, mark_show=False)}

## LAYER 6 — 💰 $0 COLLECTED in the window (Karl's $7.5K agreed, unsigned)
➕ Outside the funnel: [Chris Mclean](#{anchor("Chris Mclean")}) — Matthew referral, your 30th booked tag.


## LAYER 7 — 📊 THE RATES (all on attested truth, every basis named above)
| Metric | Basis | Number |
|---|---|---|
| Cost per lead | $6,100 / 38 leads | **$160** |
| Opt-in → booked (ever) | 29 of 38 | **76%** |
| Opt-in → instant booking | 25 of 38 | **66%** |
| The 13 non-instant → later booked | 4 of 13 | **31%** |
| Cost per booked person | $6,100 / 29 | **$210** |
| **TOTAL SHOW RATE** | 9 of 29 booked | **31%** (32% of 28 resolved · 29% counting the fake as no real show) |
| No-show rate | 17 of 29 | **59%** |
| Cancelled | 2 of 29 | **7%** |
| Show rate — triaged/connected instant bookers | 6 of 12 resolved | **50%** |
| Show rate — never-connected instant bookers | 1 of 12 | **8%** |
| Show rate — triage → booked later | 2 of 4 | **50%** |
| Show rate — ALL live-connected combined | 8 of 16 resolved | **50%** vs **8%** never-connected |
| Cost per live call | $6,100 / 9 | **$678** |
| **QUALIFIED SHOW RATE** | 1 of 9 shows (Karl) | **11%** |
| Qualified per booking / per lead | 1 of 29 / 1 of 38 | **3.4% / 2.6%** |
| **Cost per qualified live call** | $6,100 / 1 | **$6,100** |
| CPA at a 25% close rate | $6,100 × 4 | **$24,400 — vs the $15K ticket: upside-down** |
| Cash collected in window | — | **$0** (Karl $7.5K agreed, unsigned) |

## 🎤 Kai's voice note — answered line by line (real numbers)
1. 🗣️ *"you've spent 6100"* → ✅ correct, ≈$6.1K in the window ($6,451 through 8/30 across both relaunch campaigns).
2. 🗣️ *"37 unique bookings... about a 170 cost per booked call"* → ❌ 37 was a slot count, not people. **30 unique people booked** (29 ad leads + 1 referral; several booked multiple slots) → **$203–210 per booked person**.
3. 🗣️ *"Of those 15 showed... roughly 410 cost per live call"* → ❌ **9 showed** (each verified by recording or Alan's review) → **$678 per live call**.
4. 🗣️ *"show rate... 41%"* → ❌ **31%**. And it splits hard: live-connected bookers 50%, never-connected self-bookers 8%.
5. 🗣️ *"of the 15, 1 was qualified"* → the **1 is right** (Karl) — but of **9** shows, so qualified show rate = **11%**.
6. 🗣️ *"why 14 of the 15 live calls were unqualified... what made them unqualified"* → really 8 of 9: **4 no money** (Nick, Pradeep, Michael Moore, Chris Bowers) · **1 credit too weak** (Jesse) · **1 needs a personal guarantor** (Yeshaya) · **1 wanted no-PG funding we don't offer** (Jennifer) · **1 fake lead** (P Reddy — fake business/website). **The constraint is money + credit damage, not interest.**
7. 🗣️ *"what's your specific ideal client and who was showing up"* → ICP: 720+ credit, funds to invest, real funding need, PG-willing owner. Who actually books: damaged-credit / no-funds owners pulled by a "guaranteed funding" application funnel — structurally a **downsell audience**. Targeting/creative problem, not a sales problem.
8. 🗣️ *"bump show rate to 50%... $800 per qualified... 25% close... 3200 CPA"* → the model is right, the inputs aren't there yet: today it's **$6,100/qualified → $24,400 CPA**. To reach his $800/qualified: at $6.1K spend you need ~7–8 qualified calls — i.e. ~50% show AND ~50% qualified-of-shows. Show rate is fixable (triage everyone: connected bookers already show 50%). **Qualified% is the ad-audience quality problem — that's the constraint.**
9. 🗣️ *"you're closing at 150"* → ticket is $15K main offer; in-window collections were $0 (Karl's $7.5K agreed-unsigned; August verified cash: $1.6K, a downsell household deal).
10. 🗣️ *"what's changed between last month and this month"* → (a) Jul 28: both old campaigns replaced by relaunches — learning reset #1; (b) **Aug 10: a tracking edit touched all 12 live ads — learning reset #2** (now banned by MEDIA LAW); (c) Medical v2 never found footing — $403+/lead with one ad eating 66% of budget; (d) outcome-recording stopped entirely in August, so the worst weeks were invisible in-system.

> **The triage split, same layers:** of the 25 instant bookers — 13 later got a live triage/connection → **6 showed (50%)**; the other 12 never connected despite 2–17 dials each → **1 showed (8%)**. The 4 who booked after triage → 2 showed (50%), including the only qualified. **Live human contact is carrying the entire funnel.**

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
