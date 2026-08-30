# Slack Audio Inventory

Every audio clip / voice note found while exporting Slack channels gets a row here, with its permalink and transcription status.

**Policy:** we do NOT machine-transcribe audio in this lane. If Slack already produced a transcription (or someone typed one in the thread), it is copied verbatim next to the row's channel export. Otherwise status stays `needs-transcription` for a human or the local session to handle.

| Date | Channel | Poster | File | Transcription |
|---|---|---|---|---|
| 2026-08-26 | #dispute-updates | Grace | `Identity Theft and Data Breach Dispute Resolution.m4a` (Slack file F0BTBHVSP4M, 12.5 MB) — Ashwini Experian call | needs-transcription (no transcript in thread) |
| 2026-08-27 | #dispute-updates | Grace | `Problemas con TransUnion Robo de Identidad y Filtración de Datos.m4a` (Slack file F0BSUDRCXRV, 18.7 MB) — Matthew TU CFPB follow-up | needs-transcription; Grace's written summary is in `../channels/dispute-updates/2026-08.md` (2026-08-27 17:45) |
| 2026-08-27 | #dispute-updates | Grace | `20260828_053829.m4a` (Slack file F0BT913GULA, 10.1 MB) — Matthew Experian call | needs-transcription; written summary at 2026-08-27 15:06 in the channel export |

Note: many dispute-call recordings are shared as **Zoom clip links** rather than Slack audio uploads — those permalinks are preserved inline in the channel exports and the originals live in the team's Zoom account.
