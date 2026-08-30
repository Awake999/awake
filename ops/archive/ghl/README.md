# GHL Archive — machine-bound data, deposited here

> 🧭 [Start Here](../START-HERE.md) · [Archive home](../README.md)

GoHighLevel (location "Prismatic", `WFkoNzKa9J9PxhngsLfl`) can only be pulled from Alan's PC — the Private Integration Token lives there and nowhere else (MCP endpoint: services.leadconnectorhq.com/mcp/). See LOCAL_PULL_RUNBOOK on Drive (`1RqEpBa4Em1iwE_GdHhuk_kxhotBYXPjx`).

## Instructions for the LOCAL session depositing GHL exports

When you run a GHL pull on Alan's PC, deposit the exports into this folder on a branch and open a PR (or push to an archive branch). Layout:

```
ghl/
  contacts/YYYY-MM-DD-export.md        ← contact snapshots, one file per pull date
  conversations/<first-last>/YYYY-MM.md ← message threads per contact, chronological, author-stamped
  audio/README.md                       ← inventory of call recordings / voicemails + transcription status
  audio/transcripts/<first-last>/YYYY-MM-DD--<slug>.md  ← verbatim transcriptions
```

Rules (same as the rest of the archive):
- **Append-only** — never rewrite an existing export; new pulls get new dated files.
- **Verbatim** — full message text, timestamps, and sender names. Summaries only ever *alongside* originals.
- Note the GHL contact ID in each contact/conversation file so it links back to the system of record.
- Update this README's inventory table below after each deposit.

## Deposit inventory

| Date deposited | What | Files | By |
|---|---|---|---|
| — | Nothing deposited yet | — | — |

Pending known work: Todd L. import package (session scratchpad `TODD_GHL_IMPORT.md`, approved write, pending local run).
