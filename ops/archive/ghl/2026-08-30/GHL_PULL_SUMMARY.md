# GHL Full Pull — 2026-08-30 (Lane 4, read-only)

Location `WFkoNzKa9J9PxhngsLfl` (Prismatic). Raw JSON in `raw/`, derived CSVs alongside this file.

| What | Count |
|---|---|
| Contacts | 259 |
| ...with any attribution data | 246 |
| ...with a utm_source | 100 |
| Contacts with appointments | 87 |
| Appointment events | 144 |
| Appointment statuses | {'confirmed': 109, 'cancelled': 25, 'noshow': 8, 'showed': 2} |
| Opportunities | 200 ({'open': 199, 'won': 1}) |
| Conversations | 256 |
| Messages | 8218 |
| Payment orders / transactions / subscriptions / invoices | 0 / 0 / 0 / 0 — GHL Payments is EMPTY; money moves outside GHL |

Statuses come from GHL `appointmentStatus` per event (confirmed / showed / noshow / cancelled / invalid).

## Verdicts on the briefed questions

- **Roster audit's 79 Unknown shows:** GHL terminal statuses resolve **16** (10 cancelled, 6 noshow) — see `ROSTER_RECONCILIATION.md`. The other 63 sit at `confirmed` in GHL (never updated after the call) or have no matching appointment: GHL was not maintained as a show/no-show ledger, so it cannot resolve them.
- **Payments — Nick S. $500:** NOT found. GHL Payments (orders/transactions/subscriptions/invoices) is empty for the whole location; Nick's opportunity is open/$0. Verify at the processor or bank.
- **Payments — Jill installments:** NOT found as payments. However a "Jill" opportunity in The Automated Appointment Funnel is **status won, $15,000** (updated 7/23) — the deal record exists, the cash trail does not live in GHL.
- **Payments — Michael M.:** NONE found (opportunity open/$0) — matches expectation; nothing to flag.
- **UTM coverage:** 246/259 contacts carry attribution data; **100/259 have a utm_source**; campaign_id/adset_id/ad_id parsed from attribution URLs where present (`contacts_2026-08-30.csv`).
- **Speed-to-lead:** computed per contact from creation → first outbound message/call (`speed_to_lead_2026-08-30.csv`).
- **Todd import (Task 2):** executed on existing contact `nIy2smghNYT9II3enmQv` — see `ops/lane4/PROCESS_LOG_2026-08-30.md`.
