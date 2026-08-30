# Slack Audio — full inventory + hard-copy backup + transcripts

## STANDING SOP (Alan, verbatim 2026-08-30: "just send links if those are videos… we do need to physically download audios and transcribe those. Transcribe them yourself" + "make that a normal standard operating procedure with constant updates. And perfect sorting… everything should be a clickable link")

1. **Audios:** physically download into `files/` (naming `YYYY-MM-DD--poster--label--SLACKFILEID.m4a`) → machine-transcribe (faster-whisper, small model) → save `*.transcript.md` BESIDE the audio (audio remains the source of truth) → add a row below → commit + push. Every archiving run re-sweeps the workspace file search for new audio.
2. **Videos:** clickable permalink only — never downloaded.
3. **Every entry in this inventory is a clickable link** — to the repo file when downloaded, to the Slack permalink when not.
4. Files over the 10 MB API cap: row keeps its permalink + 🔴 until the local session downloads it into `files/`, then it gets transcribed like the rest.

Full workspace file-search sweep run 2026-08-30 (public + private channels + DMs + group DMs, all dates): **26 audio files + 1 video clip found.** A second sweep the same day through the two external Slack Connect channels (which workspace file search does NOT cover) found **65 more voice notes** — see the second table below. **45 audio files are now backed up as actual .m4a files in [`files/`](files/)**; transcripts are generated beside them.

| Date | Poster | File | Size | In repo | Transcript |
|---|---|---|---|---|---|
| 2026-08-28 | Grace | [Identity Theft and Data Breach Dispute Resolution.m4a](https://alan-n-95.slack.com/files/U0ADC1UNXAQ/F0BTBHVSP4M/identity_theft_and_data_breach_dispute_resolution.m4a) — Ashwini EXP call | 12.5 MB | 🔴 over 10 MB API cap — local download, then transcribe | written summary in dispute-updates 8/28 09:59 |
| 2026-08-27 | Grace | [Problemas con TransUnion Robo de Identidad y Filtración de Datos.m4a](https://alan-n-95.slack.com/files/U0ADC1UNXAQ/F0BSUDRCXRV/problemas_con_transunion_robo_de_identidad_y_filtraci__n_de_datos.m4a) — Matthew TU CFPB call | 18.7 MB | 🔴 local download, then transcribe | written summary 8/27 17:45 |
| 2026-08-27 | Grace | [20260828_053829.m4a](https://alan-n-95.slack.com/files/U0ADC1UNXAQ/F0BT913GULA/20260828_053829.m4a) — Matthew EXP call | 10.1 MB | 🔴 local download, then transcribe | written summary 8/27 15:06 |
| 2026-08-22 | Alan | Audio Clip 12:41 (F0BSVDRDC48) | 2.3 MB | ✅ | [transcript ✅](files/2026-08-22--alan-nguyen--audio-clip--F0BSVDRDC48.transcript.md) |
| 2026-08-20 | Alan | audio_message a (F0BRJ6LDL5R) | 4.6 MB | ✅ | [transcript ✅](files/2026-08-20--alan-nguyen--audio-message-a--F0BRJ6LDL5R.transcript.md) |
| 2026-08-20 | Alan | audio_message b (F0BSJQBQQF2) | 78 KB | ✅ | [transcript ✅](files/2026-08-20--alan-nguyen--audio-message-b--F0BSJQBQQF2.transcript.md) |
| 2026-08-20 | Grace | audio_message (F0BSJ5M67K2) | 1.6 MB | ✅ | [transcript ✅](files/2026-08-20--grace--audio-message--F0BSJ5M67K2.transcript.md) |
| 2026-08-14 | Lynn | [Video Clip (2026-08-14 20:02:29).mov](https://alan-n-95.slack.com/files/U0ADC1UNXAQ/F0BQBLYAEUW/video_clip__2026-08-14_20_02_29_.mov) | 90.6 MB | 🔗 link only — videos are not downloaded (SOP) | n/a |
| 2026-08-13 | Alan | Audio Clip 22:55 (F0BPRFWHEUF) | 2.0 MB | ✅ | [transcript ✅](files/2026-08-13--alan-nguyen--audio-clip--F0BPRFWHEUF.transcript.md) |
| 2026-08-12 | Alan | Audio Clip 18:56 (F0BPQDGE37V) | 1.8 MB | ✅ | [transcript ✅](files/2026-08-12--alan-nguyen--audio-clip--F0BPQDGE37V.transcript.md) |
| 2026-08-06 | Alan | Audio Clip 12:07 (F0BPE29H7LY) | 428 KB | ✅ | [transcript ✅](files/2026-08-06--alan-nguyen--audio-clip-1207pm--F0BPE29H7LY.transcript.md) |
| 2026-08-06 | Alan | Audio Clip 11:16 (F0BNK9625LJ) | 1.1 MB | ✅ | [transcript ✅](files/2026-08-06--alan-nguyen--audio-clip-1116am--F0BNK9625LJ.transcript.md) |
| 2026-08-03 | Alan | Audio Clip 22:49 (F0BMCQVTG3Z) | 603 KB | ✅ | [transcript ✅](files/2026-08-03--alan-nguyen--audio-clip-2249--F0BMCQVTG3Z.transcript.md) |
| 2026-08-03 | Alan | Audio Clip 22:47 (F0BMXSLLHC4) | 952 KB | ✅ | [transcript ✅](files/2026-08-03--alan-nguyen--audio-clip-2247--F0BMXSLLHC4.transcript.md) |
| 2026-08-01 | Alan | Audio Clip (F0BMDT103LZ) | 1.4 MB | ✅ | [transcript ✅](files/2026-08-01--alan-nguyen--audio-clip--F0BMDT103LZ.transcript.md) |
| 2026-07-21 | Alan | audio_message (F0BJUNH7PRU) | 4.6 MB | ✅ | [transcript ✅](files/2026-07-21--alan-nguyen--audio-message--F0BJUNH7PRU.transcript.md) |
| 2026-07-17 | Alan | audio_message (F0BJ44ALZN2) | 3.5 MB | ✅ | [transcript ✅](files/2026-07-17--alan-nguyen--audio-message--F0BJ44ALZN2.transcript.md) |
| 2026-07-13 | Alan | audio_message (F0BH0FU1V1C) | 1.6 MB | ✅ | [transcript ✅](files/2026-07-13--alan-nguyen--audio-message--F0BH0FU1V1C.transcript.md) |
| 2026-07-07 | Alan | audio_message x3 (F0BFQKY5P0D, F0BGN8Y1B96, F0BGKPQ8N8Y) | 81 KB / 400 KB / 397 KB | ✅✅✅ | [a ✅](files/2026-07-07--alan-nguyen--audio-message-a--F0BGKPQ8N8Y.transcript.md) / [b ✅](files/2026-07-07--alan-nguyen--audio-message-b--F0BGN8Y1B96.transcript.md) / [c ✅](files/2026-07-07--alan-nguyen--audio-message-c--F0BFQKY5P0D.transcript.md) |
| 2026-06-29 | Alan | audio_message x2 (F0BEVA9HTL0, F0BDYU2TB5L) | 3.0 / 4.4 MB | ✅✅ | [a ✅](files/2026-06-29--alan-nguyen--audio-message-a--F0BDYU2TB5L.transcript.md) / [b ✅](files/2026-06-29--alan-nguyen--audio-message-b--F0BEVA9HTL0.transcript.md) |
| 2026-06-25 | Alan | audio_message (F0BE4LARW48) | 3.0 MB | ✅ | [transcript ✅](files/2026-06-25--alan-nguyen--audio-message--F0BE4LARW48.transcript.md) |
| 2026-06-20 | Alan | audio_message (F0BBY1TFSH3) | 4.6 MB | ✅ | [transcript ✅](files/2026-06-20--alan-nguyen--audio-message--F0BBY1TFSH3.transcript.md) |
| 2026-06-08 | Alan | Audio Clip 17:41 (F0BA0LKS6M6) | 733 KB | ✅ | [transcript ✅](files/2026-06-08--alan-nguyen--audio-clip--F0BA0LKS6M6.transcript.md) |
| 2026-06-01 | Alan | Audio Clip 23:07 (F0B75N9R007) | 2.3 MB | ✅ | [transcript ✅](files/2026-06-01--alan-nguyen--audio-clip--F0B75N9R007.transcript.md) |

## External Slack Connect channel audio (sweep 2 — 2026-08-30)

The [#alan-nguyen9145 ScaleClients channel](../channels/alan-nguyen9145-scaleclients/2026-03-to-2026-08.md) and [#alan-nguyen FFF channel](../channels/alan-nguyen-fff/2026-02-to-2026-08.md) carry 65 voice notes (Mar–Aug 2026) that workspace file search misses. **Alan's own 22 are downloaded ✅ into [`files/`](files/)** (each row's file is the clickable name). The 43 posted by ScaleClients members (Clint Losch, Kai Bax, Fadel) are hosted in *their* workspace — the API returns file_not_found, so they are 🔴 **local-PC task**: open the channel on the date shown, play/save the clip, drop into `files/` with the standard naming, then it gets transcribed like the rest.

**Alan's downloaded ✅ (22, all ScaleClients channel, transcription queued):** 3/26 x4 (F0ANZRA11MK, F0ANMS2PXMM, F0APG8RM31P, F0AP3C55C4A) · 6/1 x2 (F0B7GAZ784D, F0B7GACHM9B) · 6/9 x2 (F0B96FB1LUB, F0B9ES87EAD) · 6/10 x4 (F0B97U1SEEB, F0B9KV04MJR, F0B9N61R2P7, F0B9T2J5E84) · 6/22 (F0BBXHYR7K9) · 6/23 x3 (F0BCLBZ0AP8, F0BCFUUPWAF, F0BCSTXNMUH) · 6/29 x3 (F0BETQ8MZDE, F0BETQZUDJL, F0BDXC59230) · 7/3 (F0BEZ10ESJZ) · 7/20 x2 (F0BJDRK1B19, F0BJL3Q8L10)

**External-hosted 🔴 (43, by poster + date, ScaleClients channel unless noted):**
- **Clint Losch (33):** 3/5 F0AJRB2K4NN · 3/10 F0AL4SMMUJD · 3/12 F0ALHJVTX97 · 3/13 F0ALNT2DPLL · 3/16 F0AM9BEA45P · 3/26 F0AP6CHFECC · 3/31 F0AQ0ELDSJJ · 4/1 F0AR3UHH09E · 4/2 F0AQHH10734 · 4/10 F0AS1NT68CE · 4/13 x3 F0AS68XGBCP F0ASKLS927Q F0AT0KMMVRP · 4/16 F0ATT6Y1DT3 · 4/17 F0AT8RQ3FF1 · 4/21 x2 F0AUB5239SN F0AURRK8WKT · 4/22 F0AVDP1TVL0 · 4/24 F0B0191AP7B · 4/29 F0B0J2K6FTM · 4/30 F0B0VGM0LMR · 5/1 F0B11GJERPX · 5/6 F0B209MV30V · 5/22 F0B5M9RNE73 · 6/1 F0B7CRDDQTD · 6/10 x2 F0B9HRSM6DU F0B99952JET · 6/12 F0BA92YEV33 · 6/15 F0BAVPLR8BW · 6/22 F0BC9EKGEN9 · 6/23 x2 F0BCNAY7RGS F0BC5NF9R7Z · 7/3 F0BF3SQ7H17 · 7/6 F0BFDNZJRN2 · 7/31 F0BLT1KNX47
- **Kai Bax (4):** 6/1 x3 F0B7QPCA2N8 F0B8FEMK4RE F0B75MNT47R · **8/28 F0BU77N0Q2C (his reply to the metrics audit — high priority)**
- **Fadel (4):** 3/3 F0AJ6BK5C5C · 6/2 x2 F0B7M3LN2E7 F0B7RCS5XML · 7/1 F0BELE6EF34
- *(3 more of Alan's from this channel were already in the first sweep: 6/1 F0B75N9R007, 6/8 F0BA0LKS6M6, 7/13 F0BH0FU1V1C.)*

## Local-session task (the 4 red rows)
On Alan's PC, download from Slack (each file's message is findable by its file ID or date in the source channel) and drop into `files/` with the same naming pattern, then flip 🔴 → ✅ here.

## Related audio living outside Slack
- **Zoom cloud recordings** (7, all with official transcripts): `../../calls/zoom/INDEX.md`
- **Zoom Clips** (dispute-team bureau-call clips): links preserved throughout `../channels/dispute-updates/2026-08.md`; hard-copy export needs the Zoom web UI (local task).
- **Fathom/Krisp** recordings: their platforms hold audio+video; verbatim transcripts are what this archive stores (see `../../calls/`).
