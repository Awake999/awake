# ENTERPRISE BANK & TRUST — DEEP-VERIFY DOSSIER (v6)
*Compiled 2026-06-10 by ENTERPRISE agent. All claims traced to the Clayton-MO charter unless flagged.*

## HEADER BLOCK — IDENTITY (VERIFIED)
| Field | Value | Source |
|---|---|---|
| Legal name | **Enterprise Bank & Trust** | FDIC BankFind API, fetched 2026-06-10 |
| FDIC CERT | **27237** (ACTIVE=1, est. 05/09/1988) | api.fdic.gov/banks/institutions?filters=CERT:27237 |
| HQ | Clayton, Missouri | same |
| Holding company | Enterprise Financial Services Corp ("ENTERPRISE FINL SERVICES CORP" per FDIC; NASDAQ: EFSC) | same |
| Website | http://www.enterprisebank.com (FDIC WEBADDR field) | same |
| Size | $17.196B assets / $14.657B deposits (call rpt 2026-03-31) | same |
| Routing # | 081006162 (shown in site footer) | enterprisebank.com/personal/credit-cards, fetched 2026-06-10 |

### ⚠️ DISAMBIGUATION LEDGER — name-twins encountered and EXCLUDED
FDIC name search "Enterprise" (2026-06-10) confirms multiple twins. Twins that actually polluted search results during this session:
| Twin | Domain | Why dangerous | Status |
|---|---|---|---|
| **Enterprise Bank (Pittsburgh, PA)** | enterprisebankpgh.com | Its card pages carry the Elan boilerplate — raw HTML fetched 2026-06-10 contains *"Elan Financial Services provides zero fraud liability"*. **This is the source of the prior session's near-miss Elan misattribution.** A WebSearch summary this session again wrongly asserted Elan was "the issuer of Enterprise Bank & Trust cards" — disproven against raw HTML (below). | EXCLUDED |
| **Enterprise Bank and Trust Company (Lowell, MA)** | enterprisebanking.com | Acquired — its card-services URL now renders "Welcome to Rockland Trust" (raw HTML, 2026-06-10). | EXCLUDED |
| Enterprise Bank of South Carolina (CERT 11539), Enterprise Bank Omaha NE (CERT 33380, enterprise.bank), Enterprise Bank NJ (CERT 57055, inactive), Pacific Enterprise Bank Irvine CA (CERT 58415, defunct 2022) | various | Name collisions in search results | EXCLUDED |

Every finding below traces to enterprisebank.com raw HTML, api.fdic.gov for CERT 27237, or is explicitly labeled otherwise.

---

## 1. UNDERWRITER PROOF — VERDICT: **SELF-ISSUER / SELF-UNDERWRITER, HIGH confidence** (upgraded from v5 MED-HIGH)

**Evidence FOR self-issuance (all checked 2026-06-10):**
1. **Card loans on its own balance sheet — the decisive new evidence.** FDIC call-report financials for CERT 27237 show field LNCRCD (credit card loans) = **$3.155M (2026-03-31)**, $3.298M (2025-12-31), $3.192M (2025-09-30). A pure agent bank (Elan/TCM/FNBO program) holds **zero** card receivables — the agent owns them. Holding a card book = underwriting/funding its own cards. Source: api.fdic.gov/banks/financials?filters=CERT:27237&fields=LNCRCD. **VERIFIED.**
2. **FIS self-processor rails, zero agent tells.** enterprisebank.com/credit-card-login (fetched 2026-06-10) links only to: ezcardinfo.com (FIS eZCard consumer), ezbusinesscardmanagement.com (FIS eZBusiness), scorecardrewards.com (FIS ScoreCard). Personal card page footnote: *"Download ScoreCard® Bonus Point Program Rules"*. **VERIFIED.**
3. **No Elan anywhere on the real site.** `grep -ci elan` on raw HTML of /business/credit-cards and /personal/credit-cards = **0 matches both pages** (2026-06-10). No myaccountaccess.com, cardpartner.com, TCM, FNBO, or "issuer of this card" boilerplate. Only external href on the business card page is a UHC transparency-in-coverage link. **VERIFIED (negative finding).**
4. **CFPB credit card agreement database** (consumerfinance.gov/credit-cards/agreements/, embedded `cfpbIssuers` list of 800 issuers parsed 2026-06-10): **"Enterprise Bank & Trust" is NOT an issuer-of-record**; nearest string match is irrelevant "ROGERS ENTERPRISES". Elan-program agreements file under "U.S. BANK NATIONAL ASSOCIATION" (present in list). Interpretation: absence is **consistent with self-issuance under the de minimis exemption** (issuers with <10,000 open consumer accounts need not file — a $3.2M card book fits). It does NOT prove agent issuance. **VERIFIED (neutral-to-supportive).**
5. Cards branded both Visa (consumer "Visa® Preferred") and Mastercard (2020 "Mastercard Guide to Benefits" PDF on enterprisebank.com) — mixed-network portfolio is typical of self-issuers, not single-network agent programs. INFERRED, low weight.

**Gap (flagged):** the literal cardholder-agreement sentence ("The creditor and issuer of this card is ___") was **not found** for the Clayton charter — no agreement PDF is published on enterprisebank.com and none is filed with CFPB (exempt). The only "Elan issuer" sentences found belong to the Pittsburgh name-twin. Verdict stands on items 1–4.

---

## 2. CARD PRODUCTS (source: enterprisebank.com raw HTML + WebFetch, 2026-06-10 — VERIFIED)

**Business** (/business/credit-cards) — three products, all **19.25% APR (Prime+12.5%)**, **no 0% intro offered**:
| Card | Annual fee | Rewards |
|---|---|---|
| Business Rewards | $0 | 1.25x points/$ (cash back, gift cards, travel) |
| Business Preferred Rewards | $50 | 1.5% unlimited cash back / 1.5x points |
| Commercial Card Solution | $0 | automatic monthly statement credits on prior-month volume |

**Application channel:** NO online application exists — the only links on the business card page are `tel:(833)896-2850` and a contact email; page touts *"consultative support through our dedicated card relationship managers"*. Apply = phone/email/branch RM. **VERIFIED.**

**Personal** (/personal/credit-cards), for context: Visa Non-Rewards ($0 AF, **0% intro APR 12 billing cycles**, then 10.99–21.99%); Visa Rewards ($0 AF, 0% intro 6 cycles, then 15.49–23.99%, 1.25 pts/$); Visa Rewards Plus ($50 AF, 0% intro 6 cycles, 1.50 pts/$). Cash advance 24.99%. Page disclaims *"accurate as of 06/27/2022"*. Application = web contact form ("let's find the right credit solution"), no online app. **VERIFIED.**

---

## 3. THE ~$50K NO-DOC CLAIM — VERDICT: **UNVERIFIED-CLAIM (broker channel only; zero public datapoints)**

Searches run 2026-06-10 across Reddit/myFICO/CreditBoards/Doctor of Credit/YouTube/blog surface (queries combining "Enterprise Bank & Trust" with $50k / no doc / app only / hard pull / approval / Morrow / Credit with Colin / Credit Veterans / Freedom Funders): **no public datapoint names Enterprise Bank & Trust** in any approval thread, pull database, or video result. This bank is a datapoint desert — the claim lives only inside the paid broker communities.

**Scaffolding that DOES check out (all 2026-06-10):**
- **The banker is real but the name in the brief is off:** theorg.com lists **"Jessica Morrow — AVP Business Banker at Enterprise Bank & Trust"** (theorg.com/org/enterprise-bank-trust/org-chart/jessica-morrow). Matches jmorrow@enterprisebank.com. "Jordan Morrow" appears nowhere — treat "Jordan" as an error. VERIFIED (identity), COMMUNITY-DP (her role in the program).
- **The broker rail is real:** enterprisebank.com/business/sba-lending states *"SBA Lending Division pays referral fees as permitted by state laws"* — a published mechanism for Freedom Funders-type intermediaries. VERIFIED.
- **A plausible underwriting box exists:** same page — SBA *"Express Program"* up to **$500,000** including *"term loans and lines of credit"*, and *"Preferred Lender status with the SBA"* with *"delegated credit authority"*. SBA Express ≤$50K commonly runs on streamlined/app-only docs at PLP lenders, which would make a "$50K app-only" pitch internally consistent — but the bank publishes **no** app-only tier. INFERRED.
- **The community ecosystem is real and has complaints:** Freedom Funders / Credit Veterans / Credit with Colin = Colin Matthew Dedely (freedomfunders.io; northpennnow.com 2025-11-04); **BBB complaints** against Freedom Funders LLC allege unfulfilled promises/refund disputes (bbb.org profile, seen 2026-06-10). UNVERIFIED-CLAIM territory — get terms in writing from the bank, not the broker.

**Bottom line:** keep v5's "~$50K via broker channel UNVERIFIED" label. Only path to verification: direct contact with jmorrow@ / (833) 896-2850 asking for the program parameters in writing (limit, docs, pull type, PG, deposit requirement).

---

## 4. BUREAUS — VERDICT: **UNKNOWN (zero datapoints)**

- **Personal hard-pull bureau:** Not present in Doctor of Credit "Which Credit Bureau Does Each Card Issuer Pull", uponarriving.com credit-pulls DB, CardRight list, or any forum thread surfaced 2026-06-10. UNKNOWN.
- **Business bureau reporting (D&B / Experian Biz / Equifax Biz / SBFE):** SBFE anonymizes members (*"securely stores and manages data from over 140 members"*, sbfe.org, 2026-06-10) and sbfe.org/current-members now 404s — membership not publicly checkable. No tradeline-reporting datapoints found. UNKNOWN.
- Action: this is a first-party question for the banker call (ask which bureau they pull and whether they report to SBFE/Experian Biz).

---

## 5. DEPOSIT RELATIONSHIP / CHEX-EWS — VERDICT: **N/M, RM-relationship inferred**

- **Checking-first requirement:** nothing published. Card pages route everything through *"dedicated card relationship managers"* and a contact form — relationship banking posture strongly suggests a deposit relationship is expected, but no stated requirement. INFERRED.
- **ChexSystems/EWS:** local corpus check 2026-06-10 — /home/user/awake/research/v6/docs_D3.md (DoC EWS list), docs_D4.md, docs_D5.md grep for "Enterprise Bank" = **zero hits**; the bank appears on neither the DoC ChexSystems nor EWS pull lists. Web search for "Enterprise Bank & Trust" + ChexSystems/Early Warning = no datapoints. **UNKNOWN / no-disclosure (datapoint desert), consistent with v5 "N/M".**

---

## 6. SOCAL FOOTPRINT — **8 branches, VERIFIED from FDIC Summary of Deposits 2025 (CERT 27237)**
Source: local files /home/user/awake/research/v6/out/sod_2025_*.json (FDIC SOD 2025), re-extracted 2026-06-10.

| County | City | Branch | Address |
|---|---|---|---|
| LA | Cerritos | Cerritos Main Branch (ex-First Choice HQ) | 12845 Towne Center Dr, 90703 |
| LA | Los Angeles (DTLA) | Los Angeles Branch | 888 W 6th St, Ste 550, 90017 |
| LA | Pasadena | Pasadena Branch | 918 E Green St, Ste 100, 91106 |
| LA | Alhambra | Alhambra Branch | 407 W Valley Blvd, Unit 1, 91803 |
| Orange | Anaheim | Anaheim Branch | 2401 E Katella Ave, Ste 125, 92806 |
| Orange | San Juan Capistrano | SJC Branch | 31351 Rancho Viejo Rd, Ste 101, 92675 |
| San Diego | Chula Vista | Chula Vista Branch | 530 Broadway, 91910 |
| San Diego | Encinitas | Encinitas Branch | 277 N El Camino Real, Ste A, 92024 |

- **Rowland Heights: NOT in SOD 2025.** The legacy First Choice Rowland Heights office is absent from the current branch roster — do not list it. VERIFIED (negative).
- Provenance: EFSC announced acquisition of **First Choice Bancorp (Cerritos, CA; ~$2.5B assets)** 2021-04-26, ~$397.7M all-stock, closed Q3 2021 (businesswire.com/news/home/20210426005693; SEC Form 425 exhibits). San Diego presence traces to the 2020 Seacoast Commerce acquisition (v5 note, not re-verified this session). VERIFIED (First Choice) / CARRIED-FORWARD (Seacoast).

---

## ROW UPDATE RECOMMENDATIONS (v5 → v6)
- **Self-UW?**: `Yes — VERIFIED (HIGH)` — upgrade from "MED-HIGH inference". New evidence string for Underwriter cell: `Self (VERIFIED: $3.2M card loans on own call report LNCRCD 2026-03-31 — agent banks hold $0; FIS rails eZCard/eZBusiness/ScoreCard; 0 Elan mentions in raw HTML; absent from CFPB agreement DB = de minimis self-issuer; Elan tells traced to name-twin enterprisebankpgh.com)`
- **Underwriter confidence note**: replace "no agreement PDF found" with `agreement PDF still unpublished (CFPB-exempt); issuer-of-record proven via balance sheet instead`
- **Est. Credit Limit**: keep `~$50K claimed via broker channel (UNVERIFIED, 2026-06-10; zero public DPs)`
- **Mentor List / banker**: `Jessica Morrow, AVP Business Banker (theorg.com verified 2026-06-10), jmorrow@enterprisebank.com — NOT "Jordan"`
- **HP Bureau**: `N/M — confirmed datapoint desert as of 2026-06-10 (absent from DoC/CardRight/UponArriving pull lists)`
- **Reports To (biz bureaus)**: `N/M — SBFE membership not publicly checkable (anonymized); ask banker`
- **ChexSystems / EWS**: `N/M — absent from DoC Chex+EWS lists (docs_D3 re-checked 2026-06-10)`
- **CA Footprint**: `8 SoCal branches (FDIC SOD 2025, CERT 27237): Cerritos, DTLA, Pasadena, Alhambra, Anaheim, San Juan Capistrano, Chula Vista, Encinitas. Rowland Heights CLOSED/absent from SOD 2025.`
- **Card Products**: unchanged (confirmed 2026-06-10): Business Rewards $0/1.25x; Business Preferred Rewards $50/1.5x; Commercial Card Solution $0/statement credits; all 19.25% (P+12.5%), no biz 0% intro; personal cards have 0% intro 6–12 cycles.
- **How to Apply**: `Phone (833) 896-2850 / email / branch RM — no online application (only tel: link in page HTML, 2026-06-10)`
- **Sources cell — add**: `api.fdic.gov financials LNCRCD CERT 27237 (2026-06-10); CFPB cfpbIssuers list (800 issuers, no EBT entry, 2026-06-10); theorg.com/org/enterprise-bank-trust/org-chart/jessica-morrow`
- **Confidence / Date**: `HIGH self-issuer + products + footprint (2026-06-10); $50K claim still UNVERIFIED`

## DIAMOND/PLATINUM TIER ASSESSMENT
| Criterion | Status |
|---|---|
| Self-underwritten | ✅ **VERIFIED HIGH** (balance-sheet card loans + FIS rails + no agent tells) |
| $25–50K no-doc | ⚠️ **UNVERIFIED** — broker-channel claim only; zero public DPs; bank publishes no app-only tier (SBA Express ≤$500K is the plausible vehicle) |
| No Chex/EWS | ❓ **UNKNOWN** — no disclosure, no datapoints either way |
| CA-accessible | ✅ **VERIFIED** — 8 SoCal branches across LA/OC/SD (FDIC SOD 2025) |

**Verdict: PLATINUM-CANDIDATE, not Diamond.** Two of four criteria verified (self-UW, CA access); the tier-defining $25–50K no-doc box and Chex/EWS behavior both hinge on a single unverified broker claim. The self-issuer upgrade materially raises the ceiling (they control their own credit box, RM channel can flex), but promote to Diamond only after written program terms from jmorrow@/(833) 896-2850 confirm limit, app-only docs, pull type, and PG. Until then: Platinum with a 🎯 follow-up flag.
