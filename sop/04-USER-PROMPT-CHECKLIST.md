# 📋 USER PROMPT CHECKLIST

> **Sub-SOP of the [Universal Prime SOP](../UNIVERSAL-PRIME-SOP.md).** The intake and comprehension gate — Stage 1.

**Purpose:** To make it structurally impossible to start work on a misunderstood prompt, and impossible to finish while an item is silently unaddressed.

**Owned by:** 🎯 Clarity Agent · closed out by 🧵 Coherence Agent

---

## 1. INTAKE (before any work)

| # | Step | Required |
| :-: | :--- | :------- |
| 1 | **Store the prompt verbatim** in a named, backed-up file | 🌱 |
| 2 | **Decompose** the prompt into discrete, numbered, individually-verifiable asks | 🌱 |
| 3 | **Separate** explicit asks from inferred/implied ones — label which is which | 🌱 |
| 4 | **Flag ambiguities** 🛑 — anything with more than one reasonable reading | 🌱 |
| 5 | **Relay the numbered checklist back** to the user | 🌱 |
| 6 | **STOP — await human confirmation** 💻 | **BLOCKING** |

> **Step 6 is a hard gate.** No research, no drafting, no building until confirmed. This gate exists specifically to eliminate the "user has to repeat the same prompt multiple times" failure.

---

## 2. THE RELAY FORMAT

```
UNDERSTANDING CHECKLIST — awaiting your confirmation 💻

You are asking me to:
  1. [explicit ask, restated precisely]
  2. [explicit ask]
  3. [explicit ask]

I have inferred (confirm or correct):
  4. [inferred ask]

Ambiguities I need resolved 🛑:
  A. [item] — could mean X or Y. Which?

Out of scope unless you say otherwise:
  — [thing deliberately excluded]

Confirm, adjust, or add before I begin.
```

---

## 3. LIVE TRACKING (during work)

Each numbered item carries a live status throughout:

| Status | Meaning |
| :----: | :------ |
| 🌱 | Fulfilled and verified |
| 🟠 | In progress |
| ⬜ | Not started |
| 🛑 | Blocked or at risk — reason stated |
| 🐞 | Attempted, problem encountered |
| 💻 | Needs user input to proceed |

Any item not 🌱 carries a **why** next to it. A bare status without a reason is incomplete.

---

## 4. CLOSEOUT (end of every output)

The 🧵 Coherence Agent reports the same numbered checklist back with final status:

```
CONCLUSION CHECKLIST

  1. [ask] ................ 🌱 Done — [proof / where]
  2. [ask] ................ 🌱 Done — [proof / where]
  3. [ask] ................ 🟠 Partial — [what remains + why]
  4. [ask] ................ 💻 Blocked — [what's needed from you]

REMAINING:  [explicit list of what still needs doing]
```

**Nothing is closed silently.** An item that turned out to be unnecessary is marked and explained, never dropped.

---

## 5. STANDING ITEMS (checked every time, on every prompt)

These are permanent requirements that apply regardless of what was asked:

- [ ] Original prompt stored verbatim 🌱
- [ ] Sources carry verbatim quotes + verifiable links
- [ ] Every output/sub-output labeled with its source
- [ ] Tokens reserved for proactive troubleshooting
- [ ] **Token & time report included** ← historically the most-dropped
- [ ] Debrief + summary table + icon guide at top
- [ ] "Where we are in the process" marker present
- [ ] Deliverables materialized as named, located, linked documents
- [ ] Prior versions backed up and labeled before any overwrite
- [ ] Conclusion checklist present
- [ ] Improvement pass run and logged

> If a standing item is missed, it is a **systemic error** — root-caused and fixed per the [Operations SOP](03-OPERATIONS-SOP.md) failure log, not merely apologized for.
