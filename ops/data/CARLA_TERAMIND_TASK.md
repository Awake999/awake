# ✅ TERAMIND SETUP — task card for Carla
*From Alan, 2026-09-03. ~25 minutes total. Everything below is a setting; nothing here is destructive and all of it is reversible.*

## Part 1 — Export today's data (5 min) 🔴 DO FIRST
1. Teramind → **Reports → Web & Application Usage**
2. Range **Sep 1 – Sep 3**, Users: **All** → **Export CSV**
3. Repeat for **Time Records** and **Behavior Alerts**
4. Put all three CSVs in **Google Drive** and tell Alan they're there.

## Part 2 — Fix the settings so the numbers mean something (10 min)
Teramind → **Configurations → Monitoring Profiles**
- ✅ **Turn ON chat/IM capture** (off for 4 days — most of our coordination is Slack)
- ✅ **Exclude Zoom and Google Meet from idle detection** — on calls people listen, they don't type. This is why a 2-hour sales call currently scores as idle time.
- ✅ **Raise the idle timeout to 10+ minutes** (reading a credit report is work)
- ✅ **Set working hours** 7:00 AM – 5:00 PM PST per user
- ✅ **Add an owner/manager exemption to the "Job search websites" rule** — it fired on Alan's own machine during our hiring research

## Part 3 — Classify the apps (10 min)
Teramind → **Configurations → Productivity Profiles**. Use the full list here: **ops/data/TERAMIND_APP_CLASSIFICATION.md**
⚠️ **Two things that must not be got wrong:**
- **Instagram, TikTok and Facebook are PRODUCTIVE for Lynn and Carla** — IG DMs feed ManyChat, TikTok carries content, Facebook runs the ads. Do not mark social unproductive.
- **LinkedIn / Glassdoor / Indeed are PRODUCTIVE for Alan and Carla only** (the hiring campaign) — neutral for everyone else.

## Part 4 — Schedule it so nobody has to click again (5 min)
Teramind → **BI Reports → Create**: fields `user · date · interval · active · idle · productive · application · website · window title`, grouped by **User** then **Time**, granularity **10 minutes**, **scheduled every 4 hours → CSV → support@ascendprimewealth.com**.
Second report: alerts (`user · timestamp · rule · URL · action`) daily 9 PM PT to the same address.

**When Part 1 lands in Drive, the whole team timetable gets rebuilt at real resolution the same day.**
