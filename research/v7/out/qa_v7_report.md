# QA-VERIFIER-2 ADVERSARIAL AUDIT — ca_business_credit_funding_v7.xlsx
Auditor: QA-VERIFIER-2 (independent; did not build the workbook)
Date: 2026-06-11
Artifacts audited:
- /home/user/awake/research/v7/deliverables/ca_business_credit_funding_v7.xlsx
- /home/user/awake/research/v7/deliverables/ca_business_credit_funding_v7_best_targets.csv
- /home/user/awake/research/v7/deliverables/ca_business_credit_funding_v7_funding_table.csv
Baselines: /home/user/awake/research/v6/deliverables/ca_business_credit_funding_v6.xlsx; /home/user/awake/research/v7/out/* (bureau_pulls.csv, 5 bureau findings MDs, assets_fill.csv, geo_*.csv, w2_geo_screen.csv)

## VERDICT: PASS-WITH-ISSUES
- CRITICAL: 0
- MAJOR: 1
- MINOR: 6

---

## 1. SIMPLICITY — Tab '1. BEST TARGETS' — PASS
- Columns: 14 (limit ≤15). Headers: Rank | Institution | Why it's here | Nearest location + miles | Bureau pulled (+grade) | ChexSystems | EWS | Biz card confirmed? | Stated/Est. limit | No-doc? | Self-UW / issuer | Apply | Assets | Next action.
- Cell length: ZERO cells >120 chars (longest = 82 chars, col I row 4).
- One row per institution: 32 rows, 32 unique institutions, ranks 1–32 strictly sequential.
- Frozen header: freeze_panes=A2. Autofilter: A1:N33 (covers all rows).
- Color key: Tab 1 uses exactly the 3 fills declared on '0. README' — green 00C6EFCE (confirmed favorable), amber 00FFE699 (unknown/verify), red 00FFC7CE (blocker). Hyperlinks are blue (0563C1) + single-underline, matching the README "blue underline = clickable" rule.
- **30-SECOND SCANNABILITY VERDICT: YES.** A non-analyst opening Tab 1 gets location+miles, bureau (+evidence grade), Chex, EWS, card-confirmed, limit, and no-doc as seven dedicated, short, color-coded columns on one ranked screen. Blockers (Southland/LAFCU/Banner Chex, CU SoCal no-biz-card) are red-flagged inline, not hidden.

## 2. NUMBERED TABS — PASS
17 tabs, every name starts with its number, in exact order 0–16:
0. README / 1. BEST TARGETS / 2. MENTOR BUREAU LIST / 3. FUNDING TABLE MASTER / 4. DIAMOND-PLATINUM / 5. GEO - LONG BEACH / 6. GEO - FONTANA / 7. ICBA COMMUNITY BANKS / 8. BUREAU EVIDENCE / 9. EWS-CHEX MAP / 10. FDIC SOD 6CTY / 11. NCUA 6CTY / 12. IBANKNET CA / 13. CHANGE LOG / 14. LEGEND (v5) / 15. CENSUS 4CTY FDIC (v5) / 16. CENSUS 4CTY NCUA (v5).

## 3. CLICKABLE LINKS — PASS-WITH-ISSUES
Real openpyxl hyperlink objects counted (not text URLs):
- Tab 1: every one of the 32 rows has 6–7 hyperlinks (requirement ≥5/row). PASS.
- Tab 2: 13 of 14 institutions have ≥1 hyperlink. **LAFCU row 15 has 0** — cell honestly reads "(none found)" and verdict is NO-DATA, but the literal ≥1/institution bar is missed (see MAJOR-1).
- Tab 8: 27 hyperlinks across 35 rows; the 8 link-less rows (LAFCU, Premier America, Comerica, East West, Valley Strong, Wescom, BCU, Skyla) exactly match the "(none found)"/"(inference - verify)" source cells in bureau_pulls.csv — consistent, no fabricated links.
- Other tabs: Tab 5 = 23, Tab 6 = 15, Tab 7 = 36 hyperlinks; 9 internal cross-ref anchors to Tab 8. Tabs 3 and 4 carry URLs as plain text only (v6 legacy format) — see MINOR-4.

### Spot-click results (15 URLs, WebFetch):
ALIVE (12): arrowheadcu.org/arrowhead-visa; mercury.com/credit; doctorofcredit.com EWS list; directory.icba.org/19522/Sunwest-Bank; enterprisebank.com/business/credit-cards; kinecta.org dispute PDF (real 62KB PDF, binary); calbanktrust.com business credit cards; usbank.com business credit cards; rizecu.com/business-visa ("Variable credit limits from $5,000 to $50,000" — confirms workbook claim); wallethub.com PNC-bureau answer (confirms EX-mainly); tustin.bank (confirms NO card product — validates the CONFLICTS verdict); fairfigure.com TU article (confirms BMO TU).
ALIVE-BUT-BLOCKED, 403 bot-block (3): sfcu.org/personal/credit-cards/ (workbook itself notes "site 403s"); ficoforums.myfico.com First Citizens thread 6704468 (findings MD notes "myFICO 403s"); southlandcu.org business checking.
**DEAD LINKS (404/NXDOMAIN): 0.**

## 4. MENTOR LIST — PASS
Tab 2 contains all 14 institutions in the mentor's grouping/order:
- EXPERIAN: PNC, Sunwest, Tustin Community
- EQUIFAX: First Citizens, KeyBank, California CU, First Western Trust
- TRANSUNION: Banner, Valley (Valley National), BMO, Western Alliance, WaFd, LAFCU
- BRANCH VERIFY: California Bank & Trust
Each row has mentor claim, verdict, 1-line evidence, evidence link (except LAFCU — none exists), caveat/next step. All 14 verdicts, evidence summaries, grades, and links match bureau_pulls.csv verbatim (field-by-field comparison). No factual contradictions with the bureau_*_findings.md files; the findings MDs use a slightly different verdict vocabulary in places (e.g. KeyBank "PARTIAL" in MD vs "AGREES [CONSUMER-PROXY]" in CSV/tab; Sunwest "NO-DATA" in MD vs "CONFLICTS (stale)") — the underlying evidence statements are identical, only the labels were re-bucketed at integration (see MINOR-2/MINOR-3).

## 5. ASSETS/DEPOSITS COMPLETE — PASS
- Tab 3 rows 2–237 (the 236 v6 master rows): **0 blank / '—' / 'N/M' cells** in both Assets (col 12) and Deposits (col 13). assets_fill.csv contains exactly 174 funding_table fill rows, matching the Change Log claim.
- Tab 12 (451 rows): 0 blank Assets, 0 blank Deposits; exactly **29 'N/A' Deposits cells**, all on the FBO/FFIEC-002 office rows (rows 424–452: Woori LA BR … Sumitomo SF BR) with the documented "ibanknet fast-facts shows assets only — detailed RAL report behind captcha" note. Matches the documented 29 FBO N/A allowance precisely. 87 Tab-12 rows carry v7 appends = assets_fill.csv's 87 ibanknet rows.
- Note: the 7 NEW v7 rows (Tab 3 rows 238–244) have Deposits='N/M' (see MINOR-5).

## 6. ADD-ONLY — PASS (independently recomputed)
- Tab 3 rows 1–237 × 36 cols vs v6 'Funding Table': 8,097 cells identical, 225 appended-with-original-prefix-intact, 210 filled-from-blank/'—'/'N/M', **0 violations** (no v6 value altered or destroyed).
- Tab 4 vs v6 Diamond-Platinum: 0 violations (4 appends; Rize P5 added into previously blank row 30).
- Tab 12 vs v6 ibanknet: 174 appended cells, 0 violations.
- Carried tabs cell-identical to v6: 9. EWS-CHEX MAP (214×12, 0 diffs), 10. FDIC SOD 6CTY (123×18, 0), 11. NCUA 6CTY (162×18, 0), 14. LEGEND (58×1, 0), 15. CENSUS 4CTY FDIC (114×9, 0), 16. CENSUS 4CTY NCUA (141×8, 0). (v5 originals not on disk; v6 copies are the carried source and match byte-for-value.)
- Tab 13 rows 1–172 identical to v6 'v6 Change Log'; v7 entries appended at rows 174–202.

## 7. PROVENANCE SPOT-CHECKS (10/10 PASS)
1. **BMO bureau=TU AGREES** — Tab 1 r7 "TU — mentor AGREES"; Tab 3 r10 col 23 v7 append "verdict [COMMUNITY-DP] vs mentor 'TransUnion' = AGREES"; live fairfigure.com fetch confirms TU. PASS.
2. **PNC product nuance not flattened** — Tab 1 r11 "EX hard (std card); BusinessOptions/LOC = SOFT EQ"; Tab 3 r6 col 23 preserves "Hard-pull cards: Experian. BusinessOptions: SOFT pull, Equifax (NO hard inquiry!)" with v7 append. Not collapsed to 'EX'. PASS.
3. **Tustin no-card-product** — Tab 2 r5 "CONFLICTS (no product) … NO credit card product offered"; live tustin.bank fetch confirms no card product today. PASS.
4. **FNBO bureau=EX biz-specific** — Tab 1 r5 "EX — BUSINESS-specific DP (prequal language)"; Tab 4 D1 "bureau RESOLVED = EXPERIAN, business-specific DP". PASS.
5. **Rize claims trace to w2_geo_screen** — "$5,000–$50,000 published", ACC join, Ontario 7.88 mi, likely-self-issued all present verbatim in w2_geo_screen.csv; rizecu.com live fetch confirms the $5K–$50K range. PASS.
6. **Banner Chex blocker carried to Tab 1** — r31 has red fill, "Chex BLOCKER" in cols C and F ("Yes — SENSITIVE (BLOCKER; BankOn acct = fallback)"), Next action = "Clean Chex first; ask bureau post-app". NOT presented as clean. PASS.
7. **Wescom/SchoolsFirst no-biz-card corrections** — Tab 3 r147 and r139 col 17 carry the v7 "CORRECTION: NO business credit card/card product" appends, sourced to bureau_cus_findings.md. PASS.
8. **Pacific Premier→Columbia flag** — Tab 3 r138 Bank cell "⚠ MERGER" + col 35 full merger text (Columbia Banking System, Sept 2025, treat PPBI defunct). Comerica→Fifth Third (r49) and First Foundation→Sunflower (r129) flags also verified. PASS.
9. **Tab 1 distances match geo CSVs** — all checked values exact: LB: BoC 0.0, CNB 0.09, CB&T/Zions 0.12, Chase 0.44, F&M 0.47, ICB 0.56, Comerica 0.58, BMO 0.68, USB 0.80, Southland 1.14, BofA 2.11, First Citizens 2.82, Arrowhead 4.75; Fontana: Chase 1.18, Arrowhead 1.22, USB 1.40, BofA 1.50, 5/3(ex-Comerica) 5.29, Banner 5.37, Chino 5.50, BMO 7.16, BoC 7.80, CNB 7.91; Rize Ontario 7.88 (w2_geo_screen). PASS.
10. **Sam's Club no-PG in-club-only still qualified** — Tab 1 r15 "EIN-only path: NO personal pull; PG path: Synchrony HP", Apply=In-club, action gated on D&B file; Tab 3 r222 "No-PG possible (in-club EIN-only, established biz file); PG otherwise" + "IN-CLUB kiosk… insist on EIN-only". PASS.

## 8. INTERNAL CONSISTENCY — PASS
- All 32 Tab 1 institutions resolve to Tab 3 rows (incl. renamed forms: Chase Ink→Chase (JPMorgan Chase) r2, Amex→American Express r7, F&M→Farmers & Merchants Bank of Long Beach r56, Rize r238, Southland r239, ICB/American Plus r240/r35-rank34 cross-ref, Arrowhead r158, Kinecta r26, Stanford r216).
- CSV exports: funding_table.csv = 244×36, 0 mismatches in 400 sampled cells vs Tab 3. best_targets.csv = 33×14; every cell either matches Tab 1 exactly or equals `cell_text (hyperlink_URL)` — the documented URL-in-parentheses export pattern (Change Log row 202); 0 non-pattern mismatches across ALL cells.
- Change Log v7 entries (rows 175–202) sampled >10 and all verified against real diffs: tab renames (✓ names), 35 HP-Bureau appends (✓ counted 35), 174 Tab-3 asset fills (✓ assets_fill.csv 174 funding rows; 0 blanks remain), PPB/Comerica/First Foundation/Community West merger flags (✓ in cols 3+35), Wescom r147 ✓, SchoolsFirst r139 ✓, WaFd r18 ✓, American Plus TCM update ✓, 7 new rows 238–244 ✓, Tab 4 FNBO/Stanford/Rize appends ✓, 87 ibanknet fills ✓, new tabs 0/1/2/5/6/7/8 ✓, CSV export note ✓.

---

## FINDINGS

### CRITICAL
(none)

### MAJOR
- **MAJOR-1 — Tab 2 LAFCU row has 0 clickable evidence links, missing the explicit ≥1-link-per-institution acceptance bar.** Evidence-link cell reads "(none found)". Mitigation: verdict is NO-DATA, the absence is honest (bureau_pulls.csv also says "(none found)"), and fabricating a link would be worse — but the bureau_mentor_extu_findings.md LAFCU entry cites a ~2010 myFICO thread + Dovly TU tie-in that COULD have been linked (Tab 1 r25 cites exactly those as "[PARTIAL proxy]"). The evidence exists in-project and was not linked on Tab 2.

### MINOR
- **MINOR-1 — LAFCU characterization differs between Tab 1 and Tab 2.** Tab 1 r25 bureau cell: "TU (mentor + ~2010 rep DP + Dovly tie-in) [PARTIAL proxy]"; Tab 2 r15 verdict: "NO-DATA (prior conflict stands)". Both trace to real sources (extu findings MD vs bureau_pulls.csv) but a reader sees TU-supported on one tab and NO-DATA on the next.
- **MINOR-2 — Verdict-label drift between findings MDs and bureau_pulls.csv/Tab 2** (KeyBank PARTIAL→AGREES; First Citizens PARTIAL→AGREES-WEAKLY; Sunwest NO-DATA→CONFLICTS(stale); Tustin NO-DATA→CONFLICTS(no product); Valley PARTIAL→CONFLICTS(Elan=variable)). Evidence text is identical; only the bucket names changed at integration. Not factual contradictions, but the mapping is undocumented.
- **MINOR-3 — KeyBank CA-footprint warning dropped.** bureau_mentor_eq_findings.md flags "No CA footprint — CA applicant may be ineligible"; this caveat does not appear on Tab 2's KeyBank row.
- **MINOR-4 — Tabs 3 and 4 have zero clickable hyperlinks** (URLs are plain text, carried v6 format). README line 2 implies all sources are clickable. Criterion 3 only requires Tabs 1/2/8, so not a failure — noted for completeness.
- **MINOR-5 — The 7 new v7 rows (Tab 3 rows 238–244) have Deposits = 'N/M'** while their Assets are filled. New rows weren't covered by the 174-fill pass; deposits for Rize/Southland/etc. are obtainable from NCUA.
- **MINOR-6 — Stale autofilter ranges:** Tab 3 autofilter A1:AJ237 excludes the 7 new rows 238–244; Tab 13 autofilter A17:I162 excludes change-log rows 163–202 (incl. all v7 entries). Filtering on those tabs silently hides the newest rows.

---

## BOTTOM LINE
The workbook genuinely satisfies the user's complaints this round: Tab 1 is instantly scannable (30-second verdict: YES), tabs are numbered 0–16 in order, links are real and alive (0 dead of 15 clicked; 3 bot-blocked), the 14-name mentor list is complete and faithful to the research record, assets/deposits are complete to spec (0 gaps on Tab 3 master rows; exactly the 29 documented FBO N/As on Tab 12), the add-only contract is mathematically clean (0 violations across Tabs 3/4/12 and 6 carried tabs), and all 10 provenance spot-checks trace. The single MAJOR (LAFCU's missing Tab-2 evidence link) and six MINORs are polish items, not data-integrity failures.
