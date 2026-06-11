import json, csv, re

cands = json.load(open("candidates.json"))
fdic = json.load(open("fdic_financials.json"))
ncua = json.load(open("ncua_financials.json"))
osm = json.load(open("osm_banks.json"))

def norm(s):
    s = s.upper()
    s = re.sub(r'[^A-Z0-9 &]',' ',s)
    s = re.sub(r'\b(THE|OF|NATIONAL ASSOCIATION|N A|NA|FSB|FCU|FEDERAL CREDIT UNION|CREDIT UNION|BANK AND TRUST COMPANY|TRUST COMPANY|BANK|FEDERAL|INC|COMPANY|CORP|CU)\b',' ',s)
    return ' '.join(s.split())

# institution-level aggregation, within 10 mi
inst = {}
for r in cands:
    if r["miles"] > 10: continue
    key = (r["src"], r["id"])
    e = inst.setdefault(key, {"src":r["src"],"id":r["id"],"name":r["inst"],"branches":[]})
    e["branches"].append(r)
for e in inst.values():
    e["branches"].sort(key=lambda b: b["miles"])
    b = e["branches"][0]
    e["nearest"] = b
    e["miles"] = b["miles"]
    e["n5"] = sum(1 for x in e["branches"] if x["miles"] <= 5)
    if e["src"]=="SOD":
        f = fdic.get(e["id"], {})
        e["asset_k"], e["dep_k"], e["hq"] = f.get("asset_k"), f.get("dep_k"), f.get("hq","")
        e["type"]="Bank"
    else:
        f = ncua.get(e["id"], {})
        e["asset_k"], e["dep_k"], e["hq"] = f.get("asset_k"), f.get("shares_k"), f.get("hq","")
        e["type"]="CU"
    e["found_by"] = {e["src"]}

# v6 table membership
v6rows = list(csv.reader(open("/home/user/awake/research/v6/deliverables/ca_business_credit_funding_v6_funding_table.csv")))
v6names = [r[2] for r in v6rows[1:] if len(r)>2]
v6norm = {norm(n): n for n in v6names}
ALIAS_V6 = {"JPMORGAN CHASE":"Chase (JPMorgan Chase)","CITIBANK":"Citi (Citibank)","U S":"U.S. Bank (direct)",
 "FARMERS & MERCHANTS LONG BEACH":"Farmers & Merchants Bank of Long Beach","FIRST CITIZENS & TRUST":"First Citizens Bank",
 "NUVISION":"Nuvision Credit Union","FLAGSTAR":"Flagstar Bank, N.A."}
def v6_match(name):
    n = norm(name)
    if n in v6norm: return v6norm[n]
    for k,v in ALIAS_V6.items():
        if k in n or n in k: return v
    for vn, orig in v6norm.items():
        if vn and (vn == n or (len(vn)>4 and vn in n) or (len(n)>4 and n in vn)): return orig
    return None
for e in inst.values():
    e["v6"] = v6_match(e["name"])

# OSM matching: map OSM names to institutions
OSM_ALIAS = {"CHASE":"JPMORGAN CHASE","US":"U S","U S":"U S","ONE WEST":"FIRST CITIZENS & TRUST",
 "UNION":"U S","COMERICA":"COMERICA","CALIFORNIA & TRUST":"ZIONS BANCORPORATION",  # CB&T is Zions division
 "LBS":"LBS FINANCIAL","SOUTH LAND":"SOUTHLAND","ORANGE COUNTY S":"ORANGE COUNTY S"}
instnorm = {}
for e in inst.values():
    instnorm.setdefault(norm(e["name"]), e)
osm_only = []
for o in osm:
    if o["miles"] > 5: continue
    n = norm(o["name"]) or norm(o.get("brand",""))
    matched = None
    if n in instnorm: matched = instnorm[n]
    if not matched and n in OSM_ALIAS and OSM_ALIAS[n] in instnorm: matched = instnorm[OSM_ALIAS[n]]
    if not matched:
        for k,e in instnorm.items():
            if k and n and (k in n or n in k): matched = e; break
    if matched:
        matched["found_by"].add("OSM")
        o["matched"] = matched["name"]
    else:
        osm_only.append(o)

print("Institutions <=10mi:", len(inst))
near5 = sorted([e for e in inst.values() if e["miles"]<=5], key=lambda e:e["miles"])
print("Institutions with branch <=5mi:", len(near5))
for e in near5[:20]:
    print(f'{e["miles"]:5.2f} {e["type"]:4} {e["name"][:45]:46} {e["nearest"]["addr"]}, {e["nearest"]["city"]}')
print("\nOSM-only within 5mi:")
for o in osm_only:
    print(f'{o["miles"]:5.2f} {o["name"]} | {o["addr"]} {o["city"]} | {o["osm_id"]}')
json.dump({"inst":[{**e,"found_by":sorted(e["found_by"])} for e in sorted(inst.values(), key=lambda x:x["miles"])],
           "osm_only":osm_only}, open("merged.json","w"), indent=1)
