# Rail Dispute Resolution: who issues behind `lp.applycommunitycard.com` / `yourcommunitycard.com`?

**Resolved:** 2026-07-26. **Verdict: Claim A is correct. Claim B is refuted.**

The issuer/creditor behind `lp.applycommunitycard.com` and `*.yourcommunitycard.com` is
**Bankers' Bank, Madison WI** (FDIC CERT 23537) — its "Community BankCard" agent-bank
program, processed by FIS. **TCM Bank, N.A. has no role in these hosts.**

The working hypothesis was confirmed in mechanism and sharpened in conclusion:

* Hypothesis (a) **CONFIRMED as to mechanism** — byte-identical HTML/JS proves a *shared
  multi-tenant application platform* (CreditSnap), not a shared issuer. The domain alone
  cannot identify an issuer, and Claim B's central inference is invalid.
* **Refinement:** on this particular host family the issuer does *not* in fact vary. Every
  tenant traced on `lp.applycommunitycard.com` and `*.yourcommunitycard.com` resolves to
  Bankers' Bank. So the *reasoning* in Claim B was wrong, but so was its *conclusion*.
* Hypothesis (b) **REJECTED** — Bankers' Bank is not a TCM agent or reseller. It is the
  creditor of record in its own right (see §4).

---

## 1. The deciding evidence: the platform's own tenant-routing table

`lp.applycommunitycard.com` and `mycommunitycc.com` are byte-identical — confirmed
independently, all four bundles:

| Asset | md5 (both hosts) |
|---|---|
| `/` (index HTML) | `13b7c5af552736d36b82f62bd7b56ef5` |
| `main.js` | `53fff2dd394ab32a841dbe894ad0cc51` |
| `polyfills.js` | `04292a518def8b81e2d98bfff30e1444` |
| `chunk-3I5JGJXI.js` | `0f1c7e3916ec420714e08b824f77c3e6` |
| `chunk-TDZFEMQK.js` | `0000d8db57053fdfb66db653152cf3a2` |

Claim B was right about the bytes and wrong about what they mean. **The platform is
CreditSnap** (San Antonio TX; acquired by SavvyMoney May 2025). The index HTML preconnects
to `https://creditsnap-public.s3.amazonaws.com`, `main.js` builds favicons from
`https://s3.amazonaws.com/creditsnapimages/{institutionId}/fav.png`, and the API base is
`https://prod-api-elb2.creditsnap.com/csb2b/`.

CreditSnap ships **one** Angular bundle for **all** its card-application tenants and
resolves the tenant at runtime from `window.location.hostname`. Byte-identity is therefore
the *expected* result for any two CreditSnap tenants and carries zero information about the
issuer.

Decisively, the identical bytes themselves contain the production routing table
(`chunk-3I5JGJXI.js`, array `i0`), which assigns the two disputed hosts to two **different**
institutions:

```js
i0=[{url:"mycommunityccard.com",         institutionId:"TCM",  cxUrl:"https://apply.mycommunityccard.com"},
    {url:"mycommunitycc.com",            institutionId:"TCM",  cxUrl:"https://apply.mycommunityccard.com"},
    {url:"www.mycommunityccard.com",     institutionId:"TCM",  cxUrl:"https://apply.mycommunityccard.com"},
    {url:"www.mycommunitycc.com",        institutionId:"TCM",  cxUrl:"https://apply.mycommunityccard.com"},
    {url:"lp.apply.cardsupportcenter.com",institutionId:"BBOK", cxUrl:"https://apply.cardsupportcenter.com"},
    {url:"lp.applycommunitycard.com",    institutionId:"2471", cxUrl:"https://sm.lp.applycommunitycard.com"},
    {url:"lp.apply.ubb.com",             institutionId:"2512", cxUrl:"https://apply.ubb.com"}];
...
function r0(e="local"){let n=QC().location.hostname; ... let i=t.find(r=>r.url===n); ...}
var o0=r0("prod"), x={type:"prod",production:!0,institutionCode:o0.institutionId,
   s3Url:"https://creditsnap-public.s3.amazonaws.com/",
   apiUrl:"https://prod-api-elb2.creditsnap.com/csb2b/", ...}
```

* `mycommunitycc.com` → institutionId **`TCM`** (TCM Bank, confirmed)
* `lp.applycommunitycard.com` → institutionId **`2471`** — **not TCM**

The non-prod tables name the tenants: `tcm-lp.creditsnap.com`→`TCM`,
`bbok-lp.creditsnap.com`→`BBOK`, `bbow-lp.creditsnap.com`→**`2471`**,
`2512-lp.creditsnap.com`→`2512`. So `2471` is internally the **`bbow`** tenant — a
bankers'-bank tenant, alongside `BBOK` (Bankers' Bank of Oklahoma, `cardsupportcenter.com`)
and `2512` (United Bankers' Bank, `apply.ubb.com`). CreditSnap's card-application book of
business is essentially *bankers' banks* plus TCM.

Corroboration that these are four genuinely distinct brands: each institution serves its own
favicon (`2471` = 2,025 b; `TCM` = 3,307 b; `BBOK` = 116,087 b; `2512` = 9,659 b). The
`2471` favicon renders as a maroon **"BB" monogram** — Bankers' Bank's mark.

> Note: `2471` is a CreditSnap-internal tenant ID, not an FDIC cert (Bankers' Bank Madison is
> CERT 23537). The load-bearing fact needs no interpretation of the number: **`2471` ≠ `TCM`**
> in the application's own configuration.

## 2. `yourcommunitycard.com` is a *different* platform — and it names Bankers' Bank literally

The per-bank cardholder/application portals (`westptebank.`, `fncbank.`, `csbankcadott.`,
`thebankofnewglarus.` `.yourcommunitycard.com`) are **not** the CreditSnap app at all. They
are Next.js apps on **MK Decision's CCOS**, referencing
`assets.ccos.mkdecision.com`, `api.axiom.alpha.mkdecision.com`, `ccos1-1.alpha.mkdecision.com`.

Every one of the four ships this in its `runtimeConfig`:

```json
"apiUrl":"https://bankersbank.close.mkdecision.com"
```

That is first-party infrastructure naming the tenant **`bankersbank`** outright. And it
matches Bankers' Bank's own public announcement: `bankersbank.com/credit-card-origination/`
names vendor **MK Decision** and its **"Credit Card Origination System (CCOS™)"**, with
"customizable branding for each community bank partner."

This dismantles Claim B's second pillar. The "TCM product artwork set" on
`fncbank.yourcommunitycard.com` is served from `assets.ccos.mkdecision.com` — MK Decision's
shared multi-tenant asset CDN for its bank partners — not from TCM.

## 3. The discriminators all point one way

| Discriminator | TCM Bank | Bankers' Bank / FIS | Observed on the disputed hosts |
|---|---|---|---|
| Cardholder service | 800-883-0131 | **800-423-7503** | 800-423-7503 (Forte, Ergo, Mayville, Capitol, Bankers' Bank's own site) |
| Rewards | cRewardsCard.com | **scorecardrewards.com** | scorecardrewards.com (Forte, Ergo, Capitol, New Glarus, Peoples, Loyal) |
| Statements | — | **MyCardStatement.com** | MyCardStatement.com (Forte, Ergo, Mayville, Farmers Savings, Portage Cty) |
| Program desk | — | **BBCards@bankersbank.com / 877-636-7244** | Farmers Savings, Capitol ("Community BankCard Department at Bankers' Bank") |

`tcmbank.com` lists cardholder service as **800-883-0131** and identifies itself as
"TCM Bank, N.A., a subsidiary of ICBA Payments." Neither that number, nor cRewardsCard.com,
nor the string "TCM" appears anywhere on any of the 12 Wisconsin bank pages, on
`lp.applycommunitycard.com`, or on any `yourcommunitycard.com` portal. `tcmbank.com` never
names `applycommunitycard.com` or `yourcommunitycard.com` as its hosts.

## 4. First-party issuer disclosures (weighted highest) — and a balance-sheet check

Two Wisconsin banks state the issuer on their **own** pages, verbatim:

* **Forte Bank:** "The creditor and issuer of these credit cards is Bankers' Bank, pursuant
  to a license from Visa U.S.A. Inc. in association with Forte Bank."
* **Ergo Bank:** "The creditor and issuer of these credit cards is Bankers' Bank, pursuant
  to a license from VISA U.S.A. Inc. in association with Ergo Bank." — and "Credit cards are
  issued by Bankers' Bank, Madison WI."

Bankers' Bank's own card-marketing page (`cardmarketing.bankersbankusa.com/cards/113`,
Forte's linked product page) states: **"Credit cards are issued by Bankers' Bank, Madison WI."**
with "Online Access: MyCardStatement.com | Rewards: ScoreCardRewards.com | Customer Support:
800-423-7503."

**Independent confirmation that Bankers' Bank is the creditor, not a pass-through agent for
TCM:** Bankers' Bank (CERT 23537) reports **$13,685K of credit-card loans (LNCRCD)** on its
own balance sheet. It books the receivables — which is what being the creditor means, and
which an agent/reseller for TCM would not do. Hypothesis (b) is therefore rejected.

## 5. Method note — the generalizable lesson

Shared-bundle byte-identity is evidence of a **shared vendor**, never of a shared issuer.
Here the very bytes offered as proof of TCM contained the table proving the opposite. The
correct discriminators, in descending weight, are: (1) a first-party "creditor and issuer"
disclosure; (2) the tenant identifier in the platform's own shipped config; (3) the servicing
and rewards stack; (4) balance-sheet receivables. Domain and artwork inference ranks last.

---

## Per-bank re-classification

All 12 → **BankersBank**. Two labels flip on substance (FNC Bank from TCM; Capitol Bank and
Peoples Community Bank from SELF). Full rows in `rail_reclassified.csv`.

| Bank | CERT | City | Prev | FINAL | Conf. |
|---|---|---|---|---|---|
| Forte Bank | 5297 | Hartford | OTHER-BankersBank/Fiserv | **BankersBank** | HIGH |
| Ergo Bank | 10004 | Markesan | OTHER-BankersBank | **BankersBank** | HIGH |
| Capitol Bank | 34074 | Madison | *SELF* | **BankersBank** | HIGH |
| Farmers Savings Bank | 13025 | Mineral Point | OTHER-BankersBank | **BankersBank** | HIGH |
| First National Community Bank (FNC) | 5357 | New Richmond | *TCM* | **BankersBank** | MED-HIGH |
| West Pointe Bank | 34162 | Oshkosh | OTHER-BankersBank (INFERRED) | **BankersBank** | MED-HIGH |
| Citizens State Bank | 2467 | Cadott | OTHER-BankersBank | **BankersBank** | MED-HIGH |
| Mayville Savings Bank | 30585 | Mayville | OTHER-BankersBank/Fiserv | **BankersBank** | MED-HIGH |
| The Peoples Community Bank | 15046 | Mazomanie | *SELF* | **BankersBank** (personal only) | MED-HIGH |
| The Bank of New Glarus | 10378 | New Glarus | NO-CARD | **BankersBank** (personal only) | MED-HIGH |
| The Portage County Bank | 10012 | Almond | NO-CARD | **BankersBank** (personal only) | MED-HIGH |
| Citizens State Bank of Loyal | 6186 | Loyal | NO-CARD | **BankersBank** (personal only) | MED-HIGH |

**No bank on these hosts is TCM.** No row is left UNCERTAIN: the four banks lacking their own
issuer disclosure (FNC, West Pointe, Citizens State Cadott, Mayville) are each carried by
*first-party platform-tenant* evidence — `bankersbank.close.mkdecision.com` in their own
portals' shipped config, and/or CreditSnap tenant `2471` — which outranks domain inference
and is affirmative rather than merely absence-of-TCM. They are held at MEDIUM-HIGH rather
than HIGH precisely because that is infrastructure evidence, not a legal disclosure.

Business-card coverage note: of the 12, **eight** advertise a business credit card
(Forte, Ergo, Capitol, FNC, Farmers Savings, West Pointe, Citizens State Cadott, Mayville).
Four are personal-card-only and remain out of scope for business-card counts
(Peoples Community, New Glarus, Portage County, Loyal).
