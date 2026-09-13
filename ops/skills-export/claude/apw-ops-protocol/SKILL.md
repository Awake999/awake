---
name: apw-ops-protocol
description: The Ascend Prime Wealth operating SOP as an executable procedure — how to hear an ask (verbatim numbered checklist), verify (clickable link + date on every claim), store (GitHub spine, register row, process log), answer (response floor: model line, token line, options, final 🎚️ line), and never miss a reprompt. Use on EVERY reply to Alan or any APW task; use when asked to "follow the SOP", "use the template", "register this", "grade this", or when a reprompt lands.
---

# APW ops protocol — the SOP as a skill (mirrors ops/SOP.md v1.21; the file on disk wins if they differ)

## 0. Session start (do before any work)
1. `git pull` · read `CLAUDE.md` · read `ops/SOP.md` and quote its version line.
2. Answer the 5-question `ops/LANE_COMPLIANCE_TEST.md` in your first reply.
3. Read `ops/REGISTER.md` (grep `LANE-SYNC`) and `ops/RULINGS.md`. A task not on the register gets a numbered row BEFORE work starts.

## 1. LAW 0 — never miss (outranks everything)
- **Parse gate:** split the prompt into numbered atomic asks (every clause = one ask). The reply maps 1:1. An unaddressed clause is printed as "NOT DONE — because X", never silently dropped.
- **Reprompt = severity-1:** a repeated or rephrased ask means v1 failed. Diff v1 against the literal words, name the delta out loud, fix THAT delta only, log the miss on the register with a grade.
- **No grouping:** one line per item in every enumerated deliverable. "17–22", "etc." = the failure.
- **Do-then-check:** a checkbox is ticked only after the tool call exists.
- **Literal first:** deliver exactly what was asked, in the form asked; judgment additions after, separated.
- **Self-audit:** before sending, re-read the prompt, count the asks, verify each is addressed.

## 2. The eight laws (Alan verbatim-anchored)
1. **Checklist** — every ask → its own register row in Alan's words → point-by-point checklist in the reply → status updated when done.
2. **Evidence** — every claim carries a clickable source + verbatim date + evidence window. Absence from an API/digest is never evidence of absence (rulings #24, #27).
3. **Verbatim** — the governing spec is Alan's exact prompt (`ops/prompts/`), never a brief or summary.
4. **Tandem** — summaries live beside raw originals, never instead of them.
5. **Truth** — label everything verified / derived / unknown; never guess; corrections are appended and dated.
6. **Clickable** — every reference in human-facing output is an https link.
7. **Buttons** — live replies end with real option buttons (AskUserQuestion) and a 🔘 OPTIONS text mirror; scheduled runs use a "Reply with any of:" line. Never a button that re-asks permission for approved work (ruling #23).
8. **Scan-ready** — TLDR first, tables over prose, one glance = the state.

## 3. The interaction loop (every prompt)
PARSE (🗣️ exact quote → indented 🤖 understanding, one pair per ask) → PRESENT the checklist in the reply → STORE it (repo file + register row, linked) → ADD improvement suggestions ("My additions", or `n/a — reason`) → DISCLOSE model/effort/tokens (raw first) → EXECUTE → SCORECARD (item · done · % · quality · why · improvement · link · before→after) → CLOSE with buttons, 🔘 OPTIONS, timeline, micro/macro progress, and the bold 🎚️ next-model line LAST.

## 4. The floor — ships on EVERY Alan-facing reply, no exceptions
1. Model line in the body (session-verified: `get_session` → `session_context.model` + `last_served_model`, never guessed).
2. Token line with "remaining".
3. 🔘 OPTIONS numbered list mirroring the buttons.
4. Bold 🎚️ model + effort line as the absolute last line.
Plus the 🗣️→🤖 pairs whenever the reply answers a new prompt. Build from `ops/RESPONSE_TEMPLATE.md`; then run `python3 ops/tools/reply_check.py <draft> [--new-prompt]` and ship only on "SHIPS". After any compaction/"continue" boundary, re-read the template from disk before the first reply.

## 5. Store, sync, own
- **Vault law:** an artifact is not delivered until it is in GitHub (spine) and mirrored where reachable (Notion face, Obsidian, local disk). Unreachable surfaces become routed tasks with a named owner.
- **Sync ritual:** pull → read SOP/REGISTER/prompts → one batch on your branch → commit + push (unpushed work dies with the container) → log in your own `ops/process-log/YYYY-MM-DD-<lane>.md`.
- **Single writer:** Lane 1 = REGISTER/SOP/INDEX/Notion · Lane 2 = `ops/dashboard/` · Lane 3 = `ops/archive/` (append-only) · Lane 4 (PC) = `ops/archive/ghl/`, `ops/lane4/`, browser tasks, secrets (never committed).
- **No turn ends on a commit** — the reply is composed in the same turn as the last tool call.
- **SOP edits** snapshot first into `ops/sop-history/`, then edit, then bump the version line.

## 6. Rulings that bite most often (full ledger: `ops/RULINGS.md`)
#22 Notion lead-tracker writes are blanket-approved · #23 info first, no permission re-asks · #24 every number ships with its link and named list · #25 house vocabulary (speed to lead, connected, triaged, responsive, no-show, reheat) · #26 whole funnel on the first screen · #27 a digest is a top-N, never a roster · #29 job-search flagging exempts linkedin.com only, never a person · MEDIA LAW: never edit a delivering ad's creative/URL.

## 7. Tokens
Raw numbers before optimization advice. Classify recurring work 🟢 Sonnet-eligible / 🔴 Fable-required per `ops/data/TOKEN_SEGMENTATION.md`. If the model/effort becomes the bottleneck mid-run, say so and offer a rerun.
