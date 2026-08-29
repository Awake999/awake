# awake — company data tracking

## Purpose

Track and query company data across internal sources. Current sources: **Fathom**
(meeting recordings/transcripts) and **Slack** (internal comms). Gmail, Notion,
Trello, Google Calendar and Zoom are connected but not yet part of the tracking
layer.

## Standing instruction: always report coverage

**On every research/lookup request, state explicitly what was done AND what was
not done, relative to the specific prompt.** Never let an answer imply exhaustive
coverage that wasn't actually achieved.

Every answer must carry a coverage section that names:

1. **Scope searched** — exact sources, exact date window, exact filters used.
2. **Depth reached** — e.g. "read 4 of 48 transcripts", not "searched Fathom".
3. **What was NOT searched** — sources skipped, pages not paged, transcripts not
   read, date ranges not covered.
4. **Known blind spots of the tools used** — e.g. Fathom `search_meetings`
   matches titles + AI summaries only, never transcript text.
5. **Confidence** — and what specifically would be required to close the gap.

Rules:

- A negative result ("no evidence found") is only reportable alongside the exact
  scope that produced it. "I found nothing" is not an answer; "I found nothing in
  X, having checked Y of Z, and did not check W" is.
- Do not present a summary-level search as a content-level search.
- If a finding is later found to have been missed, say so plainly and identify
  which coverage gap allowed it.
- Prefer stating a gap over quietly narrowing the request to fit what was easy.

## Tool notes (learned)

### Fathom
- `search_meetings` searches **titles + AI summaries ONLY** — it does NOT search
  transcript text. A statement spoken in a call but absent from its AI summary is
  invisible to this tool. This has already produced one false negative.
- There is **no full-text transcript search**. Exhaustive coverage requires
  fetching transcripts one at a time via `get_meeting_transcript`.
- AI summaries are lossy. Do not treat a summary as evidence of absence.
- The same call often appears as multiple `recording_id`s (one per recorder).
  Dedupe before counting coverage.
- Large transcripts auto-persist to a file under
  `~/.claude/projects/.../tool-results/`. Grep those files instead of loading
  full transcripts into context.

### Slack
- `from:<@USERID>` with **no keyword** is the strongest bound on "did X ever say
  this" — it spans public channels, private channels, DMs and group DMs visible
  to the account.
- Results are paginated at 20; page to the end before claiming completeness.
- Semantic search is available; keyword-only searches miss paraphrases.

## People / IDs

- Alan Nguyen — Slack `U0ADC1UNXAQ` — nguyenalan95@gmail.com (workspace owner)
- Carla Stivala — Slack `U0BNZC4G6ER` — cvstivala@icloud.com /
  carla@ascendprimewealth.com — TZ America/New_York
- Lynn (Neves) — Slack `U0BMPBL29UN` — neves.lynn7@gmail.com
- Grace (Ina Grace Langub) — Slack `U0BPYLF1MA4` — langubinagrace@gmail.com
- Rosemarie Anne Fabian — rosemarieannefabian@gmail.com
- Sabrina Neves — recorder on several Fathom calls
- Constantine Adamopoulos — external sales coach
- Clint Losch — external (scaleclients.io)

## Key Slack channels

- `C0BR5H27FAP` — group DM: Alan + Lynn + Carla
- `D0BP6H6AF44` — DM: Alan + Carla
- `D0BMPBLHXSA` — DM: Alan + Lynn
- `C0BPFS7HN05` — `#--daily-start-and-end-of-day-reports` (SOD/EOD reports)
- `C0AJ9D4NEQ4` — `#alan-nguyen9145`
- `#-announcements`, `#admin-ops-staff`, `#sales-team-chat`
