#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a REAL multi-day activity record from the Teramind daily-digest emails.

    python3 ops/tools/build_digest_record.py

Source: ops/archive/teramind/digests/DIGESTS.json — the verbatim numbers from the
Teramind snapshot emails. This is the ONLY real Teramind data that reaches a cloud
lane today (the alert emails + these digests). It is real, but SHALLOW: each list is
a TOP-3 leaderboard, so a person absent from a day is 'not in the top 3', never
proven idle (ruling #27). The full per-minute, all-roster record needs an export or
API token — see TERAMIND_DAILY_APP.md.
"""
import json, pathlib, datetime
REPO = pathlib.Path(__file__).resolve().parents[2]
D = json.loads((REPO/"ops/archive/teramind/digests/DIGESTS.json").read_text())
BR="claude/new-session-1ofk4w"; GH=f"https://github.com/Awake999/awake/blob/{BR}"
GM=lambda mid:f"https://mail.google.com/mail/u/0/#inbox/{mid}"
INST="ascendprimew.us.teramind.co"

# email → person
WHO={"nguye@a51":"Alan (nguye@a51)","malizgill31@gmail.com":"ML (malizgill31)",
     "langubinagrace@gmail.com":"Grace","cvstivala@icloud.com":"Carla",
     "neves.lynn7@gmail.com":"Lynn","rosemarieannefabian@gmail.com":"Anne",
     "langubinagrace":"Grace"}
def who(k): return WHO.get(k,k)

days=D["days"]; ids=D["_email_ids"]
# _email_ids keys use padded labels ("Sep 01"); map by ISO date to avoid mismatch.
_ID_BY_DATE={"2026-08-29":"1a051040017f139a","2026-08-30":"1a05606eb638aa38",
             "2026-08-31":"1a05b274d422cfb6","2026-09-01":"1a060651bb90d954",
             "2026-09-02":"1a0657b64b87aee1"}
def midd(iso): return _ID_BY_DATE.get(iso,"")
def dl(d): return datetime.date.fromisoformat(d).strftime("%b %d").replace(" 0"," ")

L=[]
L.append("# 📊 APW ACTIVITY RECORD — from Teramind's own daily reports (REAL)")
L.append(f"*Built {datetime.date.today()} · Lane 1 · Register #167. **100% real Teramind data** — the numbers Teramind emailed to "
         "support@ascendprimewealth.com, read verbatim. Every day links to its source email. This is NOT the demo.*\n")
L.append("> ⚠️ **Read this once.** Each Teramind digest lists only the **top 3** per category, not the whole team. "
         "So a person missing from a day means *not in that day's top 3* — **never** 'idle' or 'unmonitored' (ruling #27). "
         "The full per-person, minute-by-minute day — the thing you actually want — is **not in these emails**; it needs a "
         f"one-time export or API token ([how](" + GH + "/ops/data/TERAMIND_DAILY_APP.md)). What IS below is real and verified.\n")

# ── activity % matrix
L.append("## 🎚 ACTIVITY % — by person, by day (Teramind's own productivity score)\n")
people=[]
for d in days:
    for k in d["activity"]: 
        if who(k) not in people: people.append(who(k))
L.append("| Person | " + " | ".join(f"[{dl(d['date'])}]({GM(mid(datetime.date.fromisoformat(d['date']).strftime('%b %d').replace(' 0',' '))) or ''})" if False else dl(d['date']) for d in days) + " |")
L.append("|---|" + "---|"*len(days))
for p in people:
    row=[f"**{p}**"]
    for d in days:
        v=next((vv for kk,vv in d["activity"].items() if who(kk)==p), None)
        row.append(f"**{v}**" if v else "·")
    L.append("| "+" | ".join(row)+" |")
L.append("| _org headline_ | " + " | ".join(f"_{d['activity_headline'] or '—'}_" for d in days) + " |")
L.append("\n*`·` = not in that day's top-3 activity list (not a zero). The org headline is Teramind's account-wide activity number for the day.*")
L.append("\n**What's already visible in 5 days of real data:**")
L.append("- **Activity runs 21%–48% and Teramind's own org headline sits at 44–49%.** By Teramind's scoring the team is active under half the tracked time — but that score depends on how apps are classified, and APW's classification is **not yet calibrated** (ruling #28), so treat these as Teramind's raw number, not a verdict.")
L.append("- **ML (malizgill31) is real and active** — new user Aug 30, then on the board every day since (35%, 39%, 21%). Earlier I called ML \"never logged in\"; the digests disprove that. Corrected.")
L.append("- **Lynn, Carla, Grace and ML all appear; Anne does not appear in any top-3 these 5 days** — which, again, means not-top-3, not absent.")

# ── email volume
L.append("\n## 📧 EMAIL VOLUME — received / sent\n")
L.append("| Day | Org total | Per-person (top 3) | Source |")
L.append("|---|---|---|---|")
for d in days:
    pp=" · ".join(f"{who(k)} {v}" for k,v in d["emails"].items())
    L.append(f"| **{dl(d['date'])}** | {d['emails_total']} | {pp} | [email]({GM(midd(d['date']))}) |")
L.append("\n**The email story is one person.** Alan's own machine accounts for essentially the entire inbox volume every day "
         "(70, 10, 119, 171, 162 received) while everyone else is single digits or absent. That's an owner-inbox pattern, "
         "not a team-throughput pattern — worth knowing before reading 'emails' as team output.")

# ── alerts + printed + sites
L.append("\n## 🚩 ALERTS · 🖨 PRINT · 🌐 SITES — per day\n")
L.append("| Day | Alerts | Docs/pages printed | Sites visited | Top sites (Teramind's top 3) | Source |")
L.append("|---|---|---|---|---|---|")
for d in days:
    al=" · ".join(f"**{who(a[0])}: {a[1]}**" for a in d["alerts"]) or "none"
    ts=" · ".join(f"{s} {m}" for s,m in d["top_sites"])
    L.append(f"| **{dl(d['date'])}** | {al} | {d['printed']} | {d['websites_total']} | {ts} | [email]({GM(midd(d['date']))}) |")
L.append("\n**youtube.com is in the top-3 sites every single day** (0–12 min). Low minutes, but a standing presence. "
         "Aug 30 shows doordash + a whatsapp process; Sep 02 shows creditkarma. None are job boards — the job-search alerts "
         f"are tracked separately in [the job-search audit]({GH}/ops/data/JOB_SEARCH_AUDIT_2026-09-03.md).")

# ── the honest gap
L.append("\n## 🧱 WHAT THIS CANNOT TELL YOU — and how to get it\n")
L.append("The digest is a leaderboard, so five things you asked for are simply **not in it**:")
L.append("| You want | In the digest? | Where it actually lives |")
L.append("|---|---|---|")
L.append("| Every person, every day (full roster) | ❌ top-3 only | Web & Apps export / API |")
L.append("| Minute-by-minute timeline | ❌ | Web & Apps export / API |")
L.append("| What each person was *doing* | ❌ | export (has URL + title per event) |")
L.append("| Duration per activity | ❌ | export (has start/end) |")
L.append("| Clickable session-player video per event | ⚠️ only on alerts | export gives session ids → player links |")
L.append(f"\n**All five unlock the same way:** one Web & Apps CSV per day into `ops/archive/teramind/inbox/`, and "
         f"[APW DAILY]({GH}/ops/tools/teramind_daily.py) prints exactly that — the full-spectrum EODR/SODR you asked for. "
         "The engine is built and waiting; only the data door is closed, and it opens from inside Teramind.")
L.append(f"\n---\n*Every figure above is quoted from a Teramind email. Source emails: "
         + " · ".join(f"[{dl(d['date'])}]({GM(midd(d['date']))})" for d in days) + ".*")

out=REPO/"ops/data/TERAMIND_ACTIVITY_RECORD.md"
out.write_text("\n".join(L)+"\n",encoding="utf-8")
print("✓",out.relative_to(REPO),len(L),"lines")
