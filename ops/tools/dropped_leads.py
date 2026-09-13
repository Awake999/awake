#!/usr/bin/env python3
"""Regenerate the dropped-leads follow-up page from the NEWEST GHL pull.

Safe + stdlib-only. Reads the latest ops/archive/ghl/<date>/raw/ that exists
(refreshed by ghl_full_pull.py on the PC) and writes a live, setter-ready page:
every lead who sent the last message and got no reply, minus opt-outs and B2B
spam, each with a one-click GHL deep-link and days-silent to today.

    python3 ops/tools/dropped_leads.py            # uses newest pull, silent-to = today
"""
import json, re, datetime, pathlib, sys
REPO = pathlib.Path(__file__).resolve().parent.parent.parent
GHL = REPO / "ops" / "archive" / "ghl"
LOC = "WFkoNzKa9J9PxhngsLfl"
OUT = REPO / "ops" / "data" / "DROPPED_LEADS_LIVE.md"

def newest_raw():
    days = sorted([p for p in GHL.iterdir() if p.is_dir() and re.match(r"\d{4}-\d{2}-\d{2}$", p.name)])
    for d in reversed(days):
        if (d / "raw" / "messages_by_conversation.json").exists():
            return d.name, d / "raw"
    sys.exit("no GHL pull with messages found under ops/archive/ghl/")

def main():
    date, raw = newest_raw()
    msgs = json.load(open(raw / "messages_by_conversation.json"))
    contacts = {c["id"]: c for c in json.load(open(raw / "contacts.json"))}
    today = datetime.datetime.now(datetime.timezone.utc)
    g = lambda x: (x or "")
    url = lambda cid: f"https://app.gohighlevel.com/v2/location/{LOC}/contacts/detail/{cid}"
    optout = re.compile(r"dnd enabled|^\s*(stop|unsubscribe|remove me|opt.?out)\s*$", re.I)
    # RULE (register #180): a reply is a WRITTEN SMS/email, or a call that connected.
    # Type-based, not text-based — text matching kept hiding people (Greco, P Reddy).
    SMS, EMAIL, CALL = 2, 3, 1
    autotxt = re.compile(r"your appointment (has been scheduled|is confirmed)"
                         r"|thank you for your appointment|please share your feedback"
                         r"|see you in 15 minutes|sent you a document|view document"
                         r"|reply stop|unsubscribe", re.I)
    def is_reply(m):
        if m.get("direction") != "outbound":
            return False
        t = m.get("type")
        if t in (SMS, EMAIL):
            b = g(m.get("body")).strip()
            return len(b) > 3 and not autotxt.search(b)
        if t == CALL:
            return (((m.get("meta") or {}).get("call") or {}).get("duration") or 0) >= 30
        return False   # activities, reactions, blank bodies are never a reply

    junk_tag = re.compile(r"name via lookup|couldn.t find caller", re.I)
    junk_body = re.compile(r"\bstop\b|reply help|dispute credit report|yelp|reminder:|consultation|unsubscribe", re.I)
    staff = re.compile(r"ascend|support team|\bliza\b|blossom|^test", re.I)
    rows = []
    for conv, arr in msgs.items():
        ms = sorted([m for m in arr if m.get("dateAdded")], key=lambda m: m["dateAdded"])
        if not ms:
            continue
        ins = [m for m in ms if m.get("direction") == "inbound" and m.get("type") in (2, 3, 45)
               and len(g(m.get("body")).strip()) > 3]
        if not ins:
            continue
        last = ins[-1]
        human_out = [m for m in ms if is_reply(m)]
        if human_out and human_out[-1]["dateAdded"] > last["dateAdded"]:
            continue          # a real person wrote back or a call connected
        bot_only = any(m for m in ms if m.get("direction") == "outbound"
                       and m["dateAdded"] > last["dateAdded"])
        c = contacts.get(last.get("contactId"), {})
        name = g(c.get("contactName")) or (g(c.get("firstName")) + " " + g(c.get("lastName"))).strip()
        tags = ",".join(c.get("tags", []))
        body = g(last.get("body")).strip().replace("\n", " ")
        if optout.search(body) or junk_tag.search(tags) or junk_body.search(body):
            continue
        if not name or staff.search(name):
            continue
        real_in = [m for m in ms if m.get("direction") == "inbound" and len(g(m.get("body")).strip()) > 3]
        if not real_in:
            continue
        li = datetime.datetime.fromisoformat(last["dateAdded"].replace("Z", "+00:00"))
        rows.append({"name": name, "phone": g(c.get("phone")), "cid": last.get("contactId"),
                     "tags": tags, "when": last["dateAdded"][:10],
                     "silent": round((today - li).total_seconds() / 86400, 1),
                     "last": body[:220], "bot_only": bot_only,
                     "n_in": sum(1 for m in ms if m["direction"] == "inbound"),
                     "n_out": sum(1 for m in ms if m["direction"] == "outbound")})
    rows.sort(key=lambda r: r["when"], reverse=True)
    L = [f"# 📞 LEADS WE DROPPED — LIVE (auto-generated {today:%Y-%m-%d %H:%M UTC})",
         "",
         f"*Source: GHL pull **{date}** · {len(msgs)} conversations scanned · {len(rows)} leads got **no human reply** after their last message.*",
         "*Auto-built by `ops/tools/dropped_leads.py`. For the narrated, setter-friendly version see [DROPPED_LEADS_FOLLOWUP.md](DROPPED_LEADS_FOLLOWUP.md).*",
         "", "Excluded automatically: `DnD`/opt-outs (compliance stops), B2B \"name via lookup\" spam, our-side-only threads.",
         "", "🤖 = only an automated message went out after they spoke. Nobody human ever replied.",
         "", "| Lead | Phone | Last THEY said | When | Silent (days) | in/out | Open GHL |",
         "|---|---|---|---|---|---|---|"]
    for r in rows:
        safe = r["last"].replace("|", "\\|")[:120]
        bot = " 🤖" if r["bot_only"] else ""
        L.append(f"| **{r['name']}**{bot} | {r['phone']} | {safe} | {r['when']} | {r['silent']} | {r['n_in']}/{r['n_out']} | [open]({url(r['cid'])}) |")
    OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} — {len(rows)} leads from GHL pull {date}")

if __name__ == "__main__":
    main()
