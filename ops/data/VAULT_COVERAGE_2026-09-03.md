# 🗄 APW VAULT — coverage audit, 2026-09-03
*First run of the Vault Agent's job, done by hand. **Question: of everything we have built, what actually lives on every surface?** Answer: the spine is complete, the face is stale, and one surface has never been wired at all.*

## 📊 THE FOUR SURFACES, HONESTLY
| Surface | State | Coverage |
|---|---|---|
| **GitHub** (spine) | ✅ **Complete** — every artifact, script, SOP version, ruling and register row, versioned and pushed | **100%** |
| **Notion** (face) | ⚠️ **Stale** — the register mirror is synced through **#138**; rows **#139–161 are not there** (23 rows incl. the Vault Law itself) | ~85% |
| **Live board** (face) | 🔴 **Badly stale** — carries none of the last week's work: no funnel truth, no setter/SPL analysis, no EODRs, no team tracking, no timetables, no Teramind work. The 3-way ad toggle change order is still unshipped by Lane 2 | ~20% |
| **Obsidian** (local knowledge) | 🔴 **NEVER WIRED** — zero artifacts have ever reached it. This is the largest single gap in the Vault | **0%** |
| **Local disk** (Alan's PC) | ⚠️ **Unknown staleness** — Lane 4's clone has not reported a pull since the 8/31 rescue | unverified |

## 🔴 THE HEADLINE
**Obsidian has never received a single artifact.** Every plan, funnel analysis, SOP, ruling and report from this entire build exists in GitHub and partially in Notion — **and nowhere in the local knowledge graph you asked to be part of the system.** That is not a sync failure; the pipe was never built.

## 📦 WHAT'S IN THE SPINE BUT NOT ON THE FACE (last 7 days)
| Artifact | GitHub | Notion | Board | Obsidian |
|---|---|---|---|---|
| [FUNNEL_EXPLORER.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/FUNNEL_EXPLORER.md) — the whole 38-lead truth | ✅ | ✅ page | ❌ | ❌ |
| [SETTER_AND_SPL.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/SETTER_AND_SPL.md) — the false-SPL correction | ✅ | ❌ | ❌ | ❌ |
| [AD_ACCOUNTS_MAP.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/AD_ACCOUNTS_MAP.md) — CCA + SCIO | ✅ | ❌ | ❌ *(toggle unshipped)* | ❌ |
| EODR + team tracking + timetables (5 files) | ✅ | ❌ | ❌ | ❌ |
| Teramind suite (classification · export spec · SOP · Carla card · 2 scripts · MCP server) | ✅ | ❌ | ❌ | ❌ |
| SOP v1.18→v1.21 · rulings #22–30 | ✅ | ❌ | ❌ | ❌ |

## ✅ THE FIX, IN ORDER
1. **Wire Obsidian** — routed to Lane 4 (cloud lanes cannot reach a local vault). Simplest working design: point an Obsidian vault at the cloned repo's `ops/` folder. Zero sync code — Obsidian reads markdown natively, so **every file already written becomes a linked note the moment the vault opens on that folder.** This is a 2-minute fix for a 0% surface.
2. **Sync Notion #139–161** — 23 rows including the Vault Law itself.
3. **Lane 2: ship the board.** It is the face of the Vault and it is showing last week's face.
4. **Lane 4: confirm the local clone is current.**
