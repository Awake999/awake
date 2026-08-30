# APW MULTI-LANE OPERATING SOP — binding on every lane
*v1.0 · 2026-08-30 · Owner: Lane 1 (Command). A lane that has not read this file this session may not write anything.*

## 1. The laws (non-negotiable, from Alan verbatim)

1. **CHECKLIST LAW** — *"every time I ask you for something, you have to give me a point-by-point, verbatim checklist so we know what's being done."* Every ask → its own numbered line in `ops/REGISTER.md`, quoted in Alan's words, BEFORE work starts → point-by-point checklist in the reply → status updated when done.
2. **EVIDENCE LAW** — *"Anything that is being claimed should have a direct link... verbatim dates, times, and the source... everything needs to be verifiable."* Every claim in any summary carries its clickable source + verbatim date + evidence-window IN THE SUMMARY. Claims that outlive their window are re-verified, never repeated. Absence from an API is never evidence of absence (two confirmed Fathom-lag cases).
3. **VERBATIM LAW** — *"It needs all specific information because it just is cutting corners."* Lane briefs are ROUTING, not specs. The governing spec is always Alan's verbatim prompt in `ops/prompts/`. If your brief conflicts with or omits something the verbatim prompt contains, THE PROMPT WINS — read it, don't trust the summary of it.
4. **TANDEM LAW** — summaries live BESIDE originals, never instead of them.
5. **TRUTH LAW** — verified / derived / unknown labels on everything; never guess a stage, a show, or a dollar; corrections are appended and dated, never silently overwritten.
6. **CLICKABLE LAW** — *"the links are supposed to be clickable URLs."* Every reference in any human-facing surface is a clickable https URL — bare IDs and `collection://` URIs live only in machine columns of pointer-map.md.
7. **SCAN-READY LAW** — *"Everything you should be saying should be scan-ready and easy."* Every report, file, and reply: TLDR first, tables over prose, one glance = the state. Applies to all lanes.

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
