# 💬 Slack DM Exports — in progress

> 🧭 [Start Here](../../START-HERE.md) · [Archive home](../../README.md) · [Slack hub](../README.md)

One folder per DM conversation. Raw pages are saved as captured (newest-first, verbatim, one file per API page) the moment they are pulled — the rendered chronological export is built once a conversation's pages are complete. Status:

| DM | Channel | Pages captured | Rendered export |
|---|---|---|---|
| [Carla Stivala](carla-stivala/) | D0BP6H6AF44 | ✅ COMPLETE — 9 pages, 802 messages, Aug 9–29 ([page 1](carla-stivala/raw-page1.txt) … [page 9](carla-stivala/raw-page9.txt)) | ✅ [export.md](carla-stivala/export.md) (chronological, verbatim) |
| [Lynn N.](lynn-n/) | D0BMPBLHXSA | ✅ COMPLETE — 7 pages, 676 messages, Aug 5–30 ([page 1](lynn-n/raw-page1.txt) … [page 7](lynn-n/raw-page7.txt)) | ✅ [export.md](lynn-n/export.md) (chronological, verbatim) |
| [Ina Grace Langub](grace-langub/) | D0BP49VMRUJ | ✅ COMPLETE — 3 pages, 254 messages, Aug 9–29 ([page 1](grace-langub/raw-page1.txt) … [page 3](grace-langub/raw-page3.txt)) | ✅ [export.md](grace-langub/export.md) (chronological, verbatim) |
| Rosemarie Anne Fabian | — | queued | — |

⚠️ FOR LANE 1 — plaintext credentials found in these DMs (rotation recommended, per the register-#73 pattern):
- 8/27 14:30 PDT: Carla's Teramind password (register #73 already flags this one).
- 8/12 13:34 PDT: Carla's `carla@ascendprimewealth.com` Google login password, sent in-DM.
- 8/12 14:28 PDT: standalone credential string "APW2026$$" (context: credit-report portal for the Whitney lead).
- Lynn DM, 8/20 09:35 PDT: Alan sent Lynn's new `lynn@ascendprimewealth.com` GHL login password in plaintext (`L9CDAHjP4BuU2hL=`), raw page 3.

Rendering tool: [`tools/render_dm.py`](../../tools/render_dm.py) — builds export.md chronologically from the raw pages, content untouched; rerun after any new page lands.
