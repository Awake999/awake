# Bottleneck root causes and the permanent fix (Lane 4, 8/31)
*Alan's 4-step order: identify the mistakes, understand why, express why, solve sustainably.*

## The five mistakes, each with its why

| # | Mistake | Root cause (why it happened) | Permanent fix |
|---|---|---|---|
| 1 | Revenue blended across periods (Ed's July $2K shown against August; Jill's July deal too; Matthew's payment missing entirely) | Dollar figures were HAND-TYPED into surfaces from call summaries and register lines. The payments system of record (Whop) was never wired in; GHL payments is empty; so summaries stood in for raw money data - the exact failure the raw-originals law exists to prevent | CANON law (below) + Whop wiring (Task 8). Until Whop is connected, money cells show "pending Whop" - never an estimate |
| 2 | Design lane blank on triage/dispositions | The board waited for MANUAL Notion tags (prospective from Sep 1) while the proof already sat in raw GHL messages. Nobody derived; everyone waited | derive_triage.py now runs with every pull: 246 touched / 156 engaged / 87 pre-slot, per-contact CSV, labeled DERIVED. Lane 1 backfills Notion from it |
| 3 | Publish races - lanes wiping each other's board sections | Multiple writers to one artifact with no protocol; sections lived only in the publisher's file | GHLBOOK-style markers + single-publisher rule + content converged into every lane's branch (already holding across 5 republishes) |
| 4 | Teramind / Whop stalls repeated for days | Machine-bound auth treated as a side quest; no owner, no visible status - a silent blocker | BLOCKERS ledger in CANON_NUMBERS (data source -> auth status -> owner) surfaced on the board, so a missing credential is a red cell, not a silence |
| 5 | Auth evaporating (Chrome restart killed the Teramind session mid-task) | Session-cookie access is ephemeral; the durable pattern (creds in local .env, like the GHL PIT) was recommended but not completed | Store read-only creds in apw-intel/.env for every machine-bound system; browser sessions are for one-off UI work only |

## The one sentence underneath all five
**Every bottleneck traces to a figure or capability whose provenance was human memory instead of a machine-readable source** - hand-typed numbers, summaries standing in for raw, credentials living in one person's head or one browser tab.

## THE CANON LAW (proposed for SOP; Lane 1 to ratify)
1. Every number on any surface (board, register, report) must be traceable to CANON_NUMBERS.json or a raw file in ops/archive/** - no hand-typed figures, ever.
2. CANON_NUMBERS.json is generated ONLY by pull scripts from raw API responses; hand-editing it is prohibited.
3. Every value carries one of three labels: VERIFIED (raw system data) / DERIVED (computed, method stated) / PENDING (source not wired - shown as pending, never estimated).
4. Every dollar carries a period label (month + quarter). Blended lifetime figures are prohibited on period-labeled surfaces.
5. The BLOCKERS ledger (source, auth status, owner, since-when) lives in canon and renders on the board.
