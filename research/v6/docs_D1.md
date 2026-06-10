  PROJECT — Master Requirements Checklist

`origin: CA_BizCard_Project_Master_Checklist.md`

==============================================================================


## Master Requirements Checklist — CA / SoCal Business Credit Card Funding Project

Every requirement mined from the chat, in order, with status. `[x]` = done in v4, `[~]` = partial, `[ ]` = open/next.

---

### A. Core objective & deliverable
- [x] Research California financial institutions, ranked by assets highest to lowest. (Originally specified as ibanknet.com; ibanknet's data tables are JavaScript-rendered and the site blocks automated browsers, so the identical underlying FFIEC/FDIC/FRB/NCUA call-report data was pulled from **visbanking.com**, which republishes it. Footnote this everywhere.)
- [x] Deliverable importable into Google Sheets (**.csv**) AND viewable/filterable (**.xlsx**).
- [x] Each new output gets a **new version number** (v1 → v2 → v3 → v4). Preserve prior versions.
- [x] Operational checklist run per institution, top-down.
- [x] Start with a 3–10 institution proof of concept, then scale.

### B. Required data fields (per institution)
- [x] Institution name
- [x] SoCal? (Yes/No) + Region (LA / Orange County / Inland Empire–Riverside+San Bernardino / Coachella Valley / San Diego / Santa Barbara–Ventura / Other CA / Out-of-state) + nearest major city
- [x] City / county / footprint (cities + states where they operate)
- [x] Total assets + total deposits (both shown). **"Withdrawals" dropped** — not a reported bank metric.
- [x] Website link
- [x] Business credit card products (named/listed) + card page link
- [x] Card rate & terms; **0% intro?** (Yes/No + length) as its own clean column
- [x] Apply online? + application link
- [x] **How to apply** when NOT online: visit branch / call number / fill form / relationship manager
- [x] Deposit/relationship account required to apply? (Yes/No)
- [x] Other no-doc / low-doc business products
- [x] **Underwriter / issuer**, standardized: Self-issued / Elan / TCM / FNBO / ServisFirst / TIB / UMB / CorServ-Pinnacle / None
- [x] Hard-pull personal bureau (TransUnion / Equifax / Experian)
- [x] Business bureaus reported to (D&B / Experian Business / Equifax Business / SBFE)
- [x] Reports to personal bureau? (Yes/No)
- [x] **Estimated business credit limit — with references/sources/reasoning**
- [x] Forum approval data (myFICO, Doctor of Credit, CreditBoards, Reddit): approval amounts, starting limits, applicant profile, prerequisites, CLI behavior, one-hard-pull→multiple-approvals — with **verifiable source links**
- [x] Confidence label per field (VERIFIED / INFERRED / UNKNOWN) + sources

### C. Scope rules
- [x] Institution types: banks + thrifts + **credit unions**
- [x] Exclude mega national consumer issuers (Chase/Amex/etc.) from the **count**; include regional banks + everything else as data
- [x] Target: **20–50 self-underwritten** institutions (v4 = 49)
- [x] **Don't omit data** even if it doesn't fit the goal — keep everything; make the gold easy to find
- [x] Geographic focus: SoCal — **LA / OC / Inland Empire (Riverside) highest**, Coachella Valley acceptable/lowest; San Diego + Santa Barbara included as SoCal
- [x] **Rec# count applies to SoCal institutions only**; out-of-state & NorCal/Central = un-numbered reference rows
- [x] Coverage: **all CA institutions above $1B** included (foreign-owned, trust, and bankers' banks intentionally excluded — no retail small-business cards)
- [x] Statewide sweep completed (SoCal + NorCal/Central) + national CUs + national self-issuers as reference

### D. Column order & UX (no "seas of text")
- [x] Most relevant columns first; **SoCal right after Type**
- [x] **Estimated credit limit, then Assets, Deposits, Footprint** near the front
- [x] Standardized values + Yes/No flags so nothing requires parsing prose
- [x] Sortable **Rec#** + **Tier**; auto-filters on every column; frozen header + first columns
- [x] Three data tabs: All Institutions (ranked) · Self-Underwritten · SoCal Gold + CA-Accessible · plus a Legend tab

### E. Color coding (discernible without reading)
- [x] **Institution name = GOLD** when it meets all 4 (self-underwritten + apply online + SoCal + has business card); **mint = 3/4**; `Match` column states what's missing
- [x] Type colored: Bank vs Credit Union vs Card issuer
- [x] **Every underwriter its own color** (Self / Elan / TCM / FNBO / ServisFirst / TIB / UMB / CorServ / None)
- [x] CA Access colored (green = accessible / amber = partial / red = not accessible)
- [x] Apply colored (online / partial / in-person / no card)
- [x] Legend tab: full color key + scoring + term definitions

### F. Recommendation logic
- [x] Best = self-underwritten + apply-online (then in-person) + SoCal + high reported limits + high assets/deposits
- [x] Documented score weights and Tiers A/B/C/D (see master prompt)

### G. CA-accessibility / local-presence rule (critical correction)
- [x] Many "national" banks require **local branch presence / an existing account** — a CA business can't get approved if they've left CA. Flag **PNC, KeyBank, Truist, Citizens, Fifth Third, Regions, M&T, Huntington** as NOT CA-accessible
- [x] CA-accessible nationals: Chase, U.S. Bank (CA branches); Amex, Capital One (online nationwide); Comerica (CA branches)
- [x] Out-of-state CUs flagged by whether a **CA business owner can actually JOIN** (membership eligibility)
- [x] "Why are out-of-state banks listed" explained in-sheet (national card availability, with the local-presence catch)

### H. Verification & integrity
- [x] Self-issued detection = the **"The creditor and issuer of this card is ___"** line on the card page/terms, plus the **CFPB credit-card-agreement database** (issuer-of-record)
- [x] No fabrication; VERIFIED / INFERRED / UNKNOWN on every field; cite sources; quotes <15 words
- [x] Corrections logged: **Pinnacle Bank (Gilroy) = TIB agent, not self** (the self-issuing "Pinnacle" is the unrelated Nebraska bank); **Beneficial State Bank = self**; **Fremont Bank = Pinnacle Bank TN/CorServ agent** and **Community West Bank = TCM agent** (both were user examples assumed self, but are agent-issued)
- [x] Deep dive on top SoCal self-issued: exact APR, apply method, bureaus, limits, membership

### I. Process
- [~] When asking the user something, use **button format** (AskUserQuestion). NOTE: the button/question widget repeatedly errored ("permission stream closed") in this environment; fell back to inline A/B/C and flagged it.

### J. OPEN — the next frontier (the real gap)
- [ ] **Community-sourced "gold" leads** that the call-report/website method structurally misses: e.g., **Enterprise Bank & Trust** (HQ Missouri; operates in CA) reportedly offering ~$50K business LOC and/or card **with no financials, app-only**, via banker jmorrow@enterprisebank.com (introduced through Credit Veterans / Credit with Colin / Freedom Funders); and **LFCU (Langley FCU, VA)** — high-limit/soft-pull, missed because it's out-of-state.
- [ ] Build a **community-mining discovery engine** (see master prompt §8): start from funding-community knowledge, not a bank directory; track the real gold signals (soft pull, no financials, no PG, high starting limit, EIN-only, currently approving), regardless of HQ; then verify each lead against the bank.
- [ ] Verify third-party "funding plug" claims before trusting them.
- [ ] Apply the CA-accessibility filter to any out-of-state lead.

---

#### Why the first extracts kept missing the gold (root cause)
1. **Geography anchor:** the source list was California-HQ institutions ranked by assets. Out-of-state banks that lend into CA (Enterprise = MO, Langley = VA) can never appear.
2. **Source anchor:** call reports show assets/deposits; bank websites show marketing. Neither publishes "this banker is approving $50K no-doc right now." That intel lives only in the funding community and is banker- and time-specific.
3. **Proxy vs signal:** "self-underwritten + apply online + SoCal" is a structural *guess* at fundability. The real gold signal is empirical: soft pull, no financials, no PG, high limit, EIN-only, currently approving.




==============================================================================

