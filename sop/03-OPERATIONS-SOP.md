# ⚙️ OPERATIONS SOP

> **Sub-SOP of the [Universal Prime SOP](../UNIVERSAL-PRIME-SOP.md).** Memory, recall, caching, checkpointing, backups, file naming, and the token/time accounting.

**Purpose:** The mechanics that keep data intact. Every systemic loss — a forgotten requirement, an overwritten master, a compaction that ate the most important part — is an Operations failure. This SOP closes those holes.

---

## 1. PROMPT RECALL & MEMORY

| Rule | Detail |
| :--- | :----- |
| **Verbatim storage** | Every original user prompt is stored **word-for-word** in a named, backed-up file |
| **Standard** | 100% recall and accuracy — verbatim, not paraphrased |
| **Supplementary caches** | Created as needed when recall gets chunky, kept **separate** from the original file |
| **Alignment** | Every cache stays aligned with the intention of the original. A cache never replaces or rewrites the source. |
| **High-value prompts** | Detailed directive prompts are cached verbatim into **[Quality Core Standards](05-QUALITY-CORE-STANDARDS.md)** |

---

## 2. FILE NAMING & LOCATION

Every artifact must be:

- **Clearly named** — specific and verifiable, never "doc", "new file", "v2 final final"
- **Versioned** — version in the name where versions exist
- **Located** — full folder path stated in the output
- **Linked** — a human-verifiable link provided
- **Readable by the user** — not an opaque internal cache the user can't open

> Stating the folder location alone is **not** sufficient. Name + location + link, every time.

---

## 3. CHECKPOINT PROTOCOL

A checkpoint is not just "saving." Every checkpoint must explicitly break down:

| # | Required disclosure |
| :-: | :----------------- |
| 1 | **Which files** are being created or updated |
| 2 | **Why** each one — what it preserves |
| 3 | **File name + location** for each |
| 4 | **Tokens required** for the checkpoint operation itself |
| 5 | **Tokens used afterward** — what remains |
| 6 | **Backups made** — which prior versions were preserved and under what label |

### Backup rule
**Before overwriting any master, back up and label the previous working version.** Saving over a master without a labeled prior version is a failure, even if the new content is better.

### Headroom rule 🛑
Checkpoint token budgets must include the backup cost. **Do not cut it close.** The final portion of a process carries the most integrity-critical data — running out of headroom there loses exactly the data that matters most. Historical safe practice: begin checkpointing with substantial reserve (~100–120K tokens), not at the edge.

---

## 4. TOKEN & TIME ACCOUNTING

Reported on **every** output. No exceptions.

| Component | What's reported |
| :-------- | :-------------- |
| **Tokens spent** | On this output |
| **Tokens reserved** | For proactive troubleshooting (Stage 5) |
| **Tokens remaining** | Current headroom |
| **Checkpoint cost** | When a checkpoint occurs |
| **Time** | Elapsed / estimated where relevant |

> **This is the single most frequently dropped requirement in the system's history.** Its omission is treated as a systemic error requiring a root-cause fix — logged by the 🔧 Updater/Optimizer — not a one-off slip to apologize for and repeat.

---

## 5. SOURCE & OUTPUT LABELING

Every output **and sub-output** carries:

- **Its source** — which document, which prompt, which prior decision
- **Its stage** — where in the process it was produced
- **Its status icon** — per the [Communications SOP](02-COMMUNICATIONS-SOP.md)

Anything without a traceable source is flagged: **"new addition — needs confirmation"** 💻

---

## 6. THE PRIORITY-LAYER + POINTER MODEL

To stay coherent without drowning in detail:

```
PRIME LAYER (this SOP family)
   │  Priority details that CANNOT be missed.
   │  100% accuracy, always loaded.
   │
   ├──► macro pointer ──► heavy detail cache ──► deeper sub-caches
   ├──► macro pointer ──► heavy detail cache
   └──► macro pointer ──► heavy detail cache
```

The prime layer holds the can't-miss essentials plus **pointers** to the heavy material. Operational coherence is maintained *before* diving into deep work — so granular expansion never costs the thread.

---

## 7. FAILURE LOG

When a systemic error occurs (a dropped requirement, a lost file, a token overrun), Operations records:

| Field | |
| :---- | :-- |
| **What** | The failure |
| **Which agent** | Should have caught it |
| **Why** | It wasn't caught |
| **Fix** | The effective, physical change made |
| **Test** | Proof the fix actually works |
| **Timestamp** | When |

Identifying the cause is not enough. The fix must be **materialized into a referenceable document** and **tested**.
