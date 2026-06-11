import json, csv, re

cands = json.load(open("candidates.json"))
fdic = json.load(open("fdic_financials.json"))
ncua = json.load(open("ncua_financials.json"))
osm  = json.load(open("osm_banks.json"))

def norm(s):
    s = s.upper().replace("&"," AND ")
    s = re.sub(r'[^A-Z0-9 ]',' ',s)
    s = re.sub(r'\b(THE|OF|NATIONAL ASSOCIATION|N A|NA|FSB|FCU|FEDERAL CREDIT UNION|CREDIT UNION|TRUST COMPANY|BANK|BANC|FEDERAL|INC|COMPANY|CORP|CU)\b',' ',s)
    return ' '.join(s.split())

inst = {}
for r in cands:
    if r["miles"] > 10: continue
    e = inst.setdefault((r["src"], r["id"]), {"src":r["src"],"id":r["id"],"name":r["inst"],"branches":[]})
    e["branches"].append(r)
for e in inst.values():
    e["branches"].sort(key=lambda b: b["miles"])
    b = e["branches"][0]
    e["nearest"] = b; e["miles"] = b["miles"]
    e["n5"] = sum(1 for x in e["branches"] if x["miles"] <= 5)
    if e["src"]=="SOD":
        f = fdic[e["id"]]; e["type"]="Bank"
        e["asset_k"], e["dep_k"], e["hq"] = f["asset_k"], f["dep_k"], f["hq"]
        e["src_link"] = f"https://api.fdic.gov/banks/institutions?filters=CERT:{e['id']}&fields=NAME,ASSET,DEP"
    else:
        f = ncua[e["id"]]; e["type"]="CU"
        e["asset_k"], e["dep_k"], e["hq"] = f["asset_k"], f["shares_k"], f["hq"]
        e["name"] = f.get("name", e["name"])
        e["src_link"] = "NCUA call report 2026-03 FS220 (ACCT_010/ACCT_018), CU_NUMBER "+e["id"]
    e["found_by"] = [e["src"]]

# ---- v6 table ----
v6names = [r[2] for r in list(csv.reader(open("/home/user/awake/research/v6/deliverables/ca_business_credit_funding_v6_funding_table.csv")))[1:] if len(r)>2]
v6map = {norm(n): n for n in v6names}
ALIAS_V6 = {"ZIONS BANCORPORATION":"California Bank & Trust","JPMORGAN CHASE":"Chase (JPMorgan Chase)",
 "CITIBANK":"Citi (Citibank)","FIRST CITIZENS AND":"First Citizens Bank","WASHINGTON":"WaFd Bank","NUVISION":"Nuvision Credit Union","U S":"U.S. Bank (direct)","SCHOOLSFIRST":"SchoolsFirst Federal Credit Union","FINANCIAL PARTNERS":"Financial Partners Credit Union","SOUTHERN CALIFORNIA":"Credit Union of Southern California (CU SoCal)"}
def v6_match(name):
    n = norm(name)
    if n in v6map: return v6map[n]
    for k,v in ALIAS_V6.items():
        if k in n or n==k: return v
    for vn, orig in v6map.items():
        if vn and n and (vn==n or (len(vn)>5 and vn in n) or (len(n)>5 and n in vn)): return orig
    return None
for e in inst.values(): e["v6"] = v6_match(e["name"])

# ---- OSM matching ----
OSM_REMAP = {  # stale/brand tags -> current institution norm
 "CHASE":"JPMORGAN CHASE","US":"U S","UNION":"U S","ONE WEST":"FIRST CITIZENS AND",
 "CALIFORNIA AND TRUST":"ZIONS BANCORPORATION","LUTHER BURBANK SAVINGS":"WASHINGTON",
 "INTERNATIONAL CITY":"AMERICAN PLUS","COMERICA":"COMERICA","SOUTH LAND":"SOUTHLAND",
 "LBS":"LBS FINANCIAL","ORANGE COUNTY S":"ORANGE COUNTY S"}
instnorm = {norm(e["name"]): e for e in inst.values()}
osm_only, osm_notes = [], []
for o in osm:
    if o["miles"] > 5: continue
    n = norm(o["name"]) or norm(o.get("brand",""))
    m = instnorm.get(n)
    if not m:
        for k,t in OSM_REMAP.items():
            if n==k or (len(k)>3 and k in n):
                for ik,e in instnorm.items():
                    if t in ik: m=e; break
                if m: break
    if not m:
        for ik,e in instnorm.items():
            if ik and n and (ik in n or n in ik): m=e; break
    if m:
        if "OSM" not in m["found_by"]: m["found_by"].append("OSM")
        m.setdefault("osm_ids",[]).append(o["osm_id"])
    else:
        osm_only.append(o)

# web-confirmed institutions
WEB = ["CITIBANK","BANC CALIFORNIA","WELLS FARGO","ZIONS","JPMORGAN","AMERICA NATIONAL","U S BANK","SOUTHLAND","LBS","FINANCIAL PARTNERS","ORANGE COUNTY","LONG BEACH CITY EMPLOYEES","AMERICAN PLUS"]
for e in inst.values():
    un = e["name"].upper()
    if any(w in un.replace("&","AND") or w in norm(e["name"]) for w in WEB):
        pass
for key in ["CITIBANK","BANC CALIFORNIA","WELLS FARGO","ZIONS BANCORPORATION","AMERICAN PLUS","SOUTHLAND","LBS FINANCIAL","FINANCIAL PARTNERS","ORANGE COUNTY S","LONG BEACH CITY EMPLOYEES"]:
    for ik,e in instnorm.items():
        if key in ik and "web" not in e["found_by"]: e["found_by"].append("web")

def fmt(k):
    if k is None: return ""
    d = k*1000
    if d>=1e12: return f"${d/1e12:.2f}T"
    if d>=1e9: return f"${d/1e9:.2f}B"
    return f"${d/1e6:.1f}M"

near5 = sorted([e for e in inst.values() if e["miles"]<=5], key=lambda e:e["miles"])
ring  = sorted([e for e in inst.values() if 5<e["miles"]<=10], key=lambda e:e["miles"])

GEO = {"census_batch":"US Census batch geocoder","census_oneline":"US Census geocoder","nominatim":"OSM Nominatim"}
rows=[]
for i,e in enumerate(near5,1):
    b=e["nearest"]
    links = e["src_link"]
    if e["src"]=="SOD": links += "; FDIC SOD 2025 (local sod_2025_*.json)"
    if e.get("osm_ids"): links += "; https://www.openstreetmap.org/"+e["osm_ids"][0]
    rows.append([i, e["name"], e["type"], f'{b["addr"]}, {b["city"]}, CA {b["zip"]}', e["miles"],
        ("CERT "+e["id"]) if e["src"]=="SOD" else ("Charter "+e["id"]), e["hq"],
        fmt(e["asset_k"]), fmt(e["dep_k"]), e["n5"], "Yes — "+e["v6"] if e["v6"] else "No",
        "+".join(e["found_by"]), links])

with open("geo_longbeach.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["Rank_by_distance","Institution","Type","Nearest_branch_address","Distance_miles",
        "CERT_or_Charter","HQ_City_State","Total_Assets","Total_Deposits","Branches_within_5mi",
        "In_v6_table","Found_by","Source_links"])
    w.writerows(rows)

# ---- markdown ----
md=[]
md.append("# Bank & Credit Union Census — One World Trade Center, Long Beach, CA 90831\n")
md.append("**Anchor point:** 1 World Trade Center, Long Beach, CA 90831 — geocoded to **33.767378, -118.199441** (US Census geocoder, Public_AR_Current benchmark, 2026-06-11). All distances are straight-line (haversine) miles from this point.\n")
md.append("## Method\n")
md.append("1. **FDIC SOD 2025** (local `research/v6/out/sod_2025_Los_Angeles.json` + `sod_2025_Orange.json`): 308 bank branches in 29 candidate cities; street addresses geocoded via the free **US Census batch geocoder** (382/406 matched), remainder via Census oneline + **OSM Nominatim** fallback. 406/406 geocoded.")
md.append("2. **NCUA 2026-Q1 branch file** (`cr202603/Credit Union Branch Information.txt`): 98 CU branches in the same cities, geocoded identically. CU financials from **FS220** (`ACCT_010` total assets, `ACCT_018` total shares & deposits, cycle 2026-03-31).")
md.append("3. **Organic map view — OpenStreetMap Overpass API**: `amenity=bank` within 8,047 m (5 mi) of the point → 45 elements, 26 distinct names; matched to institutions, stale tags investigated.")
md.append("4. **Web searches** (banks near One WTC Long Beach; downtown business banking; downtown CUs) for LPO/business-center finds.")
md.append("5. Bank assets/deposits from **FDIC institutions API** (`api.fdic.gov/banks/institutions`, fields ASSET/DEP, pulled 2026-06-11). One row per institution; nearest branch wins.\n")
md.append(f"## Within 5 miles: {len(near5)} institutions ({sum(1 for e in near5 if e['type']=='Bank')} banks, {sum(1 for e in near5 if e['type']=='CU')} credit unions; {sum(e['n5'] for e in near5)} branch locations)\n")
md.append("| # | Institution | Type | Nearest branch | Mi | CERT/Charter | HQ | Assets | Deposits | Br<=5mi | v6 table | Found by |")
md.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    md.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {r[8]} | {r[9]} | {r[10]} | {r[11]} |")
md.append("\n## Found only by organic map/web search (not a current SOD/NCUA branch)\n")
md.append("- **Opus Bank, 211 E Ocean Blvd (0.50 mi)** — stale OSM tag (way/238272353). Opus merged into Pacific Premier Bank (2020; Pacific Premier merged into Columbia Banking System 2025); the downtown LB office is closed. Pacific Premier's nearest live SOD branch is San Pedro, 6.37 mi.")
md.append("- **International City Bank, 249 E Ocean Blvd (0.54 mi)** — OSM tag (way/351202548). ICB merged into United Fidelity Bank fsb (2021); the branch was then acquired by **American Plus Bank, N.A.** and still operates dba International City Bank — captured above under American Plus Bank (rank 8).")
md.append("- **One West Bank, 3500 E 7th St (2.83 mi)** — stale OSM tag; OneWest -> CIT -> First-Citizens Bank & Trust (rank 14).")
md.append("- **Luther Burbank Savings, 5348 E 2nd St (3.94 mi)** — stale OSM tag; Luther Burbank merged into WaFd; SOD lists it as Washington Federal Bank (in table).")
md.append("- **Union Bank (downtown, OSM/Chamber web listing)** — stale; MUFG Union Bank merged into U.S. Bank (2023).")
md.append("- **Nix Neighborhood Lending, ~2.78 mi (node/5640830050)** — check-cashing/consumer-lending storefront (ex-Kinecta 'Nix'), not an insured bank or CU branch; excluded from the census.")
md.append("- **Beach Business Bank, 180 E Ocean Blvd** — web find (Yelp): CLOSED; was merged into First Foundation Bank lineage. Excluded.")
md.append("\nNo live, insured institution within 5 mi was found by OSM/web that is absent from FDIC SOD / NCUA data — the organic layer's net new value was confirming on-the-ground presence and flagging the four stale tags above.\n")
md.append("## Notables 5-10 miles out\n")
md.append("| Institution | Type | Nearest branch | Mi | Assets |")
md.append("|---|---|---|---|---|")
for e in ring:
    b=e["nearest"]
    md.append(f"| {e['name']} | {e['type']} | {b['addr']}, {b['city']} | {e['miles']} | {fmt(e['asset_k'])} |")
md.append("\n## Sources\n")
md.append("- US Census geocoder: https://geocoding.geo.census.gov/geocoder/locations/onelineaddress and /addressbatch (benchmark Public_AR_Current)")
md.append("- FDIC institutions API: https://api.fdic.gov/banks/institutions (ASSET/DEP in $000s, current quarter)")
md.append("- FDIC SOD 2025: local research/v6/out/sod_2025_Los_Angeles.json, sod_2025_Orange.json")
md.append("- NCUA 2026-03 call report files: research/v6/out/cr202603/ (branch file, FS220, FOICU)")
md.append("- Overpass API: https://overpass-api.de/api/interpreter — amenity=bank around:8047 of 33.767378,-118.199441")
md.append("- OSM Nominatim (fallback geocoding): https://nominatim.openstreetmap.org/search")
md.append("- Web: yelp.com/biz/citibank-long-beach-2; yelp.com/biz/banc-of-california-long-beach; wellsfargo.com locator 111 W Ocean Blvd; bankbranchlocator.com international-city-bank-history; business.lbchamber.com (Union Bank downtown, stale)")
open("geo_longbeach.md","w").write("\n".join(md)+"\n")

print("CSV rows:", len(rows), "| 5-10mi ring:", len(ring))
print("OSM-only leftover:", [(o["name"],o["miles"],o["osm_id"]) for o in osm_only])
for r in rows[:15]: print(r[0], r[4], r[1], "|", r[7], r[8], "|", r[10], "|", r[11])
