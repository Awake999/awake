# LAFCU Dossier — Los Angeles Federal Credit Union

**Legal name:** Los Angeles Federal Credit Union (LAFCU)
**NCUA charter #:** 1207 (federal charter, chartered 1936-03-31) — VERIFIED via local NCUA census file (`/home/user/awake/research/v6/v5_ncua_census.csv` row: charter 1207 = "LOS ANGELES" FCU) and corroborated by creditunions.org/c/los-angeles-federal-credit-union-1207 and bestcashcow.com/credit-unions/los-angeles-1207 (checked 2026-06-10)
**HQ:** 300 S Glendale Ave, Glendale, CA 91205
**Assets / members:** ~$1.2–1.28B; ~53,500 members; 7–8 LA County branches
**Website:** https://www.lafcu.org

⚠️ **DISAMBIGUATION (enforced):** lafcu.com = LAFCU of Lansing, MICHIGAN — appeared in search results ("Credit Cards - LAFCU", lafcu.com/creditcards) and was **discarded**. LFCU = Langley FCU (VA) — not encountered. Every source below is lafcu.org or explicitly references charter 1207 / Glendale CA.

Local docs check: `grep -i 'lafcu|los angeles federal'` over docs_D3.md, docs_D4.md, docs_D5.md → **zero hits** (2026-06-10). Only mentions are in v5_ncua_census.csv, v5_all_institution_names.txt, v5_funding_table.csv.

---

## 1. UNDERWRITER PROOF — Self-underwritten: YES (VERIFIED)

- **Creditor identity:** lafcu.org Visa Variable Credit Cards Agreement & Disclosure (fetched 2026-06-10, https://www.lafcu.org/disclosures/visa-variable-credit-cards-agreement-and-disclosure) states verbatim: "'We,' 'Us,' 'Our,' and 'Credit Union' mean the LOS ANGELES FEDERAL CREDIT UNION." No Elan, TCM Bank, or any agent issuer appears anywhere. **Caveat:** that posted agreement covers *consumer* Visas (Platinum, Signature Rewards Platinum); a separate business-card agreement is not posted publicly. INFERRED (high confidence) the business Visa is also LAFCU-issued: same in-house application portal, no agent-issuer branding anywhere on the business pages.
- **Application flow:** Consumer card "Apply" buttons → `access.meridianlink.com/pos/lafcu_250220/...` (LAFCU's own MeridianLink consumer LOS). Business loan AND Business Visa "Apply" → `app.loanspq.com/apply.aspx?enc=...` (LoansPQ = MeridianLink's commercial LOS, white-labeled for LAFCU). Both fetched 2026-06-10 from lafcu.org/loans-credit/visa and /loans-credit/business-loans. **No redirect to Elan/myaccountaccess, TCM, or any third-party issuer.** VERIFIED.
- **CFPB agreement database:** issuer page consumerfinance.gov/credit-cards/agreements/issuer/los-angeles-federal-credit-union/ returned 404 on 2026-06-10 (database is JS-driven; direct slug failed). Note: CFPB's database covers consumer agreements only — business card agreements are not required filings. UNKNOWN (database listing), but immaterial given the on-site agreement language above.
- **Velera/CURewards** = card processor/rewards program only, consistent with v5 row. INFERRED.

## 2. PRODUCTS & LIMITS (VERIFIED 2026-06-10, lafcu.org)

- **Business Rewards Platinum Visa:** "Up to $50,000" credit limit; **15.75% variable APR**; **no annual fee**; 2x CURewards points on gas/groceries/restaurants/travel, 1x elsewhere; concierge, purchase protection, travel accident insurance. (lafcu.org/loans-credit/business-loans + lafcu.org/rates, rates "as of 6-10-26".) No 0% intro.
- **Business term loans:** $20,000–$50,000 fixed-rate, "no prepayment penalties."
- **Business line of credit:** $20,000–$50,000 variable-rate. (No published LOC APR on rates page — UNKNOWN.)
- **Business vehicle:** $20K–$150K; **CRE:** $300K–$3M.
- **2-year gate verbatim (VERIFIED, lafcu.org/loans-credit/business-loans, 2026-06-10):** "The business must be established and operating for a minimum of two full years."
- Also verbatim on same page: "48-hour prequalification turnaround" and "No application fee"; "Local decision-making and approvals."

## 3. NO-DOC REALITY

- **Published checklist:** NONE for lending. The business-loans page lists no documentation requirements (no tax returns/financials mentioned) and directs callers to (877) 695-2328 ext. 6495. UNKNOWN whether the LoansPQ business app demands financials — "$50K app-only no-doc" remains **UNVERIFIED** (matches v5 flag).
- **Business *account* docs (VERIFIED, lafcu.org/accounts/business-accounts, 2026-06-10):** entity formation docs + EIN letter + "Business Account Service Questionnaire" + photo ID per signer; in-branch only. Also: "LAFCU does not offer business accounts with a large volume of business activity" — a soft activity gate worth noting.
- **Community DPs on business card/LOC approvals: ZERO found.** Searched myFICO, Reddit, DoC, CreditBoards (2026-06-10) — no business-card approval DPs exist publicly. COMMUNITY-DP void confirmed.
- **Consumer proxies (COMMUNITY-DP):**
  - myFICO #6722499 ("LAFCU Visa Signature Rewards", 2023-11): member saw in-portal **pre-approvals**, clicked card app, "instantly approved" — $5K SL @ TU 804 per v5 row (thread now 403s direct fetch; details corroborated via search snippets 2026-06-10).
  - myFICO #6596415 ("LAFCU DP and Info", 2022): joined 2021-06 (TU hard pull); Visa app 2022-05 → **denied for inquiries (4 recent)**; "very conservative"; "human underwriting for most loans"; "definitely not recommended from my perspective."
  - myFICO #838290 (2011, dated): pulls TU only; reports TU + Experian, not Equifax.
- **Verdict:** conservative, human-underwritten, inquiry-sensitive shop. $50K is an advertised ceiling with no public evidence anyone has hit it, doc-free or otherwise.

## 4. BUREAUS

- **Membership/account opening:** hard pull — own site verbatim (VERIFIED live 2026-06-10, lafcu.org/accounts/credit-union-membership AND /accounts/checking): "A 'ChexSystems' and hard-hit on your credit will be run." Bureau = TransUnion per 2021-06 member DP (myFICO #6596415). COMMUNITY-DP.
- **Card application:** CONFLICTING COMMUNITY-DPs — the 2022-05 Visa app in thread #6596415 is summarized as an **Equifax** hard pull in one 2026-06-10 search-result rendering, while the v5 row recorded it as **EX (Experian)**; direct thread fetch returns HTTP 403 so the exact bureau could not be re-read. 2023-11 approval (#6722499) was TU-based per v5. **Flag: card-pull bureau = TU and EQ-or-EX mixed; treat as multi-bureau risk.** Old 2011 DP: TU pull, reports to TU+EX only.
- **Business card bureau:** UNKNOWN (zero DPs).

## 5. CHEX / EWS

- **ChexSystems at membership: VERIFIED live 2026-06-10** — "A 'ChexSystems' and hard-hit on your credit will be run" appears on BOTH lafcu.org/accounts/credit-union-membership and lafcu.org/accounts/checking. This is a hard gate at the membership step, before any lending.
- **Second-chance policy:** NOT found on the live site (membership and checking pages checked 2026-06-10 — neither mentions second-chance/fresh-start). One 2026-06-10 search summary asserted a "Second Chance Checking" product but could not be confirmed on any lafcu.org page and may conflate other institutions (e.g., LAPFCU) — the v5 claim "2nd-chance if Chex balances paid" is **DOWNGRADED to UNVERIFIED**.
- **EWS:** no mention anywhere. UNKNOWN (no evidence of use).

## 6. MEMBERSHIP ELIGIBILITY (VERIFIED 2026-06-10, lafcu.org/accounts/credit-union-membership + /accounts/business-accounts)

- **Consumer paths:** (a) live or operate a business in **Los Angeles, Orange, Riverside, San Bernardino, or Ventura** county → $8 donation to Los Angeles Charitable Association (LACA); (b) outside those counties → $8 Financial Fitness Association membership; (c) City of Los Angeles employee.
- **Open requirements:** $10 to open ($5 fee + $5 savings); $50 savings balance after 6 months or fees; CA ID + SSN + income info; site states Greater LA metro residency expected.
- **Business accounts:** **in-branch ONLY**, via LACA; verbatim: "Your business must be located in Southern California." Entity docs + EIN + questionnaire per Section 3. Business membership is the prerequisite for the business Visa/loan application.

---

## ROW UPDATE RECOMMENDATIONS (field: value)

1. **Chex/2nd-chance field:** change "2nd-chance if Chex balances paid" → "Chex + hard credit pull at membership (verbatim, live 2026-06-10); NO second-chance product found on site — prior 2nd-chance claim unverified."
2. **Bureau field:** "Membership = TU hard (2021 DP). Card = mixed: 2022 denial pull EQ-or-EX (source thread 403s; conflicting renderings), 2023 approval TU. Business card bureau N/M."
3. **App-flow field:** add "Consumer cards: access.meridianlink.com/pos/lafcu_250220; Business loan+Visa: app.loanspq.com (same enc URL for both) — confirms in-house LOS, no agent issuer."
4. **Self-UW field:** keep "A — Self-UW"; add "consumer Visa agreement names LAFCU as creditor verbatim; business-card agreement not publicly posted (inferred same issuer)."
5. **Membership field:** add "business accounts in-branch only via LACA; 'business must be located in Southern California' (verbatim); LAFCU declines high-activity business accounts (own site)."
6. **Notes field:** add "Business LOC APR unpublished; rates page (eff 6-10-26) lists only the Business Visa at 15.75% var / $50K max / $0 AF."
7. **Charter field:** confirm "NCUA charter #1207, chartered 1936."
8. Keep: GOLD 4/4, 2-full-years TIB gate (re-verified verbatim 2026-06-10), zero public business DPs, $50K advertised max.

## DIAMOND / PLATINUM TIER ASSESSMENT

- **Diamond (self-UW + $25–50K no-doc + no Chex/EWS + CA-accessible): FAIL.**
  - Self-UW: YES. $25–50K product: YES (advertised). CA-accessible: YES (5-county SoCal field of membership).
  - **No Chex/EWS: FAIL** — ChexSystems + hard credit pull is stated verbatim on the live membership page; it is unavoidable at the join step.
  - "No-doc": UNVERIFIED with zero approval DPs; human/conservative underwriting and a 2-full-year TIB gate make app-only $50K implausible.
- **Platinum (self-UW + $20K+ card + no Chex/EWS + SoCal-near): FAIL** — same Chex disqualifier; everything else qualifies (self-UW, $50K card, 8 LA County branches).
- **Honest read:** LAFCU stays **GOLD (4/4)**. It is a genuine self-underwriting SoCal CU with a $50K business Visa ceiling and online card app — but the membership-stage Chex + hard pull, in-branch-only business membership, 2-full-year TIB gate, conservative/inquiry-sensitive human underwriting, and a total absence of business approval DPs disqualify Diamond and Platinum. Best fit: clean-Chex, low-inquiry, 2yr+ SoCal businesses willing to visit a branch.
