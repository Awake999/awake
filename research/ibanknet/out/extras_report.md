# EXTRAS-CFPB Report — CFPB Agreement DB Match, PG/CLI Policies, Material Findings
Date: 2026-06-12. Companion data: `out/extras_cfpb.csv` (101 rows). All claims sourced; fetch dates are 2026-06-12 unless noted.

## JOB 1 — CFPB Credit Card Agreement Database bulk match

**Mechanism used (live):** https://www.consumerfinance.gov/credit-cards/agreements/ renders its issuer dropdown from a JSON array embedded in the page as `window.cfpbIssuers` (798 issuers, value=slug / label=name, as of the most recent quarterly collection). Parsed 2026-06-12. Per-issuer agreements live at `/credit-cards/agreements/issuer/<slug>/` with PDFs on files.consumerfinance.gov. Note: there is no longer a visible bulk-ZIP link on this page; the embedded issuer list + issuer pages are the live mechanism (archive at `/credit-cards/agreements/archive/`).

**Scope caveat (applies to every row):** the CFPB database contains **consumer** credit card agreements (CARD Act submission duty, with a de-minimis exemption for issuers under 10,000 open accounts). Our underwriter calls are about **business** cards. Therefore ABSENT never contradicts a SELF business-card call, and PRESENT for an Elan-agent bank is a tension, not an automatic error.

**Results: 43 PRESENT / 58 ABSENT (of 101).**

- By our underwriter call: SELF 67 → 40 PRESENT / 27 ABSENT; Elan 26 → 1 PRESENT (Bank of Stockton) / 25 ABSENT; FNBO 2 → 0 PRESENT; TCM 2 → 0 PRESENT; UNKNOWN 2 → 1 PRESENT (Valley First) / 1 ABSENT (Rize).
- **Creditor-name audit:** for all 40+ PRESENT institutions, one filed agreement each was downloaded and its text scanned for third-party creditor names (Elan Financial, TCM Bank, FNBO, U.S. Bank ND, etc.). **Zero hits — no CRITICAL tensions.** Every readable agreement names the institution itself as creditor (4 PDFs were scanned images with no text layer: Valley National, Sierra Central, Bay Federal, First Entertainment — filed under the institutions' own names, no contrary evidence).
- **Namesake false-positives caught (would have been wrong matches):**
  - CFPB "FIRST BANK" is the **North Carolina** First Bank (filed agreement: governing law North Carolina) — NOT our First Bank (St. Louis). Ours = ABSENT.
  - CFPB "UNIVERSITY CREDIT UNION" is the **Maine** entity (governing law Maine) — NOT our LA-based University CU. Ours = ABSENT.
  - CFPB "CITY NATIONAL BANK" **is ours** — verified via agreement payment address (P.O. Box 54830, Los Angeles) + CA governing law + cnb.com/cashback reference, agreement dated 12/2025.
  - CFPB "AMALGAMATED BANK OF CHICAGO" ≠ our Amalgamated Bank (NY; FNBO agent) — ABSENT, consistent.
  - "LOS ANGELES POLICE FCU" ≠ our LAFCU; "FIRST NORTHERN BANK OF WYOMING" ≠ First Northern Bank of Dixon — both ABSENT.
- **Name variants resolved:** Orange County's CU listed as "ORANGE COUNTYS CREDIT UNION" (PRESENT); Valley First listed under its old federal-charter name but the filed agreement names "Valley First Credit Union" (Modesto) — PRESENT.

**Tensions (none critical):**
1. **BANK OF STOCKTON (we call Elan) is PRESENT** — files its own-name consumer Credit Card Agreement + Secured agreement (scanned PDFs). Our Elan call is anchored on its business application portal (mycardapply.com = Elan). Most likely a dual program (in-house consumer, Elan business), but the Elan call should be re-verified before it's load-bearing. https://www.consumerfinance.gov/credit-cards/agreements/issuer/bank-of-stockton/
2. **VALLEY FIRST CU (UNKNOWN)** — PRESENT with own-name TruStage/CUNA agreement → upgrade UNKNOWN toward SELF (at least consumer; business card likely in-house on same rails).
3. Large SELF institutions ABSENT (Tri Counties $8.4B, Western Alliance $17B, Fremont, SAFE CU, WaFd, Tri Counties, etc.) — consistent with de-minimis consumer books or no consumer card; explicitly **not** a contradiction (see scope caveat). SAFE CU's absence is mildly surprising for a 250k-member CU but compliance/listing gaps are common.

## JOB 2 — PG & CLI policies (top self-issuers; verbatim where found)

Best verbatim PG quotes captured (full set incl. URLs in CSV cols PG_policy/CLI_policy):

| Issuer | PG | CLI |
|---|---|---|
| Wells Fargo (Signify, agr. eff. 3/31/2026) | "The Account Guarantor agrees to take full responsibility, along with the business, for paying off all amounts you owe on this Account, even if the business receives more credit in the future." WF need not proceed against the business first. | "We can adjust your Credit Limit at any time, including automatically increasing your Credit Limit if you qualify" (auto-CLI; DoC: mostly soft). |
| Chase (Ink) | Chase's own page: "many business credit cards, including the Chase Ink credit cards, require both joint and several liability." | Cardholder-initiated CLI "will always result in a hard pull" (Doctor of Credit). |
| BMO | "personally guarantee payment of any and all obligations under this Agreement or any subsequent agreement governing the Account" (BCagreement.pdf). | n/p |
| Tri Counties Bank | App BCC-301: "Guarantors unconditionally and irrevocably guarantee in their individual capacity payment... of any and all present and future amounts owed to the Bank"; broad waivers. | Agreement: over-limit posting ≠ limit increase; no published request channel. |
| Travis CU (CFPB-filed business agr., BCCDISC 01/26) | "If you are an organization, the officer or owner that obtained the account for the organization is also personally obligated for all charges made under the account." | "Your credit limit will be reviewed periodically... You can apply for an increase in your credit limit at any time." |
| PNC | Company and applicant "jointly and severally liable" for all transactions (Rates-Visa-Business.pdf). | n/p business |
| WaFd | "Underwriting... is based on your personal credit, and you are personally responsible for the payment of all balances incurred on this account." | n/p |
| Stanford FCU | Business agreement binds "each officer or owner of the organization"; app requires Personal Financial Statement, 640+ FICO, 2 yrs in business. | n/p |
| Citibank | **No-PG path exists**: AAdvantage Business offers corporate-only liability option ("The business is liable for paying charges on the account"). | Citi: instant decision = soft, delayed = hard (DoC). |
| BofA | PG required (app T&C; prior: PG via SSN, no tax returns). | Soft pull since May 2018 (DoC). |
| U.S. Bank | PG (SSN/income; personal hard pull at app). | Online/self-service CLI soft (DoC; myFICO business DPs: revenue-only instant CLI = soft; manual review may hard-pull). |
| First-Citizens | "In most cases, a personal guarantee will be required"; all significant owners credit-pulled. | n/p |
| Redwood CU | PG not verbatim, but app requires business income statement + federal tax returns + personal credit review (doc-heavier than peers). | n/p |
| City National | Relationship-managed: Business Lending App + Personal Financial Statement + Single Name Aggregate Exposure Report (PG implied, not published). | n/p |

Not published online (noted as such, dated, in CSV): Zions, Western Alliance (prior: conditional PG), Kinecta, SDCCU, Fremont, Enterprise B&T, Citizens Bank NA, MidFirst, Logix (prior: inferred), SAFE CU (prior: explicit PG), Patelco (CFPB-filed business T&C is rates-only), Five Star Bank (CA).

## JOB 3 — Material findings (dated, sourced)

1. **Umpqua Bank no longer exists by that name** — legal name became **Columbia Bank** 7/1/2025; brand unified 9/1/2025 (same day Columbia closed its Pacific Premier acquisition). Our roster name is stale; cards/routing unchanged. https://www.columbiabank.com/globalassets/media/documents/columbia_bank_dba_umpqua_bank.pdf ; https://www.columbiabankingsystem.com/news-market-data/press-releases/press-release/2025/Columbia-Banking-System-Completes-Acquisition-of-Pacific-Premier-Bancorp-and-Unifies-Columbia-Brand/default.aspx [2026-06-12]
2. **Mechanics Bank + HomeStreet merger completed 9/2/2025** (~$22B, 166 branches); systems integration targeted Q1 2026 — product set may shift post-conversion. https://www.mechanicsbank.com/about-us/who-we-are/news-press/2025-news-articles/mechanics-bank-completes-strategic-merger-with-homestreet-inc/ [2026-06-12]
3. **First Foundation Bank merged into Sunflower Bank, N.A. 4/1/2026** (FirstSun all-stock); system migrations through Q3 2026. Sunflower (#66 in our files) is the surviving bank. https://ir.firstsuncb.com/news/news-details/2026/FirstSun-Capital-Bancorp-and-First-Foundation-Inc--Complete-Merger/default.aspx [2026-06-12]
4. **Hanmi Bank ↔ Fifth Third signal (the rumored rollout):** live hanmi.com business-cards page (fetched 2026-06-12) still discloses verbatim "The creditor and issuer of these cards is Elan Financial Services..." with Elan's standard suite (Business Zero+/Real Rewards/Cash Preferred/Smart Business Rewards) — our Elan call stands today. BUT the search-indexed version of the *same URL* describes "World & World Elite Business Credit Cards" **issued by Fifth Third Bank, N.A.** with a 50K-point bonus, and Fifth Third announced a commercial-card partnership with Brex on 12/9/2025 ($5.6B volume, "default commercial card solution" for Fifth Third commercial clients). Read: an Elan→Fifth Third program migration appears in-flight or imminent at Hanmi. Monitor; re-verify before relying on the Elan call for 2026 underwriting. https://www.hanmi.com/business/business-credit-cards/ ; https://www.brex.com/journal/press/brex-announces-partnership-with-fifth-third-bank [2026-06-12]
5. **Kinecta + NuVision (BOTH in our 101)** filed an NCUA merger application (announced March 2024); no completion or withdrawal announcement found live as of 2026-06-12 — status unresolved; a combined entity would consolidate two roster rows (~$9B combined CA deposits). https://www.prnewswire.com/news-releases/kinecta-federal-credit-union-and-nuvision-federal-credit-union-file-merger-application-with-ncua-123256923.html [2026-06-12]
6. **Shinhan Bank America (SELF, #98): FDIC AML consent order lifted March 2026** after ~8 years; parent injecting $50M capital for U.S. expansion — removes a regulatory overhang on a roster bank and signals growth posture. https://www.businesskorea.co.kr/news/articleView.html?idxno=241048 [2026-06-12]
7. **SBFE membership signals:** Wells Fargo Signify application terms state business-entity reporting via the **Small Business Financial Exchange**; BofA surfaces D&B SBFE-based scores in Business Advantage 360; SBFE says all 10 of the 10 largest business card issuers are members. Useful for the bureau-reporting matrix. https://www.wellsfargo.com/biz/business-credit/credit-cards/signify-business-cash-credit-card-terms-conditions/ ; https://business.bankofamerica.com/en/resources/credit-score-basics-for-small-businesses ; https://www.sbfe.org/faqs [2026-06-12]
8. **Citi product motion:** consumer lineup rebuilt into Strata family (Strata 5/2025, Strata Elite 7/2025); business lineup still co-brand-heavy with a transferable-points business card as the obvious 2026 gap; AAdvantage Business corporate-liability option remains the documented no-PG path. https://www.citigroup.com/global/news/press-release/2025/citi-launches-citi-strata-elite-credit-card ; https://creditcards.aa.com/credit-cards/corporate-guarantee/ [2026-06-12]
9. **Travis CU business program freshly re-papered:** CFPB-filed Business Credit Card disclosure coded **BCCDISC 01/26** (January 2026) — active, current business program with published PG/CLI terms (see JOB 2). https://www.consumerfinance.gov/credit-cards/agreements/issuer/travis-credit-union/ [2026-06-12]
10. **Santa Cruz Community CU recheck** (not in the 101; flagged for recheck): scccu.org business pages still show "This item is not available yet, but check back soon" placeholders — the 'coming soon' state persists, no launch detected. https://scccu.org/business/business-resource-center/ [2026-06-12]
11. **Five Star Bank namesake risk:** the NY Five Star Bank (five-starbank.com) discloses Elan as its consumer-card issuer; our CA Five Star Bank (fivestarbank.com, Roseville) names no issuer on its live cards page (Business/Consumer/Corporate cards + "Five Star Bank VISA Business card"). SELF call rests on its relationship-based Corporate Card Program — keep, but unconfirmed; never source Five Star facts from the wrong domain. https://www.fivestarbank.com/credit-cards [2026-06-12]
12. **Bank of Stockton dual-program tension** (see JOB 1, tension #1) — re-verify the Elan business call. [2026-06-12]
13. Adjacent-market context: Community West Bancshares completed its merger with United Security Bancshares 4/1/2026 (~$5B, Central CA) — neither party in our 101, but Central-CA consolidation continues around roster banks. https://www.sec.gov/Archives/edgar/data/1127371/000162828026022618/communitywestbancsharesann.htm [2026-06-12]
14. **U.S. Bank CLI policy softened** (no longer hard pull via online CLI link per Doctor of Credit) — relevant to CLI guidance for all Elan-twin programs underwritten on U.S. Bank rails as well. https://www.doctorofcredit.com/u-s-bank-no-longer-hard-pull-credit-limit-increases/ [2026-06-12]

## Method notes / honesty
- Issuer list parsed from `window.cfpbIssuers` (798 entries) embedded in the live page; matching = exact after normalization, then manual resolution of every fuzzy/partial case (no auto-accepted fuzzy matches).
- One agreement per PRESENT institution was text-scanned for third-party creditor names; 4 were scanned images (no text layer) and could not be audited — flagged, not assumed.
- "Not published" PG/CLI entries mean we looked and found nothing public on 2026-06-12; they are not evidence of absence of a PG (industry default is PG-required).
- Forum-sourced CLI behavior (myFICO/Doctor of Credit) is labeled as such and should be treated as anecdotal data points, not policy.
