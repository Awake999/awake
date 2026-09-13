@echo off
REM ============================================================
REM  APW DAILY  -  double-click this. It does the whole thing.
REM  1 pull  2 (optional) API pull  3 build the page  4 push  5 open it
REM ============================================================
setlocal
cd /d "%~dp0\..\.."

echo.
echo == APW DAILY ================================================
echo  Repo: %CD%
echo.

echo [1/5] Pulling latest law + tools...
git pull --quiet || echo   (pull failed - continuing with the local copy)

echo [2/5] Trying the Teramind API (skipped if no key)...
python ops\lane4\teramind_pull.py 2>nul || echo   (no API key or endpoint yet - will use the CSV inbox)

echo [3/5] Building today's page...
python ops\tools\teramind_daily.py
if errorlevel 2 (
  echo.
  echo  ^>^> NO DATA YET. Do this once, it takes 60 seconds:
  echo     Teramind - Reports - Web ^& Applications - set today - Export CSV
  echo     Save the file into:  ops\archive\teramind\inbox\
  echo     Then double-click this file again.
  echo.
  echo  To see the exact layout right now with sample data:
  echo     python ops\tools\teramind_daily.py --demo
  pause
  exit /b 2
)

echo [4/5] Saving to the Vault...
git add ops/data/teramind ops/data/TERAMIND_TODAY.md ops/archive/teramind >nul 2>&1
git commit -q -m "APW daily: Teramind page for %date%" >nul 2>&1 || echo   (nothing new to commit)
git push -u origin claude/new-session-1ofk4w --quiet || echo   (push failed - run it again when back online)

echo [5/5] Opening the page...
start "" "https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/TERAMIND_TODAY.md"
start "" "ops\data\TERAMIND_TODAY.md"

echo.
echo == DONE. The page above is today's answer to "what is everyone doing". ==
pause
