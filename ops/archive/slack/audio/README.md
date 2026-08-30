# Slack Audio — full inventory + hard-copy backup

Full workspace file-search sweep run 2026-08-30 (public + private channels + DMs + group DMs, all dates): **26 audio files + 1 video clip found.** 23 audio files are now **backed up as actual .m4a files in `files/`** in this repo (47.7 MB); 4 files exceed the 10 MB API download limit and need the local session (marked 🔴 below). File naming: `YYYY-MM-DD--poster--label--SLACKFILEID.m4a`.

**Transcription status:** Slack's API surface available to this lane returns the audio binary only — no built-in transcription is exposed. NO transcript exists yet for any of these except the written summaries Grace posted alongside her three call recordings (in `../channels/dispute-updates/2026-08.md`). Machine transcription is outside this lane's rules — the audio is preserved verbatim here so a transcription pass (local session, or on Alan's go) can produce `*.transcript.md` files next to each audio, tandem-style.

| Date | Poster | File | Size | In repo | Transcript |
|---|---|---|---|---|---|
| 2026-08-28 | Grace | Identity Theft and Data Breach Dispute Resolution.m4a (F0BTBHVSP4M) — Ashwini EXP call | 12.5 MB | 🔴 too large for API — local pull | written summary in dispute-updates 8/28 09:59 |
| 2026-08-27 | Grace | Problemas con TransUnion….m4a (F0BSUDRCXRV) — Matthew TU CFPB call | 18.7 MB | 🔴 local pull | written summary 8/27 17:45 |
| 2026-08-27 | Grace | 20260828_053829.m4a (F0BT913GULA) — Matthew EXP call | 10.1 MB | 🔴 local pull | written summary 8/27 15:06 |
| 2026-08-22 | Alan | Audio Clip 12:41 (F0BSVDRDC48) | 2.3 MB | ✅ | needs-transcription |
| 2026-08-20 | Alan | audio_message a (F0BRJ6LDL5R) | 4.6 MB | ✅ | needs-transcription |
| 2026-08-20 | Alan | audio_message b (F0BSJQBQQF2) | 78 KB | ✅ | needs-transcription |
| 2026-08-20 | Grace | audio_message (F0BSJ5M67K2) | 1.6 MB | ✅ | needs-transcription |
| 2026-08-14 | Lynn | Video Clip 20:02 (F0BQBLYAEUW, .mov) | >10 MB | 🔴 local pull | needs-transcription |
| 2026-08-13 | Alan | Audio Clip 22:55 (F0BPRFWHEUF) | 2.0 MB | ✅ | needs-transcription |
| 2026-08-12 | Alan | Audio Clip 18:56 (F0BPQDGE37V) | 1.8 MB | ✅ | needs-transcription |
| 2026-08-06 | Alan | Audio Clip 12:07 (F0BPE29H7LY) | 428 KB | ✅ | needs-transcription |
| 2026-08-06 | Alan | Audio Clip 11:16 (F0BNK9625LJ) | 1.1 MB | ✅ | needs-transcription |
| 2026-08-03 | Alan | Audio Clip 22:49 (F0BMCQVTG3Z) | 603 KB | ✅ | needs-transcription |
| 2026-08-03 | Alan | Audio Clip 22:47 (F0BMXSLLHC4) | 952 KB | ✅ | needs-transcription |
| 2026-08-01 | Alan | Audio Clip (F0BMDT103LZ) | 1.4 MB | ✅ | needs-transcription |
| 2026-07-21 | Alan | audio_message (F0BJUNH7PRU) | 4.6 MB | ✅ | needs-transcription |
| 2026-07-17 | Alan | audio_message (F0BJ44ALZN2) | 3.5 MB | ✅ | needs-transcription |
| 2026-07-13 | Alan | audio_message (F0BH0FU1V1C) | 1.6 MB | ✅ | needs-transcription |
| 2026-07-07 | Alan | audio_message x3 (F0BFQKY5P0D, F0BGN8Y1B96, F0BGKPQ8N8Y) | 81 KB / 400 KB / 397 KB | ✅✅✅ | needs-transcription |
| 2026-06-29 | Alan | audio_message x2 (F0BEVA9HTL0, F0BDYU2TB5L) | 3.0 / 4.4 MB | ✅✅ | needs-transcription |
| 2026-06-25 | Alan | audio_message (F0BE4LARW48) | 3.0 MB | ✅ | needs-transcription |
| 2026-06-20 | Alan | audio_message (F0BBY1TFSH3) | 4.6 MB | ✅ | needs-transcription |
| 2026-06-08 | Alan | Audio Clip 17:41 (F0BA0LKS6M6) | 733 KB | ✅ | needs-transcription |
| 2026-06-01 | Alan | Audio Clip 23:07 (F0B75N9R007) | 2.3 MB | ✅ | needs-transcription |

## Local-session task (the 4 red rows)
On Alan's PC, download from Slack (each file's message is findable by its file ID or date in the source channel) and drop into `files/` with the same naming pattern, then flip 🔴 → ✅ here.

## Related audio living outside Slack
- **Zoom cloud recordings** (7, all with official transcripts): `../../calls/zoom/INDEX.md`
- **Zoom Clips** (dispute-team bureau-call clips): links preserved throughout `../channels/dispute-updates/2026-08.md`; hard-copy export needs the Zoom web UI (local task).
- **Fathom/Krisp** recordings: their platforms hold audio+video; verbatim transcripts are what this archive stores (see `../../calls/`).
