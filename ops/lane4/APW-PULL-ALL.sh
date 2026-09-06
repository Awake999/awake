#!/usr/bin/env bash
# ============================================================
#  APW PULL ALL  —  run this on the PC. It does the whole pull:
#  GHL (live) + Teramind (full export) + rebuild dropped-leads + push.
#  Nothing touches any cloud lane. Creds stay in ../apw-intel/.env, never committed.
# ============================================================
set -uo pipefail
cd "$(dirname "$0")/../.." || exit 1
echo "== APW PULL ALL =====================  repo: $(pwd)"
echo "[1/6] git pull"; git pull --quiet || echo "  (pull failed, using local copy)"
echo "[2/6] GHL live pull (uses GHL_TOKEN in ../apw-intel/.env)"
python3 ops/lane4/ghl_full_pull.py || echo "  (GHL pull failed — check GHL_TOKEN in ../apw-intel/.env)"
echo "[3/6] GHL derived tables"; python3 ops/lane4/ghl_derive.py 2>/dev/null || echo "  (derive skipped)"
echo "[4/6] Rebuild dropped-leads page from the fresh pull"
python3 ops/tools/dropped_leads.py || echo "  (dropped-leads rebuild skipped)"
echo "[5/6] Teramind FULL export (only if TERAMIND_API_KEY is set)"
if grep -q '^TERAMIND_API_KEY=' ../apw-intel/.env 2>/dev/null; then
  python3 ops/lane4/teramind_pull.py --all 2026-07-07 && python3 ops/lane4/teramind_pull.py --video-download || echo "  (teramind export hit an error — see EXPORT_LOG)"
else
  echo "  SKIPPED. To include Teramind: Teramind → your username (top-right) → Access Tokens → ADD ACCESS TOKEN,"
  echo "  then:  echo 'TERAMIND_API_KEY=<paste>' >> ../apw-intel/.env   and run this again."
fi
echo "[6/6] Save to the Vault"
git add ops/archive/ghl ops/archive/teramind ops/data/DROPPED_LEADS_LIVE.md >/dev/null 2>&1
git commit -q -m "APW pull-all: GHL live + Teramind export + dropped-leads refresh ($(date +%F))" >/dev/null 2>&1 || echo "  (nothing new to commit)"
git push -u origin claude/new-session-1ofk4w --quiet && echo "  pushed." || echo "  (push failed — rerun when online)"
echo "== DONE. Do NOT cancel Teramind until ops/archive/teramind/export/EXPORT_LOG.txt says DONE."
