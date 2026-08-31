# APW OPS — READ THIS FIRST (auto-loaded by every local Claude session)

You are working inside the Ascend Prime Wealth ops repo. **Before doing anything:**

1. **Read [`ops/SOP.md`](ops/SOP.md)** — the binding laws (verbatim checklists, evidence links, raw originals, scan-ready output) + lane ownership + the sync ritual (git pull first, push after every batch).
2. **Read [`ops/REGISTER.md`](ops/REGISTER.md)** — every ask Alan has made, verbatim, numbered, with status + grade. Grep `LANE-SYNC` for cross-lane notices. If your task isn't on the register, it gets a numbered line before work starts.
3. **Alan's original prompts, in full:** [`ops/prompts/ALL_PROMPTS_FULL.md`](ops/prompts/ALL_PROMPTS_FULL.md) (every prompt verbatim, chronological) and [`ops/prompts/2026-08-30-full-funnel-spec.md`](ops/prompts/2026-08-30-full-funnel-spec.md) (the governing spec). **Prompts govern over any brief or summary.**
4. **Find anything:** [`ops/INDEX.md`](ops/INDEX.md) — clickable pointers to every dashboard, database, audit, and decision across Notion/GitHub/Drive/GHL.

**LAW 0 — NEVER-MISS PROTOCOL (outranks all):** parse every prompt into numbered atomic asks before working; a REPROMPT = severity-1 failure — diff v1 against the literal words, name the delta, fix that delta only; one line per item in every enumerated deliverable, never grouped; checkboxes only after the tool call exists; literal ask first, judgment second.

**The laws in one line each:** every ask → verbatim numbered checklist · every claim → clickable link + date + evidence window · raw originals beside every summary, never replaced · verified/derived/unknown labels, never guess · scan-ready output, TLDR first · pull before work, push after every batch (unpushed work dies with the container).

**Lane ownership (single-writer):** Lane 1 (cloud command) owns REGISTER/SOP/INDEX/Notion-ops · Lane 2 owns `ops/dashboard/` · Lane 3 owns `ops/archive/` (append-only) · Lane 4 (this PC) owns `ops/archive/ghl/` + `ops/lane4/` + browser tasks. Everyone writes their own `ops/process-log/YYYY-MM-DD-<lane>.md`, never another lane's.

Dashboard live URL: https://claude.ai/code/artifact/c6ad801c-50fc-49d3-847a-e6a8b0ddd392

---

## Recall subsystem — `recall/` (business comms Q&A)

For questions about **what was said** in internal comms — who committed to what,
when a decision was made, what a client was told. Read
[`recall/README.md`](recall/README.md) before answering one.

**Standing instruction — always report coverage.** State explicitly what was
done AND what was not done, relative to the specific prompt. Never let an answer
imply exhaustive coverage that was not achieved. Every answer names: scope
searched (exact sources, window, filters) · depth reached ("read 34 of 47
recordings", not "searched Fathom") · what was NOT searched · known tool blind
spots · confidence and what would close the gap.

A negative result is only reportable alongside the scope that produced it. "I
found nothing" is not an answer; "I found nothing in X, having checked Y of Z,
and did not check W" is.

Distinguish **"X said it"** from **"it was said near X"** from **"someone else
said it about X"** — three different claims; collapsing them produces false
conclusions. `recall/tools/scan_by_speaker.py` separates them.

### Tool blind spots (learned the hard way)

| Tool | Blind spot | Consequence |
|---|---|---|
| `Fathom search_meetings` | Searches **titles + AI summaries only**, never transcript text | Produced a confirmed false negative on 2026-08-29 |
| `Fathom` (overall) | **No full-text transcript search exists** | Exhaustive coverage requires fetching transcripts one at a time |
| Fathom AI summaries | Lossy — omit material exchanges | Never treat a summary as evidence of absence |
| `Fathom list_meetings` | Same call listed once per recorder | Dedupe before counting coverage |
| `get_meeting_transcript` | Large ones persist to disk; small ones return inline | Inline transcripts never touch disk, so disk scanners miss them — track separately |
| `Slack` search | Paginates at 20; keyword-only misses paraphrases | Page to the end; semantic search is available |

Reference case: a search of 71 meetings for "Saturday" returned zero hits while
the relevant exchange sat verbatim in a transcript, absent from that meeting's
own AI summary. Write-up:
[`recall/findings/2026-08-29-carla-saturday.md`](recall/findings/2026-08-29-carla-saturday.md).

### Where transcripts live

`ops/archive/` is the curated, committed store (Lane 3, append-only) — per the
lane ownership law above. `/archive/` at the repo root is a **gitignored scratch
cache** for a single session's scans; it is not a second archive and must not be
committed.

### Timezone caution

Grace and Rosemarie are in the Philippines. A "Saturday" in a transcript may be
theirs, not the speaker's. People and Slack channel IDs:
[`recall/README.md`](recall/README.md).
