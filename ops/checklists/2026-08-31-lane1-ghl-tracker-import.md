# LANE-SYNC — CHANGE ORDER FOR LANE 1: import ALL GHL contacts into the Notion tracker (Alan-ordered 8/31)

> 🗣️ Alan, 8/31 (verbatim, [stored ↗](../prompts/2026-08-31-data-correction-demands.md)):
> *"everyone that's in GHL, put it into the automated tracker. Why is that not already there?
> It's messing up our data."*

## The gap, exactly
- GHL holds **259 contacts** (Lane 4 pull, 8/30). The Notion tracker holds **104 rows**.
- **154 GHL contacts are NOT in the tracker** — full payload with every field needed to create
  the rows: [`ops/data/ghl_tracker_import_2026-08-31.csv`](../data/ghl_tracker_import_2026-08-31.csv)
  (name · GHL contactId · clickable GHL link · dateAdded · source · tags · appointment count ·
  email/phone present).
- **8 of the missing 154 have GHL appointments** — booked people invisible to the tracker.
  They are sorted to the top of the CSV by recency.

## Why it wasn't already there (honest answer, not an excuse)
The tracker was built from the audited funnel (83 rows) + the 21 leads imported 8/30 — the
roster audit imported only contacts that matched funnel activity, not the whole book. A
full-book import was never ordered until now; meanwhile the board bridged the gap with the
"+ Raw GHL book" toggle (dashboard-side only, which is why Alan sees the data mismatch).

## What Lane 1 executes (you own Notion writes)
1. Create one tracker row per CSV line: Name (GHL casing), Created = GHL `dateAdded` (true
   arrival, NOT import date), Entry Path from `source` ("Application…" → Opt-In Form;
   "Upload"/empty → Untagged-Import), GHL contactId in the record, Stage = New Lead unless
   `appointments > 0` (→ Booked Call).
2. Tag every imported row (e.g. `ghl-import-8/31`) so audited vs imported stays queryable.
3. Post a LANE-SYNC line when done — the board's live layer picks the new rows up on its
   ~10-min refresh automatically; Lane 2 then re-verifies counts (tracker should read 258±,
   and the board's "Tracked funnel" chip converges with the Raw GHL book).
4. Dupes/junk (secondary phones, test rows like "Njjnn Of"): import them anyway, tagged
   `dupe-candidate` where obvious — Alan rules on deletions; nothing is silently dropped.

*Until this lands, the board's Raw-GHL-book default (v8.7+) is the stopgap that keeps all 259
visible. — Lane 2, 8/31*
