#!/usr/bin/env python3
"""Render downloadable testimonial cards (PNG) + a library page from the verified quote table.

Source of truth for quote text = ops/data/CLIENT_TESTIMONIALS.json (built by testimonials_build.py).
Each card's display text must be an exact contiguous substring of a verified quote ("[…]" allowed for
skipped words) — the script refuses to render anything else, so cards can never drift from the record.

Outputs
  ops/data/testimonials/cards/<person>--<n>--square.png   1080x1080 (feed)
  ops/data/testimonials/cards/<person>--<n>--story.png    1080x1920 (story / reel cover)
  ops/data/testimonials/LIBRARY.md                         gallery: preview · quote · person · background · date · proof link · downloads
  ops/data/testimonials/cards.json                         machine-readable index

Photos: drop a headshot at ops/data/testimonials/photos/<person-slug>.jpg (or .png) and re-run; the card
uses it automatically. Until then the card shows the person's initials. No likeness is used in ads
without a consent row in REGISTER.md.

Run: python3 ops/tools/testimonials_cards.py   (needs the pre-installed Chromium at CHROME)
"""
import json, re, pathlib, subprocess, html, base64, sys, datetime

REPO = pathlib.Path(__file__).resolve().parents[2]
OUT = REPO/"ops/data/testimonials"; CARDS = OUT/"cards"; PHOTOS = OUT/"photos"
CARDS.mkdir(parents=True, exist_ok=True); PHOTOS.mkdir(exist_ok=True)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
RAW = "https://raw.githubusercontent.com/Awake999/awake/claude/new-session-1ofk4w/ops/data/testimonials/cards/"
D = json.load(open(REPO/"ops/data/CLIENT_TESTIMONIALS.json"))
Q = {p["name"]: p for p in D["people"]}
def F(call, sec): return f"https://fathom.video/calls/{call}?timestamp={sec}"

# ---- who they are, in their own words, each with the line it comes from ----------------------
PEOPLE = {
 "Matthew LoGuidice": dict(bg="Tech-startup founder · formerly owned 300 apartments", public_bg="Tech-startup founder · former multifamily owner", proof=F(723857619,1800), proof_note="6/25 call: \"I got to raise some more money for my startup tech company\" (11:40) · \"I used to own 300 apartments\" (30:01)"),
 "Ashwini Anand":     dict(bg="Cardiologist", proof=F(764436554,359), proof_note="7/29 call: \"you know me, I'm a busy cardiologist\" (5:59)"),
 "Michael Moore":     dict(bg="Physician · opening a holistic wellness med spa in North Carolina", public_bg="Physician · opening a wellness med spa", proof=F(795906439,1896), proof_note="8/26 call: \"as a physician\" (3:33) · \"a wellness medical spa\" (31:36)"),
 "Nick (Nazir) Samara": dict(bg="Family-entertainment business owner (indoor playland → outdoor events)", public_bg="Family-entertainment business owner", proof=F(795906442,1108), proof_note="8/25 call: \"indoor playland for family, children… we used to have multiple locations\" (18:28)"),
 "Yeshaya Dank":      dict(bg="Serial entrepreneur · 13 businesses, 7 more in development", proof=F(783351348,3844), proof_note="8/14 call: \"I have like 13 businesses and another seven in development\" (1:04:04)"),
 "Ed (Edwin) Choi":   dict(bg="Owner of multiple medical clinics incl. a cosmetic-surgery practice", public_bg="Owner of multiple medical clinics", proof=F(728895030,802), proof_note="6/30 call: \"Jonah Medical Group, Nanum Medical Group, VM Cosmetic Surgery\" (13:22) · \"one of my clinics\" (9:32)"),
 "Jill Peralta":      dict(bg="20-year military veteran · Space Force acquisitions program manager · acquiring a beauty business", public_bg="20-year military veteran · acquiring a beauty business", proof=F(739063325,1335), proof_note="7/9 call: \"I'm a veteran, 20 years\" (11:58) · \"Space Force… program manager, acquisitions field\" (22:15) · \"beauty industry, teeth whitening\" (3:39)"),
 "Allen Sims":        dict(client=False, bg="Financial advisor (Northwestern Mutual) · startup founder", proof=F(759494613,0), proof_note="7/27 call: \"I'm a financial advisor for Northwestern Mutual\""),
 "Gunjan Patel":      dict(client=False, bg="Acquiring a pharmacy · works with medical-practice owners", proof=F(767888047,2255), proof_note="8/1 call: \"After I acquire a pharmacy\" (37:35)"),
}

# ---- which quotes become cards: (person, exact display text). Display text must be a contiguous
#      substring of a verified quote (or pieces joined by "[…]"). Order = library order. -------------
CARD_QUOTES = [
 ("Matthew LoGuidice", "I've worked with consultants for 30 years, he might be the most diligent, you know, guy, just , honestly, just amazing so far, amazing. And he puts up with me"),
 ("Matthew LoGuidice", "You deserve a gold medal and a huge bonus for putting up with me I appreciate your unending patience with me"),
 ("Matthew LoGuidice", "You've been tremendously helpful I can't thank you enough for all the efforts of you and your team"),
 ("Matthew LoGuidice", "Wow!!!!! Thanks Alan Great work!!!!"),
 ("Ashwini Anand", "I would go for it a 10 out of 10. That is exactly what I want to do. […] this is a wonderful thing that you're doing."),
 ("Ashwini Anand", "I was just telling my wife that this should be a godsend."),
 ("Ashwini Anand", "I feel like I'm in good hands with you"),
 ("Ashwini Anand", "Awesome job Alan!!! Unbelievable! Looks like all 3 bureaus have reported a huge uptick in scores."),
 ("Ashwini Anand", "I'm absolutely enjoying our new found association and friendship. It's wonderful to have you watch out for me."),
 ("Michael Moore", "you're such a nice person. your disposition is wonderful and you're very patient."),
 ("Michael Moore", "I have never spoken to anyone like yourself. […] what I'm hearing from you is something very ingenious and creative. And I really wholeheartedly appreciate what you're doing"),
 ("Michael Moore", "thank you very much. I'm very grateful."),
 ("Nick (Nazir) Samara", "You are the man."),
 ("Nick (Nazir) Samara", "the way you handle the business and your optimization for anything is very impressive and you're doing a wonderful job."),
 ("Nick (Nazir) Samara", "Alan, you're amazing young man. have very good knowledge, and the way you're patient, too, with your client, that's a good thing."),
 ("Nick (Nazir) Samara", "You could be teaching this stuff."),
 ("Yeshaya Dank", "Thank you so much for your time Alan! Your incredible. I learned so much during that 1.5 hours"),
 ("Yeshaya Dank", "I really appreciate your service because you made it possible for me to get like reset up in the States."),
 ("Yeshaya Dank", "your business is like, it's very smart. It's like a smart business"),
 ("Ed (Edwin) Choi", "Very good. Let's take forward to working with you."),
 ("Jill Peralta", "this was much better. […] I feel like I'm actually making progress."),
 ("Allen Sims", "But the best presentation and the best deal, overall deal."),
 ("Allen Sims", "the way you explain it, how your process sounds amazing, to be honest. It sounds amazing."),
]

norm = lambda s: re.sub(r"\s+", " ", s).strip()
def find_source(person, text):
    parts = [norm(x) for x in text.split("[…]")]
    for q in Q[person]["quotes"]:
        src = norm(q["quote"].replace("[…]", " "))
        pos, ok = 0, True
        for x in parts:
            i = src.find(x, pos)
            if i < 0: ok = False; break
            pos = i + len(x)
        if ok: return q
    return None

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def initials(n): return "".join(w[0] for w in re.sub(r"\(.*?\)", "", n).split()[:2]).upper()
def nice_date(d): return datetime.date.fromisoformat(d).strftime("%b %-d, %Y")
def photo_tag(person):
    for ext in ("jpg", "jpeg", "png"):
        p = PHOTOS/f"{slug(person)}.{ext}"
        if p.exists():
            b64 = base64.b64encode(p.read_bytes()).decode()
            return f'<img src="data:image/{ext};base64,{b64}" style="width:100%;height:100%;object-fit:cover">'
    return f'<div class="mono">{initials(person)}</div>'

CSS = """
*{box-sizing:border-box} body{margin:0;background:#0B1F3A;color:#fff;font-family:'DejaVu Sans','Liberation Sans',sans-serif}
.card{width:%dpx;height:%dpx;position:relative;padding:%dpx;display:flex;flex-direction:column;justify-content:space-between;
 overflow:hidden;background:radial-gradient(1200px 800px at 80%% -10%%,#17406f 0%%,#0B1F3A 55%%,#071427 100%%)}
.brand{font-size:%dpx;letter-spacing:.32em;text-transform:uppercase;color:#D4A947;font-weight:700}
.brand small{display:block;letter-spacing:.12em;color:#9fb3cc;font-weight:400;margin-top:10px;text-transform:none;font-size:%dpx}
.qmark{font-family:'DejaVu Serif','Liberation Serif',serif;font-size:%dpx;line-height:.6;color:#D4A947;margin-top:%dpx}
.mid{flex:1 1 0;min-height:0;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:24px 0}
.quote{font-family:'DejaVu Serif','Liberation Serif',serif;font-size:%dpx;line-height:1.28;font-weight:700;margin-top:%dpx}
.who{display:flex;align-items:center;gap:%dpx;margin-top:%dpx}
.av{width:%dpx;height:%dpx;border-radius:50%%;overflow:hidden;background:#D4A947;flex:none;display:flex;align-items:center;justify-content:center}
.mono{font-size:%dpx;font-weight:700;color:#0B1F3A}
.name{font-size:%dpx;font-weight:700} .bg{font-size:%dpx;color:#c9d6e6;margin-top:6px;max-width:%dpx}
.foot{font-size:%dpx;color:#8fa3bd;margin-top:%dpx;display:flex;justify-content:space-between;gap:20px}
.foot b{color:#D4A947}
"""
def css(w, h, pad, story):
    s = 1.0 if not story else 1.0
    return CSS % (w, h, pad, 26, 22, 220, 30, 0, 24, 28, 60, 130, 130, 52, 40, 30, w-2*pad-190, 22, 60)

def quote_size(text, story):
    n = len(text)
    base = 74 if n < 60 else 60 if n < 110 else 48 if n < 170 else 40 if n < 230 else 34
    return base + (12 if story else 0)

def first_name(n): return re.sub(r"\(.*?\)", "", n).split()[0]
def render(idx, person, text, q, story, public=False):
    w, h, pad = (1080, 1920, 96) if story else (1080, 1080, 84)
    shown = first_name(person) if public else person
    mono = f'<div class="mono">{shown[0]}</div>' if public else photo_tag(person)
    src = "Fathom call recording" if q["source"].startswith("Fathom") else "text message to APW" if "SMS" in q["source"] else q["source"]
    body = f"""<!doctype html><html><head><meta charset="utf-8"><style>{css(w,h,pad,story)} .quote{{font-size:{quote_size(text,story)}px}}</style></head><body>
<div class="card">
 <div><div class="brand">Ascend Prime Wealth<small>Client feedback · verbatim, on the record</small></div>
  </div>
 <div class="mid"><div class="qmark">&ldquo;</div>
  <div class="quote">{html.escape(text)}&rdquo;</div></div>
 <div>
  <div class="who"><div class="av">{mono}</div><div><div class="name">{html.escape(shown)}</div><div class="bg">{html.escape(PEOPLE[person].get('public_bg', PEOPLE[person]['bg']) if public else PEOPLE[person]['bg'])}</div></div></div>
  <div class="foot"><span><b>{nice_date(q['date'])}</b> · {src}</span><span>verified · ascendprimewealth.com</span></div>
 </div></div></body></html>"""
    kind = ("public-" if public else "") + ("story" if story else "square")
    name = f"{slug(person)}--{idx:02d}--{kind}"
    hp = CARDS/f"{name}.html"; png = CARDS/f"{name}.png"
    hp.write_text(body)
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={w},{h+140}", f"--screenshot={png}", f"file://{hp}"], capture_output=True, timeout=90)
    hp.unlink()
    from PIL import Image
    im = Image.open(png); im.crop((0, 0, w, h)).save(png, optimize=True)
    return png.name

rows = []; per = {}
for person, text in CARD_QUOTES:
    q = find_source(person, text)
    if not q: sys.exit(f"REFUSED: card text is not a verbatim substring of any verified quote — {person}: {text[:60]}")
    per[person] = per.get(person, 0) + 1; i = per[person]
    sq = render(i, person, text, q, False); st = render(i, person, text, q, True)
    is_client = PEOPLE[person].get("client", True)
    psq = render(i, person, text, q, False, public=True) if is_client else None
    pst = render(i, person, text, q, True, public=True) if is_client else None
    rows.append(dict(person=person, first_name=first_name(person), client=is_client, n=i, text=text, date=q["date"], source=q["source"], proof=q["link"], note=q.get("note",""),
                     background=PEOPLE[person]["bg"], background_proof=PEOPLE[person]["proof"], square=sq, story=st, public_square=psq, public_story=pst))
    print("rendered", sq, st)

# ---- library page ------------------------------------------------------------------------------
L = ["# Testimonial card library — Ascend Prime Wealth\n",
     f"**Built:** {datetime.date.today()} · **Cards:** {len(rows)} quotes × 2 formats (square 1080×1080, story 1080×1920) × 2 versions (public first-name / internal full-name) · **Generator:** `ops/tools/testimonials_cards.py` · **Quote record:** [CLIENT_TESTIMONIALS.md](../CLIENT_TESTIMONIALS.md)\n",
     "Every card's text is a verbatim, contiguous excerpt of a quote in the record (the generator refuses anything else). `[…]` marks skipped words. Click **proof** to jump to the second of audio or the GHL thread. Click a download link, then *Save image as…* (or use the raw URL directly in an ad tool).\n",
     "**Photos:** no client headshot exists in GHL (0 of 259 contacts have a profile photo) and I do not pull faces off the web. Cards show initials until a headshot is dropped at `ops/data/testimonials/photos/<person-slug>.jpg` and the generator is re-run.\n",
     "**Consent (Alan, 2026-09-07, REGISTER #187):** *\"i already have everyone's signature and consent when coming on as a client\"* — the client agreement signed at onboarding covers use of feedback. **Public set = first-name-only cards, clients only.** Allen Sims and Gunjan Patel were prospects (no client agreement), so they have internal cards only, no public variant.\n",
     "**Two versions of every client card:** *internal* (full name, specific background) for the sales team and the record, *public* (first name only, profession-only background) for ads and social.\n",
     "## People\n| Person | Background (their own words, linked) | Cards | Headshot |\n|---|---|---|---|"]
for p, info in PEOPLE.items():
    n = sum(1 for r in rows if r["person"] == p)
    has = any((PHOTOS/f"{slug(p)}.{e}").exists() for e in ("jpg","jpeg","png"))
    L.append(f"| **{p}** | {info['bg']} — [proof]({info['proof']}) <sub>{info['proof_note']}</sub> | {n} | {'✅' if has else 'initials (drop `photos/'+slug(p)+'.jpg`)'} |")
L.append("\n## Cards\n| Public preview (first name) | Quote (verbatim) | Who · when | Proof | Download — PUBLIC (ads) | Download — internal (full name) |\n|---|---|---|---|---|---|")
for r in rows:
    prev = r['public_square'] or r['square']
    pub = f"[square]({RAW}{r['public_square']}) · [story]({RAW}{r['public_story']})" if r['public_square'] else "— prospect, no client agreement"
    L.append(f"| <img src=\"cards/{prev}\" width=\"220\"> | *\"{r['text']}\"* | **{r['person']}** — {r['background']}<br>{nice_date(r['date'])} · {r['source']} | [proof]({r['proof']}) | {pub} | [square]({RAW}{r['square']}) · [story]({RAW}{r['story']}) |")
L.append("\n## Not carded, on purpose\n- **Teresa Graham** (med-spa owner + a second brand, Luxovia): her 9/2 call has no line about APW itself — her praise is about her own debt-relief work — so no card until she says something on the record.\n- **Whitney Young**: no verified positive line on any recording or text (see the record's Not-found table).\n- Matthew's *\"you seem like a very nice professional guy\"* (6/25): inside a tense pricing exchange — excluded by the context rule.\n- Mixed messages (Ashwini's 10/10 work / 2/10 communication) are quoted whole in the record and not carded.\n")
(OUT/"LIBRARY.md").write_text("\n".join(L) + "\n")
(OUT/"cards.json").write_text(json.dumps(dict(built=str(datetime.date.today()), raw_base=RAW, people=PEOPLE, cards=rows), indent=1, ensure_ascii=False))
print(f"{len(rows)} cards · library at {OUT/'LIBRARY.md'}")
