<!-- SNAPSHOT: SOP v1.6 · commit d12928b · committed 2026-08-31T00:26:50+00:00 · READ-ONLY -->
# APW MULTI-LANE OPERATING SOP — binding on every lane
**🏁 BRIEF:** how every lane hears (checklist), verifies (evidence+links), stores (repo+Notion), answers (buttons+trackers+grade), and never loses data (raws+history).
**⏱ Timeline:** 🗣️ Alan prompts → ✅ checklist in reply → 👍 confirm → 🔨 execute → 🎯 grade vs SOP → 🔘 buttons+progress → 💾 all stored+pushed
*v1.6 · 2026-08-31 (v1.5 + §1.9 8e supervisor + template law, §1.11 token optimization, §1.12 local-session bootstrap) · Owner: Lane 1 (Command). A lane that has not read this file this session may not write anything.*

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
8. **CLOSE** — every final output ends with buttons (incl. Claude-suggested options) + a timeline tracker + progress trackers of the micro AND the macro.

**5b. NO SIZE EXCEPTION** — the model/effort line appears on EVERY reply, micro replies included (miss logged 8/30, register #94b).
**8b. COMPLIANCE FOOTER** — every reply ends with one compact SOP-check line: ✓/✗ per protocol step + links to [the SOP](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/SOP.md), the run's checklist, AND the run's grade file ([Grading SOP](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/gradings/README.md): vertical/mobile, did·didn't·%·quality·why·link·before/after + limitations w/ automatic fixes + 🧠 reasoning digest). Lean in the reply; depth one click away ("don't bloat, but let me verify" — Alan).
**8c. CONVERSATION LEDGER** — every session re-archives its raw transcript at batch end and regenerates [ops/archive/conversation/](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/conversation/README.md) via [build_conversation_ledger.py](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/tools/build_conversation_ledger.py) (numbered NNN-title-date-timeZ files; prompt verbatim open, AI layers collapsible; vanilla-friendly README). Honest limit on record: the platform stores thinking blocks EMPTY — the 🧠 layer is unavailable for any turn, by platform design, not by loss.

**8e. SUPERVISOR + TEMPLATE (the "coach over the shoulder")** — two layers, because rules alone kept failing:
- *Layer 1, prevention:* every Alan-facing reply is built by filling [ops/RESPONSE_TEMPLATE.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/RESPONSE_TEMPLATE.md) — a skeleton with a slot per SOP step, so a skipped step is a visible hole, not a memory lapse.
- *Layer 2, inspection:* every mastery cycle spawns a SUPERVISOR agent that reads the session's last replies from the raw transcript, grades each against §1.9 slot-by-slot, and auto-files any miss to the register with root cause. Misses get fixed in the next reply, not re-argued.

**8d. NO TURN ENDS ON A COMMIT** — the user-facing reply (buttons, footer, trackers) is composed in the same turn as the final tool call; a commit is never the last act (root cause of the 8/30 missed-buttons misses).

Standing exception unchanged (§1.7): autonomous/scheduled runs close with a quick-answer line instead of buttons. New lanes inherit this automatically via the root CLAUDE.md.

## 1.11 TOKEN OPTIMIZATION (Alan 8/31: "we keep running into massive token issues")
Track: every §1.9 reply carries session tokens used/remaining; every mastery cycle logs exact usage (from the session record) to its process log; every run-grade states the run's estimated cost. Segment: recurring tasks are classified 🟢 Sonnet-eligible / 🔴 Fable-required in [ops/data/TOKEN_SEGMENTATION.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/TOKEN_SEGMENTATION.md) — mechanical batch work moves to Sonnet chats (paste-brief in that file); Fable stays for law-drafting, forensics, and Alan-facing judgment. Raw numbers before optimization advice, always.

## 1.12 LOCAL-SESSION BOOTSTRAP (why local Claudes "keep missing the whole checklist thing")
Diagnosis [V]: the SOP auto-loads ONLY when a session starts INSIDE this repo folder (root [CLAUDE.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/CLAUDE.md) is the loader). A local chat opened elsewhere, or on a stale clone, never sees it — pointing at it mid-chat is weaker than loading it at start. The fix, every local session: (1) open the chat IN the repo folder (or a worktree), (2) first message = `git pull, read CLAUDE.md, confirm SOP version`, (3) if any reply misses the format, paste: "Follow SOP §1.9 — respond via ops/RESPONSE_TEMPLATE.md." A lane that can't confirm the current SOP version may not write.

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
