# 🏷 TERAMIND APP CLASSIFICATION — the APW list (register #156)
*2026-09-03 · Built because the activity % is currently uncalibrated: Alan scored **43% on a day containing a 2-hour closing call**. Until apps are classified, the number cannot tell a sales call from an idle screen. Paste-ready — one pass, ~15 minutes.*

**Where:** Teramind → **Configurations → Productivity Profiles** (classify apps/sites) and **Configurations → Monitoring Profiles** (capture + idle settings). Apply to **All Users** first, then add the role exceptions in §4.

---

## 1️⃣ PRODUCTIVE — the core stack
**CRM / pipeline**
`app.gohighlevel.com` · `gohighlevel.com` · `leadconnectorhq.com`

**Comms & meetings** *(also see §3 — these must be excluded from idle detection)*
`zoom.us` · `us06web.zoom.us` · `Zoom.exe` · `meet.google.com` · `slack.com` · `app.slack.com` · `Slack.exe` · `mail.google.com`

**Docs, ops & knowledge**
`notion.so` · `app.notion.com` · `trello.com` · `docs.google.com` · `sheets.google.com` · `drive.google.com` · `claude.ai`

**Credit repair / dispute work** — the dispute team lives here
`experian.com` · `transunion.com` · `equifax.com` · `annualcreditreport.com` · `identitytheft.gov` · `reportfraud.ftc.gov` · `consumerfinance.gov` · `kyoag.highq.com` · `oag.ca.gov` · *(add each state AG portal as it is used)* · `ilovepdf.com` · `creditkarma.com`

**Marketing & ads**
`business.facebook.com` · `adsmanager.facebook.com` · `app.manychat.com` · `manychat.com` · `submagic.co` · `vidalytics.com` · `loom.com` · `fathom.video`

**Money & agreements**
`whop.com` · `hellosign.com` · `app.hellosign.com` · `sendlink.co` · lender portals (`vikingfunding.com`, etc.)

**Training**
`skool.com` · `ascendprimew.us.teramind.co`

**Dev / technical**
`WindowsTerminal.exe` · `Code.exe` · `github.com`

---

## 2️⃣ NEUTRAL — do not penalise, do not reward
`youtube.com` — **⚠️ Neutral, NOT unproductive.** Lynn uses it for Submagic/editing reference and the team watches training there. Marking it unproductive punishes real work.
`google.com` search · `chrome.exe` (the browser shell itself) · `outlook`/webmail · `calendar.google.com` · `explorer.exe` · OS utilities · `spotify.com`

---

## 3️⃣ UNPRODUCTIVE — keep this list short and defensible
`netflix.com` · `hulu.com` · `disneyplus.com` · gaming sites/launchers · `amazon.com` *(shopping — but see the caveat below)* · dating/gambling sites

⚠️ **Deliberately NOT on this list:**
- **`instagram.com`, `tiktok.com`, `facebook.com` (personal feed)** — **these are work tools at APW now.** IG DMs feed ManyChat, TikTok carries content, Facebook runs the ads. Marking social unproductive would penalise Lynn and Carla for doing their jobs.
- **`glassdoor.com`, `indeed.com`, `linkedin.com`** — see §4; these are *hiring* tools for Alan and Carla.

---

## 4️⃣ ROLE EXCEPTIONS — where a flat list gets it wrong
| Site | Alan & Carla | Everyone else |
|---|---|---|
| `linkedin.com` · `glassdoor.com` · `indeed.com` | **PRODUCTIVE** — running the credit-specialist hiring campaign + APW LinkedIn build | Neutral, and the existing "job search websites" alert stays on |
| `instagram.com` · `tiktok.com` | **PRODUCTIVE** for Lynn & Carla (content + IG lead DMs) | Neutral |
| `amazon.com` | Neutral | Neutral |

**Also fix the false positive we already hit:** the *"Job search websites"* rule fired on Alan's own machine (`nguye@a51`) on 8/31 while he was doing hiring research. **Add an owner/manager exemption to that rule** or it will keep crying wolf.

---

## 5️⃣ THE SETTINGS THAT MATTER MORE THAN THE LIST
1. **⭐ Exclude Zoom / Meet / phone apps from idle detection.** On a call you listen more than you type. This single setting is the likeliest cause of Alan's 43% on a 2-hour-sales-call day, and of Carla's 40% across seven meeting hours.
2. **Raise the idle timeout to 10+ minutes** (default is usually 3–5). Reading a credit report or a contract is work; short timeouts score it as absence.
3. **Turn ON IM/chat capture** — off for three days running. Most of this team's coordination is Slack; right now the digest measures the smallest channel they use.
4. **Set working hours per user** so overnight/weekend idling doesn't drag the daily percentage.

---

## 6️⃣ VERIFY IT WORKED
Re-check **Sep 2** after applying: Alan's day contained a **2-hour Teresa Graham sales call** and read **43%**. If the same day now reads meaningfully higher, the classification is live and the metric finally means something. Lynn's **36% → 48%** jump when her ManyChat/internet were fixed is the control case — it shows the number *does* move with reality once the inputs are right.

**Then, and only then, raise the frequency.** More frequent reporting on an uncalibrated metric just delivers the same wrong number more often.
