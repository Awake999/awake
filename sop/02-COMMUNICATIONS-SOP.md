# 💬 COMMUNICATIONS SOP

> **Sub-SOP of the [Universal Prime SOP](../UNIVERSAL-PRIME-SOP.md).** How every output is structured, labeled, and made scannable.

**Purpose:** Large outputs are unreadable without structure. This SOP guarantees that any output — no matter how big or how granular — can be understood at a glance, and that the reader always knows where they are in the total process.

---

## 1. THE ICON GUIDE (printed on every major output)

| Icon | Meaning |
| :--: | :------ |
| 🌱 | **Done / healthy** — completed and verified |
| 🟠 | **Work in progress / pending** — started, not finished |
| 🛑 | **Caution** — potential risk, dependency, or thing to watch |
| 🐞 | **Problem / bug** — a defect requiring attention |
| ❗ | **Serious / critical** — reserved for high-severity only |
| 💻 | **User input needed** — blocked, awaiting human confirmation |
| ⬜ | **Not started** |

### Distinctness rule
No two icons may read as similar at a glance. Specifically:
- 💻 (user input) must never resemble 🛑 (caution)
- 🐞 (bug) is distinct from ❗ (critical) — ❗ is reserved for genuinely serious issues
- 🌱 (healthy/done) is the growth symbol, not a generic check

If a new status is ever added, it gets a visually distinct symbol **and** this guide is updated in the same breath.

---

## 2. OUTPUT STRUCTURE (mandatory)

### Every output OPENS with:

**① Debrief** — 1–2 sentences, plain language. What this output is.

**② Summary table with icons** — scannable status of the parts.

**③ "Where we are" marker** — position in the total process:
```
WHERE WE ARE:  Stage 4 of 7 — Validation
  DONE:        Clarity ✅ · Sources ✅ · Draft ✅
  NOW:         Verifying deliverables against checklist 🟠
  REMAINING:   QA · Documentation · Coherence ⬜
```

### Every output CLOSES with:

**④ Conclusion checklist** — what was done relative to the prompt, what still needs doing, and **why** for anything incomplete.

**⑤ Sources** — verbatim quotes + human-verifiable links.

**⑥ Token & time report** — spent and remaining.

> **The #1 historically-dropped item is ⑥.** It is mandatory. Omitting it is a systemic failure, not a minor oversight.

---

## 3. NEW SOP / NEW DOCUMENT ANNOUNCEMENTS

Whenever a new SOP or significant document is created, it must be **impossible to miss**:

- 📢 **Announced explicitly** in the conversation — clearly labeled as what it is (e.g. "COMMUNICATIONS SOP UPDATE")
- 📄 **Named** — a clear, specific, verifiable file name
- 📍 **Located** — folder path stated
- 🔗 **Linked** — a human-verifiable link the user can actually open
- 💾 **Backed up** — prior version preserved and labeled

A document mentioned only in chat has **not** been delivered.

---

## 4. GRANULARITY PROTECTION

When work gets deep and sub-fractalized, context is the first casualty. Therefore:

- Every output states its **position in the total process** (see ②/③ above)
- Every sub-output is **labeled with its parent** — which deliverable, which stage, which source
- **Visuals accelerate understanding** — use tables, trees, and flow diagrams over walls of prose

---

## 5. LANGUAGE STANDARD

- Write for a **human**, in headlines: what is expected, what the procedure is, why it is that way, what was asked, what the checklist is.
- Lead with the answer. Detail follows.
- Never bury a blocker 💻 or a problem 🐞 inside a paragraph — surface it in the summary table.
- State what's true plainly. If something failed, say so with the evidence. If a step was skipped, say that.

---

## 6. OPTIMIZATION CYCLE LABELING

When entering the improvement loop, label it explicitly:

```
OPTIMIZATION CYCLE — Round [#]
```

Each round: suggestions with reasoning → user confirms / adjusts / rejects each → incorporate → repeat until the user confirms no further improvements → only then advance to the next step.
