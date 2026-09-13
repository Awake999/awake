#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Local Teramind MCP server for APW — runs on Alan's PC over stdio.
No Anthropic API fees: Claude Code talks to this process directly, and it talks
to Teramind with the private key that never leaves the machine.

INSTALL (one time, on the PC):
    pip install "mcp[cli]"
    # add the key to apw-intel/.env:  TERAMIND_API_KEY=...  TERAMIND_API_BASE=/api/v1
    claude mcp add teramind -- python3 <full path to this file>

Then Claude Code sees: mcp__teramind__list_users · mcp__teramind__activity ·
mcp__teramind__timeline · mcp__teramind__raw
"""
import os, json, pathlib, urllib.request, urllib.error

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    raise SystemExit("Missing dependency. Run:  pip install \"mcp[cli]\"")

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
ENVP = REPO.parent / "apw-intel" / ".env"
ENV = {}
if ENVP.exists():
    ENV = dict(l.split("=", 1) for l in ENVP.read_text().splitlines() if "=" in l and not l.startswith("#"))

INSTANCE = ENV.get("TERAMIND_INSTANCE", "ascendprimew.us.teramind.co").strip()
KEY = ENV.get("TERAMIND_API_KEY", "").strip()
BASE = ENV.get("TERAMIND_API_BASE", "/api/v1").strip()

mcp = FastMCP("teramind")

def _get(path: str, params: dict | None = None) -> str:
    if not KEY:
        return json.dumps({"error": f"TERAMIND_API_KEY missing from {ENVP}"})
    url = f"https://{INSTANCE}{BASE}{path}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items() if v)
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {KEY}", "Accept": "application/json",
        "User-Agent": "APW-ops-mcp/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode()
    except urllib.error.HTTPError as e:
        return json.dumps({"error": f"HTTP {e.code}", "url": url,
                           "hint": "wrong TERAMIND_API_BASE? run teramind_pull.py --discover"})
    except Exception as e:
        return json.dumps({"error": type(e).__name__, "url": url})

@mcp.tool()
def list_users() -> str:
    """List every monitored Teramind user — the real roster, not the digest top-3."""
    return _get("/users")

@mcp.tool()
def activity(date_from: str, date_to: str = "", user: str = "") -> str:
    """Per-user activity for a date range (YYYY-MM-DD). Optional user filter."""
    return _get("/reports/activity", {"from": date_from, "to": date_to or date_from, "user": user})

@mcp.tool()
def timeline(date_from: str, date_to: str = "", interval: str = "10m", user: str = "") -> str:
    """Interval timeline — the true 10-minute breakdown. interval e.g. 10m, 30m, 1h."""
    return _get("/reports/timeline", {"from": date_from, "to": date_to or date_from,
                                      "interval": interval, "user": user})

@mcp.tool()
def applications(date_from: str, date_to: str = "", user: str = "") -> str:
    """Application/website time per user for a date range."""
    return _get("/reports/applications", {"from": date_from, "to": date_to or date_from, "user": user})

@mcp.tool()
def raw(path: str, params_json: str = "{}") -> str:
    """Escape hatch: call any Teramind endpoint under the configured base.
    path like '/reports/productivity'; params_json a JSON object of query params."""
    try:
        params = json.loads(params_json or "{}")
    except Exception:
        return json.dumps({"error": "params_json must be a JSON object"})
    return _get(path, params)

if __name__ == "__main__":
    mcp.run()
