# APW MULTI-LANE OPERATING SOP — binding on every lane
**🏁 BRIEF:** how every lane hears (checklist), verifies (evidence+links), stores (repo+Notion), answers (buttons+trackers+grade), and never loses data (raws+history).
**⏱ Timeline:** 🗣️ Alan prompts → ✅ checklist in reply → 👍 confirm → 🔨 execute → 🎯 grade vs SOP → 🔘 buttons+progress → 💾 all stored+pushed
*v1.20 · 2026-09-02 (v1.19 + **8j THE PRE-SEND SCAN IS A SCRIPT** — supervisor inspections #2, #3, #4 and #5 all recommended mechanizing the reply check and it was logged four times instead of built; the script now exists at ops/tools/reply_check.py. Also from #5: the model line must appear in the BODY, not only in the 🎚️ final line, because those two slots were being satisfied by one string. v1.19 was 8i MINIMUM VIABLE REPLY; from supervisor inspection #4: three template slots — additions heading, SOP-check footer, real buttons — showed ZERO recovery across a whole window even with reprompts at 0. A 7-slot template at 50% compliance is worse than a 4-slot floor at 100%: the floor is now law and the rest is explicitly conditional) · Owner: Lane 1 (Command). A lane that has not read this file this session may not write anything; the [5-question compliance test](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/LANE_COMPLIANCE_TEST.md) gates every session start.*

## 0. THE NEVER-MISS PROTOCOL (Law 0 — outranks everything; from Alan: "plan a strategy to NEVER miss on a user prompt. ESPECIALLY a 2nd reprompt")

Root causes of every miss to date: compression reflex, answering the adjacent question instead of the literal one, claiming before doing, and treating a reprompt as a fresh ask instead of a failure signal. The mechanism:

- **0.1 PARSE GATE** — before ANY work: decompose the prompt into numbered atomic asks (every clause = one ask). The reply maps 1:1 to that decomposition. An unaddressed clause appears as "NOT DONE — because X", never silently absent.
- **0.2 REPROMPT RULE (severity-1)** — a repeated or rephrased ask means v1 FAILED. Required sequence: (a) diff the previous deliverable against the user's literal words, word by word; (b) name the exact delta out loud; (c) fix THAT delta — never regenerate a fresh variant; (d) log the miss on the register with a grade.
- **0.3 NO-GROUPING RULE** — in any enumerated deliverable (register, roster, checklist, table): ONE LINE PER ITEM, always. Grouping, eliding, "17–22", "etc." = the failure itself. Token cost is never a justification.
- **0.4 DO-THEN-CHECK** — a checkbox is marked ONLY after the action's tool call exists in the log. (The Todd-ID incident.)
- **0.5 LITERAL-FIRST** — deliver exactly what was asked, in the form asked, FIRST; judgment additions come after, clearly separated.
- **0.6 SELF-AUDIT LINE** — before sending any reply to Alan: re-read his prompt once, count the asks, verify each is addressed; on a reprompt, verify the named delta is actually fixed in this reply.

## 1. The laws (non-negotiable, from Alan verbatim)

1. **CHECKLIST LAW** — *"every time I ask you for something, you have to give me a point-by-point, verbatim checklist so we know what's being done."* Every ask → its own numbered line in `ops/REGISTER.md`, quoted in Alan's words, BEFORE work starts → point-by-point checklist in the reply → status updated when done.
2. **EVIDENCE LAW** — *"Anything that is being claimed should have a direct link... verbatim dates, times, and the source... everything needs to be verifiable."* Every claim in any summary carries its clickable source + verbatim date + evidence-window IN THE SUMMARY. Claims that outlive their window are re-verified, never repeated. Absence from an API is never evidence of absence (two confirmed Fathom-lag cases).
3. **VERBATIM LAW** — *"It needs all specific information because it just is cutting corners."* Lane briefs are ROUTING, not specs. The governing spec is always Alan's verbatim prompt in `ops/prompts/`. If your brief conflicts with or omits something the verbatim prompt contains, THE PROMPT WINS — read it, don't trust the summary of it.
4. **TANDEM LAW** — summaries live BESIDE originals, never instead of them.
5. **TRUTH LAW** — verified / derived / unknown labels on everything; never guess a stage, a show, or a dollar; corrections are appended and dated, never silently overwritten.
6. **CLICKABLE LAW** — *"the links are supposed to be clickable URLs."* Every reference in any human-facing surface is a clickable https URL — bare IDs and `collection://` URIs live only in machine columns of pointer-map.md.
7. **BUTTON LAW** — *"every time you push out a response, it should be an easy response for me to respond to with buttons. Without fail."* Every reply to a live Alan message ends with tappable option buttons (AskUserQuestion) covering the open decisions — free-text always remains available. Exception: autonomous/scheduled cycle reports (nobody present to tap) end with a "reply with any of: ..." quick-answer line instead.
8. **SCAN-READY LAW** — *"Everything you should be saying should be scan-ready and easy."* Every report, file, and reply: TLDR first, tables over prose, one glance = the state. Applies to all lanes.

## 1.9 INTERACTION PROTOCOL (Alan verbatim spec 8/30, CONFIRMED — binding on every current and FUTURE lane/agent, every user prompt)
*Spec: [ops/prompts/2026-08-30-interaction-protocol-spec.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/prompts/2026-08-30-interaction-protocol-spec.md) · Checklist: [ops/data/INTERACTION_PROTOCOL_CHECKLIST.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/INTERACTION_PROTOCOL_CHECKLIST.md) · Notion hard-code: linked from the register mirror.*

The loop, for EVERY user prompt:
1. **PARSE** — break the WHOLE prompt into a verbatim-anchored numbered checklist: each item = 🗣️ the user's exact quote, then on the NEXT line, indented as a sub-bullet, 🤖 the AI's understanding (same column every item; survives chat AND GitHub rendering). Zero fidelity loss.
2. **PRESENT** — that checklist appears IN the response for the user to confirm / deny / add to, BEFORE work starts.
3. **STORE** — the checklist is hard-coded: repo file (ops/data/) + Notion mirror + register line, with clickable links in the response (compaction-proof).
4. **ADD** — Claude appends its own improvement suggestions — for AI and for humans; beginner-friendly AND master-grade, never sacrificing the beginner.
5. **DISCLOSE (model/effort/tokens)** — the plan block ends with: which model+effort served THIS prompt (verify via the session record; ask if unknown) · recommended model/effort + reasoning (incl. whether ultracode/extra/max is needed, for plan AND execution) · estimated tokens · estimated time · sustainable runway before limits, accounting for token limits + daily/weekly/monthly usage + Fable 5 usage + plan usage (20x max). Order is always: RAW data first, optimized plan second, options third — never pre-shrink to save tokens. If mid-execution the model/effort becomes the bottleneck, SAY SO and offer a rerun.
6. **ASK-THEN-EXECUTE** — execute only on the user's confirm.
7. **SCORECARD** — after execution, a cross-off table, one row per checklist item, columns: Item · Done? · Status · % complete · Quality · Why rated that way · Suggested improvements · Clickable link straight to the work · Before → After.
8. **CLOSE** — every final output to a LIVE Alan message ends with ACTUAL TAPPABLE BUTTONS (AskUserQuestion — never a text "reply with any of" line; that substitution is a §1.9 violation, logged 8/31 as 101b) + timeline tracker + micro AND macro progress. The quick-answer text line exists ONLY for scheduled/autonomous runs where nobody is present to tap.
8f. **OPTIONS IN TEXT (Alan 8/31: "so they don't get lost")** — the reply body prints a clearly-labeled 🔘 OPTIONS list mirroring the buttons, immediately before the final 🎚️ line; a dismissed widget never loses the choices — typing an option = tapping it.
9. **FINAL LINE (Alan 8/31: "can NOT be missed")** — the ABSOLUTE LAST text line of every reply is a standalone bold 🎚️ line: recommended model + effort for the next prompt/phase. Nothing after it, ever.

**5c. RECOMMENDATIONS FORMAT (Alan 8/31)** — any list of recommendations/options is NUMBERED in priority order, and each line carries: est. tokens · timeline · model/mode · effort level. No bare suggestion lists.
**5b. NO SIZE EXCEPTION** — the model/effort line appears on EVERY reply, micro replies included (miss logged 8/30, register #94b).
**8b. COMPLIANCE FOOTER** — every reply ends with one compact SOP-check line: ✓/✗ per protocol step + links to [the SOP](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/SOP.md), the run's checklist, AND the run's grade file ([Grading SOP](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/gradings/README.md): vertical/mobile, did·didn't·%·quality·why·link·before/after + limitations w/ automatic fixes + 🧠 reasoning digest). Lean in the reply; depth one click away ("don't bloat, but let me verify" — Alan).
**8c. CONVERSATION LEDGER** — every session re-archives its raw transcript at batch end and regenerates [ops/archive/conversation/](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/conversation/README.md) via [build_conversation_ledger.py](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/tools/build_conversation_ledger.py) (numbered NNN-title-date-timeZ files; prompt verbatim open, AI layers collapsible; vanilla-friendly README). Honest limit on record: the platform stores thinking blocks EMPTY — the 🧠 layer is unavailable for any turn, by platform design, not by loss.

**8e. SUPERVISOR + TEMPLATE (the "coach over the shoulder")** — two layers, because rules alone kept failing:
- *Layer 1, prevention:* every Alan-facing reply is built by filling [ops/RESPONSE_TEMPLATE.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/RESPONSE_TEMPLATE.md) — a skeleton with a slot per SOP step, so a skipped step is a visible hole, not a memory lapse.
- *Layer 1b MECHANIZED (inspection #2, adopted 8/31):* the heading check is a LITERAL SCAN of the drafted reply, never memory — and the footer may print a ✓ ONLY for a slot the scan found. Printing an unearned ✓ = forged self-certification, the gravest §1.9 violation (caught twice, inspection #2). The scan runs in the cycle self-test too.
- *Layer 1b-micro:* even tail/close/micro blocks carry the model line + a token line (they held 6 of 8 misses in inspection #2).
- *RULINGS LEDGER ([ops/RULINGS.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/RULINGS.md)):* every Alan ruling = one line, appended the turn it lands; every action list validates against it before shipping (kills the "like I said" reprompt class). No lane ever self-declares a streak grade — only supervisor counts stand.
- *Layer 1c, the health metric (Alan-ratified 8/31):* SOP health = the consecutive-A streak. 5 consecutive Alan-facing replies graded A with zero reprompts = working as intended; every supervisor inspection reports the current streak; a break is reported to Alan, a healthy streak is not. Every mastery cycle also runs the 31-point mechanical self-test (SOP sections, template headings, loader, file existence, index completeness, ledger sync, clean tree).
- *Layer 2, inspection:* every mastery cycle spawns a SUPERVISOR agent that reads the session's last replies from the raw transcript, grades each against §1.9 slot-by-slot, and auto-files any miss to the register with root cause. Misses get fixed in the next reply, not re-argued.

**8g. ERROR-SOLUTION AGENT (Alan 8/31: "implement error solution agent into SOP")** — every error triggers it automatically: an Alan reprompt · a supervisor-filed miss · a self-test failure · a lane compliance failure · any broken tool/flow. The agent's mandate: (1) ROOT-CAUSE from primary sources (transcript, logs, diffs) — never from memory; (2) design the MECHANICAL fix (a scan, a template slot, a script, a ledger — never "try harder"); (3) IMPLEMENT it (SOP edits via the §1.13 snapshot ritual; scripts into ops/tools/); (4) file the miss + fix to the register (and RULINGS.md if a ruling was involved); (5) report fix-verified with a link. Lane 1 spawns it within the same cycle the error surfaces; the supervisor's next pass verifies the fix held. Errors are hand-fixed ZERO times — the loop is the fixer.
*Duplicate-delivery adjudication (v1.17, from run #1):* an apparent reprompt still spawns the agent, but severity-1 is filed ONLY after the transcript shows two DISTINCT human sends (different event uuids). If the "second send" is the SAME message uuid delivered twice by the platform (queued mid-turn → queue-remove reason `absorbed_mid_turn` → re-delivered on session resume behind a synthetic isMeta "Continue from where you left off."), it is a platform duplicate, not an Alan reprompt: no severity-1, verify v1 against the literal words, answer idempotently, file as platform-duplicate. Adjudication recipe lives in the [charter](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/agents/ERROR_SOLUTION_AGENT.md). Proven live: register 108c — the 8/31 "reprompt" of 108 was uuid `5550f4b8` delivered at both 05:50:57Z and 06:12:50Z.

**8i. THE MINIMUM VIABLE REPLY — the floor that never bends (v1.19, from supervisor inspection #4: "My additions" 0/6, §8b footer 0/6, real buttons 0/6 across a clean, reprompt-free window — slots that decay silently are slots that were never mechanical)**
Four slots ship on EVERY Alan-facing reply, no size exception, no autonomy exception, no compaction exception:
1. **Model line** — which model/effort actually served the reply (session-verified, never guessed).
2. **Token line** — raw used this run + session remaining. "Remaining" is not optional; §1.11 has no size exception.
3. **🔘 OPTIONS mirrored in text** (8f).
4. **Bold 🎚️ model+effort line as the absolute last line** (step 9).
Plus, whenever the reply answers a NEW Alan prompt: the **verbatim 🗣️ quote → indented 🤖 understanding** pair, one line per atomic ask (§1.9 step 2). A reply that cannot carry the floor does not ship.
**Conditional slots — required on substantive work-delivery replies, and when omitted the reply must PRINT `additions: n/a — <reason>` / `scorecard: n/a — <reason>`:** My additions · cross-off scorecard · §8b SOP-check footer · timeline + micro/macro progress. Silence is no longer an allowed omission — an unmarked missing slot is a Layer-1b failure, exactly like an unearned ✓ (v1.14).
**Real buttons (v1.15/v1.18, sharpened):** a real AskUserQuestion widget fires whenever the reply ends on a genuine fork for Alan — and at minimum once per live exchange chain while he is present. Text-only OPTIONS are the mirror (8f), never the substitute. The one banned use stays banned: a button that re-asks permission for work Alan already ordered (ruling #23).

**8h. COMPACTION RE-BOOTSTRAP (v1.18, from supervisor inspection #3 — the 07:53Z 8/31 compaction wiped template compliance for 4.5 hours: tokens/additions/footers/checklists all went to zero and the first freehand reply became the copied pattern)** — a compaction or "continue from where you left off" boundary is treated EXACTLY like a fresh session start: before the FIRST Alan-facing reply after any such boundary, (1) re-read [RESPONSE_TEMPLATE.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/RESPONSE_TEMPLATE.md) from disk and compose from it; (2) run the Layer-1b literal heading scan on the drafted reply; (3) the mastery-cycle self-test gains a standing check: "did a compaction occur since the last cycle, and did the first post-compaction reply pass the heading scan?" A summary in the context window is NOT the template — only the file on disk is.

**Buttons law × ruling #23, reconciled in writing (v1.18):** REAL AskUserQuestion buttons remain mandatory on every Alan-facing output (v1.15) with ONE carve-out, from Alan's own ruling #23: permission-gate questions on already-approved work are banned — a button set must offer forward CHOICES (ship / next task / fix), never re-ask approval for something Alan already ordered. The 🔘 OPTIONS text mirror (8f) and the final 🎚️ line (step 9) have NO exceptions, compaction or otherwise.

**8j. THE PRE-SEND SCAN IS A SCRIPT, NOT A HABIT (v1.20 — the fourth-time-of-asking rule)** — [`ops/tools/reply_check.py`](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/tools/reply_check.py) greps a DRAFTED reply for the literal strings and exits non-zero if it must not ship: FLOOR (model identity in the body · token line containing "remaining" · 🔘 OPTIONS list · 🎚️ as the absolute last line), CONDITIONAL (verbatim 🗣️→🤖 pair when Alan sent a new prompt · "My additions" — each satisfiable ONLY by the section itself or a printed `n/a — reason`), EVIDENCE (any reply carrying numbers must carry a link, ruling #24). Usage: `python3 ops/tools/reply_check.py draft.md [--new-prompt]`. **A recommendation that survives four inspections is no longer a recommendation, it is the failure** — when the supervisor repeats itself, the repeat becomes the highest-priority build, not another register line.

*Two structural findings this law encodes (inspection #5):* (a) the model line and the 🎚️ line were being satisfied by the SAME string, so a 4-slot floor was really 3 — the model identity must now appear in the body independently; (b) the mastery-cycle reply template shipped zero links while the nightly template linked properly — **evidence discipline must not vary by which trigger is driving**; the EVIDENCE check enforces it either way.

**8d. NO TURN ENDS ON A COMMIT** — the user-facing reply (buttons, footer, trackers) is composed in the same turn as the final tool call; a commit is never the last act (root cause of the 8/30 missed-buttons misses).

~~Standing exception~~ ABOLISHED 8/31 — buttons on everything (see step 8). New lanes inherit this automatically via the root CLAUDE.md.

## 1.11 TOKEN OPTIMIZATION (Alan 8/31: "we keep running into massive token issues")
Track: every §1.9 reply carries session tokens used/remaining; every mastery cycle logs exact usage (from the session record) to its process log; every run-grade states the run's estimated cost. Segment: recurring tasks are classified 🟢 Sonnet-eligible / 🔴 Fable-required in [ops/data/TOKEN_SEGMENTATION.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/TOKEN_SEGMENTATION.md) — mechanical batch work moves to Sonnet chats (paste-brief in that file); Fable stays for law-drafting, forensics, and Alan-facing judgment. Raw numbers before optimization advice, always.

## 1.12 LOCAL-SESSION BOOTSTRAP (why local Claudes "keep missing the whole checklist thing")
Diagnosis [V]: the SOP auto-loads ONLY when a session starts INSIDE this repo folder (root [CLAUDE.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/CLAUDE.md) is the loader). A local chat opened elsewhere, or on a stale clone, never sees it — pointing at it mid-chat is weaker than loading it at start. The fix, every local session: (1) open the chat IN the repo folder (or a worktree), (2) first message = `git pull, read CLAUDE.md, confirm SOP version`, (3) if any reply misses the format, paste: "Follow SOP §1.9 — respond via ops/RESPONSE_TEMPLATE.md." A lane that can't confirm the current SOP version may not write.

## 1.13 SOP VERSIONING (Alan spec 8/30, executed 8/31)
Before ANY change to ANY SOP: snapshot the current file into [ops/sop-history/](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/sop-history/README.md) named `SOP-vX.X-date-timeTZ`, cross-check the live file matches the newest snapshot, THEN edit; also snapshot at creation. Snapshots are read-only (chmod 444) with git as the second permanent layer. Department-SOP architecture: one main SOP (this file, all lanes inherit) + department SOPs that extend it, never contradict it, each registered here and at the front door.

## 1c. RATIFIED ARCHITECTURE (Alan: "47 go", 8/30)
One front door, one job per tool: **Notion = index + live client data** · Google Docs = long-form working docs · Sheets = number grids · Trello = task execution/accountability · Slack = signals only (anything lasting gets a home + link within 24h) · GitHub vault = permanence + raws · GHL = funnel ground truth (statuses maintained per #64) · **Whop = payments source of truth (Alan: "65 whop")**. Three enforcement rules: nothing lives in two places · every new doc registers at the front door within 24h · Slack is ephemeral by policy.

## 1b. Idle-restart reality (cloud lanes)
Cloud containers DO restart when idle — that is WHY state lives in the repo, never the container. A cloud lane that restarts loses nothing pushed; it resumes by running the sync ritual (§3). Wake an idle cloud lane with a one-shot trigger, or replace it with a LOCAL lane: multiple local Claudes on one PC use separate clones or `git worktree add ../awake-<lane> <branch>` — same ritual, same repo, same sync. Cloud vs local is interchangeable; the repo is the team.

## 2. Lane map + ownership (single-writer per surface)

| Lane | Session | Owns (writes) | Reads everything, writes NOTHING else |
|---|---|---|---|
| 1 · Command | the original ops session | `ops/REGISTER.md`, `ops/SOP.md`, `ops/INDEX.md`, Notion mirrors, daily sweeps, all Notion data ops | — |
| 2 · Dashboard | "APW Dashboard Lane" | `ops/dashboard/**`, artifact publish | numbers/claims (Lane 1's) |
| 3 · Archive | "APW Archive Lane" | `ops/archive/**` (append-only) | everything else |
| 4 · Local (Alan's PC) | local Claude Code/Cowork | `ops/archive/ghl/**`, `ops/lane4/**`, GHL (Todd import only), browser tasks (Loom, Teramind) | everything else |
| Every lane | — | its OWN dated file in `ops/process-log/` | never another lane's log |

## 3. The sync ritual (how a change HERE becomes a change THERE)

The repo is the only sync channel. Notion pages are human-readable MIRRORS; `ops/` files are CANONICAL.

**Every lane, every work batch:**
1. `git pull` FIRST — receive all other lanes' changes.
2. Read, in order: `ops/SOP.md` (this file — check version header) → `ops/REGISTER.md` (your items + anything marked LANE-SYNC) → your lane's verbatim prompts in `ops/prompts/`.
3. Do ONE batch of work on your own branch.
4. Commit + push. Pushing IS the broadcast — no push, no sync, and unpushed work dies with the container.
5. Log the batch in your own `ops/process-log/YYYY-MM-DD-<lane>.md` file: what changed, register item numbers touched, resume point.

**Register changes:** only Lane 1 edits `ops/REGISTER.md` (single-writer = no merge conflicts). Other lanes report status in their process-log; Lane 1 merges into the register and re-mirrors to Notion. A change that affects other lanes gets a `LANE-SYNC:` marker line in the register; every lane greps for `LANE-SYNC` at ritual step 2.

**Why this is effective:** one canonical file, one writer per surface, pull-before-work, push-after-batch. Fidelity can't silently degrade because the spec each lane executes is Alan's verbatim text, not a summary; and every batch starts by re-reading it.

## 4. WHERE EVERYTHING IS BACKED UP — the literal map (Alan's requirement)

| Layer | What | Durability |
|---|---|---|
| **GitHub** `awake999/awake` (PRIVATE) | everything in `ops/` — register, SOP, prompts, transcripts, archive, dashboards, dossiers | ☁️ durable cloud; every commit = restore point |
| **Alan's PC clone** (Lane 4) | full repo copy on `git pull` | 💻 local physical copy |
| **Obsidian** | point Obsidian at the repo folder on the PC — every `ops/` file is vault-ready markdown | 💻 same files, vault navigation |
| **Google Drive · "APW Data Hub"** | index/pointer mirrors + pre-existing runbooks & findings | ☁️ second cloud |
| **Notion** | human mirrors: register, checklists, audits, client tracker (Notion is CANONICAL only for live client DATA — the tracker databases) | ☁️ third cloud, edit surface |
| **Cloud session containers** | working clones | ⚠️ EPHEMERAL — never the only copy of anything; hence push-after-batch |

## 5. Navigation
Start at `ops/INDEX.md` — the pointer file to every prompt, SOP, dataset, transcript, dashboard, and mirror, across every medium.
