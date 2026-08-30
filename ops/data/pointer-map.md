# Pointer Map — where everything lives (point, don't re-derive)

## Notion — data sources (query with `collection://` IDs)
| Database | ID | Rows (8/30) |
|---|---|---|
| Clients & Leads (MASTER) | `collection://5614ffa0-e3d0-40cb-ae64-b32ec52e288c` | 74 |
| Communications Log | `collection://09c1e23f-9c55-468f-b4f2-19c7fe011477` | 341 |
| Documents | `collection://725de51f-afb9-49ba-b121-d325dc33acb1` | 117 |
| Ad Scoreboard | `collection://e6b27822-c7a7-43af-b6e3-c8832c6f34a4` | 26 |
| Call Library | `collection://51af1527-a898-480a-94e1-14c28f396da0` | 146+ |
| SOP Library | `collection://9f07f2d4-493f-4d66-9d91-3195ab28d6f8` | 21+ |
| Master Ops Checklist | `collection://377886f5-f8e6-492b-8099-10f9c8943a96` | 55+ |
| Stage History | `collection://0cd9f603-f15a-4fc2-9169-72bc50826bc7` | ~28 |
| Deals & Payments | `collection://0c2059ee-3910-4eb8-8927-d0a44ccaf53d` | — |
| Disputes | `collection://237947ff-e465-42b8-b49c-4b3dfa99a6ef` | — |

## Notion — key pages
- APW OPS HUB: `3ba5bb1ffef48182b54cde51f6da1ae2`
- Client Tracking Command Center: `3b75bb1ffef48196aa4efcf029dc732d`
- FULL-FUNNEL INSIGHT REBUILD — Master Checklist: `3cc5bb1ffef48188aefad6ab7527616f`
- Qualification Standard (Kai): `3cc5bb1ffef481aa8c8ce7c33bade43b`
- 4-Day Dispute SOP: `3ca5bb1ffef481468487e9be6136ba40`
- Pre-Booking Qualification Filter SOP: `3ca5bb1ffef481d08aa6ed398c388176`
- Master Closing Framework v2: `3b95bb1ffef481f293fbeaf311e224e4`
- Client Document Dossiers: `3b95bb1ffef481bf8a6ad869157d72e0`
- Pricing conflict row (FIVE structures): `3bc5bb1ffef481e2aba4d89e9032c29c`

## Clients & Leads — funnel-tracking schema (added 8/30 per Alan's spec)
`Entry Path` (Direct Booked Call / Opt-In Form / DM / Referral) · `Human Triaged` (Yes-before / Yes-after / No / Unknown) · `Triage Date` · `Speed to Lead (min)` · `Booking to Triage (hrs)` · `Qualification` (Main / Downsell / Unq-NoFunds / Unq-Mismatch / Unq-Other) · `Unqualified Reasons` (multi) · `No-Close Reason`

## Drive
- LOCAL_PULL_RUNBOOK (GHL, machine-bound): `1RqEpBa4Em1iwE_GdHhuk_kxhotBYXPjx`
- BACKFILL_FINDINGS v3 FINAL: `1cc38HfZOekS2TqhubCckI0lDDLajplJA`
- AD_TRACKING_SPEC: `1ymOUhLTkuTJLoOaz5ba0gyXom85nP9kq`
- COWORK_HANDOFF_PROMPT: `1_dyhMd9ol_-q0wVUaV5BTkCMI232zKuo`

## GHL (local-only access)
Location "Prismatic" `WFkoNzKa9J9PxhngsLfl` · MCP: services.leadconnectorhq.com/mcp/ · Bearer PIT on Alan's PC only.
Todd L. import package: session scratchpad `TODD_GHL_IMPORT.md` (approved write, pending local run).

## Meta
Ad account (from billing receipt): `1821085838595242` · UTM template in AD_TRACKING_SPEC · url_tags immutable on existing ads — set at campaign level in Ads Manager.

## Key recordings (doctrine sources)
- AG escalation strategy: fathom.video/calls/803352097 + /803353666
- 4-day dispute doctrine: fathom.video/calls/801867207
- Funnel rebuild w/ Jacob (Sep 1 A/B): fathom.video/calls/801234866
- Revenue diagnosis ($0 August): fathom.video/calls/803087357
- Qualification standard origins: /798787726 (Robert M.), /803053542 (ICP mismatch)
