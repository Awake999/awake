# APW OPS — READ THIS FIRST (auto-loaded by every local Claude session)

You are working inside the Ascend Prime Wealth ops repo. **Before doing anything:**

1. **Read [`ops/SOP.md`](ops/SOP.md)** — the binding laws (verbatim checklists, evidence links, raw originals, scan-ready output) + lane ownership + the sync ritual (git pull first, push after every batch).
2. **Read [`ops/REGISTER.md`](ops/REGISTER.md)** — every ask Alan has made, verbatim, numbered, with status + grade. Grep `LANE-SYNC` for cross-lane notices. If your task isn't on the register, it gets a numbered line before work starts.
3. **Alan's original prompts, in full:** [`ops/prompts/ALL_PROMPTS_FULL.md`](ops/prompts/ALL_PROMPTS_FULL.md) (every prompt verbatim, chronological) and [`ops/prompts/2026-08-30-full-funnel-spec.md`](ops/prompts/2026-08-30-full-funnel-spec.md) (the governing spec). **Prompts govern over any brief or summary.**
4. **Find anything:** [`ops/INDEX.md`](ops/INDEX.md) — clickable pointers to every dashboard, database, audit, and decision across Notion/GitHub/Drive/GHL.

**LAW 0 — NEVER-MISS PROTOCOL (outranks all):** parse every prompt into numbered atomic asks before working; a REPROMPT = severity-1 failure — diff v1 against the literal words, name the delta, fix that delta only; one line per item in every enumerated deliverable, never grouped; checkboxes only after the tool call exists; literal ask first, judgment second.

**LAW 1.9 — INTERACTION PROTOCOL (Alan-confirmed 8/30, binding on every lane incl. NEW ones):** every user prompt → verbatim numbered checklist IN the response → user confirms → store hard-coded (repo+Notion, linked) → Claude adds improvement suggestions → model/effort/token disclosure (raw first) → execute on confirm → cross-off scorecard table (status·%·quality·why·improvements·link·before/after) → close with buttons + timeline + micro/macro progress. Full text: ops/SOP.md §1.9. EVERY Alan-facing reply is built from ops/RESPONSE_TEMPLATE.md (fill every slot). Token rules: ops/SOP.md §1.11 + ops/data/TOKEN_SEGMENTATION.md. Local sessions MUST start inside this repo folder and run: git pull → read CLAUDE.md → confirm SOP version (§1.12).

**The laws in one line each:** every ask → verbatim numbered checklist · every claim → clickable link + date + evidence window · raw originals beside every summary, never replaced · verified/derived/unknown labels, never guess · scan-ready output, TLDR first · pull before work, push after every batch (unpushed work dies with the container).

**Lane ownership (single-writer):** Lane 1 (cloud command) owns REGISTER/SOP/INDEX/Notion-ops · Lane 2 owns `ops/dashboard/` · Lane 3 owns `ops/archive/` (append-only) · Lane 4 (this PC) owns `ops/archive/ghl/` + `ops/lane4/` + browser tasks. Everyone writes their own `ops/process-log/YYYY-MM-DD-<lane>.md`, never another lane's.

Dashboard live URL: https://claude.ai/code/artifact/c6ad801c-50fc-49d3-847a-e6a8b0ddd392
