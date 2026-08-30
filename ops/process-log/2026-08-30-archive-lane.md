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

## Batch: calls sweep continued (2026-08-30, post-channel-completion)

- **Zoom: COMPLETE.** All 7 cloud recordings archived (verbatim + raw JSON). The 5 new ones (7/6 6.7-hour, 7/8, 7/9 x2, 7/12) are all Alan+Lynn — Lynn's onboarding/training week.
- **Krisp:** SCIO 8/4 (+raw) and the 8/28 day-capture (+raw) archived; SCIO 6/23 verified mic-check-only (no content).
- **Fathom: 25/234 archived** (+2 verified no-content). New this batch: Nick Samara 8/25+8/26 (+raw), Michael Moore 8/20 (+raw) + **8/26 close call ("We are a go", $1K custom deposit)**, Karl Krummenacher 8/20 whale call (Modern Thyroid $8M/yr, $500-750K BLOC at prime-minus-1, exit plan), Daniel Jimenez GHL tech call 8/25, dispute-team dailies 8/25+8/26 (+raw), all three 8/25 daily-sync captures (+raw, coexistence). Connor Robertson 8/17: Fathom holds NO transcript.
- **Slack audio transcription:** batch 1 (23 files) COMPLETE — all transcripts committed + linked in README table. Batch 2 COMPLETE — **all 45 voice notes in the repo are transcribed**, every inventory row links its transcript (commit 96acbce). Remaining audio work is local-PC only: 3 oversize Grace call audios + 43 external-hosted ScaleClients voice notes.

## Batch: formatting SOP v1.0 (Alan, verbatim, 2026-08-30)

> "the longer ones, please split them up and transcribe them"
> "also please optimize and organize and format to be human + AI friendly simultaneously so it's not just giant blocks of text for humans. make it easy to navigate thank you"
> "plan it out if you need to with the intention to create a flawless SOP"

Delivered as **`ops/archive/SOP-formatting.md`** (8 laws: HEADER / CHAPTERS / CONTENTS / SPLIT / VERBATIM / AUDIO / CONSTANT UPDATES / HUMAN+AI TANDEM) + two committed, idempotent, any-machine tools in **`ops/archive/tools/`**:
- `format_transcripts.py` — 10-min chapters + clickable TOC on every transcript; >150KB files split into linked `transcript-part-N.md` files with `transcript.md` as index. Applied across the archive: **41 call transcripts + 45 audio transcripts processed; 38 chaptered; 5 monsters split** (Krisp 8/4 SCIO → 5 parts; Zoom 7/6 marathon → 4 parts; Krisp 8/19 + 8/28 and Fathom 8/26 dispute daily → 2 parts each). Verbatim preservation VERIFIED line-by-line against raws for every split (3-4 empty Krisp section-label lines initially dropped from preambles were restored; tool patched so part 1 always keeps the preamble).
- `transcribe.py` — standing transcriber (supersedes the scratchpad copy): any new audio in `slack/audio/files/` on any machine; long recordings come out pre-chaptered with TOC. This is the "split them up and transcribe" answer for the 46 locally-downloadable files.
Download retries re-confirmed the hard limits: Slack API 10MB cap (file_too_large) + external-workspace files invisible (file_not_found) — server-side splitting impossible because the download itself is refused; the split/transcribe pipeline runs the moment files land locally.
FOR LANE 1: register the three verbatim asks above; SOP-formatting.md extends SCAN-READY LAW.

## Batch: navigation SOP (Alan, verbatim, 2026-08-30)

> "in the Fathom inventory, I like how everything's organized. Please make sure that there are links to everything that are clickable within it, so no copy-pasting stuff like that. Everything should be a hyperlink to another page relative to what it is that we're wanting to explore and expand on. Make it user-friendly from a human perspective."
> "make sure that the interface is intuitively and easily navigable for a human in addition to AI simultaneously. This should be beginner-friendly. There should be a landing page within the files... Every navigation leads into another category, which leads into a subcategory, which all have clickable links that are able to go backwards and forwards"

Executed against a 6-item checklist (A landing page / B hubs / C Fathom / D other indexes / E breadcrumbs / F codify):
- **`START-HERE.md`** — beginner landing page (what/where/how-organized/how-to-navigate), linked from the top of the archive README; **`calls/README.md`** + **`slack/README.md`** category hubs created so every tree level has a page.
- **Fathom INDEX rebuilt**: every title → clickable fathom.video recording link; every archived row → direct links to transcript/summary/meta; month sections + contents + status counts; recording IDs kept as small `<sub>` text on queued rows (the API needs them for future pulls).
- **Krisp INDEX**: titles → app.krisp.ai/m/<id> links, archived rows → file links (Wafd 5-segment row given per-segment links). **Zoom INDEX**: all rows → transcript links. **Slack channels INDEX**: channel names → Slack deep links (alan-n-95.slack.com/archives/<id>), export paths → file links.
- **`tools/add_breadcrumbs.py`** (idempotent, committed) added 🧭 back-navigation lines to **193 files** (every transcript/part/summary/meta, channel export, audio transcript, people page).
- Link-integrity check across the archive: 1097 relative links verified, 1 real break found + fixed.
- **SOP-formatting.md → v1.1**: new NAVIGATION law (#8), breadcrumb tool registered, end-of-run ritual now 7 steps. FOR LANE 1: register the verbatim asks; NAVIGATION extends SCAN-READY LAW.

## Resume points (next run starts here)

*(Updated end-of-day 8/30 — supersedes the earlier version of this list.)*
1. **Fathom** (`calls/fathom/INDEX.md`, **25/234 archived + 2 verified no-content**): all client-named August calls done. Continue top-down through the unnamed "Impromptu Zoom Meeting" backlog (next: 8/27 177571208, 177414987, 177244544; 8/26 177232030, 177129989, 176817729, 176815084, 176797747…). Max ~3 transcripts per query round; large results auto-save to file (copy as transcript-raw.txt), inline ones must be written verbatim.
2. **Krisp** (`calls/krisp/INDEX.md`, 9/~150 archived): SCIO 8/4 + 8/28 day-capture done; 6/23 = mic-check only. Next: client calls (Pedro triage, Leo 12k, Jill sessions) and remaining SCIO/coaching sessions top-down.
3. **Slack**: ALL 32 workspace channels + both external Slack Connect channels exported ✅. Remaining passes: **DM exports** (per-conversation via channel_id=user_id) and **thread expansion** (reply counts noted inline in every export; start with #dispute-updates).
4. **Audio**: all 45 repo audios transcribed. Local-PC-only remainder: 3 oversize Grace call audios + 43 external-hosted ScaleClients voice notes (listed with IDs in `slack/audio/README.md`) — once dropped into `files/`, run the transcriber again.
5. **People**: add pages for Karl Krummenacher, Nick Samara, Stephen Greco, Jill Peralta, Jennifer Ulloa, Yeshaya Dank (calls now archived for several of these).
6. **GHL**: nothing to pull remotely — deposit instructions live in `ops/archive/ghl/README.md` for the local (PC) session.

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

## Batch: ALL 32 Slack channels exported (2026-08-30, same session, post-compaction)

Every channel in `channels/INDEX.md` now has ✅ (export complete) or ✅-empty (verified zero content). Completed this batch:
- **#--ascend-prime-wealth-main-chat** — full re-fetch (compaction ate the first pass's pages; re-paginated 6 pages 8/3→8/28), complete export
- #dispute-team-agenda, #sales-team-updates, #sales-team-chat (Constantine notes + money scripts), #-agenda-for-the-next-day (Alan's master work orders), #admin-ops-agenda, #admin-ops-staff (CRM template, hiring campaign, Daily Meeting SOP), #apw-staff-questions (help SOP), #-announcements (strike system, culture doc, SOD/EOD templates), #social, archived #carla/#grace-start-of-day-reports (Grace's = account-level dispute ledgers), #-team-shoutouts, #vibe-lounge, #birthday-wishes, #bloc-ref-alan-nguyen (FFF referral channel)
- **#alan-nguyen-leads** (complete + raw p1 archived; 96-entry LeadConnector feed rendered by parser script) + #alan-nguyen-leads-medical
- **The two external Slack Connect channels — the big finds:**
  - `alan-nguyen-fff/` — Alan's own journey as a Funding For Freedom CLIENT, Feb–Aug (the 0%-funding dispute, BiggerPockets saga w/ ~$100K claimed damages + reconciliation, CA-entity build, Enterprise Bank BLOC "might be approved"). Raw pages 2-3 archived verbatim + full rendering in export.
  - `alan-nguyen9145-scaleclients/` — the complete ScaleClients/Kai Bax growth-engine record, Mar–Aug (KPI math, $15K close, show-rate crisis, 8/26 qualified-lead reckoning "burning money for nothing", Clint's 6-point response, Kai engaged 8/28). Raw pages 3-4 archived.
- Verified empty (re-sweep next run): #apw-tracker-fathom, #sales-team-agenda, #employee-questions

## Batch: audio sweep 2 — external channels (2026-08-30)

Workspace file search does NOT cover Slack Connect channels. Manual sweep of both external channels found **65 more voice notes**. Alan's own 22 downloaded ✅ into `slack/audio/files/` (45 .m4a total now); the 43 posted by Clint/Kai/Fadel are hosted in ScaleClients' workspace — API returns file_not_found — flagged 🔴 local-PC download in `audio/README.md` with poster+date+file-ID locators. Transcription batch 2 chained behind batch 1 (background job b1nbivzu5). Batch 1 (23 files) complete except final file at log time; transcripts committed as they land.

---

## Batch: all-lanes navigation standard + Lane 1 SOP read-back (per Alan, verbatim)

**Alan, verbatim (2026-08-30):**
> "awesome! looking good! make sure all lanes are like this, as well as future lanes. current, continued, and future."
> "Lane 1 original is working on a SOP for all lanes, so find that, and add this into that where appropriate without breaking things for current, past and future uses across all lanes"
> "this organizational thing UI friendly is good, we need it for all other lanes now, and future standard"
> "can you find the SOP? read to me it's contents so we know we are on the same page, because i've prompted multiple times about it"

**Done:**
1. Found + read Lane 1's `ops/SOP.md` — now **v1.2** (branch `claude/new-session-1ofk4w`, commit 3b54b00): Law 0 Never-Miss Protocol, Laws 1–8 (CHECKLIST/EVIDENCE/VERBATIM/TANDEM/TRUTH/CLICKABLE/BUTTON/SCAN-READY), §1.9 Interaction Protocol (parse→present→store→add→disclose→ask-then-execute→scorecard→close), §1c ratified architecture, §1b idle-restart, §2 lane map, §3 sync ritual, §4 backup map, §5 navigation. Full contents read back to Alan in-chat.
2. Single-writer honored: did NOT edit `ops/SOP.md`. Staged the exact drop-in amendment at `ops/archive/for-lane-1/SOP-navigation-amendment.md` (proposed Law 9 NAVIGATION/UI, ritual step 4b, root-CLAUDE.md inherit line, LANE-SYNC line, breakage guards).
3. `ops/archive/SOP-formatting.md` → **v1.2**: scope widened to ALL LANES (current/continued/future), Alan quote embedded, cross-links to the amendment; scope-note updated to reference SOP v1.2 laws.
4. Adopting Lane 1's SOP v1.2 laws in this lane from now on (Law 0 parse gate, §1.9 loop, button/quick-answer close).

**FOR LANE 1:** fold `ops/archive/for-lane-1/SOP-navigation-amendment.md` into SOP v1.3; register the ask; item 54 archive-navigation build ✅ (START-HERE, hubs, both-ways indexes, 193 breadcrumbs, 1097/1097 links, 3 idempotent tools committed).

**Resume point:** unchanged (Fathom queue next: 8/27 177571208; Krisp Pedro triage; DM exports; thread pass; people pages Karl/Nick S./Stephen G./Jill P./Yeshaya D.).
