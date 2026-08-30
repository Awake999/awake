# LANE 4 BRIEF — Alan's PC (machine-bound work)
*Written 2026-08-30 by Lane 1. Everything here requires the local machine: GHL PIT auth, interactive permission approvals, Ads Manager UI, Teramind admin.*

## A. Paste this into your LOCAL Claude Code / Cowork session (the big one)

> You are LANE 4 (local) of the APW multi-lane build. Clone/pull `awake999/awake`, check out branch `claude/new-session-1ofk4w`, and read `ops/README.md` + `ops/data/pointer-map.md` first. Work on your own new branch `claude/lane4-ghl-pull`; touch only `ops/archive/ghl/**` and `ops/lane4/**` plus your own dated process-log file.
>
> TASK 1 — GHL FULL PULL (read-only). Connect the GHL MCP: `https://services.leadconnectorhq.com/mcp/`, Bearer = the PIT stored on this machine, locationId `WFkoNzKa9J9PxhngsLfl` (location "Prismatic"). Pull and write into `ops/archive/ghl/` as dated CSV + markdown:
> 1. ALL contacts: id, name, email, phone, source, UTM fields (utm_source/medium/campaign/term/content, campaign_id, adset_id, ad_id), created date, tags, DND.
> 2. ALL appointments: contact, calendar, booked-at, slot time, STATUS (showed / no-show / cancelled / rescheduled) — this resolves 79 unknown show outcomes in the booking roster audit (`ops/data/BOOKING_ROSTER_AUDIT.md`).
> 3. Opportunities/pipeline stages with timestamps; payments/invoices/transactions; first-message/first-call timestamps per contact (speed-to-lead).
> 4. Conversations metadata (message counts, channels, any call recordings list — export links only, not audio files).
>
> TASK 2 — TODD IMPORT (the ONE approved GHL write, Alan authorized 8/12 and re-confirmed): execute `ops/lane4/TODD_GHL_IMPORT.md` §§1–7 exactly — create/update contact Todd LoGuidice (toddloguidice@gmail.com), tags, opportunity ($0 upfront / 4% success, Closed Won), notes timeline, document links, tasks. Capture the resulting GHL Contact ID into your report. Make NO other writes to GHL.
>
> TASK 3 — PUBLISH THE DASHBOARD: publish `ops/dashboard/apw_command_board.html` as a claude.ai Artifact, favicon "⚡", with capabilities `{"mcp":{"servers":[{"server":"Notion","tools":["notion-query-data-sources"]}]}}`. Alan is present to approve the permission prompt. Put the URL in your process-log + PR description.
>
> TASK 4 — commit + push your branch, open a draft PR "Lane 4: GHL ground truth + Todd import + publish". Report counts: contacts pulled, appointments with statuses, how many of the roster audit's 79 unknowns are now resolved, payments found (verify: Nick S. $500, Michael M. — expect NONE for Michael, flag if found; Jill installments).

## A2. TASKS 5–6 — ALSO CLAUDE-EXECUTABLE LOCALLY (added 8/30 after they were missed: they were mislabeled "manual" below; local Cowork CAN browser-control these)

> TASK 5 — LOOM LOCKDOWN (browser control; Alan present to approve): fetch Notion checklist row `3b95bb1ffef4813e9ac2d16384dfe7e9` for the 3 public Loom video URLs containing client SSNs/passwords. Open loom.com in the browser, set EACH to private/workspace-only, and report each video's final visibility state verbatim. Highest-severity open security item.
>
> TASK 6 — TERAMIND TOKEN (browser control): open the Teramind admin console → Settings/Integrations → API, generate an API token, save it to a LOCAL file outside the repo (never commit it, never paste it into any shared doc), and report only that it exists + its local path. If admin access needs Alan's login, hand him the keyboard for that step.
>
> RAW-ORIGINALS LAW (all tasks): store the RAW API responses (JSON) in ops/archive/ghl/raw/ alongside any derived CSV/markdown — Alan verbatim: "we need everything to have the same data, not the summaries but the raw, actual original."

## B. Manual steps while you're there (SUPERSEDED for items 1 & 3 by Tasks 5–6 above — remaining truly-manual: 2, 4, 5)

1. **Lock the 3 public Loom videos** containing client SSNs/passwords — checklist row `3b95bb1ffef4813e9ac2d16384dfe7e9`. Two minutes; highest-severity open risk.
2. **Meta Ads Manager → URL parameters** on the two ACTIVE campaigns (Medical Relaunch v2, Prof/BizOwners relaunch): `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&campaign_id={{campaign.id}}&adset_id={{adset.id}}&ad_id={{ad.id}}` (campaign-level; existing ads' url_tags are immutable — set it where Ads Manager allows, and on ALL new ads incl. the Sep 1 A/B).
3. **Teramind** (register item #49): grab an API token (Teramind admin → API) OR schedule a daily CSV export to the APW Data Hub Drive folder. Either one turns the contractor reports from hearsay into tool data.
4. **Invite Jacob to Meta Ads Manager** (blocks the Sep 1 10:00 AM PT A/B launch).
5. **Notion pending join request** — approve/deny ("1 user waiting to join Ascend Prime Wealth", likely ML).
