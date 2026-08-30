# FOR LANE 1 — drop-in amendment for ops/SOP.md (proposed Law 9: NAVIGATION/UI LAW)

> 🧭 [Start Here](../START-HERE.md) · [Archive home](../README.md) · Source standard: [SOP-formatting.md](../SOP-formatting.md)

**From Alan, verbatim (2026-08-30, to Archive Lane):**
> "make sure all lanes are like this, as well as future lanes. current, continued, and future."
> "Lane 1 original is working on a SOP for all lanes, so find that, and add this into that where appropriate without breaking things for current, past and future uses across all lanes"
> "this organizational thing UI friendly is good, we need it for all other lanes now, and future standard"

**Why this file exists instead of a direct edit:** `ops/SOP.md` is single-writer (Lane 1, per SOP §2/§3). Lane 3 does not edit it; this file is the exact text to fold in, written to ADD without changing any existing law, section number, or ritual step. Nothing below conflicts with Laws 0–8, §1.9, §1b, §1c, §2, §3, §4, or §5.

---

## A. Add to §1 as Law 9 (verbatim drop-in)

9. **NAVIGATION/UI LAW** — *"Everything should be a hyperlink… beginner-friendly… a landing page… every navigation leads into another category, which leads into a subcategory, which all have clickable links that are able to go backwards and forwards."* Every lane's file tree is a navigable UI, not a folder dump: (a) a **START-HERE landing page** per major surface explaining what it is, how it's housed, how to navigate (archive's front door: `ops/archive/START-HERE.md`; repo-wide front door stays `ops/INDEX.md`); (b) **hub pages** per category with links down to every subcategory; (c) a **🧭 breadcrumb line** at the top of every file (Start Here · home · category hub · ⬆ its index) so backwards navigation is always one click; (d) **indexes clickable both ways** — every row links to the archived files here AND the original on the source platform; (e) **no giant text blocks** — transcripts/long docs get headers, 10-minute chapters, clickable TOCs, and oversize files split into linked parts. Full spec + committed idempotent tools: `ops/archive/SOP-formatting.md` (tools in `ops/archive/tools/`: `format_transcripts.py`, `add_breadcrumbs.py`, `transcribe.py`). Applies to every current, continued, and FUTURE lane; new lanes inherit via root CLAUDE.md.

## B. Add one step to §3's ritual (between current steps 4 and 5, or as step 4b)

4b. Before pushing, run the navigation pass over any surface you touched: `python3 ops/archive/tools/add_breadcrumbs.py` and (for transcripts) `python3 ops/archive/tools/format_transcripts.py` — both idempotent, safe on the whole repo. New files must not land without a 🧭 breadcrumb and an index row linking to them.

## C. Add one line to root CLAUDE.md (so future lanes auto-inherit)

> NAVIGATION/UI LAW (SOP §1.9 / Law 9): every file you create gets a 🧭 breadcrumb, an index row (clickable both ways), and chapters/TOC if long — see ops/archive/SOP-formatting.md; run ops/archive/tools/add_breadcrumbs.py + format_transcripts.py before every push.

## D. Register housekeeping (Lane 1's call)

- Register this ask as its own item (Alan's verbatim above) and mark item 54's navigation build ✅ for the archive surface (landing page, hubs, both-ways indexes, breadcrumbs ×193 files, 1097/1097 link check, tools committed).
- Suggested LANE-SYNC line: `LANE-SYNC 8/30: NAVIGATION/UI LAW adopted (SOP Law 9) — all lanes: breadcrumbs + both-ways clickable indexes + no giant text blocks; tools in ops/archive/tools/; spec ops/archive/SOP-formatting.md.`

## E. What must NOT change (breakage guards)

- Tool paths stay `ops/archive/tools/` — 193+ existing breadcrumbs and both SOPs link there; moving them breaks past uses. If Lane 1 prefers `ops/tools/`, add copies/symlinks, never move.
- Raw originals (`*-raw.*`) stay exempt from ALL formatting (SOP-formatting Law 5 / repo VERBATIM + RAW-ORIGINALS laws).
- Existing anchors/filenames in `ops/archive/**` are load-bearing (TOCs, indexes, cross-refs) — append-only stands.
