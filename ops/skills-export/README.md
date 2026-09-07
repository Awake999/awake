# APW skills export — import into Claude AND GPT

Two skills, exported 2026-09-07 from the live SOP (v1.21). Same laws, three formats.

| Skill | What it does | Claude (folder) | ChatGPT / GPT (paste + upload) |
|---|---|---|---|
| **apw-ops-protocol** | The operating SOP as a procedure: never-miss parsing, evidence law, response floor, storage/sync, rulings | `claude/apw-ops-protocol/` | `gpt/APW_OPS_PROTOCOL.instructions.md` + `gpt/knowledge/*` |
| **client-testimonials** | Verbatim client quotes with proof links, not-found table, cards | `claude/client-testimonials/` | `gpt/CLIENT_TESTIMONIALS.instructions.md` + `gpt/knowledge/CLIENT_TESTIMONIALS_SOP.md` |

## Import into Claude
- **Claude Code (this repo):** nothing to do — `.claude/skills/*/SKILL.md` auto-loads in any session started inside the repo. Type `/apw-ops-protocol` or `/client-testimonials`.
- **Claude Code (another repo or your PC):** copy the folder `claude/<skill>/` into that repo's `.claude/skills/`, or into `~/.claude/skills/` for every repo.
- **claude.ai / Claude Desktop / Cowork:** Settings → Capabilities → Skills → upload `apw-skills-claude.zip` (this folder zipped; each skill is a folder with a `SKILL.md` at its root). Alternatively drag the folder into a Project's files.
- The `reference/` and SOP copies inside each folder are snapshots so the skill works away from the repo; the repo file always wins when both are available.

## Import into GPT (OpenAI)
- **Custom GPT:** ChatGPT → Explore GPTs → Create → *Configure* → paste `gpt/APW_OPS_PROTOCOL.instructions.md` into **Instructions** (it is under the 8,000-character limit) → **Knowledge**: upload every file in `gpt/knowledge/` → save. Make a second GPT the same way with `gpt/CLIENT_TESTIMONIALS.instructions.md`, or paste both into one GPT if they fit.
- **ChatGPT Project:** Project → Instructions → paste the same file; add the knowledge files to the project.
- **API / Assistants:** use the instructions file as the `system` prompt and attach the knowledge files with file search.
- GPT has no button widget and cannot read your session's model, so the GPT version prints text options and states the model as "unverified" unless the platform shows it. Everything else is identical.

## Keep them in sync
Edit the source of truth only (`ops/SOP.md`, `ops/RULINGS.md`, `ops/RESPONSE_TEMPLATE.md`, `ops/sops/CLIENT_TESTIMONIALS_SOP.md`, `.claude/skills/*/SKILL.md`), then run `python3 ops/tools/skills_export.py` to regenerate this folder and the zip.
