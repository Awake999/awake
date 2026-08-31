# Formatting, Navigation & Transcription SOP — v1.2 (2026-08-30) — ALL-LANES STANDARD

> 🧭 [Start Here](START-HERE.md) · [Archive home](README.md)

**SCOPE (v1.2, per Alan 2026-08-30):** this standard is binding on **every lane — current, continued, and future** — not just the archive. Alan, verbatim: *"make sure all lanes are like this, as well as future lanes. current, continued, and future… this organizational thing UI friendly is good, we need it for all other lanes now, and future standard."* Any lane creating human-facing files (dashboards, data notes, dossiers, exports, logs meant for reading) applies the laws below to its own surface: landing page or hub entry, 🧭 breadcrumbs, both-ways clickable indexes, no giant text blocks. A reference write-up exists at [for-lane-1/SOP-navigation-amendment.md](for-lane-1/SOP-navigation-amendment.md) — Lane 1 adds it to `ops/SOP.md` where relevant, at Lane 1's discretion (Alan, 8/31: Lane 3 keeps all changes on its own side).

**TLDR:** No giant blocks of text, ever. Every transcript gets a header, 10-minute chapters, and a clickable table of contents; anything huge is split into linked part-files; every long audio is transcribed in chapters. Two committed tools do this automatically on every run, on any machine. Verbatim content is never altered — structure is only ever ADDED.

## Why this SOP exists (Alan, verbatim, 2026-08-30)

> "the longer ones, please split them up and transcribe them"
> "please optimize and organize and format to be human + AI friendly simultaneously so it's not just giant blocks of text for humans. make it easy to navigate"
> (standing, from earlier the same day:) "make that a normal standard operating procedure with constant updates. And perfect sorting. Remember, everything should be a clickable link."

---

## The laws

| # | Law | What it means in practice |
|---|---|---|
| 1 | **HEADER** | Every archived file opens with a short metadata block: what it is, date, source system + ID, clickable source link, pointer to the raw original, archived date. |
| 2 | **CHAPTERS** | Transcripts get a `## Chapter N (MM:SS to MM:SS)` heading every 10 minutes of meeting time. A new recording segment (timestamps reset) starts a new chapter. |
| 3 | **CONTENTS** | Any file with 2+ chapters gets a `### Contents` list of clickable chapter anchors right under the header. |
| 4 | **SPLIT** | Any transcript over ~150 KB is split into `transcript-part-N.md` files (~110 KB each); `transcript.md` becomes the index — header + a Parts & chapters map linking into every part. |
| 5 | **VERBATIM** | Formatting only ADDS structure (headings, TOC, metadata). Content lines are never altered, dropped, or paraphrased. Raw originals (`transcript-raw.*`) are NEVER touched or split. |
| 6 | **AUDIO** | Every audio file gets downloaded into `slack/audio/files/` (naming `YYYY-MM-DD--poster--label--FILEID.m4a`) and machine-transcribed beside itself; long audio comes out pre-chaptered with a TOC. Audio stays the source of truth. Videos stay links. |
| 7 | **CONSTANT UPDATES** | Both tools are idempotent (formatted files carry `<!-- formatted: chapters-v1 -->` and are skipped), so every archiving run ends by re-running them over the whole archive. |
| 8 | **NAVIGATION** | Every file opens with a 🧭 breadcrumb line (Start Here · Archive home · category hub · ⬆ its index) so a human can always click backwards. Every index row is clickable both ways: to the archived files here AND to the original on the source platform (fathom.video / app.krisp.ai / Slack). No copy-pasting paths or IDs, ever. The front door for beginners is [START-HERE.md](START-HERE.md). |
| 9 | **HUMAN + AI TANDEM** | Humans get scannable chapters, clickable TOCs, and bolded speaker/timestamp lines. AI gets stable line formats (`[MM:SS](link) Speaker: text`, `**Name** [HH:MM:SS]: text`, `**Name | MM:SS**`), predictable anchors, and raw originals beside every rendering. Same files serve both — no duplicates to drift. |

## The tools (committed in [`tools/`](tools/) so ANY machine can run them)

| Tool | What it does | Run |
|---|---|---|
| [`tools/format_transcripts.py`](tools/format_transcripts.py) | Chapters + TOC on every transcript; splits oversize ones into parts; idempotent | `python3 ops/archive/tools/format_transcripts.py` |
| [`tools/transcribe.py`](tools/transcribe.py) | Transcribes every audio in `slack/audio/files/` that lacks a transcript; chaptered output for long recordings | `pip install faster-whisper` once, then `python3 ops/archive/tools/transcribe.py` |
| [`tools/add_breadcrumbs.py`](tools/add_breadcrumbs.py) | Adds the 🧭 navigation line to any new file that lacks one; idempotent | `python3 ops/archive/tools/add_breadcrumbs.py` |

## The end-of-run ritual (every archiving session, every lane)

1. Pull latest (`git pull`).
2. Archive new material per the existing capture SOPs (raw beside rendering, naming conventions).
3. `python3 ops/archive/tools/transcribe.py` — picks up any newly dropped audio.
4. `python3 ops/archive/tools/format_transcripts.py` — chapters/TOCs/splits anything new.
5. `python3 ops/archive/tools/add_breadcrumbs.py` — navigation line on anything new.
6. Link new transcripts into [`slack/audio/README.md`](slack/audio/README.md) and flip INDEX rows (clickable both ways: source platform + archived files).
7. Commit + push. Log the batch in your lane's process-log file.

## Local-PC flow for unreachable audio (the 46 files)

The 3 oversize Grace recordings (>10 MB Slack API cap) and the 43 ScaleClients-hosted voice notes (external workspace — API returns file_not_found) can only be downloaded from a logged-in Slack client. On Alan's PC:
1. Open the message (each is listed with poster + date + file ID in [`slack/audio/README.md`](slack/audio/README.md)), download the file.
2. Drop it into `ops/archive/slack/audio/files/` with the standard naming.
3. Run `python3 ops/archive/tools/transcribe.py` (splits long ones into chapters automatically), then commit + push — or just commit + push the audio and any cloud lane will transcribe on its next run.

## Scope notes

- Slack **channel exports** are already structured (date/topic headings, bolded speakers, grouped logistics) — the SPLIT law applies to them too if one ever exceeds ~150 KB.
- **Summaries** stay short by design (TANDEM law: summary beside transcript, never replacing it).
- This SOP extends — never overrides — the repo-wide laws in `ops/SOP.md` (v1.2 read 2026-08-30: Law 0 Never-Miss, Laws 1–8, §1.9 Interaction Protocol — all honored here). A reference write-up for Lane 1 sits at [for-lane-1/SOP-navigation-amendment.md](for-lane-1/SOP-navigation-amendment.md); Lane 1 uses it where relevant, at its own discretion (Alan's 8/31 ruling: changes stay on the archive side; Lane 3 does not add onto Lane 1's work).

**Simple TLDR:** run the two tools at the end of every session; they make everything chaptered, clickable, and split — without ever changing a word.
