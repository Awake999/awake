# DM GRINDER BRIEF — Lane 3c (Sonnet), Slack DM captures

> 🧭 [Start Here](../START-HERE.md) · [Archive home](../README.md) · Governing: [SOP-formatting.md](../SOP-formatting.md) · sibling brief: [BRIEF.md](BRIEF.md) (Fathom grinder — same laws apply)

**Who you are:** Lane 3c, the DM Grinder — capturing Alan's Slack DM conversations verbatim into `ops/archive/slack/dms/`, following the exact pattern proven on [carla-stivala/](../slack/dms/carla-stivala/) (9 raw pages + rendered export).

**Targets, in order:** (1) Lynn — Slack user U0BMPBL29UN (neves.lynn7@gmail.com); (2) Ina Grace Langub ("Grace"); (3) Rosemarie Anne Fabian ("Anne"). Find any missing user IDs via slack_search_users.

## Non-negotiable laws (read ../SOP-formatting.md + the repo SOP digest in BRIEF.md §laws first)
1. **VERBATIM** — save each API page exactly as returned, newest-first, in `<person-slug>/raw-pageN.txt` with a one-line header (channel id, capture date, time range covered, next-page cursor). Never paraphrase, trim, or reorder inside a raw page.
2. **INCREMENTAL WRITES** — commit EVERY page the moment it is captured (one commit per page). Never hold pages in memory across calls; a compaction or restart must never lose a fetched page.
3. **RENDER LAST** — when a conversation's pages are complete, run `python3 ops/archive/tools/render_dm.py ops/archive/slack/dms/<slug> "<title>"` to build export.md. Never hand-write the export.
4. **SCOPE PARTITION** — you write ONLY `ops/archive/slack/dms/**` and your own log `ops/process-log/YYYY-MM-DD-dm-grinder.md`. Nothing else, ever.
5. **CREDENTIAL FLAGS** — any plaintext password/token/credential found in a DM: keep it verbatim in the raw (full-fidelity is directed; PRIVATE repo) but add a ⚠️ line to `dms/README.md`'s Lane-1 flag list with timestamp and what it unlocks. NEVER send repo content to any external surface.
6. **NAVIGATION** — update the status table in [dms/README.md](../slack/dms/README.md) as each conversation completes; run `python3 ops/archive/tools/add_breadcrumbs.py` before each push (it skips raws automatically).
7. **PUSH DISCIPLINE** — `git pull --rebase origin claude/archive-lane-canonical-store` before every push; retry up to 4 times on rejection. Push after every page.

## Procedure per person
1. `slack_read_channel` with the user_id as channel_id (opens the DM), limit 100, response_format concise. First page = raw-page1.txt.
2. Follow `next_cursor` until "no more messages available"; number pages sequentially; final page's header says "FINAL — beginning of the conversation".
3. Render export.md (law 3), update dms/README.md row, log, push.

## Quality gates
- **AUDIT GATE:** after Lynn's DM is fully captured + rendered + pushed, STOP and wait for Lane 3's audit message before starting Grace. While waiting, do nothing else.
- Self-check per page: the saved file's message count matches the API response; header cursor recorded.
- If the Slack tools are unavailable in your session, write that finding to your process log, push, and STOP — do not improvise.

## Report style
Autonomous lane: end each work session with a scan-ready report (TLDR, per-person status table with file links, resume point) + a "reply with any of: …" line.
