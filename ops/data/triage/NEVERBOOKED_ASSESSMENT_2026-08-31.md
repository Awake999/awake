# 🔍 The 9 never-booked cohort leads — per-person assessment (Alan-ordered 8/31)

> 🗣️ Alan, 8/31 (verbatim, [stored ↗](../../prompts/2026-08-31-data-correction-demands.md)):
> *"analyze if they have an unresponsive tag, otherwise look at our actual correspondence with
> them to assess each"*

Method: GHL tags first (raw pull `contacts.json`), then the actual correspondence
(`messages_by_conversation.json` — every dial, text, email, and inbound reply). Numbers
verified 8/31; "connected" counts completed call legs with duration > 0 (voicemail-length
included). Assessments also show live on the board — hover any of these rows' 🎯.

| Person | GHL tags (verbatim) | Dials (conn.) | Texts out/in | Last touch | ASSESSMENT |
|---|---|---|---|---|---|
| Javaris Johnson | new lead scio · medical · 0 lynn - spl - yes · 0 - no answer · **0 - unresponsive** | 8 (6) | 10/0 +1 email | 8/27 | **UNRESPONSIVE — tag verified by data** |
| Njjnn Of | new lead scio · 0 - no answer · **0 - unresponsive** | 6 (6) | 6/0 | 8/26 | **UNRESPONSIVE (tag) — fake-looking opt-in** |
| Natalia Rumbuc | new lead scio · 0 - no answer · **0 - unresponsive** | 11 (8) | 9/0 | 8/27 | **UNRESPONSIVE — tag verified by data** |
| LeRoy McCall | 0 - no answer · 1 - connected · **0 - unresponsive** | 6 (2) | 7/**1** | 8/18 | **UNRESPONSIVE (tag)** — one inbound 7/29: “Please text me.” — then silence through 7 texts |
| Noel Rivera | new lead scio · **2 - hung up** | 5 (1) | 5/0 | 8/26 | **HUNG UP** — reached live once, hung up; nothing since |
| John Mazzocchi | 0 - no answer (no unresponsive tag) | 10 (5) | 9/0 | 8/26 | **UNRESPONSIVE IN FACT** — untagged; Lane 1 should tag |
| HERMAN ROGERS | high priority · 0 - no answer (no tag) | 9 (7) | 10/0 | 8/27 | **UNRESPONSIVE IN FACT** — untagged despite high-priority chase; Lane 1 should tag |
| Fernando De Pieri | 0 - no answer (no tag) | 4 (3) | 4/0 | 8/28 | **NO REPLY YET** — fresh 8/27 lead, only 2 days of chase at pull time; too early to call unresponsive |
| Marko Sakren | new lead scio (no status tag) | 2 (1) | 2/0 | 8/18 | **UNDER-WORKED** — only 2 dials + 2 texts, chase stopped 8/18; unresponsiveness NOT proven — re-chase or close out |

## What this changes
- 4 verified UNRESPONSIVE (tagged) · 2 unresponsive in fact (Lane 1: add the tag) · 1 hung-up ·
  1 too-fresh · 1 under-worked (the one actionable re-chase).
- LANE-SYNC → Lane 1: tag John Mazzocchi + HERMAN ROGERS `0 - unresponsive` in GHL/Notion
  (their data already proves it); decide Marko Sakren (re-chase vs close).
- Assessments are injected into the board (APW_L1 `note`) and appear in each row's 🎯 hover.
