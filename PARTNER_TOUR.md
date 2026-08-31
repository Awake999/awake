# 👋 PARTNER TOUR — start here

You've been given access to the private ops repo of **Ascend Prime Wealth** (business funding + credit repair). This is a live, multi-lane AI-ops system: several Claude sessions ("lanes") working the same repo under one written constitution, with self-policing (a supervisor agent that grades the work, and an error agent that root-causes every miss).

⚠️ **Confidentiality:** this repo is PRIVATE and contains real client data — names, phone numbers, credit details, payment records, call transcripts. Do not copy, forward, or publish any of it. Learn from the system, not from the people in it.

---

## 🗺️ The 10-minute tour, in order

| # | Read this | Why it matters |
|---|---|---|
| 1 | [`CLAUDE.md`](CLAUDE.md) | The bootstrap. Auto-loads into every session that opens in this folder. Note the ⛔ pull-first mandate at the top — that exists because a stale local clone once loaded dead law for a full day. |
| 2 | [`ops/SOP.md`](ops/SOP.md) | **The constitution.** Law 0 = never-miss protocol. §1.9 = the interaction protocol every reply is built from. §1.13 = SOP versioning (snapshot before any edit). Read §0 and §1.9 if you read nothing else. |
| 3 | [`ops/RESPONSE_TEMPLATE.md`](ops/RESPONSE_TEMPLATE.md) | The fill-in-the-slots skeleton every user-facing reply must pass. Prevention layer. |
| 4 | [`ops/RULINGS.md`](ops/RULINGS.md) | Every standing ruling, one line each. Exists because stale to-do items survived three list rebuilds after being cancelled. Validated before any action list. |
| 5 | [`ops/REGISTER.md`](ops/REGISTER.md) | **The spine.** Every request ever made, numbered, verbatim, with status + grade + evidence links. Read the last 20 rows to see the system under load. |
| 6 | [`ops/data/FUNNEL_EXPLORER.md`](ops/data/FUNNEL_EXPLORER.md) | The best single artifact: a 30-day paid funnel rebuilt from raw CRM exports, call logs and recordings — every count expands to names, every claim links to proof. |
| 7 | [`ops/data/gradings/`](ops/data/gradings/) | **Where the debugging value is.** Supervisor inspections #1–#3 grade the assistant's own replies and escalate failures. #3 is the honest one: 1 A / 3 B / 8 C / 10 D. |
| 8 | [`ops/PATH_TO_100.md`](ops/PATH_TO_100.md) | The burn-down: what's still open, who owns it, one action each. |

---

## 🏗️ How the system is built

**Lanes (single-writer per surface — this is what stops merge chaos):**
| Lane | Owns | Where |
|---|---|---|
| Lane 1 — Command | SOP, REGISTER, RULINGS, INDEX, Notion ops | cloud session |
| Lane 2 — Dashboard | `ops/dashboard/` (the live board) | cloud session |
| Lane 3 — Archive | `ops/archive/` (append-only) | cloud session |
| Lane 4 — Local | `ops/lane4/`, browser/API tasks, secrets that must stay on one machine | the owner's PC |

Every lane writes its own `ops/process-log/YYYY-MM-DD-<lane>.md`, never another lane's. Cross-lane messages are `LANE-SYNC` lines inside the register.

**The self-policing loop (the interesting part):**
1. **Prevention** — every reply composed from `RESPONSE_TEMPLATE.md`, then a literal heading scan before send.
2. **Inspection** — a supervisor agent grades sent replies against the SOP from the raw transcript. A metric governs health: *5 consecutive A-grades with zero reprompts.* Currently 0/5 and escalated — see inspection #3.
3. **Correction** — an [error-solution agent](ops/agents/ERROR_SOLUTION_AGENT.md) fires on every miss: root-cause from primary sources → design a **mechanical** fix (never "try harder") → implement it as law → file it → the next inspection verifies it held.
4. **Versioning** — [`ops/sop-history/`](ops/sop-history/) holds a read-only snapshot of the SOP before every edit. v1.0 → v1.18 in about 48 hours, each version traceable to the failure that caused it.

---

## 🐛 Three failures worth studying (the system's own bug reports)

1. **The stale-clone bug.** Local sessions kept ignoring laws they'd never seen: `CLAUDE.md` loads once at session start from local disk, so a clone that hadn't pulled bootstrapped a dead constitution. Fix: the ⛔ mandate at the top of `CLAUDE.md` — pull, re-read, and print the SOP version in the first reply, or don't work. (register #109)
2. **The compaction bug.** When the assistant's context was summarized mid-session, template compliance silently vanished for 4.5 hours — the first freehand reply became the pattern and nothing restored it. Ten D-grades. Fix: SOP §8h — a compaction boundary is treated exactly like a fresh session start, template re-read **from disk**. (inspection #3 → register #122)
3. **The duplicate-delivery false alarm.** An apparent user reprompt was filed as a severity-1 failure; the error agent proved from event UUIDs that the platform had re-delivered the *same* message. Fix: adjudicate apparent reprompts against the transcript before filing severity. (register #108c) — a good example of the loop refuting its own first hypothesis.

---

## 📐 The rules that produce the output style

- **Verbatim first** — every request is quoted word-for-word and turned into a numbered checklist *inside the reply* before any work starts.
- **Evidence law** — no claim ships without a clickable link to its primary source; no count ships without its names.
- **Raw beside summary** — originals are never replaced by summaries.
- **Verified / derived / unknown** — labelled, never guessed.
- **The reply IS the deliverable** — writing it to a file and linking it doesn't count as answering.
- **House vocabulary** — reports use the team's own words (speed to lead, direct to booking, connected, triaged, unresponsive), never invented jargon.

---

## ❓ Questions worth asking after you've read it
- Where would this break at 10× the volume?
- The supervisor grades the same system it belongs to — where's the blind spot?
- Which of these laws are genuinely mechanical, and which still depend on the model remembering?

Welcome aboard — poke holes in it. The failure log is the point.
