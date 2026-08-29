# awake — business comms data recall

## What this workspace is

A system for answering questions about internal company communications: who
said what, who committed to what, when a decision was made, what a client was
told.

Sources in use: **Fathom** (meeting recordings/transcripts) and **Slack**.
Gmail, Notion, Trello, Google Calendar and Zoom are connected to the session but
are not yet part of this system.

**Read `recall/README.md` before answering any recall question.** It holds the
workflow, the tools, and the traps.

## Standing instruction: always report coverage

**On every research/lookup request, state explicitly what was done AND what was
not done, relative to the specific prompt.** Never let an answer imply
exhaustive coverage that was not actually achieved.

Every answer carries a coverage section naming:

1. **Scope searched** — exact sources, exact date window, exact filters used.
2. **Depth reached** — "read 34 of 47 recordings", not "searched Fathom".
3. **What was NOT searched** — sources skipped, pages not paged, transcripts not
   read, date ranges not covered.
4. **Known blind spots of the tools used** — see the table below.
5. **Confidence** — and specifically what would close the remaining gap.

Rules:

- A negative result is only reportable **alongside the scope that produced it.**
  "I found nothing" is not an answer. "I found nothing in X, having checked Y of
  Z, and did not check W" is.
- Never present a summary-level search as a content-level search.
- If a finding is later shown to have been missed, say so plainly and name the
  coverage gap that allowed it.
- Prefer stating a gap over quietly narrowing the request to fit what was easy.
- Distinguish **"X said it"** from **"it was said near X"** from **"someone else
  said it about X"**. These are three different claims and collapsing them
  produces false conclusions. `recall/tools/scan_by_speaker.py` separates them.

## Tool blind spots (learned the hard way)

| Tool | Blind spot | Consequence |
|---|---|---|
| `Fathom search_meetings` | Searches **titles + AI summaries only**, never transcript text | Produced a confirmed false negative on 2026-08-29 |
| `Fathom` (overall) | **No full-text transcript search exists** | Exhaustive coverage requires fetching transcripts one at a time |
| Fathom AI summaries | Lossy — omit material exchanges | Never treat a summary as evidence of absence |
| `Fathom list_meetings` | Same call listed once per recorder | Dedupe before counting coverage |
| `get_meeting_transcript` | Large ones persist to disk; small ones return inline | Inline transcripts never touch disk, so disk scanners miss them — track separately |
| `Slack` search | Paginates at 20; keyword-only misses paraphrases | Page to the end; semantic search is available |

The 2026-08-29 case is the reference example: a search of 71 meetings for
"Saturday" returned zero hits while the relevant exchange sat verbatim in a
transcript, absent from that meeting's own AI summary. Full write-up in
`recall/findings/2026-08-29-carla-saturday.md`.

## Layout

```
CLAUDE.md                     these rules
recall/
├── README.md                 workflow and playbook — read first
├── index/                    what meetings exist, per window, with coverage status
├── findings/                 answered questions, with citations and scope
└── tools/                    scan scripts + fetch procedure
archive/                      local transcript cache — GITIGNORED, never commit
```

## Privacy

`archive/` is gitignored and stays that way. Raw transcripts contain consumer
credit account numbers, client home addresses, identity-theft and SSN case
detail, employee compensation and termination discussions, and credential
references. Fathom is the system of record and stores them durably under its own
access controls; copying them into git adds exposure and no durability.

Commit the index and findings — metadata plus narrowly quoted excerpts. Quote
only what an answer needs. Never paste client account numbers or addresses into
a committed file.

## People

| Name | Slack ID | Email | Notes |
|---|---|---|---|
| Alan Nguyen | `U0ADC1UNXAQ` | nguyenalan95@gmail.com | Owner |
| Carla Stivala | `U0BNZC4G6ER` | cvstivala@icloud.com / carla@ascendprimewealth.com | Ops/admin lead; TZ America/New_York |
| Lynn (Neves) | `U0BMPBL29UN` | neves.lynn7@gmail.com | Setting/sales |
| Ina Grace Langub | `U0BPYLF1MA4` | langubinagrace@gmail.com | Dispute team; Philippines TZ |
| Rosemarie Anne Fabian | — | rosemarieannefabian@gmail.com | Dispute team |
| Sabrina Neves | — | — | Recorder on several calls |
| Ma. Liza Tizon ("ML") | — | malizgill31@gmail.com | Joined ~Aug 28 |
| Constantine Adamopoulos | — | — | External sales coach |
| Braden Sky | — | — | External recruiter |
| Clint Losch | — | clint@scaleclients.io | External |
| Daniel Jimenez | — | — | External, GoHighLevel tech |

Note the timezone spread — Grace and Rosemarie are in the Philippines. A
"Saturday" in a transcript may be theirs, not the speaker's.

## Key Slack channels

| ID | Channel |
|---|---|
| `C0BR5H27FAP` | Group DM: Alan + Lynn + Carla |
| `D0BP6H6AF44` | DM: Alan + Carla |
| `D0BMPBLHXSA` | DM: Alan + Lynn |
| `C0BPFS7HN05` | `#--daily-start-and-end-of-day-reports` |
| `C0AJ9D4NEQ4` | `#alan-nguyen9145` |
| — | `#-announcements`, `#admin-ops-staff`, `#sales-team-chat` |

## Recurring meeting structure (as of 2026-08-28)

Useful for locating a conversation by time of day. Restructured repeatedly
during Aug 2026 — verify against the calendar before relying on it.

- Daily Sync 7:00–7:30 (capped at 30 min)
- Operations 7:30–8:15
- Dispute team 8:15–9:00
- Sales daily 11:00
- Alan's open office hours 9:00–10:00 Mon/Tue/Thu
- Tuesdays & Fridays 9:00–10:00 blocked for owner strategic work
