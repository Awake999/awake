@echo off
REM ============================================================
REM  APW PULL ALL  -  double-click on the PC. Full pull:
REM  GHL (live) + Teramind (full export) + dropped-leads + push.
REM  Nothing touches any cloud lane. Creds stay in ..\apw-intel\.env.
REM ============================================================
setlocal
cd /d "%~dp0\..\.."
echo == APW PULL ALL ==  repo: %CD%
echo [1/6] git pull
git pull --quiet || echo   (pull failed - using local copy)
echo [2/6] GHL live pull (uses GHL_TOKEN in ..\apw-intel\.env)
python ops\lane4\ghl_full_pull.py || echo   (GHL pull failed - check GHL_TOKEN)
echo [2b/6] GHL call recordings + transcriptions (every answered call; add --audio for mp3s)
python ops\lane4\ghl_pull_recordings.py || echo   (recordings pull failed - token or API; transcripts stay as-is)
echo [3/6] GHL derived tables
python ops\lane4\ghl_derive.py 2>nul || echo   (derive skipped)
echo [4/6] Rebuild dropped-leads page from fresh pull
python ops\tools\dropped_leads.py || echo   (dropped-leads rebuild skipped)
echo [5/6] Teramind FULL export (only if key present)
findstr /b "TERAMIND_API_KEY=" ..\apw-intel\.env >nul 2>&1
if %errorlevel%==0 (
  python ops\lane4\teramind_pull.py --all 2026-07-07
  python ops\lane4\teramind_pull.py --video-download
) else (
  echo   SKIPPED. Teramind - your username top-right - Access Tokens - ADD ACCESS TOKEN,
  echo   then add a line  TERAMIND_API_KEY=paste  to  ..\apw-intel\.env  and run again.
)
echo [6/6] Save to the Vault
git add ops/archive/ghl ops/archive/teramind ops/data/DROPPED_LEADS_LIVE.md >nul 2>&1
git commit -q -m "APW pull-all: GHL live + Teramind export + dropped-leads (%date%)" >nul 2>&1 || echo   (nothing new)
git push -u origin claude/new-session-1ofk4w --quiet || echo   (push failed - rerun when online)
echo == DONE. Do NOT cancel Teramind until ops\archive\teramind\export\EXPORT_LOG.txt says DONE.
pause
