#!/usr/bin/env python3
"""Verify every row of ops/data/CLIENT_TESTIMONIALS.json against the raw source that lives in the repo.

  GHL SMS rows      -> exact substring of an inbound SMS body on that date for that contact
  Fathom rows       -> exact substring of the archived transcript line at that timestamp, if the call
                       is archived under ops/archive/calls/; otherwise reported as "not in repo" (verify live)
  GHL phone rows    -> exact substring of ops/archive/ghl/recordings/<folder>/transcript.md

Exit 1 on any mismatch. "not in repo" is not a failure but is listed so the reader knows what was
verified only against a live Fathom fetch.
"""
import json, re, html, pathlib, sys, glob

REPO = pathlib.Path(__file__).resolve().parents[2]
D = json.load(open(REPO/"ops/data/CLIENT_TESTIMONIALS.json"))
exports = sorted(p for p in (REPO/"ops/archive/ghl").iterdir() if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name))
norm = lambda s: re.sub(r"\s+", " ", s or "").strip()

sms = {}
for ex in exports:
    f = ex/"raw/messages_by_conversation.json"
    if not f.exists(): continue
    for conv, msgs in json.load(open(f)).items():
        for m in msgs:
            if m.get("direction") == "inbound" and m.get("type") in (2, 3):
                b = norm(html.unescape(re.sub(r"<[^>]+>", " ", m.get("body") or "")))
                sms.setdefault(m.get("contactId"), []).append((m.get("dateAdded", "")[:10], b))

# archived Fathom/Zoom transcripts: map url-number -> text
arch = {}
rec_id = D.get("recording_ids", {})
for f in glob.glob(str(REPO/"ops/archive/calls/**/transcript*"), recursive=True):
    try: t = open(f, errors="ignore").read()
    except Exception: continue
    nums = set(re.findall(r"fathom\.video/calls/(\d+)", t))
    folder = pathlib.Path(f).parent.name
    nums |= {u for u, r in rec_id.items() if folder.endswith("--" + r)}
    for n in nums:
        arch[n] = arch.get(n, "") + t
rec = {p.name: (p/"transcript.md").read_text(errors="ignore") for p in (REPO/"ops/archive/ghl/recordings").glob("*") if (p/"transcript.md").exists()} if (REPO/"ops/archive/ghl/recordings").exists() else {}

ok = bad = notrepo = 0
for p in D["people"]:
    for q in p["quotes"]:
        parts = [norm(x) for x in q["quote"].split("[…]")]
        src, link = q["source"], q["link"]
        if src.startswith("GHL SMS") or src.startswith("GHL email"):
            hit = any(q["date"] == d and all(x in b for x in parts) for d, b in sms.get(p["ghl_contact_id"], []))
        elif src.startswith("Fathom"):
            n = re.search(r"calls/(\d+)", link).group(1)
            if n not in arch:
                notrepo += 1; print(f"NOT IN REPO (verify live) {p['name']} {q['date']} {link}"); continue
            hit = all(x in norm(arch[n]) for x in parts)
        elif src.startswith("GHL phone"):
            folder = re.search(r"recordings/([^/]+)/", link)
            hit = bool(folder) and all(x in norm(rec.get(folder.group(1), "")) for x in parts)
        else:
            hit = False
        if hit: ok += 1
        else: bad += 1; print(f"MISMATCH {p['name']} {q['date']} {src} | {q['quote'][:90]}")
print(f"verified {ok} · mismatched {bad} · not-in-repo {notrepo} (of {ok+bad+notrepo})")
sys.exit(1 if bad else 0)
