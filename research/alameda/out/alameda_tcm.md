# Alameda County Community Banks — TCM / TIB / Elan Card Rail Analysis

_Compiled 2026-06-30. Scope: which Alameda County / Oakland-area community banks issue BUSINESS credit cards via the ICBA-ecosystem agent rails, conflict resolution, and a no-doc / no-seasoning profile of TCM Bank for a new-LLC applicant._

## TL;DR / Verdict

- **The clean TCM card in the county is Metropolitan Bank (Oakland)** — apply link routes to `mycommunitycc.com`, issuer = **TCM Bank, N.A.**
- **Summit Bank (Oakland/Emeryville) is NOT TCM — it is TIB.** Its portal `cardaccount.net` and its application/disclosure name **TIB The Independent BankersBank, N.A.** (Dallas TX). This corrects the prior "TCM (cardaccount.net)" tag.
- **`cardaccount.net` = TIB rail; `mycommunitycc.com` = TCM rail.** They are two distinct ICBA-adjacent agent issuers, not the same.
- **United Business Bank conflict — resolved as far as public evidence allows: it is NOT Elan.** No Elan agent-index / "Real Rewards" footprint exists for UBB. The "Standard/Preferred Points" screen is TIB product language. Best evidence => TIB (or TIB-family); definitively NOT a clean Elan no-doc card. Issuer not publicly confirmable; confirm by phone/app.
- **TCM bureau = Experian (personal).** Grade B (corroborated, not bank-published).
- **TCM no-doc/no-seasoning fit = HIGH.** App is app-only on the guarantor's personal credit (mandatory personal guaranty); no financial statements or tax returns required to apply (docs only for lines >= $25,000); no time-in-business minimum (new LLC can apply). Caveat: SBA-eligibility cap (<= $7MM revenue / < 50 employees).

---

## PART A — Rail resolution

### 1. Summit Bank (Oakland/Emeryville) — **TIB, not TCM** (CORRECTION)
- Card page `summitbanking.com/business/loans/credit-cards/` shows **"Standard Card"** (no annual fee) and **"Preferred Points Card"** ($49/yr); cardholder portal **www.cardaccount.net**; rewards `mypreferredpoints.com`.
- The downloadable **business application + disclosure** name the issuer as **"TIB The Independent BankersBank, N.A."**, Box 569120 Dallas TX; servicing fax/email `tib.bank`.
- `cardaccount.net/privacy` is a **TIB privacy notice** — cardaccount.net is the TIB servicing portal, not TCM.
- **NOT a no-doc card:** application states in caps: _"IMPORTANT! THE FOLLOWING INFORMATION MUST ACCOMPANY APPLICATION: CURRENT YEAR END FINANCIAL STATEMENTS INCLUDING BALANCE SHEET AND INCOME STATEMENT. IF APPLICANT IS A CORPORATION, INCLUDE CORPORATE RESOLUTION AND ARTICLES OF INCORPORATION."_ Plus mandatory personal guaranty; guarantors _"shall furnish to Bank annually ... financial statements."_ => **NoDoc fit LOW.**
- Note on identity: the Oakland bank is **summitbanking.com (FDIC CERT 23864)**; `sbko.bank` is an unrelated **Summit Bank of Oregon** (Eugene). The earlier reference to sbko.bank was the wrong bank.

### 2. United Business Bank (BayCom) — CONFLICT RESOLVED: not Elan; most likely TIB; issuer not publicly confirmable
- `unitedbusinessbank.com/loans-credit/business-credit/business-credit-cards.html` describes a **single generic "Credit Card"** with no product names, no "Apply" link, and no issuer disclosure. The site's login menus expose only deposit/online-banking portals (`olb-ebanking.com`, `ebanking-services.com`) — **no card portal**.
- **Decisive negative evidence against Elan:** UBB does **not** appear in the Elan agent index `creditcardlearnmore.com` the way Mechanics, Westamerica, and First Federal of San Rafael do, and there is **no Elan "Real Rewards" / myaccountaccess footprint** anywhere for UBB. (The "United Business" login that resolves to chase.com is the unrelated Chase/United Airlines card.)
- The prior **"Standard / Preferred Points"** screen is **TIB product language** (byte-for-byte the same lineup as Summit's TIB card) — so the conflict resolves toward **TIB**, not Elan. The "another screen said Elan" almost certainly captured a generic Elan login/marketing page returned by a search, not UBB's actual rail.
- **Conclusion:** UBB is **not a clean Elan no-doc business card**; best evidence => TIB (cardaccount.net family, which carries the same upfront-financials burden as Summit). Definitive issuer should be confirmed by calling UBB (855-476-2265) or pulling the actual application. **NoDoc fit: LOW-to-unknown.**

### 3. Metropolitan Bank (Oakland) — **TCM** (newly determined)
- Business credit card apply link routes to **`www.mycommunitycc.com/FROlvrV1uR72`** => **TCM Bank, N.A.** rail.
- Products = TCM business family (Business Edition / Business Rewards / Business Cash Rewards). **NoDoc fit HIGH** (see Part B). This is the cleanest TCM business card in the census.

### 4. California Pacific Bank (Hayward/SF, CERT 23242) — **no card**
- `calpacificbank.com` lists loans, mobile banking, wire, check ordering — **no credit card product**. (Beware: `cpb.bank` is Central Pacific Bank of Hawaii, a different institution.)

### 5. Elan re-confirmations (all CORRECT)
| Bank | Rail | Evidence |
|---|---|---|
| Mechanics Bank | **Elan** | "The creditor and issuer of these cards is Elan Financial Services"; in Elan agent index `creditcardlearnmore.com/11t3`; `myaccountaccess.com` |
| Poppy Bank | **Elan** | Elan-issued Real Rewards; `myaccountaccess.com` |
| Bank of Marin | **Elan** | Explicit page disclosure: "...issuer of these cards is Elan Financial Services, pursuant to a license from Visa U.S.A. Inc." |
| Cathay Bank | **Elan** | Explicit: "...issuer of these cards is Elan Financial Services, pursuant to separate licenses from Visa... and Mastercard..." |
| East West Bank | **Elan** | "East West Bank's Visa credit card is issued by Elan Financial Services"; `myaccountaccess.com` |
| Westamerica Bank | **Elan** | `westamerica.com/credit-card-application`; in Elan agent index `creditcardlearnmore.com/11t3` |
| First Federal S&L of San Rafael | **Elan** | Card links to `creditcardlearnmore.com/11t3` (Elan) + login `myaccountaccess.com?theme=elan1` |

### 6. Cross-check of the 37-bank census for other TCM/TIB community banks
Reviewed `alameda_banks.csv`. The small community banks not already tagged: Heritage Bank of Commerce, Commercial Bank of California, Bank of the Orient, Hanmi, Golden Bank, First Commercial (USA), Farmers & Merchants of Central CA, Beneficial State, Gateway FSB, First Foundation. None surfaced a `cardaccount.net` / `mycommunitycc.com` rail in this pass; most either have no consumer-facing business card or route elsewhere. The only confirmed `mycommunitycc` (TCM) hit in the county is **Metropolitan Bank**; the only confirmed `cardaccount.net` (TIB) hit is **Summit Bank** (with UBB the unresolved likely-TIB candidate). The big national/super-regional banks (Wells, Chase, BofA, Citi, USB, BMO, etc.) self-issue and are out of scope.

---

## PART B — TCM Bank no-doc / no-seasoning profile (for a new-LLC applicant)

Primary source: **TCM Bank "Business Edition" mail application + Important Disclosures, dated 06/30/2026** (`tcmbank.close.mkdecision.com/.../ApplyByMail.pdf`), corroborated by the TCM Business Cardholder Agreement and forum/data sources.

**(a) Time-in-business / seasoning gate? — NO stated minimum.**
The application collects a self-reported **"Number of Years in Business"** field but states no minimum. Eligibility line: _"Only qualified individuals at least 18 years old may be approved for an account."_ A brand-new LLC can apply (enter 0 years). No seasoning gate.

**(b) Financials / tax returns, or app-only on the guarantor? — APP-ONLY on personal credit.**
- The TCM app requires only **self-reported** Annual Business Revenue, # Years in Business, # Employees, plus **a corporate authorizing document** and a Beneficial Owners (CDD) certification. **No balance sheet, income statement, or tax returns are required to apply.**
- Financials only on the back end: _"The Business also agrees to provide financial information upon request"_; and on the credit-line page: _"For credit card lines of $25,000 or more, additional documentation may be required."_
- **Mandatory personal guaranty:** _"by signing below, you will have personally guaranteed any and all credit extended under the account now or in the future"_ and _"jointly and severally liable with the Business."_ Collects SSN, DOB, mother's maiden name, monthly income, own/rent. => **Approval rides on the guarantor's personal credit, not business financials.** Ideal for a no-doc new-LLC applicant.
- (Contrast: the **TIB** program used by Summit Bank DOES demand year-end financial statements + articles/resolution up front — a very different, doc-heavy posture.)

**(c) Personal bureau hard-pulled — EXPERIAN. Grade: B.**
- The app authorizes _"Business and consumer credit reports may be requested."_ Multiple secondary sources converge on **Experian** for the personal hard pull: stacking.capital agent-issuer guide ("TCM Bank... Bureau pull: Experian"); myFICO forum thread 6303273 ("they seem to pull Experian for apps and CLI's... quite conservative"); DoctorOfCredit search snippet. No TCM-published bureau statement exists, hence grade B (well-corroborated but not first-party).

**(d) Chex/EWS — N/A** (credit card, not a deposit account).

**Caveats for the no-doc goal:**
- **SBA-eligibility cap:** TCM revolving cards are only for SBA-eligible businesses — excludes firms with **> $7MM annual revenue or 50+ employees** (those are routed to the pay-in-full Company Rewards charge card). A small new LLC easily qualifies.
- TCM is described as **conservative** underwriting; the partner bank has little say (TCM underwrites centrally on the guarantor's Experian profile).
- Keeping the requested line **under $25,000** avoids the "additional documentation may be required" trigger.

**Net:** For a NO-DOC + NO-SEASONING new-LLC applicant in this area, **Metropolitan Bank's TCM Business Edition card is the standout (HIGH fit)** — app-only, personal-guaranty/Experian-driven, no seasoning, no upfront financials. Avoid Summit Bank's TIB card (and likely UBB) for this purpose: they demand year-end financials up front.

---

## Source links (key)
- Summit Bank cards: https://www.summitbanking.com/business/loans/credit-cards/
- Summit (TIB) business application PDF: https://www.summitbanking.com/wp-content/uploads/2019/08/Business-Credit-Card-Application.pdf
- cardaccount.net = TIB (privacy notice): https://www.cardaccount.net/privacy
- United Business Bank cards: https://www.unitedbusinessbank.com/loans-credit/business-credit/business-credit-cards.html
- Metropolitan Bank: https://www.met.bank/ ; apply: https://www.mycommunitycc.com/FROlvrV1uR72
- California Pacific Bank: https://www.calpacificbank.com/
- Mechanics Bank cards: https://www.mymechanics.com/business/loans-credit/business-credit-cards/
- Bank of Marin cards: https://www.bankofmarin.com/products-and-services/credit-cards/
- Cathay Bank business cards: https://www.cathaybank.com/business/credit-cards
- Westamerica card app: https://www.westamerica.com/credit-card-application/
- First Federal of San Rafael: https://ffsavings.com/
- Elan agent index: https://creditcardlearnmore.com/11t3/index
- TCM Business Edition application + disclosures (06/30/2026): https://tcmbank.close.mkdecision.com/ccos/content/ApplyByMail.pdf
- TCM Business Agent Program: https://www.tcmbank.com/community-bank-solutions/credit-card-program/business-agent-program
- TCM Business Cardholder Agreement: https://www.tcmbank.com/docs/tcmbanklibraries/disclosures/business-cardholder-agreement.pdf
- myFICO TCM thread: https://ficoforums.myfico.com/t5/Credit-Cards/TCM-Bank-credit-cards-any-thoughts/td-p/6303273
- Agent-issuer guide (TCM=Experian, Elan=TransUnion): https://www.stacking.capital/articles/credit-card-agent-issuers-complete-guide.html
