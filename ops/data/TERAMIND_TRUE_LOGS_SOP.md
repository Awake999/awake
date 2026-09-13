# 🔐 TERAMIND TRUE LOGS — three rails, all built (register #150)
*2026-09-02 · Alan: "is there MCP? or how can we get the true logs" + "ideally avoiding API fees through claude, just keeping the normal system how we have it here with private integrations keys etc normal claude 20x included stuff" · "do it for me".*

**💸 COST, settled first: none of this bills Anthropic.** There is **no Teramind MCP server in the connector registry** [V — searched 2026-09-02, nearest hits were ClickUp/Otter/Grain, all unrelated]. Everything below runs on the plan you already pay for: MCP connectors and Claude Code on the 20x plan are not per-call billed, and Teramind's API is part of your Teramind licence. Private keys stay in `apw-intel/.env` on your PC — **never in this repo**, same rule as `GHL_TOKEN`.

---

## 🥇 RAIL 1 — scheduled report → email → read automatically (5 min, do this first)
Zero code, zero keys, nothing to maintain. The daily Teramind digest already reaches support@; this just makes it a *real* report instead of a top-3 teaser.

1. Teramind → **Reports** (or **BI Reports**) → **+ New / Create report**
2. Report type: **User Activity** (or *Productivity by User*). Add columns: **user · date · interval · active time · idle time · application/website**
3. Group by **User**, granularity **10 minutes** if the picker offers it (else 30 min — still far better than the digest)
4. **Schedule** → Daily → around **9:00 PM PT** → deliver to **support@ascendprimewealth.com** → format **CSV** (fall back to inline/HTML if CSV isn't offered — the body is readable either way)
5. Save. That's it — the nightly team-tracking report starts using real interval data on the next delivery.

## 🥈 RAIL 2 — the local pull script (already written, same pattern as GHL)
**[`ops/lane4/teramind_pull.py`](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/lane4/teramind_pull.py)** — mirrors `ghl_pull_details.py`: key from the local `.env`, raw JSON + a flat CSV committed to `ops/archive/teramind/<date>/`, so every future analysis has real history to sit on.

**On the PC, paste this:**
```bash
# 1. add the key (Teramind → Settings → API / Access tokens)
echo 'TERAMIND_API_KEY=<paste-key-here>' >> ~/apw-intel/.env
echo 'TERAMIND_INSTANCE=ascendprimew.us.teramind.co' >> ~/apw-intel/.env

# 2. find the right API base for your Teramind version (it varies — the script probes, it does not guess)
python3 ops/lane4/teramind_pull.py --discover
#    → prints the working path, e.g.  TERAMIND_API_BASE=/api/v1
echo 'TERAMIND_API_BASE=/api/v1' >> ~/apw-intel/.env   # use whatever --discover printed

# 3. pull
python3 ops/lane4/teramind_pull.py 2026-09-01
git add ops/archive/teramind && git commit -m "Teramind pull 2026-09-01" && git push
```

## 🥉 RAIL 3 — the local MCP server (written, optional)
**[`ops/mcp/teramind_mcp_server.py`](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/mcp/teramind_mcp_server.py)** — runs on the PC over stdio, so Claude Code can query Teramind **live** instead of reading yesterday's file. Still no API fees: your machine, your Teramind licence.

```bash
pip install "mcp[cli]"
claude mcp add teramind -- python3 ~/awake/ops/mcp/teramind_mcp_server.py
```
Gives Claude: `list_users` (**the real roster — the fix for the digest top-3 problem, ruling #27**) · `activity` · `timeline` (10-minute intervals) · `applications` · `raw` (escape hatch for any endpoint).

---

## ⚠️ THE ONE HONEST UNKNOWN
Teramind's REST base path and report endpoint names **differ by deployment and version**, and I have not verified yours. So neither the script nor the MCP server hard-codes an endpoint as if it were fact: `--discover` probes the documented candidates (`/api/v1`, `/rest/v1`, `/api`, `/bi/api/v1`) and tells you which one answers. If none do, the API docs live at your instance (Settings → API) and one line in `.env` fixes it. **Rail 1 needs none of this** — which is why it is first.

## 🎯 WHAT EACH RAIL UNLOCKS
| | Rail 1 email | Rail 2 script | Rail 3 MCP |
|---|---|---|---|
| Effort | 5 min clicking | 5 min paste | 10 min install |
| True 10-min intervals | ✅ if the picker offers it | ✅ | ✅ |
| Real roster (kills the top-3 problem) | ✅ | ✅ | ✅ |
| Committed history in the repo | ✗ | ✅ | ✗ |
| Live querying, any time | ✗ | ✗ | ✅ |
| Anything to maintain | none | one script | one process |
