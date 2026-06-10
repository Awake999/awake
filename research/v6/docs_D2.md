  PROJECT — Master Handoff Prompt (the operating brief)

`origin: CA_BizCard_Project_Handoff_Prompt.md`

==============================================================================


## MASTER HANDOFF PROMPT — Business Credit Card / Funding Target Database (California-focused)

> Paste this whole document into a fresh Claude (or any capable LLM with web search + file tools). It is self-contained. Attach the latest data file (`CA_BizCard_Funding_Targets_v4.xlsx` / `.csv`) if you have it; if not, the schema below lets you rebuild from scratch.

---

### 0. YOUR ROLE
You are continuing a multi-session research project for a Southern California entrepreneur who is assembling a **funding database of business credit cards and business lines of credit**. The goal is to find the **best, most-gettable, highest-limit, lowest-documentation** business funding products for a California business owner — and to rank and present them so the best targets are obvious at a glance. Build on what's done and **go farther**. Accuracy and honesty matter more than volume.

### 1. MISSION & DEFINITION OF "GOLD"
A target is **GOLD** when it meets all four:
1. **Self-underwritten** — the bank/CU is the legal "creditor and issuer" and makes its own credit decision (NOT a rented agent issuer).
2. **Apply online** — true online application (not "call a banker").
3. **SoCal** — headquartered in / serving Southern California (LA, Orange County, Inland Empire = highest priority; San Diego, Santa Barbara, Coachella Valley acceptable).
4. **Has a real business credit card** (interest-bearing/revolving).
Secondary value signals (the *real* prize, see §8): **high starting limit ($25K–$50K+), no financials / no-doc, no personal guarantee, soft pull, EIN-only, currently approving.**

### 2. WHAT IS ALREADY BUILT (current state = v4)
- **162 institutions** researched. **49 self-underwritten.** 79 SoCal. 48 with no business card. 4 tabs.
- Built from **visbanking.com** (FFIEC/FDIC/FRB/NCUA call-report data — the same data ibanknet republishes; ibanknet itself is JS-rendered and blocks bots, so use visbanking).
- Coverage: every CA bank >$1B + the SoCal long tail + NorCal/Central CA + national self-issuing super-regionals + national credit unions + the mega issuers (as reference).
- File: `CA_BizCard_Funding_Targets_v4.xlsx` (+ matching `.csv`). Versions v1–v4 preserved.

### 3. EXACT OUTPUT SCHEMA (reproduce or extend this)
Two deliverables every time: a formatted **.xlsx** (filters, frozen panes, color-coding) and a plain **.csv** (clean Google-Sheets import). **Increment the version number** each output (v5, v6…); never overwrite a prior version.

**Tabs:** (1) `Ranked - All Institutions` · (2) `Self-Underwritten (Top Targets)` · (3) `SoCal Gold + CA-Accessible` (the shortlist a CA business can actually get) · (4) `Legend & Scoring`.

**Columns, in this exact order (front = most relevant):**
1. Rec # — recommendation rank. **Numbered for SoCal institutions only**; out-of-state & NorCal/Central are left blank (reference rows).
2. Tier — A=self-issued+apply-online · B=self-issued+in-person · C=agent-issued · D=no card
3. Institution — **name cell colored GOLD if 4/4 criteria, mint if 3/4**
4. Match (criteria) — text, e.g. "GOLD 4/4" or "3/4 (missing: apply online)"
5. Type — Bank / Credit Union / Card issuer (colored)
6. SoCal? — Yes/No
7. Region — SoCal-LA / SoCal-Orange County / SoCal-Inland Empire / SoCal-Coachella Valley / SoCal-San Diego / SoCal-Santa Barbara-Ventura / Other California / Out-of-state
8. CA Access / Why listed — see §6 (colored green/amber/red)
9. **Estimated Business Credit Limit — with source/reasoning** (VERIFIED published cap, myFICO-backed range, or labeled estimate by issuer pattern)
10. Total Assets
11. Total Deposits
12. Footprint
13. Rec Score
14. City
15. County
16. Website
17. Biz card? (Yes/No)
18. Card page (URL)
19. Apply (Online / Partial online / In-person / No card)
20. **How to Apply (method / link)** — if not online: branch / phone number / form / relationship manager
21. Self-underwritten? (Yes/No)
22. Underwriter / Issuer (**colored by type** — see §5)
23. Interest-bearing? (Yes revolving / Charge card / -)
24. 0% intro? (Yes/No + length)
25. Rate & terms (APR, annual fee, rewards)
26. Hard-pull bureau (TransUnion/Equifax/Experian)
27. Business bureaus reported to (D&B / Experian Business / Equifax Business / SBFE)
28. Reports to personal bureau? (Yes/No)
29. Approval info (limits / profile / prerequisites / CLI / one-pull-multiple)
30. Approval source links (verifiable forum URLs)
31. Deposit/account required? (Yes/No + detail)
32. Other no-doc business products
33. Confidence & notes (VERIFIED / INFERRED / UNKNOWN flags)
34. Sources

### 4. SCORING & TIERS (how Rec # is computed)
Score = Self-issued **+100** · Apply online **+26** / partial **+16** / in-person **+7** · SoCal LA-OC-IE **+35**, San Diego/Santa Barbara **+24**, Coachella **+18**, Other CA **+14**, Out-of-state **0** · Reported high limits **+15** (strong) / **+8** (some) · Assets band **+2 to +10** · Revolving **+5** · 0% intro **+5** · No deposit required **+5**. Sort SoCal first (numbered by score), then the rest (un-numbered).

### 5. UNDERWRITER COLOR KEY (each distinct)
Self-issued = green · Elan (U.S. Bank) = amber · TCM Bank (ICBA) = orange · FNBO = blue · ServisFirst = purple · TIB (Independent Bankers Bank) = pink · UMB = teal · CorServ/Pinnacle Bank TN = lime · None = gray.

### 6. CA ACCESS LOGIC (critical — the local-presence rule)
A business credit card is *issued* nationally, BUT **many "national" banks require local branch presence or an existing account** and will not approve a CA business if they've left the state. Flag honestly:
- **CA-accessible:** CA-HQ banks/CUs; Chase & U.S. Bank (CA branches); Amex & Capital One (approve online nationwide, no branch needed); Comerica (CA branches).
- **NOT CA-accessible (flag red):** PNC, KeyBank, Truist, Citizens, Fifth Third, Regions, M&T, Huntington — no CA branches, local relationship required.
- **Out-of-state credit unions:** accessible only if a CA business owner can **JOIN** (open membership via a nationwide association, e.g. American Consumer Council). Joinable-from-CA examples found: Mountain America, Bethpage/FourLeaf (open US charter), DCU, Coastal (NCSEA $18), Lake Michigan (ALS Assn $5), Connexus, ESL (museum). Restricted (CA cannot join): America First, Randolph-Brooks, Suncoast, VyStar, Idaho Central, Truliant, GreenState (card geofenced out of CA).

### 7. METHODOLOGY & VERIFICATION STANDARDS
- **Self-issued detection:** find the literal "The creditor and issuer of this card is ___" line on the bank's business-card page or terms PDF. Bank/CU named = SELF. Names Elan/TCM/FNBO/ServisFirst/TIB/UMB/CorServ = AGENT. Cross-check the **CFPB credit-card-agreement database** (consumerfinance.gov/credit-cards/agreements) — the entity filing under its own name is the issuer-of-record.
- **No fabrication.** Label every field VERIFIED (official source) / INFERRED (issuer pattern) / UNKNOWN (not published). Quote ≤15 words. Cite source URLs.
- **Known traps:** same-named banks (Pinnacle Bank Gilroy CA ≠ Pinnacle Bank Nebraska; SECU NC ≠ SECU Maryland; multiple "Liberty"/"Heritage"/"Legacy" banks). Verify the exact domain. Servicing on `myaccountaccess.com`/Fiserv ≠ proof of agent-issuance — read the actual creditor line.
- **Corrections already made (don't redo wrong):** Pinnacle Gilroy = TIB agent; Beneficial State Bank = self; Fremont Bank = Pinnacle Bank TN via CorServ (agent); Community West Bank = TCM (agent). The dominant agent issuer for CA community banks is **Elan**; for small ethnic-community banks it's often **TCM**.

### 8. THE NEXT FRONTIER — COMMUNITY-SOURCED GOLD LEADS (most important)
The call-report + website method **structurally misses** the highest-value programs, because the "no-doc / $50K / app-only / soft-pull / no-PG" reality is (a) often at out-of-state banks that lend into CA, and (b) never published on websites or call reports — it lives in the **business-funding community** and is banker- and time-specific.

**Known leads to verify and add:**
- **Enterprise Bank & Trust** (HQ Clayton, Missouri; Enterprise Financial Services Corp; operates in CA among other states). Reported via Credit Veterans / Credit with Colin / Freedom Funders: ~**$50K business line of credit and/or business credit card, no financials, app-only**, contact jmorrow@enterprisebank.com. VERIFY the actual program (limit, doc requirements, soft vs hard pull, PG, who can apply, whether it's a public product or a relationship-banker channel).
- **LFCU = Langley Federal Credit Union** (VA; open membership; known in credit-stacking circles for soft pulls / high limits). Confirm business-card terms + CA joinability.

**Build the discovery engine (do this):**
1. **Mine the funding community, not a bank directory.** Search and read: myFICO **Business Credit** board, **Doctor of Credit** (esp. "which business cards report to personal credit" + soft-pull lists), **CreditBoards**, **Reddit** (r/CreditCards, r/smallbusiness, r/Entrepreneur), and the credit-funding educators/communities (Credit Veterans, Credit with Colin, Freedom Funders, and similar). Query strings: "$50k no doc business credit card", "no financials business line of credit", "app only business funding", "soft pull business card high limit", "no PG business credit card list", "EIN only business card".
2. **Track the real GOLD signals** (not the structural proxy): soft-pull pre-approval, no financials / stated underwriting, no personal guarantee, high starting limit ($25K–$50K+), EIN-only/no-SSN, reports to business bureaus, currently approving.
3. **Build a "Community-Sourced Gold Leads" tab** — institution, the claim, the source (with link), then VERIFY each against the bank's own materials. Flag unverified third-party "funding plug" claims as such.
4. **Apply the CA-accessibility filter** (§6) to every out-of-state lead.
5. **Re-scan periodically** — these programs change month to month.

**Integrity note:** "No-doc"/"stated" underwriting is legitimate (many issuers approve on personal credit + stated revenue without tax returns). Do NOT advise misrepresenting income, revenue, or business facts on any application. Find lenient *legitimate* underwriting; never facilitate misstatement.

### 9. DELIVERABLE RULES
- Output a versioned **.xlsx + .csv** every time (v5, v6, …); preserve prior versions.
- Keep the column order, color rules, tabs, and scoring above unless the user changes them.
- Don't omit data even if it doesn't fit the goal — keep everything; just make the gold obvious.
- Lead the user's chat reply with the headline finding, then a few bullets, then concrete next options.

### 10. CONDENSED REQUIREMENTS CHECKLIST (the user's standing asks)
SoCal flag right after Type · estimated credit limit + assets + deposits + footprint near front · standardized values, no prose to parse · sortable Rec# + Tier · "How to Apply" method for non-online · CA Access / why-listed column · name colored GOLD/mint by criteria · Type colored · every underwriter its own color · legend/guide for all colors · count = SoCal only · cover all CA >$1B · self-underwritten target 20–50 · verifiable forum links for approval/limit data · VERIFIED/INFERRED/UNKNOWN labels, no fabrication · versioned xlsx+csv · stick to banks with actual CA/SoCal presence or genuine online-national access · pursue community-sourced gold leads (Enterprise Bank, Langley) and build the discovery engine.

---
*Handoff written 2026-05-29. Current state: v4 (162 institutions, 49 self-underwritten). Next: verify Enterprise Bank & Langley, build the Community-Sourced Gold Leads tab, and extend the discovery engine per §8.*




==============================================================================

