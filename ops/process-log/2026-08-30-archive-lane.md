# Process log — Archive lane, 2026-08-30

Lane: canonical data store (`ops/archive/**` only). Branch: `claude/archive-lane-canonical-store` (based on master so the diff stays clean of the sibling data-ops branch; shared brain read from that branch without merging). Every batch committed + pushed — commits are the backup.

## Archived this session

**Structure** — full scaffold + navigation README (`ops/archive/README.md`), GHL deposit instructions, Slack audio inventory, people index.

**Fathom** — INDEX of all 234 meetings (Jun 21–Aug 28) with per-call archive status, plus 8 calls fully archived (verbatim transcript + companion summary + meta each). All 7 doctrine calls from pointer-map are in:
- AG escalation strategy 8/28 (803352097) + part 2 (803353666)
- 4-day dispute doctrine 8/27 (801867207)
- Funnel rebuild w/ Jacob 8/28 (801234866)
- Revenue diagnosis $0 August 8/28 (803087357)
- Robert Morawitz qualification origins 8/27 (798787726)
- Constantine ICP mismatch 8/28 (803053542)
- plus Carla EOD SOD-to-Trello 8/28 (803341537)

**Krisp** — INDEX of ~150 meetings (Jun 7–Aug 29; built from meeting lists since full-text search was broken 8/29), plus all 5 Alan+Constantine coaching sessions fully archived (6/10, 6/17, 7/22 ★variable show-rate doctrine, 8/12, 8/19).

**Slack** — complete exports, chronological + author-stamped:
- #dispute-updates (C0BPKQFC95K) Aug 12–28 — the full bureau-call evidence trail (feeds the AG complaints)
- #--daily-start-and-end-of-day-reports (C0BPFS7HN05) Aug 11–28
- #anne-start-of-day-reports (C0BPT3GP2GL) Aug 12–17
- 3 audio files inventoried in slack/audio/README.md (all needs-transcription; no transcripts existed in-thread)

**People** — 13 pages (7 team + 6 clients/prospects), each linking every archived call, Slack trail, and Notion pointer.

**Cloud** — Drive pointer doc mirroring the archive README placed in "APW Data Hub — apw-intel backups" (folder 1H2NoikDjeyYa9ZnkuBrQcbDdZ0xgI8fQ, doc 1KmLFIR55_z8EQBBeenvJ96ql4zvSn1XFW1upkTTVgVQ). INDEX tables deliberately not duplicated to Drive — they change every run; the repo copy is authoritative.

## Resume points (next run starts here)

1. **Fathom** (`calls/fathom/INDEX.md`, 11/234 archived — batch 4 added Yeshaya Dank 799338949, Chris Mclean 798638035, Todd LoGuidice funding execution 800283407): continue Aug 20+ top-down — next up 802994217, 802985297, 801909953, then remaining client-named calls (Nick Samara x2, Michael Moore x2, Karl Krummenacher, Connor Robertson…). Max ~3 transcripts per query round; large ones save to file — move into place.
2. **Krisp** (`calls/krisp/INDEX.md`, 7/~150 archived — batch 2 added SCIO 6/16 + 6/18): next ★ SCIO 6/23 (019ef5b4e5ea766bbb3023224955e76a) and 8/4 (019fcdc6c2707289bcdd692b650e0d21); then the 8/28 day-capture (01a03ec7bda3775ca1cd835bf3717525 — Alan, Carla, Lynn, Constantine, Jacob); then client calls (Pedro triage, Leo 12k, Jill sessions). Note: Krisp had no key points stored for SCIO 6/16 — transcript archived, summary marked pending.
3. **Slack**: remaining priority channels #hire-worldwide and #alan-nguyen-booked-calls (search channel IDs first); then #dispute-questions, #dispute-team-training, #dispute-team-agenda. Also: thread replies in #dispute-updates were NOT expanded (counts noted inline) — a thread-expansion pass is queued.
4. **People**: add pages as new clients' calls land (Yeshaya Dank, Karl Krummenacher, Jennifer Ulloa, Jill Peralta…).
5. **GHL**: nothing to pull remotely — deposit instructions live in `ops/archive/ghl/README.md` for the local (PC) session.

## Known limitations / notes

- **Draft PR could not be opened from this session** — the GitHub API is not enabled here (git push works; `gh`/REST blocked). Open it with one click: https://github.com/Awake999/awake/pull/new/claude/archive-lane-canonical-store — title "Archive lane: canonical data store".
- Repo has moved to `Awake999/awake` (capital A) per git remote notices; pushes still succeed via the old URL.
- Krisp full-text search still broken; meeting lists work fine.
- No audio was machine-transcribed (per lane rules); Zoom clip links in Slack exports point at originals in the team Zoom account.

## Batch: SOP v1.0 adoption (LANE-SYNC from Lane 1, ~07:36 UTC)

Read `ops/SOP.md` v1.0 + REGISTER LANE-SYNC block from `claude/new-session-1ofk4w` @ 1c58702 (master unchanged; Alan's PR merge still pending). Adopted:
- **RAW-ORIGINALS LAW** — retroactively satisfied where raws survived on disk: 15 raw API responses copied beside their rendered transcripts as `transcript-raw.txt/.json` (7 Fathom, 7 Krisp) + Slack SOD/EOD raw page 1. NO raw exists for: Fathom 801867207 / 803053542 / 803087357 / 803341537 and Slack #dispute-updates + #anne-start-of-day-reports + SOD/EOD page 2 — those API responses returned inline and were transcribed verbatim to markdown at capture time; the markdown is the capture. All future pulls store raws from the start.
- **EVIDENCE LAW / VERBATIM / TANDEM / SCAN-READY** — already lane practice; meta files carry links + dates.
- **Sync ritual** — pull-first / push-after / grep LANE-SYNC / own process-log only: adopted as written. Lane 3 ownership confirmed: `ops/archive/**` append-only.
- GHL: per LANE-SYNC, Lane 4 delivers GHL originals into `ops/archive/ghl/` — folder + deposit instructions already in place; Todd L. import complete (Contact ID nIy2smghNYT9II3enmQv), awaiting Lane 4's PR.

## Batch: TLDR format rule (Alan, verbatim, 2026-08-30)

> "TL/DR should always be a part of your SOP all throughout, but it should have context. It should also be at the very end, in an actual, easy, simple way, as well as at the beginning."

Adopted for this lane immediately: every report/reply/file opens with a TLDR that carries context, and closes with a plain, simple TLDR restatement. FOR LANE 1: this extends SCAN-READY LAW — please register this verbatim ask and fold into SOP.md next version (archive lane cannot edit SOP.md per single-writer rule).

## Batch: Slack audio SOP (Alan, verbatim, 2026-08-30)

> "For that stuff, just send links if those are videos. You don't need to physically download videos, but we do need to physically download audios and transcribe those. Transcribe them yourself."
> "make that a normal standard operating procedure with constant updates. And perfect sorting. Remember, everything should be a clickable link. Even when you're showing me stuff here, I don't want to see the BS URL right on the BS, like board/star. I need to see the actual link."

Adopted: (1) standing audio SOP written into `ops/archive/slack/audio/README.md` — audios downloaded + machine-transcribed by the lane (faster-whisper small, installed in-session; Alan's direction supersedes the earlier no-self-transcription rule), videos linked only, constant re-sweeps, perfect sorting; (2) clickable-links law — every reference in inventories AND chat replies is a named markdown link, never a raw URL. FOR LANE 1: register both verbatim asks; clickable-links extends SCAN-READY LAW.

Status: 23/26 audios in repo; transcription batch running (background job); 3 oversize Grace call audios + Lynn video have real Slack permalinks in the inventory — audios flagged for local download then transcription, video stays link-only.
