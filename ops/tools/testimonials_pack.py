#!/usr/bin/env python3
"""Pack every testimonial card into ONE zip with AI-sortable filenames + a manifest.
Filename = APW__<type>__<FirstName>__<profession>__<YYYY-MM-DD>__<quote-slug>__<public|internal>__<square|story>.png
type: result (a measurable outcome the client reported) or praise (feedback about APW / Alan).
Manifest: MANIFEST.csv + MANIFEST.json (filename, name, first name, type, date, profession, verbatim quote, proof link).
"""
import json, re, csv, zipfile, pathlib
R = pathlib.Path(__file__).resolve().parents[2]; T = R/"ops/data/testimonials"
C = json.load(open(T/"cards.json"))
RESULT = re.compile(r"uptick in scores|reset up in the States|great work|making progress|good hands", re.I)
slug = lambda s: re.sub(r"[^a-z0-9]+","-", s.lower()).strip("-")
rows = []
z = zipfile.ZipFile(T/"APW-PHOTOS-ALL.zip", "w", zipfile.ZIP_DEFLATED)
for c in C["cards"]:
    typ = "result" if RESULT.search(c["text"]) else "praise"
    prof = slug(C["people"][c["person"]].get("public_bg", c["background"]).split("·")[0])[:30]
    qs = slug(" ".join(re.sub(r"[^\w\s]", "", c["text"]).split()[:6]))
    for ver, key in (("public","public_square"),("public","public_story"),("internal","square"),("internal","story")):
        f = c.get(key)
        if not f: continue
        fmt = "story" if "story" in f else "square"
        name = f"APW__{typ}__{c['first_name'] if ver=='public' else slug(c['person'])}__{prof}__{c['date']}__{qs}__{ver}__{fmt}.png"
        z.write(T/"cards"/f, name)
        rows.append(dict(filename=name, type=typ, version=ver, format=fmt, first_name=c["first_name"], full_name=c["person"],
                         profession=C["people"][c["person"]].get("public_bg", c["background"]), date=c["date"], quote=c["text"], source=c["source"], proof=c["proof"]))
with open(T/"MANIFEST.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
(T/"MANIFEST.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
z.write(T/"MANIFEST.csv","MANIFEST.csv"); z.write(T/"MANIFEST.json","MANIFEST.json"); z.write(T/"TESTIMONIALS.txt","ALL-QUOTES.txt")
z.writestr("README.txt","APW testimonial cards. Filename = APW__type__name__profession__date__quote__public|internal__square|story.png\ntype: result = measurable outcome the client reported; praise = feedback about APW/Alan.\npublic = first name only (ad-safe, clients only). internal = full name (sales team).\nMANIFEST.csv/json map every file to the verbatim quote, date, profession and proof link.\n")
z.close(); print(len(rows), "files packed ->", T/"APW-PHOTOS-ALL.zip")
