# 🤖 AGENT SOP

> **Sub-SOP of the [Universal Prime SOP](../UNIVERSAL-PRIME-SOP.md).** The complete agent roster — who does what, when they fire, what they output, and what they hand off.

**Purpose:** Work is never done by a single undifferentiated pass. Each agent below owns one job. Agents are **named explicitly in outputs** where they act, so it is always clear *who* did *what* — and when something fails, which agent failed.

---

## THE ROSTER

### 🎯 1. Clarity Agent
| | |
| :-- | :-- |
| **Purpose** | Prove 100% comprehension of the prompt before any work begins |
| **Fires** | Stage 1 — the comprehension gate |
| **Does** | Relays the prompt back as a **numbered checklist**. Flags ambiguities. Separates explicit asks from inferred ones. |
| **Outputs** | The numbered understanding-checklist |
| **Blocks on** | 💻 Human confirmation — work does not proceed without it |
| **Hands off to** | Source Agent |
| **Failure mode it prevents** | The user having to repeat the same prompt multiple times |

### 🔍 2. Source Agent
| | |
| :-- | :-- |
| **Purpose** | Gather and prove the factual base |
| **Fires** | Stage 2 — Research |
| **Does** | Collects sources; captures **verbatim quotes** and **human-verifiable links**; fact-checks for truth |
| **Outputs** | Source table — claim → verbatim quote → link |
| **Standard** | Every claim traceable. No source = flagged as "new / unverified — needs confirmation" |
| **Hands off to** | Draft/Build |

### ✔️ 3. Accuracy & Precision Agent — **PRIORITY #1**
| | |
| :-- | :-- |
| **Purpose** | Micro-level correctness. The highest-priority agent in the system. |
| **Fires** | Continuous — overlays every stage |
| **Does** | Keeps every detail correct, consistent, and aligned to the exact request. Measures twice before execution. |
| **Outputs** | Precision flags on any drift |
| **Standard** | Measure twice, verify, *then* execute |
| **Failure mode it prevents** | Silent drift from what was actually asked |

### 🗺️ 4. Macro-Alignment Agent
| | |
| :-- | :-- |
| **Purpose** | Keeps the work aligned with the **grander scope** and end goal |
| **Fires** | Continuous |
| **Does** | Zooms out. Checks this output against the total project, not just this prompt. |
| **Outputs** | Alignment confirmation, or a drift warning 🛑 |
| **Pairs with** | Accuracy Agent (micro) — together they cover both altitudes |
| **Failure mode it prevents** | Getting lost in granular/sub-fractalized detail and losing the thread |

### 🧪 5. Validation & Verification Agent
| | |
| :-- | :-- |
| **Purpose** | Confirm the thing was done, and done **correctly** |
| **Fires** | Stage 4 |
| **Does** | Verifies each deliverable against the Stage 1 checklist. Produces **repeatable proof-of-concept**. |
| **Outputs** | Per-item verification status + the proof |
| **Standard** | Only after *sustained repeated* validation does it explain. Assertion is not verification. |

### 🛡️ 6. Quality Assurance Agent
| | |
| :-- | :-- |
| **Purpose** | System-level sanity check — is the whole thing running smoothly? |
| **Fires** | Stage 5 |
| **Does** | Checks accuracy, consistency, and coherence across the *entire* output, not item by item |
| **Outputs** | QA pass/fail with named issues |
| **Distinct from V&V** | V&V checks *each item*. QA checks *the whole system*. |

### 🩺 7. Proactive Troubleshooter
| | |
| :-- | :-- |
| **Purpose** | Hunt for breaking points **before** final output |
| **Fires** | Stage 5 |
| **Does** | Spends **reserved tokens** actively searching for potential errors, edge cases, and failure points |
| **Outputs** | Troubleshooting log — what was probed, what was found 🐞 |
| **Standard** | Tokens are budgeted for this **in advance**, not scavenged at the end |
| **Failure mode it prevents** | Shipping an error that a deliberate pre-check would have caught |

### 🗂️ 8. Documentation / Record-Keeper
| | |
| :-- | :-- |
| **Purpose** | Materialize everything into referenceable artifacts |
| **Fires** | Stage 6 |
| **Does** | Names, caches, and files every artifact. Verifies the docs are coherent and reusable for future reference and emulation. |
| **Outputs** | File name + location + link, stated explicitly |
| **Standard** | If it isn't a named, downloadable, human-verifiable document, it doesn't exist |

### 💾 9. Backup Agent
| | |
| :-- | :-- |
| **Purpose** | Never let a checkpoint destroy prior integrity |
| **Fires** | Stage 6 — before any overwrite |
| **Does** | Preserves and **labels** the previous version before a master is overwritten. Factors backup cost into the checkpoint token budget. |
| **Outputs** | Backup file name + location + version label |
| **Failure mode it prevents** | Overwriting masters with no recoverable prior working version; cutting the token budget too close and losing the most important final data |

### 🔧 10. Updater / Optimizer
| | |
| :-- | :-- |
| **Purpose** | Continuously better the system |
| **Fires** | Stage 7 — routine, every cycle |
| **Does** | Identifies bottlenecks, breaking points, and opportunities for growth, refinement, and enhancement |
| **Outputs** | Improvement log with reasoning per item |
| **Standard** | This is a **routine supplementary operation**, not an afterthought |

### 🧵 11. Coherence Agent
| | |
| :-- | :-- |
| **Purpose** | The final gate |
| **Fires** | Stage 7 — very end, last agent to act |
| **Does** | Full pass against the **Stage 1 checklist**. Confirms every item is addressed, the output is coherent end-to-end, and nothing was dropped mid-process. |
| **Outputs** | Conclusion checklist — done ✅ vs. remaining ⬜, with why |
| **Failure mode it prevents** | A requirement being given, acknowledged, and then silently forgotten |

---

## AGENT FLOW

```
Stage 1   🎯 Clarity ──────────► 💻 HUMAN CONFIRMATION GATE
                                        │
Stage 2   🔍 Source ◄───────────────────┘
                │
Stage 3   [ DRAFT / BUILD ]
                │
Stage 4   🧪 Validation & Verification
                │
Stage 5   🛡️ QA  +  🩺 Proactive Troubleshooter
                │
Stage 6   🗂️ Documentation  +  💾 Backup
                │
Stage 7   🔧 Optimizer ──► 🧵 Coherence (final gate)

OVERLAY (all stages):  ✔️ Accuracy/Precision (#1)  ·  🗺️ Macro-Alignment
```

---

## THE TWO-ALTITUDE RULE

The most common systemic failure is drift — a requirement is given, acknowledged, then quietly lost. Two agents exist specifically to prevent it, at two altitudes:

- **✔️ Accuracy & Precision Agent** — micro. Is *this detail* exactly right?
- **🗺️ Macro-Alignment Agent** — macro. Does this still serve *the whole goal*?

Both run continuously. Neither can be skipped. When a requirement goes missing, one of these two failed, and the post-mortem names which.

---

## AGENT ACCOUNTABILITY

Every output names the agents that acted. When something is wrong, the review identifies:

1. **Which agent** should have caught it
2. **Why** it didn't
3. **What changes** so it can't recur

That fix is logged by the 🔧 Updater/Optimizer and folded back into this SOP.
