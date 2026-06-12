# QA Audit — iBankNet_CA_Deposits_v2.xlsx (+ 2 CSVs)

**Auditor:** QA-IBNET-2 (adversarial verifier; did not build the deliverable)
**Date:** 2026-06-12
**Deliverables audited:**
- `/home/user/awake/research/ibanknet/deliverables/iBankNet_CA_Deposits_v2.xlsx` (9 tabs)
- `/home/user/awake/research/ibanknet/deliverables/iBankNet_CA_Deposits_v2.csv`
- `/home/user/awake/research/ibanknet/deliverables/iBankNet_NoDoc_DP_Log_v2.csv`

**Verdict: PASS-WITH-ISSUES — 0 CRITICAL / 3 MAJOR / 9 MINOR**

The build is mechanically excellent: add-only discipline is perfect, merge integrity is exact,
data fidelity to source CSVs is verbatim, and Tab 0's coverage statement matches independent
recounts on every number. The MAJORs are all evidence-hygiene gaps against the user's explicit
acceptance criteria (d)/(e): 10 none-found rows with no source trail of any kind, one duplicated
no-doc DP presented as two, and one superseded "LIKELY-NO Chex" reading still standing
uncorrected on Tab 3.

---

## Check 1 — SOURCE-COVERAGE AUDIT (criterion e): PASS-WITH-ISSUES

Method: per tab, counted claim-bearing rows vs rows carrying ≥1 hyperlink object or in-cell URL
or explicit textual citation; none-found rows checked for a listed search trail.

| Tab | Claim-bearing rows | Sourced | Coverage | Gaps |
|---|---|---|---|---|
| 0. GUIDE & LEGEND | ~14 claim sections (of 24 populated rows) | 13 textual citations, 0 hyperlinks | ~93% | Row 16 (QualiFile/LN auto-decline warning, "e.g., Banner") names no source in-cell (traceable only via Tab 1 Banner row). Tab 0 still has zero clickable hyperlinks (carried from v1). |
| 1. CA INSTITUTIONS | 451/451 | 451 (Sources col populated 451/451; ≥1 URL/hyperlink on every row) | 100% | 27 of 284 DD-appended segments lack in-cell grade/source (see Check 2 / MINOR-2) |
| 2. LIVE-CHECK CORRECTIONS | 15/15 | 15 | 100% | none (links still text-only, v1 MINOR carries) |
| 3. SECONDARY BUREAUS | 230/230 | 89 rows linked; the 141 no-link rows are all UNKNOWN rows whose Notes state provenance/null-search ("v6 ews_chex_mapping… not individually web-searched (low priority)") | 100% accounted | Rize row 182 stale — see MAJOR-3 |
| 4. BEST OF LIST | 101/101 | 101 | 100% | none |
| 5. BUREAU DEEP DIVE | 101/101 | 101 rows with ≥1 hyperlink; all 45 UNKNOWN rows list searches run | **100%** | none |
| 6. CHEX-EWS DEEP DIVE | 101/101 | 101 rows with ≥1 hyperlink | **100%** | ~6 positive findings use ad-hoc labels outside the declared grade vocabulary (MINOR) |
| 7. NO-DOC DP LOG | 102 claim-bearing (positive DP) + 47 none-found | 102/102 claim rows linked; 123/149 total linked; of 47 none-found, 21 linked + 19 list searches, **10 have neither** | claim rows 100%; none-found block 79% | **MAJOR-1**: rows 116, 125, 127, 131, 134, 135, 138, 142, 148, 150 |
| 8. PG-CLI-CFPB & FLAGS | 101 table + 14 flags | 101/101 table rows linked; 14/14 flags linked; flags-header row cites extras_report.md textually (the "1 of 116") | 115/115 actual; matches Tab 0's "115/116" | 18 populated "CLI: not published." cells are unsourced absence-claims (MINOR-8) |

**Tab 0 B27 coverage statement vs independent recount: ACCURATE on every number.**
Tab 5 101/101 ✓; Tab 6 101/101 ✓; Tab 7 123/149 (82.6%) ✓ and all 26 unlinked rows are indeed
none-found rows ✓; Tab 8 115/116 reconciles exactly (116 = 101 table + 14 flags + flags-header
row; only the header row lacks a link — it cites extras_report.md). Tab 0 B24's append counts
(101+101+70+12 = 284 cells in cols P-S, +14 Live-check-note cells in col V) also verified exact.

However, criterion (e)'s rule that **none-found rows must list the searches run is unmet on 10
Tab 7 rows** (MAJOR-1) and only partially met on 18 more (MINOR-1).

## Check 2 — AMBIGUITY AUDIT (criterion d): PASS-WITH-ISSUES

- **Structural:** Tab 5 Evidence_grade populated with declared-vocabulary grades on 101/101 rows
  (0 missing). Tab 7 grades on the 102 claim rows: VERIFIED-own-page / COMMUNITY-DP /
  UNVERIFIED-RUMOR only — all declared. Tab 1 DD-appended quick cells carry bracketed tags
  ([RAIL-INFERENCE], [UNKNOWN], [none-found], [COMMUNITY-DP]…) on 257/284 segments.
- **25-cell random sample (seed 7) across Tabs 1/5/6/7:** 21/25 carried an unambiguous grade
  tag. The 4 exceptions: 2 Tab 6 null statements ("No new EWS data [2026-06-12]" — null, not a
  claim) and 2 Tab 7 none-found rows graded "-" (see MINOR-1).
- **Bare un-graded claims found (full scan, not just sample):** 27 Tab 1 DD-appended segments
  (mostly one-line "Leniency: …" determinations, e.g. r18 Western Alliance "Leniency: No
  second-chance product", r70 Provident "VERY Chex-inquiry-sensitive — open FIRST or skip")
  carry neither a grade tag nor an in-cell source; they are sourced only transitively via the
  same institution's Tab 6 row. 6 Tab 6 finding cells use ad-hoc labels (Yes-strong-inference,
  Yes-lenient, SECOND-SOURCED, [SECONDARY (SmartAsset)], WEAK secondary, VERIFIED-absence) not
  declared in Tab 0 B25. → MINOR-2.
- **The four named notes:**
  - **Rize downgrade** — PRESENT & unambiguous on Tab 6 r79 ("REVISED to USES-BUT-LENIENT-leaning…
    prior 'LIKELY-NO Chex' should be downgraded") and Tab 1 r140 col R (DD append carries the full
    REVISED text). **BUT Tab 3 r182 still affirmatively recommends the superseded reading**
    ("🥈 LIKELY-NO — second-chance CU… NEW TARGET worth a call") with no pointer to the revision
    → old wrong reading IS recoverable as current truth from Tab 3 → **MAJOR-3**.
  - **Bay Federal strict** — UNAMBIGUOUS. Tab 6 r65: consumer + business-specific VERIFIED own-site
    footnotes, "STRICT — any Chex record disqualifies"; mirrored into Tab 1 r107 col R with
    [VERIFIED own-site; 2026-06-12]. Live fetch confirmed footnote 5 verbatim on bayfed.com.
  - **Bank of Stockton dual-program** — UNAMBIGUOUS and triple-stated: Tab 8 r36 TENSION (medium)
    note, Tab 8 FLAG 12, Tab 1 r60 col V DD append; all say "likely dual program: in-house
    consumer + Elan business — verify before relying on the Elan call."
  - **Hanmi in-flight** — UNAMBIGUOUS and quadruple-stated: Tab 1 r37 col V PROGRAM-CHANGE SIGNAL,
    Tab 5 r25 Notes caution, Tab 8 r25, and FLAG 4 (full Elan-verbatim-today / Fifth-Third-
    indexed-version / Brex-partnership chain with both URLs). Old "Elan, settled" reading is not
    recoverable as unqualified current truth.

## Check 3 — ADD-ONLY vs v1: PASS (clean)

- Cell-by-cell diff v1→v2, Tabs 0-4: **every changed cell is either identical or appends after
  "‖ DD 2026-06-12:"** — 0 violations. Tab 1: 9,817 identical + 298 appended; Tab 4: 1,124 + 202;
  Tabs 2/3: byte-identical. Tab 0 gains rows 23–27 only (pure bottom-append, rows 1–21 untouched).
- **v1 hyperlinks: 100% intact at same anchors** (Tab 1 = 826, Tab 3 = 154, Tab 4 = 101 checked;
  0 missing, 0 retargeted).

## Check 4 — DATA FIDELITY: PASS (13 rows traced; 7/8 links alive, 1 bot-blocked)

Traced verbatim from workbook cells to `out/nodoc_dps_{1,2}.csv`, `out/deep_bureau_results_{1,2,3}.csv`,
`out/deep_chex_results_{1,2}.csv`: Sierra QuickBiz (T7 r5), PNC $75K BLOC (T7 r43), Chase Ink $50K
(T7 r47), WF $50K BLOC (T7 r49), Altura (T7 r11), Patelco (T7 r9), Redwood full-doc anti-DP (T7
r19), Elan combined-pull note (T5 r42/48/66/87/93/96/99 + Tab 0 B26, myFICO 6308920), OCCU
verified-disclosure (T5 r52), SAFE no-reuse (T5 r34: "new TU pull per card / no pull-reuse",
myFICO 6150354), plus Mission Bank (T7 r31), First-Citizens BLOC (T7 r88), and 4 Tab 6 rows
(Bay Federal, Rize, Stockton, Patelco). **Zero substantive diffs; the only deltas are the
documented ⭐ prefix on 5 gold-row Product cells.**

Links clicked (8):

| # | Link | Result |
|---|---|---|
| 1 | bankofthesierra.com/QuickBiz/ | **ALIVE** — "No additional financial information required, and minimal documentation requirements", $5K–$30K deposit-tiered, FICO 700, 3 yrs: all verbatim |
| 2 | alturacu.com/business-credit-card/ | **ALIVE** — $25K OAC, no LLC required, freelancers/Amazon-eBay sellers, $0 AF, no BT fee: all verbatim |
| 3 | patelco.org …how-do-business-credit-cards-work | **ALIVE** — EIN-not-required + automated-instant language verbatim; **$40K max line NOT on this page** (MINOR-4) |
| 4 | redwoodcu.org Business Visa Platinum | **ALIVE** — "current business income statement and business federal tax returns" verbatim = anti-DP confirmed |
| 5 | bayfed.com/business/checking | **ALIVE** — footnote 5 ChexSystems-clear requirement verbatim |
| 6 | rizecu.com Fresh Start Checking | **ALIVE** — second-chance product confirmed, but the quoted "…or are on ChexSystems…" sentence not on live page (MINOR-3) |
| 7 | myFICO thread 6705063 (WF $50K BLOC) | **BOT-BLOCKED (403)** — workbook itself flags myFICO 403s/snippet grading; counts alive-unverifiable, not dead |
| 8 | doctorofcredit.com u-s-bank-no-longer-hard-pull-CLI | **ALIVE** — but article is dated 2017-06-08 with an update re-adding "sometimes" hard pulls (MINOR-5) |

**Dead links: 0.**

## Check 5 — MERGE INTEGRITY: PASS

- Tab 5 = 101 data rows, 101 unique institutions, **exact set-match to Tab 4 Best-Of (101)**: 0 missing, 0 extra.
- Tab 6 = same: exact 101/101 set-match.
- Tab 7 = **149 rows**; sort order verified against banner spec: VERIFIED-own-page block (38) →
  community approval DPs strictly amount-DESC (51, 0 violations) → published-requirements (13) →
  none-found block (47, all DP_type=none-found). **Exactly 7 gold-star rows** (r5 Sierra, r7
  Stanford FCU, r9 Patelco, r11 Altura, r13 UMB, r43 PNC, r46 WF), star char and gold fill agree 7/7.
- Tab 8 = **101 institution rows + 14 material flags** (rows 106–119); CFPB statuses sum 43 PRESENT
  + 58 ABSENT = 101, matching the Tab 8 banner verbatim.
- **CSVs:** NoDoc CSV = banner + header + 149 rows, **0 diffs** vs Tab 7. v2 Deposits CSV = header
  + 452 rows mapping 1:1 onto xlsx rows 2–453 **including the FBO separator** (v1's omission fixed);
  all 352 cell-level deltas are exactly the documented "(URL)" hyperlink-preservation pattern
  (0 anomalies). **Rank-451 row (SUMITOMO MITSUI BKG CORP SF BR) present in both xlsx and CSV** —
  restored as specced.

---

## Findings

### CRITICAL
None.

### MAJOR
1. **[Tab 7 / criterion e] 10 none-found rows carry no source trail at all** — no hyperlink, no
   URL, and no searches-run listing: r116 Five Star Bank, r125 West Coast Community, r127
   Avidbank, r131 Bay Federal, r134 Monterra, r135 Ventura County, r138 Rize, r142 America's
   Christian, r148 Sunflower, r150 California Community (Notes are bare "Zero community DPs"
   variants). Two of these even embed positive claims on the unsourced row (r131 "Published max
   $50K limit", r145-adjacent r145 Excite "Published $30K max" — r145 likewise linkless). The
   user's rule was explicit: none-found rows must list the searches run.
2. **[Tab 7] Duplicate data point presented as two rows** — r46 ("Wells Fargo Bank, National
   Association", ⭐ gold, "$50,000 BLOC", DP_date "2024") and r49 ("OFF-LIST: Wells Fargo Bank,
   N.A.", "$50,000", DP_date "2023") both cite the **same myFICO thread 6705063**. One DP, two
   rows, contradictory dates and contradictory on-list/OFF-LIST status (WF is roster rank 2, so
   the OFF-LIST label is wrong on its face). Violates the banner's "one data point per row";
   the true unique-DP count is 148, not 149. Dupe originates in the source CSVs
   (nodoc_dps_1 vs nodoc_dps_2) — the assembler mirrored faithfully but did not dedupe.
3. **[Tab 3 / criterion d] Rize old reading survives as current truth** — Tab 3 r182 still reads
   "🥈 LIKELY-NO — second-chance CU, no Chex language on own pages; NEW TARGET worth a call"
   with no DD append or pointer to the Tab 6 r79 downgrade ("REVISED to USES-BUT-LENIENT-leaning…
   prior LIKELY-NO should be downgraded"). A Tab 3 reader recovers the superseded recommendation
   intact. (Tabs 1 and 6 carry the downgrade correctly and unambiguously.)

### MINOR
1. **[Tab 7] Grade-column inconsistency on the none-found block** — 27 rows graded "-" (not in
   the declared vocabulary VERIFIED-own-page/COMMUNITY-DP/UNVERIFIED-RUMOR/none-found) vs 17
   graded "none-found"; r110 SDCCU is DP_type=none-found yet graded COMMUNITY-DP (the DP is about
   limits/EX pull, not no-doc); r107/r126 are none-found graded UNVERIFIED-RUMOR. DP_type column
   keeps determinations readable, but the grade column contradicts the declared scheme.
2. **[Tabs 1/6] 27 Tab 1 DD-appended "Leniency:"-style determinations carry no in-cell grade tag
   or source** (sourced only via the same institution's Tab 6 row), and 6 Tab 6 positive findings
   use ad-hoc labels (Yes-strong-inference, SECOND-SOURCED, WEAK secondary, VERIFIED-absence,
   [SECONDARY (SmartAsset)]) not declared in Tab 0 B25's vocabulary.
3. **[Rize quote]** Tab 6 r79's VERIFIED-own-site quote ("if you've ruined your credit or are on
   ChexSystems, it's not too late…") is not reproducible on the live Fresh Start page (page now
   carries generic second-chance language without naming ChexSystems). Downgrade rationale still
   holds; the verbatim quote does not.
4. **[Patelco]** Tab 7 r9's "$40,000 published max line" is not on the cited patelco.org page
   (the page verifies the EIN/instant-decision language only).
5. **[FLAG 14]** "U.S. Bank CLI policy softened" is sourced to a 2017-06-08 DoC article that
   itself was later updated to "sometimes" hard-pulls; the flag's [2026-06-12] reads as fresher
   than the evidence. (The Tab 8 U.S. Bank table cell does carry the nuance.)
6. **[Tab 7 banner]** Gold legend says "GOLD rows = top verified no-doc paths" but 2 of 7 gold
   rows (PNC r43, WF r46) are COMMUNITY-DP grade, not VERIFIED-own-page.
7. **[Tab 0]** Still zero clickable hyperlinks (v1 carry-over); row 16's QualiFile/LexisNexis
   auto-decline warning names no source in-cell.
8. **[Tab 8]** 18 populated "CLI: not published." cells are absence-claims with no in-cell search
   trail (row-level CFPB link does not cover the CLI claim).
9. **[myFICO links]** All ficoforums.myfico.com citations are bot-blocked (403) and snippet-graded
   per the workbook's own caveat — amounts/profiles on those rows are unverifiable by fetch,
   only by snippet. Disclosure exists (Tab 0 B26, Tab 5/7 banners), so this is accepted-risk,
   logged for completeness.

### Dead links
None (0/8 dead; 1 bot-blocked 403: myFICO thread 6705063 — workbook self-flags myFICO 403s).
