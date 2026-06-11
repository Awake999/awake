# CHEX-BANKS — SoCal Self-Underwritten Banks: ChexSystems / EWS Screening (BUSINESS-account focus)
Run date: 2026-06-11 · Companion CSV: `chex_socal_banks.csv` · Baseline: v6 `ews_chex_mapping.csv` (2026-06-10)

Method: bank's OWN deposit-agreement/disclosure PDFs first (downloaded + text-grepped locally where possible), then business-application pages, then DoC lists/comments, then forum DPs. Grades: **VERIFIED** (own doc), **DOC-LIST**, **COMMUNITY-DP**, **UNKNOWN**. Key angle preserved throughout: consumer screening ≠ business screening; several banks' own docs scope CRA pulls differently for business accounts.

## Tier table

| Tier | Banks |
|---|---|
| 🏆 GOLD (verified no Chex + no EWS, biz) | — none reached full verification — |
| 🥈 likely-no | **Beneficial State Bank** (own personal AND business agreements name no vendor, generic clause only); **Commercial Bank of California** (own 36-pp disclosures: CRA clause scoped *"(INDIVIDUAL ACCOUNT)"*; business sections = chartering docs + beneficial ownership ONLY, no CRA clause) |
| ⚠ pulls one (Chex; EWS lean-no) | **Farmers & Merchants Bank Long Beach** (VERIFIED, biz included); **Banc of California** (VERIFIED, biz signers included); **California Bank & Trust/Zions** (VERIFIED Chex + EWS-furnish; EWS inquiry unconfirmed); **City National LA** (probable Chex consumer; biz = generic CRA auth, vendor unnamed in own biz doc); **Western Alliance/Torrey Pines** (Crediful consumer; biz = signer CRA auth, vendor unnamed); **Tri Counties** (own FAQ: SOFT Chex, consumer online; biz branch-only, unconfirmed); **UMB** (DoC: Chex yes + soft pull, consumer only) |
| ❌ pulls both | — none verified — |
| ❓ UNKNOWN — ask | **Enterprise Bank & Trust**, **Sunwest Bank**, **FNBO** (DoC: "Unknown, sensitive" + soft pull, both consumer & biz bonus pages), **American Business Bank**, **Citizens Business Bank**, **Chino Commercial Bank**, **IDB Bank NY (LA)** |

## The likely-no list (best business-account targets)
1. **Commercial Bank of California (Irvine, cert 57417)** — strongest structural signal: its own posted Customer Agreements give the consumer-report authorization ONLY under "(INDIVIDUAL ACCOUNT)"; the BUSINESS ACCOUNTS provisions ask only for chartering documents and beneficial-ownership certification. No ChexSystems/QualiFile/EWS named anywhere in 36 pages. (Absence-based — confirm with banker.)
2. **Beneficial State Bank (cert 58490)** — separate Business Deposit Account Agreement (9 pp) and Personal (11 pp) both contain only the generic "credit report by a credit reporting agency" boilerplate; zero Chex/EWS mentions; no community DPs either way. CDFI mission bank → plausibly lenient.
3. Honorable mention: **FNBO** — DoC business-checking bonus page: "ChexSystems: Unknown, sensitive" + "Soft pull"; if it pulls, it's soft, but inquiry-sensitivity flagged.

## Biggest surprises
- **F&M Long Beach is NOT a quiet option**: its T&C (eff. Apr 2024) explicitly says "new accounts are subject to verification through ChexSystems®" and — unusually — states the terms "apply to both personal account owners... and business account owners." One of the few banks where business Chex screening is VERIFIED from its own doc. Zero EWS mentions though.
- **Banc of California upgraded** from a weak undated Unchex cell to VERIFIED: DAAD eff. 2026-01-01 names ChexSystems, and screening triggers "by becoming an authorized signer" — business signers are in scope. EWS absent.
- **City National's own BUSINESS deposit agreement (ID 174) never names ChexSystems** — only generic "consumer reporting agencies, account information services." The DoC "pulls Chex" DPs carry a City-National-Bank-of-West-Virginia name-twin risk (flagged in v6 too).
- **Zions/CB&T**: current charter-wide agreement (eff. 2026-07-20) names Chex mainly in the closure-REPORTING section and points consumers to earlywarning.com for their report — i.e., furnishing to both bureaus is confirmed; opening-side screening clause says "credit reporting or check reporting agency" without distinguishing business accounts.
- **Name-twin minefield**: Citizens Business Bank (every "Citizens Bank" DP online is the RI/NM/GA twin), UMB (United Mississippi Bank), Sunwest Bank (SunWest FCU AZ), City National (WV + Oklahoma cnb1901.com twins). All flagged in CSV.

## Banker questions (for the ❓ banks) — exact wording in CSV column `Banker_question_if_unknown`
Core script: *"When opening a business checking account, do you run ChexSystems, QualiFile, or Early Warning on the entity or on the signers personally — and is it decision-driving or verification-only?"*

## Files
- `/home/user/awake/research/v7/out/chex_socal_banks.csv` (17 data rows, 12 columns)
- `/home/user/awake/research/v7/out/chex_socal_banks.md` (this file)

## Source notes
All claims dated 2026-06-11 unless noted; own-doc PDFs fetched and text-extracted locally:
- FMB T&C: https://www.fmb.com/-/media/terms-and-conditions/fmb-termsandconditions.pdf
- Beneficial State (biz): https://www.beneficialstatebank.com/uploads/files/Business-Deposit-Account-Agreement-and-Disclosure.pdf
- Banc of Cal DAAD 1-1-26: https://dam.bancofcal.com/m/7ac537b3b4b71842/original/Deposit-Account-Agreement-and-Disclosure-DAAD-1-1-26.pdf
- CBC disclosures: https://cbcal.com/wp-content/uploads/2026/01/Account_Disclosures.Final_.v2.pdf
- Zions charter DAA: https://www.zionsbank.com/content/dam/zbna/disclosures/shared/general/depositagreement.pdf
- CNB biz (174): https://www.cnb.com/content/dam/cnb/business-banking/accounts/documents/business-accounts-deposit-account-agreement-174.pdf
- WAB DAA: https://www.westernalliancebancorporation.com/sites/default/files/2024-01/wab-deposit-account-agreement-and-disclosure.pdf
- DoC FNBO biz bonus: https://www.doctorofcredit.com/il-ne-ks-tx-co-in-branch-fnbo-bank-500-business-checking-bonus/
- DoC UMB bonus: https://www.doctorofcredit.com/az-co-il-mo-ne-ok-ks-tx-umb-bank-400-checking-bonus/
- Tri Counties FAQ: https://www.tcbk.com/personal/online-accounts-personal
- Crediful Western Alliance: https://www.crediful.com/chexsystems/western-alliance-bank/
