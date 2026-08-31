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

## A3. TOP-PRIORITY ADDITIONS (8/30 late — Alan: "prioritize teramind do it for me" + "65 whop")

> TASK 7 — TERAMIND (TOP PRIORITY, browser): dashboard is https://ascendprimew.us.teramind.co (confirmed from the daily digest emails). (a) Settings → API → generate token, save to a LOCAL file outside the repo, report path only. (b) While in there: check AGENT COVERAGE — the Aug 29 daily digest shows only ONE agent reporting ("nguye@a51" = Alan's own machine); verify Carla/Lynn/Anne/Grace/ML agents are installed AND reporting, list who is/isn't. (c) Turn on the richer daily digest/alerts if available. NOTE: Carla's Teramind password was posted in PLAINTEXT in Slack DM 8/27 — rotate it while there.
>
> TASK 8 — WHOP (payments source of truth, Alan-confirmed): log into Whop dashboard, (a) export all payments/orders history to CSV → ops/archive/whop/ (raw + dated, per RAW-ORIGINALS law), (b) generate a Whop API key (dashboard → developer settings), save LOCALLY outside repo, report path. This unlocks verified collected-cash on the revenue ledger (Nick $500, Jill installments, all future).

## B. Manual steps while you're there (SUPERSEDED for items 1 & 3 by Tasks 5–6 above — remaining truly-manual: 2, 4, 5)

1. **Lock the 3 public Loom videos** containing client SSNs/passwords — checklist row `3b95bb1ffef4813e9ac2d16384dfe7e9`. Two minutes; highest-severity open risk.
2. **Meta Ads Manager → URL parameters** on the two ACTIVE campaigns (Medical Relaunch v2, Prof/BizOwners relaunch): `utm_source=meta&utm_medium=paid&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&campaign_id={{campaign.id}}&adset_id={{adset.id}}&ad_id={{ad.id}}` (campaign-level; existing ads' url_tags are immutable — set it where Ads Manager allows, and on ALL new ads incl. the Sep 1 A/B).
3. **Teramind** (register item #49): grab an API token (Teramind admin → API) OR schedule a daily CSV export to the APW Data Hub Drive folder. Either one turns the contractor reports from hearsay into tool data.
4. **Invite Jacob to Meta Ads Manager** (blocks the Sep 1 10:00 AM PT A/B launch).
5. **Notion pending join request** — approve/deny ("1 user waiting to join Ascend Prime Wealth", likely ML).

## A4. TASK 9 (added 8/30 night — Alan ruled "Option A now", ping → #call-outcomes)

> TASK 9 — CALL-OUTCOME PING AUTOMATION (GHL UI build, ~45 min, Alan present for Step 0): follow `ops/data/CALL_OUTCOME_BUILD_SOP.md` verbatim — Slack incoming webhook for #call-outcomes (C0BTJL3BPPX), 5 trigger links, 5 outcome workflows (tag+note+status), the appointment-end ping workflow, then the dummy-appointment test in Step 4. This supersedes manual status-setting discipline (#64) with a machine that asks the closer after every call. NOTE: workflow creation is an approved GHL write for THIS build only; still no other writes.

## A5. TONIGHT'S 30-MIN RUN (8/31, Alan at PC — ordered by risk & Monday-launch impact)

> BOOTSTRAP FIRST (SOP §1.12): this chat must be opened INSIDE the repo folder → `git pull` → read CLAUDE.md → confirm SOP v1.9 → follow ops/RESPONSE_TEMPLATE.md for every reply to Alan.
>
> RUN ORDER (Alan 8/31: 'loom lock... then do teramind and then next'):
> 1. 🔒 TASK 5 — LOOM LOCK (2 min, highest security risk): fetch Notion row `3b95bb1ffef4813e9ac2d16384dfe7e9` for the 3 public Loom URLs w/ client SSNs → browser → set EACH to **APW workspace-ONLY** (Alan 8/31: "loom lock to only APW" — not just link-private) → report final visibility verbatim.
> 2. ❌ REMOVED (Alan 8/31: "jacob like i said does not need ads manager invite to this failing campaign, he has access to a different one") — Jacob runs the DM campaign on HIS OWN ad account; no invite to 1821085838595242. Launch is NOT gated on this.
> 3. 💳 NOTION BUSINESS TAP (1 min): open https://app.notion.com/checkout?source=mcp_tool_upsell&tool=query_data_sources&product=business&spaceId=45a5bb1f-fef4-8161-b4a1-00030e9d49c8 — Alan completes payment (human-only). Makes the board's live layer permanent.
> 4. ✅ NOTION JOIN REQUEST (1 min): approve the pending "1 user waiting to join" (likely ML = Ma. Liza Tizon, identity confirmed via malizgill31@gmail.com).
> 5. 🔑 TASK 7 — TERAMIND (10 min): https://ascendprimew.us.teramind.co → Settings→API→generate token → save LOCAL file OUTSIDE repo, report path only. Check agent coverage (digest shows only "nguye@a51" — verify/plan Carla/Lynn/Anne/Grace/ML agents). ROTATE Carla's password (was plaintext in Slack 8/27).
> 6. 💰 TASK 8 — WHOP (10 min): dashboard → export ALL payments/orders CSV → ops/archive/whop/ (raw + dated). Generate API key → LOCAL file outside repo, path only. Then check: Ashwini $1,500 (7/28), Pradeep $300 (8/11), Nick $500 (8/26) — report found/not-found each; Lane 1 flips three qualification/stage labels on your evidence.
> 7. 📞 TASK 9 — CALL-OUTCOME BUILD (45 min, can split to tomorrow if late): follow ops/data/CALL_OUTCOME_BUILD_SOP.md verbatim (Slack webhook → 5 trigger links → 5 workflows → ping workflow → dummy test).
> After each item: commit+push your process-log. Lane 1 integrates on its next cycle.
