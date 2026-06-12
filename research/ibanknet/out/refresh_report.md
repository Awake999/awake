# iBankNet California Roster — Refresh Report

- **Refresh attempt date:** 2026-06-12 (UTC), ~06:35–06:45
- **Outcome:** ibanknet.com was **completely unreachable** during this refresh (every endpoint, every retry). The authoritative roster was therefore rebuilt from the verified **2026-06-10 cached sweep** (451 rows, all list types), with assets/deposits gaps filled from `v7/out/assets_fill.csv` (FDIC/NCUA figures pulled 2026-06-11). **No list was dropped; no row was dropped.**
- **Outputs:**
  - `/home/user/awake/research/ibanknet/out/roster_ranked.csv` (451 rows, ranked by Deposits DESC)
  - `/home/user/awake/research/ibanknet/out/refresh_report.md` (this file)

## 1. Live-pull attempt log (every URL + HTTP status)

All requests used `curl -L` with a real browser User-Agent (Chrome 125 on Windows / Chrome 124 on macOS variants) and full Accept/Accept-Language headers. Every ibanknet request returned **HTTP 503** with the body:

```
upstream connect error or disconnect/reset before headers. reset reason: connection timeout
```

This is an edge/proxy (Envoy-style) error meaning the ibanknet **origin server did not respond at all** — the site is down (or hard-blocking this egress) at the TCP/connect level, not a markup change and not a bot-block page. Control fetches in the same minutes succeeded (google.com HTTP 200, api.fdic.gov HTTP 200), so outbound connectivity was healthy.

| # | URL | Status |
|---|-----|--------|
| 1 | https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=statebank&state=06 | 503 (x5 attempts: 06:37, 06:38, 06:39 x3) |
| 2 | https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=statecreditunion&state=06 | 503 |
| 3 | https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=statethrift&state=06 | 503 |
| 4 | https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=stateallfi&state=06 | 503 (retried again at 06:42 — still 503) |
| 5 | https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=sodstatebanks&state=06 | 503 |
| 6 | https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=ilc&state=06 | 503 |
| 7 | https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=ndtrust&state=06 | 503 |
| 8 | https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=fbo&state=06 | 503 |
| 9 | https://www.ibanknet.com/ (site root) | 503 |
| 10 | http://www.ibanknet.com/ (plain HTTP) | 503 |
| 11 | https://ibanknet.com/ (apex, no www) | 503 |
| 12 | https://www.ibanknet.com/scripts/callreports/bankmap.aspx (list-rediscovery page) | 503 |
| 13 | https://www.ibanknet.com/scripts/callreports/getbanklist.aspx?type=statebank&state=06 (legacy pre-migration URL) | 503 |
| 14 | WebFetch (independent fetch infrastructure) on URL #1 | 503 |

Conclusion: total origin outage. Per the fallback rule, **every list type** falls back to the cached 2026-06-10 sweep, and every roster row is marked `Source = cache 2026-06-10`.

## 2. Sources used

| Source | Path | Role |
|--------|------|------|
| Cached ibanknet sweep (2026-06-10, site was UP and fully server-rendered) | `/home/user/awake/research/v6/out/ibanknet_ca_institutions.csv` | All 451 institutions: name, city, type, assets, deposits, ibanknet detail URL |
| Assets/deposits gap-fill (FDIC API figures as of 2026-03-31, pulled 2026-06-11) | `/home/user/awake/research/v7/out/assets_fill.csv` (Sheet=`ibanknet`, 87 rows) | Total consolidated assets + HQ city/state for the 58 SOD rows; documented N/A status for the 29 FBO deposit blanks |

Fill-file match check: the 58 SOD fill rows and 29 FBO fill rows matched the cache **1:1 by exact name — zero unmatched on either side**.

## 3. Per-list counts vs the 2026-06-10 sweep

The 6/10 sweep pattern was 113 / 242 / 9 / 58 / 29 / 3 / 3. The 113 "banks" include the 6 institutions the sweep re-flagged from the `ilc` and `ndtrust` national lists (113 = 107 plain banks + 3 ILC + 3 NDT). Reproduced exactly:

| List (fiList type) | 6/10 sweep | This roster | Δ |
|---|---|---|---|
| statebank / stateallfi banks | 113 | 113 (107 Bank + 3 ILC + 3 NDT) | 0 |
| statecreditunion | 242 | 242 | 0 |
| statethrift (federal savings banks) | 9 | 9 | 0 |
| sodstatebanks (out-of-state banks w/ CA branches) | 58 | 58 | 0 |
| fbo (CA offices, USB/UFB/USA: 19/8/2) | 29 | 29 | 0 |
| ilc (subset of bank count above) | 3 | 3 | 0 |
| ndtrust (subset of bank count above) | 3 | 3 | 0 |
| **Total unique institutions** | **451** | **451** | **0** |

## 4. Reconciliation (adds / drops / renames)

- **Adds vs cache: 0. Drops vs cache: 0. Renames: 0.** Because the live site never answered, no live-vs-cache delta is observable today; the roster is byte-for-byte the cached population (add-only policy trivially satisfied — nothing flagged `dropped-from-live` because no live list loaded to compare against).
- `In_prior_sweep = Y` for all 451 rows.
- **Caveat for screeners:** any institution chartered/listed by ibanknet between 2026-06-10 and today would be missing; two days of churn is near-zero risk, but a live re-pull should be re-attempted when ibanknet recovers. Known staleness already flagged in-row: Comerica Bank (charter inactive 2026-02-01, merged into Fifth Third) and Pacific Premier Bank, N.A. (inactive 2025-09-01, merged into Columbia Bank) still appear on ibanknet's SOD list and are retained with merger notes.
- Apparent duplicate verified as legitimate: **POLAM FEDERAL CREDIT UNION** appears twice — Redwood City (ibnid usa_488484) and Los Angeles (ibnid usa_858984) are two distinct same-named federal credit unions. Both rows annotated.

## 5. Assets/deposits gap fills

- **58 SOD rows** had blank Assets in the cache (ibanknet's SOD list shows CA-branch deposits only). Filled with FDIC total consolidated assets (as of 2026-03-31) from `assets_fill.csv`; HQ city/state also taken from the FDIC legal-HQ string there. For these rows **Deposits remain CA-branch deposits (FDIC SOD 2025)** — the correct CA-footprint ranking figure — while Assets are whole-bank. Noted per row.
- **29 FBO rows** have Deposits = N/A — documented in `assets_fill.csv`: FFIEC 002 offices, ibanknet fast-facts publishes office-level assets only and the detailed RAL report sits behind a captcha. These rows are listed in a labeled `[N/A-DEPOSITS BLOCK]` at the bottom of the roster (ranks 423–451), sorted by office assets DESC. **None dropped.**
- 3 SOD rows legitimately report $0 CA branch deposits (The Bank of New York Mellon, LendingClub Bank N.A., BNY Mellon N.A.) — kept at the bottom of the numeric block (ranks 420–422).
- After fills: 0 blank Assets, and the only non-numeric Deposits are the 29 documented FBO N/As.

## 6. Output schema

`roster_ranked.csv`: `Rank, Institution, Type, City, HQ_State, Deposits, Assets, ibanknet_URL, Bank_website, Source, In_prior_sweep, Notes`

- Deposits/Assets in **$ thousands**; CA filers as of 2026-03-31 call/5300 reports (per ibanknet 6/10), SOD deposits per 2025 Summary of Deposits, SOD assets per FDIC 2026-03-31.
- Ranked by Deposits DESC (numeric, rows 1–422), then the N/A-deposits FBO block (423–451) by assets DESC.
- `Bank_website` is **blank for all rows**: it lives on the per-institution ibanknet detail pages, all unreachable today (same 503 outage). The `ibanknet_URL` column gives screeners the exact detail page to pull when the site recovers.
- Every row traceable: ibanknet detail URL + Source tag per row; SOD/FBO fill provenance in Notes points to `assets_fill.csv` (which carries the FDIC API URLs per institution).

## 7. Top 10 by deposits ($K)

| Rank | Institution | Type | Deposits ($K) |
|---|---|---|---|
| 1 | Bank of America, N.A. | SOD (CA branch deposits) | 422,113,884 |
| 2 | Wells Fargo Bank, N.A. | SOD | 299,560,094 |
| 3 | JPMorgan Chase Bank, N.A. | SOD | 287,153,152 |
| 4 | U.S. Bank N.A. | SOD | 114,337,732 |
| 5 | CITY NATIONAL BANK (Los Angeles) | Bank | 81,067,113 |
| 6 | Citibank, N.A. | SOD | 72,004,000 |
| 7 | EAST WEST BANK (Pasadena) | Bank | 69,086,073 |
| 8 | First-Citizens Bank & Trust Company | SOD | 49,197,599 |
| 9 | BMO Bank National Association | SOD | 35,458,327 |
| 10 | SCHOOLSFIRST FEDERAL CREDIT UNION (Santa Ana) | Credit Union | 31,586,618 |
