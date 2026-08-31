# 📋 CHANGE ORDER → LANE 2 — three-way ad toggle (SCIO 1 · SCIO 2 · CCA)
*Issued 2026-08-31 by Lane 1. Source: Alan verbatim — "please also CLEARLY keep it separate and toggleable in the dashboard between SCIO campaign 1 and 2 (medical and professionals) - SEPARATE from CCA ad set campaign - ad set photo ads STR - keyword FUNDS" + **"do it in a way that does NOT break anything"**. Lane 2 owns `ops/dashboard/` (single-writer law) — Lane 1 does not touch the board. Data source of truth for this build: [AD_ACCOUNTS_MAP.md](../data/AD_ACCOUNTS_MAP.md).*

## THE ASK, in one line
The board must let Alan switch between **three separate ad lenses that never blend**: SCIO 1 (Medical) · SCIO 2 (Professionals) · **CCA** (a different ad account entirely).

## NON-NEGOTIABLE: "does NOT break anything"
1. **Additive only.** The default view on load stays EXACTLY what it is today (all-SCIO). A viewer who never touches the toggle sees no change.
2. **No renames, no removals** of existing IDs, classes, data keys, or facets. New keys only.
3. **Pull trunk before publishing** (the SNAP/lead-count-104 regression has happened three times — see LANE-SYNC 8/31).
4. **Publish to the canonical artifact URL only** (`c6ad801c-…`); the duplicate `ba359183-…` stays frozen.
5. If a data field the toggle needs does not exist yet, render the toggle with an explicit **"no data yet"** state — never a zero that reads as a real number.

## THE THREE LENSES — exact identifiers [V, pulled live 8/31]
| Toggle label | Ad account | Campaign ID | Campaign name | Status |
|---|---|---|---|---|
| **SCIO 1 — Medical** | 1821085838595242 | `120251505168550556` | SCIO \| Application \| Medical \| New Videos Relaunch - v2 | 🟢 ACTIVE |
| **SCIO 2 — Professionals** | 1821085838595242 | `120251505193800556` | SCIO \| Application \| Professionals/Biz Owners \| Images - relaunch | ⏸ PAUSED |
| **CCA** | **1299632422083575** | `120246420588070292` | `STR` → ad set `FUNDS - STR 2 - Copy - 740+ Credit Scores` (`120246420588240292`) | 🟢 ACTIVE |

## BUILD SPEC
1. **Toggle control** — a 4-position segmented control at the top of the ads section: `All · SCIO 1 Medical · SCIO 2 Professionals · CCA`. Default = `All` (today's behaviour). Selection persists per viewer via localStorage (wrap reads/writes in try/catch; render correctly with no stored value).
2. **Visual separation** — CCA gets its own colour token and an **"different ad account"** badge in its panel header. It must be impossible to mistake a CCA number for a SCIO number at a glance.
3. **What each lens shows** — spend · impressions · clicks · CTR · CPC, plus the ad-level table for the selected lens (ad name, spend, impressions, clicks). CCA's ad table = the five FUNDS photo ads listed in the map file.
4. **Attribution honesty banner on the CCA lens (required):** *"CCA runs an engagement/DM objective — its leads do NOT flow into the SCIO application funnel, so booking/show/qualified counts on this board exclude CCA."* Without this line the board implies attribution that does not exist.
5. **Funnel counts stay SCIO-only** for now. Do not merge CCA into lead/booking/show/qualified totals — that would silently corrupt every rate on the board.
6. **Paused history** (CCA's `TOF | Broad USA | DM Ads` and `Warm Up`, and the 8 archived SCIO campaigns) belongs behind a collapsed "history" disclosure, not in the live numbers.

## ACCEPTANCE TEST before publishing
- [ ] Load the board with no interaction → identical to the previous version (screenshot-diff the default view).
- [ ] Switch to each of the four positions → numbers change, nothing errors, no blended totals.
- [ ] CCA lens shows the account badge + the attribution banner.
- [ ] Lead/booking/show/qualified counts are unchanged by any toggle position (they are SCIO-funnel counts).
- [ ] Lead count still reads **104**; SNAP intact.
- [ ] Published to `c6ad801c-…`; process-log entry + LANE-SYNC line written.

## REPORT BACK
One line into `ops/process-log/2026-08-31-lane2.md` + a LANE-SYNC row: which board version shipped, the acceptance boxes ticked, and anything in the spec you could not do (say it plainly rather than approximating).
