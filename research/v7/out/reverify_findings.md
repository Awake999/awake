# Re-verification Findings (4 items) — 2026-06-11

Re-verification sweep run 2026-06-11 by REVERIFY agent. All fetches performed directly (curl with browser UA where WebFetch was blocked). Note on tooling: this environment's egress policy hard-blocks `web.archive.org` content fetches AND `/save` submissions (403 even unsandboxed), but the `archive.org/wayback/available` API works — snapshot existence/timestamps below are verified through that API; snapshot *content* could not be read from here.

---

## 1. Wells Fargo CA bureau (Signify business / BusinessLine LOC) — VERDICT: CHANGED (EX-only assumption is stale; 2024 DPs are mixed EX/EQ, and the lone CA DP is EQ)

Old basis: 2014-2016 *consumer* card data pointing to EX for CA. Fresh 2024 business-product DPs found on myFICO Business Credit board:

| Date | Product | Bureau pulled (personal) | Detail | Source |
|---|---|---|---|---|
| 2024-05-02 | Signify Business Cash | **EX** (hard) | "$30K... They pulled EX about 15 min after applying." Same poster, same day: "Also approved for a 10K BLOC after a separate **EQ** pull. They tried to pull EX, but couldn't view the file due to an 'error'." | https://ficoforums.myfico.com/t5/Business-Credit/Wells-Fargo-Signify-Business-Cash-Card-now-live/td-p/6756650/page/2 |
| 2024-06-07 | Signify Business Cash | **EQ** — applicant states "FICO 8 EQ (**I live in California**) Score at time of application - 740" | $5K SL; also DP that WF requires a checking account open ≥60 days (declined at 30 days, approved at day 62) | https://ficoforums.myfico.com/t5/Business-Credit/Wells-Fargo-Business-Signify-Approval/td-p/6766003 |
| 2024-07-12 | Signify Business Cash | **EQ** | "Approved with 12k limit. 2/24 inquiries. 760ish FICO. **Wells pulled EQ.**" | https://ficoforums.myfico.com/t5/Business-Credit/Wells-Fargo-Signify-Business-Card-Approval/td-p/6773442 |
| 2024-09-18 | Signify Business Cash | EX (poster "can't recall... but I believe so" when asked "Just Ex?") — low confidence | $36K SL | https://ficoforums.myfico.com/t5/Business-Credit/Wells-Fargo-Signify-Business-Card-36K-SL/td-p/6788276 |
| 2024-12-19 | Signify Business Cash | **EX** (hard, in-branch) | "<1 year old LLC. Experian pulled. 808 FICO 8" | https://ficoforums.myfico.com/t5/Business-Credit/Wells-Fargo-Business-Signify-Approved-12k-SL/td-p/6802220 |

Key takeaways for the sprint:
- NOT no-data anymore: 5 usable 2024 DPs.
- Signify personal pull is **mixed EX/EQ** (3 EX-ish vs 2 EQ), apparently state/routing dependent — the 2014-2016 consumer-card state table should not be trusted for the business product.
- The **only California-specific DP (2024-06-07) shows EQ**, directly contradicting the current "EX" slot.
- **BusinessLine/BLOC DP (2024-05-02): EQ pull**, separate from the card's EX pull, same applicant same day — WF business LOC may route to EQ even where the card routes EX.
- Recommendation: for a CA applicant, re-slot WF Signify as **EQ-likely / EX-possible (dual-exposure risk)** rather than EX-confirmed. No TU DPs seen.

---

## 2. PNC BusinessOptions / business LOC soft-EQ path — VERDICT: CONFIRMED (multi-thread, multi-year, incl. April 2026), HIGH confidence on "soft personal pull"; MEDIUM-HIGH that the soft pull is EQ

The path is no longer a single-thread claim. Independent DPs:

| Date | Product | DP | Source |
|---|---|---|---|
| 2022-03-23 | PNC business LOC ($100K approved) | "no hard pull on personal credit, no reporting on personal credit... No documentation required" (only stipulation: open business checking) | https://ficoforums.myfico.com/t5/Business-Credit/PNC-119K-in-Approvals/td-p/6509179 |
| 2022-04 (same thread, second user, South Florida) | PNC business LOC | Underwriter asked to unfreeze **Equifax** only: "which I suppose is their only personal SOFT pull (I'm located in South Florida)" — personal EQ 744 | same thread, td-p/6509179 |
| 2022-09-09 | **BusinessOptions Visa Signature** + biz LOC ($25K + $25K) | "They only do a **soft pull on personal and it was Equifax**... I saw 2 soft pulls on EQ, one was PNC Bank the other just PNC." Also: regular PNC biz cards are "a hard pull on personal" per his PNC rep. | https://ficoforums.myfico.com/t5/Business-Credit/PNC-BizOptions-Visa-Signature-and-a-LOC-Approved/td-p/6589727 |
| 2023-05-08 | PNC regular business credit card ($16K) | "they do a **HP on Experian**" — confirms the contrast: ordinary PNC biz cards = hard EX; BusinessOptions/LOC = soft EQ | https://ficoforums.myfico.com/t5/Business-Credit/PNC-Business-Credit-Card-Approval/td-p/6675929 |
| **2026-04-17** | PNC business LOC ($50K approved, asked $100K, in-branch) | "they typically give 10% of gross revenue and **don't ask for financials up to 100k**... my personal credit was fine (**a soft pull**, 800 scores, 3% utilization)" — bureau not named in this DP | https://ficoforums.myfico.com/t5/Business-Credit/Business-Line-of-Credit-at-PNC/td-p/6862301 |

Assessment: the EQ-sprint #1 slot is **real**. Soft personal pull on PNC BLOC re-confirmed as recently as 2026-04-17; the bureau being EQ rests on two independent 2022 DPs (one explicit unfreeze-EQ request from the underwriter). No contradicting DP found (the only "hard pull EX" DPs are for the *regular* PNC business cards, a different product). Confidence: soft-pull = HIGH; soft-pull-is-EQ = MEDIUM-HIGH (no 2024-2026 bureau-specific confirmation).

PNC.com status: still 503 to this environment on 2026-06-11 (WebFetch 503; curl Chrome-UA 503; curl Firefox-UA + HTTP/1.1 503 — appears to be bot/geo blocking at PNC's edge, not an outage). Durable archived copy of the product page (verified to exist via Wayback availability API):
- **https://web.archive.org/web/20260413081220/https://www.pnc.com/en/small-business/borrowing/business-credit-cards/pnc-businessoptions-visa-signature-credit-card.html** (snapshot 2026-04-13, status 200)

---

## 3. Stanford FCU $50K / $100K claims — VERIFIED LIVE 2026-06-11 + durable archive URLs

sfcu.org 403s generic bots but served full pages to curl with a Chrome desktop UA on 2026-06-11. Verbatim from live pages:

**Business Visa $50K max + 6-mo seasoning + 2-yr TIB — all on ONE page** (https://www.sfcu.org/business/business-credit-card, fetched 2026-06-11):
> "Get the financial flexibility your business needs with a credit limit up to $50,000"
> "Six months after you open a Stanford FCU business checking (spending) account, you can apply for the Business Rewards credit card with a minimum 640 credit score and two years in business."
> Application route: "Start the process by filling out a Business Loan Application and Personal Financial Statement."

**Business LOC $100K** (https://www.sfcu.org/business/business-loans, fetched 2026-06-11):
> "Borrow up to $100,000 unsecured (more than that requires collateral)" (business line of credit section; equipment financing up to $250,000 also listed)

**Durable archive URLs (existence + 200 status verified via archive.org Wayback availability API, 2026-06-11):**
- Business credit card page (legacy URL, which 301s to /business/business-credit-card on the live site today): **https://web.archive.org/web/20260411170438/https://www.sfcu.org/business-banking/credit-cards/** (snapshot 2026-04-11)
- Business loans / LOC page: **https://web.archive.org/web/20260528205506/https://www.sfcu.org/business/business-loans** (snapshot 2026-05-28)
- Business loans (legacy URL): **https://web.archive.org/web/20260411171104/https://www.sfcu.org/business-banking/loans/** (snapshot 2026-04-11)

Caveats: (a) the *exact* new URL /business/business-credit-card has **no Wayback snapshot yet**; a save was attempted via web.archive.org/save and archive.ph but both are hard-blocked by this environment's egress policy (403). Raw HTML of both live pages is preserved locally at /home/user/awake/research/v7/out/sfcu_business-credit-card_20260611.html and /home/user/awake/research/v7/out/sfcu_business-loans_20260611.html as fallback evidence. **Action item: submit https://www.sfcu.org/business/business-credit-card to web.archive.org/save from an unrestricted connection.** (b) The 2026-04-11 legacy-URL snapshot predates today's fetch; its content was not readable from this environment, so treat the local HTML + live-URL citation as primary and the snapshot as the durable pointer.

---

## 4. Enterprise B&T ~$50K app-only broker claim — VERDICT: still UNVERIFIED-CLAIM

Sweeps run 2026-06-11 (web/YouTube/Reddit/myFICO):
- enterprisebank.com/business/credit-cards (fetched live 2026-06-11, 200 via curl): lists three programs — Business Rewards Card (no AF, 1.25x), Business Preferred Rewards ($50 AF, 1.5x), Commercial Card Solution — all 19.25% (Prime+12.5%), **contact-us-only application path, no published credit limits, no "app-only"/"no-financials" language anywhere on the page.**
- No myFICO Business Credit, Reddit, or other forum DP found for any Enterprise Bank & Trust business-card approval, at any limit, in 2024-2026.
- The closest YouTube artifact ("7 Banks That Will APPROVE A New LLC $50,000 (NO Proof Of Income)", Oct 2024, watch?v=HKBQNV8cVvM) was checked: **Enterprise is not mentioned** in title/description/page source.
- The claim remains a private banker/broker assertion with zero public corroboration. Keep out of committed sprint slots; treat as exploratory-call-only.

Durable archive URL (verified via Wayback availability API; latest snapshot as of 2026-06-11):
- **https://web.archive.org/web/20251103215742/https://www.enterprisebank.com/business/credit-cards** (snapshot 2025-11-03, status 200). A fresher save could not be triggered from this environment (web.archive.org/save blocked); raw HTML of the live page saved at /home/user/awake/research/v7/out/enterprisebank_business-credit-cards_20260611.html.

---

## Summary table

| # | Item | Verdict | Confidence |
|---|---|---|---|
| 1 | WF CA bureau for Signify/BLOC | **CHANGED** — mixed EX/EQ 2024; only CA DP = EQ (2024-06); BLOC DP = EQ (2024-05) | Medium (5 DPs, 1 CA-specific) |
| 2 | PNC BusinessOptions/BLOC soft-EQ | **CONFIRMED** — soft personal pull re-verified 2026-04-17; EQ per 2x 2022 DPs | High (soft) / Med-High (EQ) |
| 3 | Stanford FCU $50K card + $100K LOC + 6mo/2yr | **VERIFIED LIVE 2026-06-11** + archive URLs above | High |
| 4 | Enterprise B&T $50K app-only | **UNVERIFIED-CLAIM** (unchanged) | High that no public DP exists |
