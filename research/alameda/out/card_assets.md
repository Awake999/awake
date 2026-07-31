# "Card Assets" — Program Identification + Alameda-Area Footprint

**Agent:** CARD-ASSETS-RESEARCH · **Date:** 2026-07-26 · **Companion file:** `card_assets.csv`

---

## BOTTOM LINE (read this first)

1. **Card Assets is real, it is not a generic phrase, and it is not a fintech platform.** It is a **turnkey agent-bank credit card program** — legally **a division of First Arkansas Bank & Trust** (FAB&T), Jacksonville, AR (FDIC CERT 16849). Program office in metro Atlanta (Marietta/Kennesaw, GA); remittance/servicing addresses in Jacksonville AR, Tampa FL, and Charlotte NC.
2. **The partner bank is NOT the creditor.** Card Assets / FAB&T is the **issuer of record**, holds the receivable, sets credit policy, and is the entity that reports to the bureaus. Card Assets banks therefore count as **AGENT-ISSUED, never self-underwritten.**
3. **Zero Alameda-area institutions currently run Card Assets.** A full sweep of **all 81 FDIC-insured banks with a branch in Alameda / San Francisco / Contra Costa / San Mateo / Santa Clara counties**, plus **23 credit unions with an Alameda County branch**, produced **exactly one historical hit: First Foundation Bank** — and First Foundation Bank ceased to exist as a charter on **2026-04-01**.
4. **Post-conversion answer on Sunflower / First Foundation: neither Card Assets nor Elan — Sunflower Bank self-issues.** Sunflower Bank, N.A.'s own consumer and Visa Small Business/Corporate card programs are **issued by Sunflower Bank, N.A. pursuant to a license from Visa U.S.A. Inc.**, with its own published Schumer box (biz card 12.45% variable APR, no annual fee), servicing on `mycardstatement.com` / `ezbusiness` (FIS rails). The legacy First Foundation **Mastercard = Card Assets** (`24-7cardaccess.com`) and legacy **Visa/Amex = Elan** (`myaccountaccess.com`) portals are **still live for existing accounts**, but Sunflower says "most system changes [will be] completed by the end of third quarter 2026." **Which program takes NEW Oakland-office business-card applications today is UNKNOWN** — First Foundation's business card page now says only "Contact your local branch to learn more."

---

## TASK 1 — WHAT "CARD ASSETS" ACTUALLY IS

### 1.1 Identity and ownership

| Item | Value | Source |
|---|---|---|
| Legal identity | **Card Assets, a division of First Arkansas Bank & Trust** | 24-7cardaccess.com footer (live 2026-07-30); FAB&T privacy notice; CFPB-filed cardholder agreement |
| Website | **cardassets.com** (live). `card-assets.com` / `cardassets.net` — no program site found | cardassets.com |
| Parent bank | First Arkansas Bank and Trust, Jacksonville, AR — **FDIC CERT 16849**, $1.150B assets / $998.4M deposits (2026-03-31), 21 offices (20 AR + 1 GA) | api.fdic.gov |
| Program HQ | Atlanta metro — 3595 Canton Rd, Ste 312-339, Marietta, GA 30066 (T&C) / 200 Chastain Center Blvd NW Ste 200, Kennesaw, GA (D&B). Mail: P.O. Box 827, Jacksonville, AR 72078 | 24-7cardaccess.com/Home/TermsAndConditions; dnb.com |
| Phone | Program 770-372-3299 · Cardholder 1-800-854-7642 | cardassets.com/partners; 24-7cardaccess.com |
| Origin | Founded as **BV Card Assets LLC** (a BancVue/Kasasa venture, Atlanta). BancVue sold the ~$120MM portfolio to FAB&T; FAB&T took **100% control on 2012-02-28** | globenewswire.com 2012-02-28; arkansasbusiness.com |
| Scale | Self-reported **"400+ participating financial institutions"** and **"Over 80,000 cardholders"** (partners page) vs. **"over 200 financial institutions"** / **"over 200,000 credit card customers"** (about page) — the site contradicts itself; treat as **low hundreds of agent FIs** | cardassets.com/partners; cardassets.com/about |
| Still operating? | **Yes, actively.** Servicing platform "Version 2.4.3 \| Released on 30-Jul-2026"; application platform footer "© 2026 Card Assets"; CFPB agreement filings dated **2-2026** | 24-7cardaccess.com; app.thecardservicescenter.com; consumerfinance.gov |

### 1.2 Digital fingerprints (how to spot a Card Assets bank)

| Domain | Role |
|---|---|
| `www.24-7cardaccess.com` ("The Card Services Center") | **cardholder servicing portal** — the single most reliable tell |
| `app.thecardservicescenter.com/Selection/Selection?finumber=NNNN` | **application platform**; the 4-digit `finumber` identifies the agent FI |
| `www.thecardservicescenter.com` | agent-bank ("PARTNER LOGIN") portal |
| `cdn2.thecardservicescenter.com/images/CUE/...` | FI logos on application pages |
| App Store "24-7 Card Access", developer **First Arkansas Bank & Trust** | mobile servicing app |

### 1.3 Issuer of record — DEFINITIVE

Card Assets is an **agent-issuer**: the partner bank puts its brand on the card and earns a referral fee + revenue share; **Card Assets/FAB&T is the creditor and owns the paper.**

Regulator-filed evidence (CFPB Credit Card Agreement Database, Reg Z §1026.58 — filed under issuer name "FIRST ARKANSAS BANK AND TRUST", `Business_Mastercards_Cardholder_Agreement_7-2025_v7.3.pdf`):

> "The words **we, us, and our** refer to **Card Assets, a division of First Arkansas Bank & Trust** or its assigns."

> "**WE, US, and OUR** means **Card Assets, a division of First Arkansas Bank & Trust (Bank)** and our affiliates, successors and assigns…"

> "This Agreement is entered into between you and us **in Arkansas** and **we extend credit to you from Arkansas**." (§28 Governing Law — Arkansas law regardless of cardholder's state)

> "**We may report information about your account to credit bureaus.**" (§23) — the tradeline is Card Assets/FAB&T, not the branded bank.

Program-side evidence (cardassets.com/partners and /faqs):

> "Partnering with Card Assets gives you the tools to put branded credit cards in your customers' wallets **while leaving the risk and the details to us**."

> "**Card Assets assumes all liability and risk for your credit card accounts.**"

> "We offer competitive rates and secured cards, where **Financial Institutions benefit from deposits but have no credit risk**."

> "**Card Assets will be your sponsor for Visa and Mastercard®**, and you will pay an initial setup fee and then a minimal sponsorship fee each year." (Card Assets holds the network licence — the agent bank does not)

> "Your financial institution will have the option to **override the credit decision (guaranty the account) via Letter of Credit**." (the bank only takes risk by affirmatively guaranteeing an account — i.e. the default is zero bank risk)

Also, FAB&T's own privacy notice served from `fabandt.bank`:

> "The Issuer FI that is issuing this Privacy Notice is **Card Assets, a division of First Arkansas Bank and Trust**." … "Our joint marketing partners include: **Financial institutions for whom we issue credit cards.**"

**Verdict: AGENT-ISSUED. Bank does NOT keep the paper. Bank is not the creditor. Card Assets banks must never be scored as self-underwritten.**

### 1.4 Business cards — YES

Full business/commercial suite, all Mastercard (no Visa consumer/business product seen despite the Visa sponsorship language):

- **Business Platinum Classic** — 0% intro, no annual fee
- **Business Platinum Payback** — 1% cash back, redeemable in $25 increments
- **Business Platinum Preferred** — points (airfare/merchandise/gift cards)
- **World Mastercard for Business (World Elite)** — $29 AF, no FX fee
- **World Elite Plus Mastercard for Business** — $249 AF ($49 each add'l card), up to $200 airline statement credits
- **Non-Profit Organization** variants of Platinum Classic / Payback / Preferred
- Separate **Purchase Cards** product line

**Personal guarantee is required.** Verbatim from the business application flow (`app.thecardservicescenter.com/SelectionBusiness/index/…`):

> "I am an authorizing officer of the company and I understand and agree that **I will be liable, both individually and jointly with the company, for payment of all balances** on any account opened pursuant to this application."

Business cards also carry a **purchase-money security interest** in goods bought with the card (§12 of the business cardholder agreement) — unusual and worth flagging.

### 1.5 Is it the same as / related to any of the named players? — **NO, to all.**

| Named entity | Relationship to Card Assets |
|---|---|
| **TCM Bank, N.A.** | Unrelated. Limited-purpose credit card bank **wholly owned by ICBA Payments** (Tampa, FL). Competitor in the same agent-bank niche. |
| **TIB (The Independent BankersBank)** | Unrelated. Bankers' bank, Irving TX. Competitor. |
| **Elan Financial Services** | Unrelated. Agent-issuing division of **U.S. Bank / U.S. Bancorp**, ~1,300 FI partners. Direct competitor — and the dominant agent issuer in the Alameda-area bank set. |
| **CorServ / Corserv Solutions** | Unrelated. Atlanta issuer-processor that markets the **opposite** model ("a program your bank can own" / self-issuing). |
| **ServisFirst Bank** | Unrelated. Birmingham AL bank with an ABA-endorsed agent card program. Competitor. |
| **Bankers' banks** (e.g. Pacific Coast Bankers' Bank) | Unrelated ownership; overlapping distribution channel only. |
| **First National Bank of Omaha (FNBO)** | Unrelated. Separate agent-issuing bank. |
| **Fiserv / FIS** | Unrelated as owners. FIS-family rails (`mycardstatement.com`, `ezbusiness`, `scorecardrewards.com`) are what **Sunflower Bank** uses; Card Assets runs its own branded stack (`24-7cardaccess.com` / `thecardservicescenter.com`). |
| **Velera (PSCU/Co-op)** | Unrelated. Credit-union CUSO. |
| **Marqeta, Torpago, CreditSnap, MK Decision** | Unrelated. Modern card-issuing/decisioning/origination software vendors; none is a creditor and none has any tie to FAB&T. |

No acquisition, merger, or common ownership between Card Assets/FAB&T and any of the above was found in any source.

### 1.6 Published bank-partner list? — **NO**

cardassets.com has **no partner/locator page** (full sitemap.xml enumerated: home, consumer-cards, business-cards, purchase-cards, partners, about, contact, terms, privacy, faqs, two form-submission pages, careers). Partners are discoverable only by the `24-7cardaccess.com` / `thecardservicescenter.com` tells on each bank's own site, or by `finumber` enumeration on the application platform (the FI is identified only by a logo image, not text).

---

## TASK 2 — WHO USES IT NEAR ALAMEDA, CA

### 2.1 Method

- Pulled **all FDIC branch records** for Alameda + San Francisco + Contra Costa + San Mateo + Santa Clara counties → 1,039 offices, **81 distinct institutions** (`api.fdic.gov/banks/locations`).
- For each institution: fetched homepage + `/credit-cards`, `/business/credit-cards`, `/personal/credit-cards`, `/login`, `/logins`, `/card-services`, **plus every card/login URL in its `sitemap.xml`** (up to 30 pages each) and grepped for `24-7cardaccess` / `thecardservicescenter` / `cardassets.com`.
- Repeated for the **23 credit unions** with an Alameda County branch (from `alameda_cus.csv`) + 1st Nor Cal CU.

### 2.2 Result: ONE hit, and it is now defunct

| Institution | CERT | Card Assets? | Actual current program |
|---|---|---|---|
| **First Foundation Bank** (Oakland office) | 58647 | ✅ **YES — legacy Mastercard** (`24-7cardaccess.com/Login`) | Charter **INACTIVE 2026-04-01**; merged into Sunflower Bank, N.A. |
| **All 80 other Bay-Area banks** | — | ❌ none | Elan (`myaccountaccess`) at Mechanics Bank, Bank of Marin, Bank of San Francisco, Bank of Stockton, EverBank, Exchange Bank, First Federal S&L of San Rafael; FIS/`mycardstatement`+`ezbusiness` at BAC Community, Banner, Tri Counties, GBC International, Western Alliance; big-4 self-issued; rest no card |
| **All 23 Alameda-County credit unions** | — | ❌ none | — |

**No bank or credit union with a branch in or near Alameda County runs Card Assets today.** This is a strong negative, not an absence of evidence: the detection method demonstrably works (it caught First Foundation).

### 2.3 First Foundation / Sunflower — confirmed status

**Merger:** First Foundation Bank (CERT 58647, Irvine CA) — `ACTIVE: 0`, `ENDEFYMD: 04/01/2026`. Last standalone call report 2026-03-31: **$11.34B assets / $8.78B deposits**. It merged with and into **Sunflower Bank, N.A.** (FirstSun Capital Bancorp), completed **2026-04-01**.

**The Oakland office survives under the Sunflower charter.** FDIC now lists "OAKLAND OFFICE, 323 20th St, Oakland CA 94612, Alameda County" under **CERT 4767 (Sunflower Bank, N.A.)** — it is Sunflower's *only* Alameda County office and its **nearest office to Alameda city (37.7652, -122.2416) at ≈3.2 mi**. Phone **(510) 250-8130**, Mon–Fri 9am–4pm. Page disclosure: "Banking products are provided by **Sunflower Bank, N.A. dba First Foundation Bank**, Member FDIC and Equal Housing Lender."

**Card program NOW — three coexisting layers:**

1. **Legacy First Foundation Mastercard → Card Assets.** `firstfoundationinc.com/credit-card-login` still routes "First Foundation Bank Mastercard® credit card" to `https://www.24-7cardaccess.com/Login`. Still live as of this research.
2. **Legacy First Foundation Visa / American Express → Elan.** Same page routes those to `myaccountaccess.com/onlineCard/login.do?theme=elan1&loc=25901`.
3. **Sunflower Bank's own program → SELF-ISSUED VISA.** Sunflower publishes its own Schumer box under its own copyright with no agent-issuer disclosure anywhere on the page: business card **12.45% variable APR** (Prime + 5.70% margin), cash advance 23.49%, **no annual fee**, BT $5/3%, CA $10/3%, FX 1.0%, late/over-limit/returned up to $25, expedited delivery $15, pay-by-phone $10. Servicing runs on FIS rails (`mycardstatement.com`, `EZBusiness Card Management`, `scorecardrewards.com`) — **not** Elan and **not** Card Assets. Cards are "issued by Sunflower Bank, N.A. pursuant to a license from Visa U.S.A. Inc."

**Conversion timing:** Sunflower's merger-updates page states "Your debit card, credit card, or checks will continue working just as they do today — no replacements are required right now" and "We currently anticipate **most system changes to be completed by the end of third quarter 2026**."

**⚠️ Open item (UNKNOWN):** which program a *new* business-card application at the Oakland office lands in today. `firstfoundationinc.com` business credit cards now says only: "We have a number of credit card options for businesses" / "**Contact your local branch to learn more**" / "Credit cards are subject to credit qualification." No online application, no card names, no issuer named. **Phone-screen (510) 250-8130 before assuming.** The most likely post-conversion end state is the Sunflower **self-issued Visa** program (Sunflower is the surviving charter and already self-issues), which would flip this bank from agent to **self-underwritten** — a materially better profile — but that is an inference, not a confirmed fact.

⚠️ **Site access note:** `sunflowerbank.com` is behind a WAF that returns 403 to every automated fetch. Its content was verified via the identical mirror **`firstnational1870.com`** (First National 1870 is a division of Sunflower Bank, N.A.; same footer, same Schumer box) plus search-engine indexing of the sunflowerbank.com pages.

### 2.4 FDIC figures used

| Institution | CERT | Assets (2026-03-31) | Deposits (2026-03-31) | Offices |
|---|---|---|---|---|
| First Arkansas Bank and Trust (Card Assets' charter) | 16849 | $1,150,445K | **$998,431K** | 21 (20 AR, 1 GA) — **zero CA** |
| Sunflower Bank, N.A. | 4767 | $8,553,297K | **$7,151,046K** | 103 (22 CA) |
| First Foundation Bank (inactive 2026-04-01) | 58647 | $11,343,543K | **$8,783,466K** | — |

⚠️ Sunflower's 2026-03-31 figures are **pre-merger** (merger effective 04/01/2026, one day after the call-report date). Combined pro-forma ≈ **$19.9B assets / $15.9B deposits**. Q2 2026 call report data was not yet in the FDIC API as of 2026-07-31.

---

## SCORING IMPLICATION

- A **Card Assets** bank = **agent-issued (Category E-equivalent)**. Same treatment as Elan/TCM/TIB/ServisFirst: the branded bank has no underwriting say by default, no balance-sheet exposure, and the tradeline reports as Card Assets/FAB&T. **Do not count toward self-underwritten targets.**
- **Bureau pulled: UNKNOWN.** No data points found in myFICO/WalletHub/DoC for Card Assets application pulls (the one myFICO thread on "Card Assets, LLC" is 403-blocked to automated fetch). Do not guess — ask at application.
- **Alameda-area actionable Card Assets targets: ZERO.** The prior research note ("re-test Chex behavior + Card Assets program after Q3 2026 conversion" for Sunflower/First Foundation) should be re-scoped: the re-test is really *"does the Oakland office still originate the legacy Card Assets Mastercard, or has it moved to Sunflower's self-issued Visa?"* — and if the latter, First Foundation/Sunflower **upgrades** from agent to self-underwritten.

---

## SOURCES

- https://cardassets.com/ · /about · /partners · /business-cards · /faqs · /contact · /sitemap.xml
- https://www.24-7cardaccess.com/Login · /Home/Help · /Home/TermsAndConditions
- https://app.thecardservicescenter.com/Selection/Selection?finumber=3002 · /SelectionBusiness/index/3002
- https://www.consumerfinance.gov/credit-cards/agreements/issuer/first-arkansas-bank-and-trust/
- https://www.consumerfinance.gov/credit-cards/agreements/issuer/card-assets/
- https://files.consumerfinance.gov/a/assets/credit-card-agreements/pdf/FIRST_ARKANSAS_BANK_AND_TRUST/Business_Mastercards_Cardholder_Agreement_7-2025_v7.3.pdf-525412.pdf
- https://www.fabandt.bank/assets/files/10mII7YB/r/CA+Privacy+Notice.pdf · https://www.fabandt.bank/business/credit-cards
- https://www.arkansasbusiness.com/article/first-arkansas-bank-buys-bv-card-assets-will-offer-credit-cards-to-customers/
- https://www.globenewswire.com/news-release/2012/02/28/1218639/0/en/BancVue-Completes-Sale-of-120-MM-Credit-Card-Portfolio-to-First-Arkansas-Bank-Trust.html
- https://www.dnb.com/business-directory/company-profiles.card_assets_llc.a032f61e0f6cf062c940617ab7341259.html
- https://www.firstfoundationinc.com/credit-card-login · /business-banking/business-lending/business-credit-cards · /mergerupdates · /find-location/oakland-office
- https://www.sunflowerbank.com/business/business-accounts/credit-cards/small-business-and-corporate-credit-cards/ (WAF-blocked; verified via mirror)
- https://www.firstnational1870.com/business/business-accounts/credit-cards/small-business-and-corporate-credit-cards/ · /personal/loans-credit/credit-cards/consumer-credit-cards/
- https://www.sunflowerbank.com/about-us/news/firstsun-capital-bancorp-and-first-foundation-inc-complete-merger
- https://api.fdic.gov/banks/institutions?filters=CERT:16849 · CERT:4767 · CERT:58647
- https://api.fdic.gov/banks/locations?filters=CERT:4767%20AND%20STALP:CA
- https://www.icba.org/web/payments/tcm-bank-agent-credit · https://www.tcmbank.com/
- https://www.elanfinancialservices.com/credit-card/about-elan.html
- https://www.corservsolutions.com/beyond-the-agent-program/ · https://servisfirstbank.com/agent-bank-credit-card-program
