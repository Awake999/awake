# SoCal Equifax-Bank Search — Master Checklist & Ledger

Single source of truth. Lawful scope only: public-record research on which SoCal banks
issue business credit cards, which underwriter/bureau they use, deposit & no-doc posture,
and how to apply. Goal: surface institutions that **pull Equifax** (Card Assets is one
known example). Updated 2026-07-20.

## MISSION (what we're doing)
Build a deduped, deposit-ranked list of **Southern California (LA + Orange County, adjacent
IE/SD where relevant)** banks & credit unions that offer business credit cards, with the
**bureau they hard-pull identified**, prioritizing **Equifax** pullers. For each: name,
product, deposits, underwriter, bureau, no-doc posture, apply-online + link. Apply honestly
as the real business. (Non-goal / explicitly excluded: any application-tactics or
fund-framing coaching — a prior Claude session generated that; it is not part of this work.)

## DATA WE HAVE (ledger of sources)
- [x] **iBankNet_CA_Deposits_v2** — MASTER. 452 CA institutions ranked by deposits; cols for
      underwriter, bureau, no-doc, apply, secondary bureaus (Chex/EWS/LN). 9 sheets incl.
      "4. BEST OF LIST" (101), "7. NO-DOC DP LOG" (149), bureau/Chex deep dives.
- [x] **CA_Banklist_Sprint_CD_c3_v1** — Sprint list + "Full Master (164)" + **NO-GO list** +
      Mentor Intel reconciliation.
- [x] **CA_Banklist_CW_v4** — Ranked all-institutions + Self-Underwritten top targets +
      "SoCal Gold + CA-Accessible" (rich schema: est. limit, bureau, apply method, confidence).
- [x] **Code_c2_v3_CA_Banklist** — "Funding Table" (self-UW flag, no-doc /5, HP bureau, limits).
- [x] **Slack_chat_history** — mentor/community datapoints + confirmations (e.g. First Foundation
      = Card Assets = Equifax; Hanmi/Poppy/First Entertainment = Elan no-go). NOTE: the
      "tactics/what-to-say" passages here were AI-generated in a prior session and are OUT OF SCOPE.
- [x] **My live sweep (this session)** — 50 LA/OC institutions fingerprinted for Card Assets.

## DONE SO FAR (ledger of work)
- [x] Live-checked 50 LA/OC institutions for the Card Assets tell
- [x] CONFIRMED **First Foundation Bank** (Irvine, $8.78B) = Card Assets = Equifax; live app
      `app.thecardservicescenter.com/SelectionBusiness/index/0350` (⚠️ Sunflower merger 4/1/26 may migrate it)
- [x] LIKELY **Partners Bank of California** (Mission Viejo); call-to-confirm: Genesis, Beach Cities
- [x] Mapped the 50 to real issuers (Elan/Synchrony/TCM/self/none)
- [x] Ingested all 4 workbooks; quantified the gap (below)
- [x] Deliverable `socal-card-assets-banks.md` committed; PR #1 open
- [ ] Merge workbooks + sweep into one deduped SoCal Equifax target list  ← NEXT

## GAPS FOUND — and how I found what prior Claude missed
- **Underwriter unknown for ~281/452 (68%).** Found by tallying the Underwriter column.
- **Bureau essentially unpopulated for Equifax: only 7/452 mention EQ, 1 clean tag; Card Assets
  not tagged at all.** Found by scanning the Bureau column. → The roster ranks deposits well
  but does NOT yet answer "who pulls Equifax," which is the whole mission.
- **Card Assets lane entirely absent from the workbook.** Found by live-fingerprinting the
  platform (thecardservicescenter.com / 24-7cardaccess.com / cardaccount.net) — prior sessions
  never mapped it, so First Foundation's EQ lane was invisible in the sheets.
- **Coverage-source gaps:** FDIC BankFind, Bank Branch Locator, ICBA directory never queried;
  deposits are the 2026-06 sweep (stale-ish).

## HOW TO FIND MORE EQUIFAX INSTITUTIONS (methodology)
1. **Enumerate Card Assets fully = guaranteed EQ.** Every Card Assets client pulls Equifax.
   Walk `app.thecardservicescenter.com/SelectionBusiness/index/####`, capture which FI each
   resolves to, keep SoCal hits. Highest-yield EQ-specific method. (Seen live: 0350=First
   Foundation; other numbers 0260/0480/2080/5430 exist — map them.)
2. **Map underwriter→bureau at the PLATFORM level, then apply to all their banks:**
   - Card Assets → **Equifax** (target)
   - Elan → TU-leaning (also your no-go) | TCM → varies | FNBO → Experian | TIB → verify
   - CorServ/Apex, ServisFirst, Fiserv/CC Department, Synchrony → verify each platform's bureau
   This converts the 281 "unknown underwriter" + platform rows into bureau signal efficiently,
   instead of guessing bank-by-bank.
3. **Self-underwritten banks (70 SELF + more):** bureau is per-bank; grade by evidence
   (VERIFIED own-page > COMMUNITY-DP > RAIL-INFERENCE). Prioritize SoCal self-UW with EQ DPs.
4. **Complete the universe:** FDIC BankFind (all LA/OC HQ + branched) + Branch Locator +
   ICBA → diff vs the 452 → fill new rows, refresh deposits.

## PLAN FORWARD (phased)
- **Phase A — Consolidate (low effort):** merge 4 workbooks + sweep → one deduped SoCal table;
  attach the confirmed Card Assets/EQ lane; drop no-go rails. Deliverable: ranked SoCal list.
- **Phase B — Card Assets enumeration (medium, highest EQ yield):** map `index/####` → FIs →
  SoCal EQ hits.
- **Phase C — Platform→bureau fill (medium):** assign bureau to every platform-underwritten row;
  flag all EQ pullers.
- **Phase D — Universe completion (low):** FDIC/Branch Locator/ICBA diff; verify new SoCal banks.
- **Phase E — Publish:** update `socal-card-assets-banks.md` + a new `socal-equifax-targets.md`;
  push to PR #1.

## PROCESS-IMPROVEMENT INSIGHTS
- Treat **bureau** as the deliverable's weakest link — resolve it via platform mapping first
  (cheap, high coverage) before per-bank DP hunting (expensive, lower grade).
- Keep the workbook's **evidence-grade** convention (VERIFIED / COMMUNITY-DP / RAIL-INFERENCE).
- Card Assets = the gold EQ lane → enumerate it exhaustively rather than sampling.
- Re-verify First Foundation before relying on it (merger migration risk).
- Maintain this ledger every session so nothing is re-derived or lost.

## OPEN DECISIONS FOR YOU
- [ ] Start with **Phase A** (consolidate what we have into one clean list) or **Phase B**
      (Card Assets enumeration — most new EQ targets fastest)?
- [ ] Effort: Fable 5 **medium** for the runs is plenty (mapping/fetching); I'll flag if a step needs high.
- [ ] Scope: LA+OC only, or include Inland Empire / San Diego where CA-accessible?
