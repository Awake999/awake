# ICBA / Community Banks — Oakland & Alameda County, CA: Self-Issue vs Agent-Rail Card Analysis

Run date: 2026-06-30 (agent ALA-ICBA). All work done first-party; no sub-agents.
Companion files: `alameda_icba.csv` (this analysis), `alameda_banks.csv` (37-bank FDIC SOD census, prior run).

## Method note — ICBA directory API
The ICBA map directory (`directory.icba.org`) is open but **does NOT return location-filtered data via the documented endpoints**:
- `/api/directory?action=GetDirectoryMapLocations` (params `qllat`,`qllong`,`qlr`,`qln`) returns `contextData:[]` (empty) for every coordinate/state probe — the map filters client-side.
- The server-rendered page embeds a `var points=[...]` array, but only a **146-point national default sample** (5 in CA, none near Oakland) — not the full membership.
- `/api/textsearch?action=keywords` (param `qk`) throws a NullReferenceException — broken.
- **What works:** the per-bank profile URL `directory.icba.org/{ObjectId}/{Slug}` (e.g. `/7427/Summit-Bank`). A profile that loads = VERIFIED member; bare slug = 404. I resolved ObjectIds via web search (`site:directory.icba.org "<bank>"`), which is the authoritative membership proof.
So membership was verified per-bank, then cross-referenced against the FDIC census.

## ICBA members found (in/around Oakland & Alameda County)
Verified via live ICBA directory profile pages:
| Bank | ICBA ObjectId | In FDIC census |
|---|---|---|
| Summit Bank | /7427/ | Y (23864) |
| United Business Bank (BayCom) | /13445/ | Y (57716) |
| Mechanics Bank | /5206/ | Y (1768) |
| Poppy Bank | /116118, /17131, /17259/ | Y (57903) |
| Metropolitan Bank (Oakland) | /10641/ | Y (25869) |
| Bank of the Orient | /117444/ | Y (20387) |
| California Pacific Bank | /2591/ | Y (23242) |
| Beneficial State Bank | /6513/ (profile currently *unpublished*) | Y (58490) |

Beneficial State's directory record exists but renders "Page is not published"; membership corroborated by ICBA.org featuring it as a member ("Beneficial State Bank's financial activism").

## THE SELF-ISSUER community banks (the prize)
Only two banks in this market issue their own business cards rather than riding an agent rail:

1. **Beneficial State Bank** — Oakland-HQ ICBA member, CDFI (formerly One PacificCoast Bank). Its business-card page self-discloses: **"This is a card issued by Beneficial State Bank."** No `cardaccount.net` (TCM) or `myaccountaccess` (Elan) portal referenced. Program is **new / rolling out 2026** and relationship-manager–gated, so published terms are thin. This is the single confirmed self-issuer among the Oakland ICBA members and the headline find. CA/OR/WA applicants only.

2. **Fremont Bank** — Alameda County's largest locally-headquartered community bank (~$7B, Fremont HQ + Oakland and 10+ county-city branches). Issues its **own Business Platinum / Rewards / Low-Rate / World Elite Mastercards**; cardholder portal is `fremontbank.myapexcard.com` (CoreCard/Apex private-label processor) — **not** TCM's `cardaccount.net` and **not** Elan's `myaccountaccess`. So it is a genuine self-issuer. **Caveat: Fremont Bank is NOT found in the ICBA directory** — it is an independent mutual bank, not an ICBA member. It still satisfies the user's core intent (self-issue community bank in Alameda County).

## The agent-rail banks (NO-GO for self-issue)
- **Summit Bank** → **TCM Bank** (portal `cardaccount.net` = TCM/Fiserv "Community Card Connect", ICBA's own card subsidiary). *Also being acquired by San Francisco FCU, all-cash, closing Q1 2026 — franchise winding down.*
- **United Business Bank (BayCom)** → **Elan** (`card.myaccountaccess.com`).
- **Mechanics Bank** → **Elan** (`myaccountaccess.com`, support 866-552-8855).
- **Poppy Bank** → **Elan**.
- **Bank of Marin** → **Elan** (and not an ICBA member per directory).

`cardaccount.net = TCM Bank, N.A.` and `myaccountaccess.com = Elan Financial Services (US Bank)` were both confirmed — these are the two dominant agent-issuer rails for community-bank business cards.

## No-card banks (nothing to score)
- **Bank of the Orient** — debit cards only; no business credit card product.
- **California Pacific Bank** — merchant/deposit/lending focus; no card product on site.

## NEW banks not in the FDIC census
**None.** Every ICBA member identified in/around Oakland & Alameda County is already in the 37-bank FDIC SOD census. The ICBA directory's location filter being non-functional means I could not surface members lacking an Alameda branch; if the user wants ICBA members *headquartered* elsewhere but lending into Alameda, that requires a different data source. Within the in-county set, the ICBA layer added membership status and the card-rail split, not new institutions.

## No-doc / no-seasoning HIGH candidates
**None rated HIGH.** Both self-issuers are rated **MED**, because:
- **Beneficial State Bank (MED):** self-issuer + CDFI mission explicitly lends to new/underserved/startup businesses (favorable for a brand-new LLC), but the card program is brand-new and RM-gated, so no published TIB or doc requirement to confirm. Most likely personal-FICO + personal-guarantee underwriting (no tax returns), but unverified.
- **Fremont Bank (MED):** true self-issuer with its own rail; small business Mastercards at this tier are typically personal-credit + PG underwritten and often need no tax returns, but TIB and doc requirements are not published.
- The agent-rail cards (TCM/Elan) are themselves frequently **no-tax-return, personal-credit-scored** products, so if the user is willing to accept an agent-issued card, **Summit (TCM)**, **United Business / Mechanics / Poppy / Bank of Marin (Elan)** are MED no-doc candidates — they just are not self-issuers.

**Recommended next step (phone verification):** call Beneficial State Bank business banking and Fremont Bank to confirm (a) personal-guarantee-only / no-tax-return underwriting, (b) any time-in-business minimum, and (c) bureau + Chex/EWS usage. These three data points were not published online for either self-issuer.

## Name-twin discipline log
- **Heritage Bank of Commerce** (Alameda Co, CERT 33905) was **acquired by Citizens Business Bank**; `heritagebankofcommerce.bank` 301-redirects to `cbbank.com`. The many "Heritage Bank … issued by TCM Bank" web hits are *unrelated out-of-state Heritage banks* — do not attribute to the Alameda entity.
- **Metropolitan Bank (Oakland, CERT 25869)** ≠ Metropolitan Commercial Bank (NY, mcbankny.com) ≠ Metro Credit Union ≠ Metrobank card. Issuer for the Oakland entity unconfirmed (tiny bank, likely an agent rail).
- **Bank of the Orient** ≠ Oriental Bank (Puerto Rico) ≠ Oriental Bank of Commerce (India).
- **California Pacific Bank** (calpacificbank.com, SF/Oakland) ≠ **Central Pacific Bank** (cpb.bank, Hawaii — which uses Elan).

## Source links (key)
- ICBA directory profiles: directory.icba.org/{7427|13445|5206|116118|10641|117444|2591|6513}
- TCM Bank rail: https://www.tcmbank.com/community-bank-solutions/credit-card-program ; portal cardaccount.net
- Elan rail: https://card.myaccountaccess.com/
- Beneficial State self-issue disclosure: https://www.supermoney.com/reviews/business-credit-cards/beneficial-state-bank-business-credit-card ; card page https://www.beneficialstatebank.com/business-banking/credit-cards
- Fremont Bank self-issue: https://www.fremontbank.com/business/credit ; portal https://fremontbank.myapexcard.com/
- Summit acquisition: https://www.bankingdive.com/news/san-francisco-federal-credit-union-buy-in-state-summit-bank/753835/
- Heritage→CBB: https://www.cbbank.com/
- Agent-issuer reference: https://www.stacking.capital/articles/credit-card-agent-issuers-complete-guide.html
