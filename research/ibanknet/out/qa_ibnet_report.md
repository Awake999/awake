# QA Audit — iBankNet_CA_Deposits_v1.xlsx (+ CSV mirror)

**Auditor:** QA-IBNET (adversarial verifier; did not build the deliverable)
**Date:** 2026-06-12
**Deliverables audited:**
- `/home/user/awake/research/ibanknet/deliverables/iBankNet_CA_Deposits_v1.xlsx`
- `/home/user/awake/research/ibanknet/deliverables/iBankNet_CA_Deposits_v1.csv`

**Verdict: PASS-WITH-ISSUES** (0 CRITICAL, 0 MAJOR, 5 MINOR)

---

## Check 1 — COMPLETENESS (user's #1 demand): PASS

- Tab 1 contains exactly **451 data rows** (ranks 1–451, no gaps, all ranks stored as
  integers), matching `out/roster_ranked.csv` (451 rows) **1:1 on both rank and
  institution name** — 0 mismatches.
- **Deposits and Assets match the roster exactly** on all 451 rows (0 mismatches each).
- **Rank order = deposits DESC, verified monotonic** on the numeric Deposits column for
  ranks 1–422: 0 violations.
- **FBO block (ranks 423–451, 29 rows)** sits after rank 422 behind a clearly labeled
  separator row (xlsx row 424: "[N/A-DEPOSITS — FBO OFFICES] … sorted by office
  assets"). All 29 FBO Deposits cells = "N/A"; block verified **monotonic DESC on
  Assets**: 0 violations.
- **Duplicates:** only `POLAM FEDERAL CREDIT UNION` appears twice — the two legitimate
  POLAM institutions. No other duplicate names.

## Check 2 — JOIN FIDELITY (20 rows: 8 named + 12 random, seed 42): PASS

Named: Sunflower, Mission Federal, Community West, Kinecta, AltaOne, Amalgamated,
First Entertainment, Valley First. Random: Escondido FCU, Stanford FCU, Axos Bank,
United Association CU, Safe 1 CU, American First CU, FFB Bank, Bank of the Sierra,
Inland FCU, SAFE CU, California Adventist FCU, Beacon Business Bank.

All 13 mapped columns per row compared verbatim against `screened_batch_*.csv` /
`verified_batch_*.csv`. **Zero substantive discrepancies; no invented data.** Every
diff found is a documented, lossless normalization:
- Blank source cells → "—" placeholder (cosmetic).
- Underwriter labels normalized: "Elan Financial Services"→"Elan",
  "TIB, National Association"→"TIB" (matches legend row 19's declared value set).
- Source "UNKNOWN"/"N/M" underwriter on NO-card rows → "—", with the raw value
  preserved verbatim as "[raw: UNKNOWN]"/"[raw: N/M]" inside the UW evidence cell.
- ⭐ prefix added on accent cells; underlying text otherwise verbatim.
- Contradiction notes carried: Live-check note = `Agreement_vs_prior` verbatim on all
  sampled verified rows (e.g., Mission Federal twin-fix, Kinecta terms change).

## Check 3 — COLUMN SPEC: PASS

- **24 columns, exact header:** Rank, Institution, Type, City, Website, Deposits,
  Assets, Biz card?, Card link, 0% intro, Terms, Underwriter, UW evidence, Apply,
  Apply link, Bureau (quick), No-doc (quick), ChexSystems, EWS,
  LexisNexis/SageStream, Other secondary, Live-check note, Sources, Screen date.
- **Underwriter (+UW evidence) sits immediately after the card block** (Biz card? /
  Card link / 0% intro / Terms) and before Apply — per spec.
- **4 separate secondary-verification columns** present and populated on all 451 rows
  (0 blanks). Cross-checked against `out/secondary_bureaus.csv` via exact names plus
  Tab 3's `Roster_match` mapping column: **205 alias-mapped institutions ×4 cells = 0
  mismatches** (e.g., sb "California Bank & Trust" charter-wide data correctly carried
  onto Tab 1's Zions Bancorporation row; "Chase (JPMorgan Chase)", "U.S. Bank
  (direct)", "Citi (Citibank)" aliases all correct). All institutions without a
  secondary-bureau source read **UNKNOWN** — no fabricated coverage found.

## Check 4 — COLOR / LEGEND: PASS (verified on ALL 451 rows, exceeding the 15-row sample)

Fill distribution on Institution col: GREEN (C6EFCE) ×70, ORANGE-RED (F4B084) ×69,
AMBER (FFE699) ×31, no-fill ×281.
- GREEN only on Biz card YES + Underwriter SELF: **0 violations** (70/70).
- ORANGE-RED only on YES + named third party (Elan 45, TCM 13, TIB 10, FNBO 2, UMB 1,
  ServisFirst 1; 3 of these are UNCLEAR rows → amber, accounting for 72 vs 69):
  **0 violations**.
- AMBER only on YES+UNKNOWN-UW and UNCLEAR rows: **0 violations**.
- NO fill on all 281 NO rows: **0 violations**.
- **⭐/gold accents:** 65 total (0% intro ×39, Terms ×15, No-doc ×11); star character
  and gold fill (FFD966) agree in all 65 cells. 15 sampled accents all trace to source
  language: 0% intro offers (WF 0%/12mo, BMO 0%/18mo, Chase Ink, Preferred Bank, Elan
  twins), $20K+ limits (Bay Fed $50K, Patelco $40K, Altura/Sacramento $25K), and
  no-doc/flex language (SLO CU "manual/relationship underwriting… possible flex on
  docs"). **0 unjustified stars.**
- Legend tab colors (rows 7–11) match the actual fills used, byte-for-byte on ARGB.

## Check 5 — LINKS: PASS (8/8 clicked; 0 dead)

Real hyperlink objects: Tab 1 = 826, Tab 3 = 154, Tab 4 = 101 (Tab 0 = 0, Tab 2 = 0 —
see MINOR-1). URL-bearing text cells: Tab 1 = 1,160.

| # | Link | Type | Result |
|---|------|------|--------|
| 1 | creditcardlearnmore.com/11t3 (Westamerica) | Elan portal | **ALIVE** — Elan-powered page, 3 business cards shown |
| 2 | mycommunitycc.com/2f497f80fb2c/business (BAC Community) | TCM portal | **ALIVE / JS-limited** — loads "Online Application" shell; content JS-rendered, not bot-readable. Not dead. |
| 3 | cardaccount.net/application/f87a3255c0/business/new (Community West) | TIB portal | **ALIVE** — 2 business cards; on-page disclaimer confirms TIB N.A. is issuer (validates Tab 2 rail correction) |
| 4 | slocu.com/credit-cards/ | small CU | **ALIVE** — "consumer and business credit cards" confirmed |
| 5 | WF Signify Business Cash card page | card link | **ALIVE** — 0% 12 mo, 2%, $500/$5K bonus all confirmed = workbook verbatim |
| 6 | business.bankofamerica.com/en/credit-cards | card link | **ALIVE** — 3 Business Advantage cards, $0 AF, $500/50K bonuses = workbook verbatim |
| 7 | kinecta.org/credit-card/mypro | card link | **ALIVE** — MyPro card live (APR 13.49–18.00% as of 1/1/26) |
| 8 | missionfed.com/business/ | bank site | **ALIVE** — no business credit card on page, consistent with workbook's "NO — no business card program found" |

**Dead links: 0. Bot-blocked: 0. JS-limited: 1 (#2).**

## Check 6 — TAB 2 CORRECTIONS & TAB 4 BEST-OF: PASS

- Tab 2 has 15 correction rows; **15/15 trace verbatim** to the cited
  `verified_batch_N.csv` `Agreement_vs_prior` cell for the named institution (Bank of
  Hope, F&M Long Beach, SMBC Manubank, Mission Federal twin-fix, Kinecta, Westamerica,
  Community West TIB-not-TCM fix, Partners FCU twin-fix, Coast Central, American First
  twin-fix, Redwood Capital, Sunflower UW correction, Legacy Bank, Golden Valley FCU
  twin-fix, First IC Bank acquisition).
- Tab 4 (101 rows): **all 70 SELF+YES institutions from Tab 1 are present — count
  matches exactly (70/70, 0 missing)**. The 31 additional rows are all Biz card YES
  with labeled non-SELF underwriters (Elan 25, TCM 2, FNBO 2, UNKNOWN 2) carrying a
  "Why on list" rationale — a documented superset, not a derivation error.

## Check 7 — CSV MIRROR: PASS

- 452 rows (header + 451 data) × 24 columns; header identical to xlsx (UTF-8 BOM on
  first cell only).
- 25 randomly sampled cells (5 rows × 5 cols, seed 3): **0 diffs**. Post-FBO alignment
  explicitly verified on ranks 425, 430, 451: **0 diffs** across all 24 columns.
- **(URL) pattern confirmed:** 107 cells preserve hyperlink targets as trailing
  "(https://…)" text, e.g. BofA ChexSystems cell ends "(https://www.doctorofcredit.com/banks-c…)".
- The xlsx FBO separator row is intentionally omitted from the CSV (data-only mirror).

---

## Findings

### CRITICAL
None.

### MAJOR
None.

### MINOR
1. **Tab 2 and Tab 0 have no clickable hyperlink objects** — Tab 2's 15 source-link
   cells are plain text URLs (Tabs 1/3/4 have real hyperlinks). Spec says "links
   everywhere"; URLs are present and copyable but not clickable on those two tabs.
2. **Tab 1: 1,160 URL-bearing cells vs 826 hyperlink objects** — cells containing
   multiple URLs (e.g., Sources) can carry only one hyperlink per cell in xlsx;
   secondary URLs survive as text only. Format limitation, no data loss.
3. **Assembly normalization of underwriter labels** ("Elan Financial Services"→"Elan",
   "TIB, National Association"→"TIB", UNKNOWN/N/M→"—" on NO-card rows). Lossless (raw
   values preserved as "[raw: …]" in UW evidence; legend row 19 declares the value
   set) but the cells are not byte-verbatim to source.
4. **CSV mirror omits the FBO separator row** present in xlsx row 424 and carries a
   UTF-8 BOM on the header. Both standard, but a consumer diffing row counts xlsx-body
   (452) vs CSV-body (451) will see a 1-row delta.
5. **Tab 4 is a superset of SELF+YES** (70 SELF + 31 labeled third-party/unknown YES
   rows). Derivation is correct and rationale-tagged, but a reader expecting "Best of
   = SELF only" must filter the Underwriter column.

### Dead links
None (0/8 clicked dead; 1 alive-but-JS-rendered: mycommunitycc.com TCM portal).
