#!/usr/bin/env bash
# APW DAILY — run this once a day. It does the whole thing.
#   1 pull  2 (optional) API pull  3 build the page  4 push  5 open it
set -uo pipefail
cd "$(dirname "$0")/../.."
echo "== APW DAILY =============================================="
echo " Repo: $PWD"; echo

echo "[1/5] Pulling latest law + tools…"
git pull --quiet || echo "  (pull failed — continuing with the local copy)"

echo "[2/5] Trying the Teramind API (skipped if no key)…"
python3 ops/lane4/teramind_pull.py 2>/dev/null || echo "  (no API key or endpoint yet — will use the CSV inbox)"

echo "[3/5] Building today's page…"
if ! python3 ops/tools/teramind_daily.py; then
  cat <<'MSG'

  >> NO DATA YET. Do this once, it takes 60 seconds:
     Teramind → Reports → Web & Applications → set today → Export CSV
     Save the file into:  ops/archive/teramind/inbox/
     Then run this script again.

  To see the exact layout right now with sample data:
     python3 ops/tools/teramind_daily.py --demo
MSG
  exit 2
fi

echo "[4/5] Saving to the Vault…"
git add ops/data/teramind ops/data/TERAMIND_TODAY.md ops/archive/teramind 2>/dev/null
git commit -q -m "APW daily: Teramind page for $(date +%F)" 2>/dev/null || echo "  (nothing new to commit)"
git push -u origin claude/new-session-1ofk4w --quiet || echo "  (push failed — run it again when back online)"

echo "[5/5] Opening the page…"
URL="https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/TERAMIND_TODAY.md"
( command -v xdg-open >/dev/null && xdg-open "$URL" ) 2>/dev/null || \
( command -v open >/dev/null && open "$URL" ) 2>/dev/null || echo "  Open: $URL"

echo; echo "== DONE. That page is today's answer to 'what is everyone doing'. =="
