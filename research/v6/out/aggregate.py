import json, csv, re, urllib.parse
from collections import defaultdict

BASE = "/home/user/awake/research/v6"
COUNTIES = ["Los Angeles","San Bernardino","Riverside","Orange","Ventura","San Diego"]
COL = {"Los Angeles":"Branches_LA","San Bernardino":"Branches_SB","Riverside":"Branches_Riv",
       "Orange":"Branches_OC","Ventura":"Branches_Ventura","San Diego":"Branches_SD"}
PRIORITY4 = {"Los Angeles","San Bernardino","Riverside","Orange"}

def url_for(county):
    enc = urllib.parse.quote(county)
    return (f"https://banks.data.fdic.gov/api/sod?filters=YEAR:2025%20AND%20STALPBR:CA%20AND%20"
            f"CNTYNAMB:%22{enc}%22&fields=CERT,NAMEFULL,CITY,STALP,NAMEBR,CITYBR,CNTYNAMB,STALPBR,"
            f"DEPSUMBR,ADDRESBR,ZIPBR&limit=10000&format=json")

inst = {}
for c in COUNTIES:
    fn = c.replace(" ","_")
    d = json.load(open(f"{BASE}/out/sod_2025_{fn}.json"))
    assert d["meta"]["total"] == len(d["data"]), c
    for row in d["data"]:
        r = row["data"]
        cert = r["CERT"]
        if cert not in inst:
            inst[cert] = {"name": r["NAMEFULL"], "hq_city": r.get("CITY",""), "hq_st": r.get("STALP",""),
                          "branches": defaultdict(int), "deposits": 0, "urls": set()}
        inst[cert]["branches"][c] += 1
        dep = r.get("DEPSUMBR")
        inst[cert]["deposits"] += dep if isinstance(dep,(int,float)) else 0
        inst[cert]["urls"].add(url_for(c))

# v5 matching
SUFFIX_PAT = re.compile(r"\b(national association|n\.?a\.?|fsb|f\.?s\.?b\.?|ssb|s\.?s\.?b\.?|inc|corp|company|co)\b\.?$")
def norm(s):
    s = s.lower().strip()
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    for _ in range(3):
        s2 = SUFFIX_PAT.sub("", s).strip()
        if s2 == s: break
        s = s2
    return s

v5_names_raw = [l.strip() for l in open(f"{BASE}/v5_all_institution_names.txt") if l.strip()]
v5_names = {norm(n): n for n in v5_names_raw}

v5_certs = {}
with open(f"{BASE}/v5_fdic_census.csv") as f:
    for row in csv.DictReader(f):
        try: v5_certs[int(row["CERT"])] = row["Institution"]
        except (ValueError, KeyError): pass

def tokset(s): return set(norm(s).split()) - {"bank","the","of","trust","and"}

def match_v5(cert, name):
    if cert in v5_certs:
        return "IN_V5", f"CERT match in v5_fdic_census: {v5_certs[cert]}"
    n = norm(name)
    if n in v5_names:
        return "IN_V5", f"Name match in v5 list: {v5_names[n]}"
    # loose: containment / token overlap
    cands = []
    t = tokset(name)
    for vn, raw in v5_names.items():
        vt = set(vn.split()) - {"bank","the","of","trust","and","credit","union"}
        if not t or not vt: continue
        if n in vn or vn in n or (t and vt and (t <= vt or vt <= t)):
            cands.append(raw)
        elif len(t & vt) >= max(2, min(len(t), len(vt))):
            cands.append(raw)
    if cands:
        return "POSSIBLE_MATCH", "Candidates: " + "; ".join(sorted(set(cands))[:4])
    return "NEW_GAP", ""

rows = []
for cert, v in inst.items():
    counties = [c for c in COUNTIES if v["branches"][c] > 0]
    pri = "PRIORITY-4CTY" if any(c in PRIORITY4 for c in counties) else "OUTLIER"
    status, note = match_v5(cert, v["name"])
    rows.append({
        "CERT": cert, "Institution": v["name"], "HQ_City": v["hq_city"], "HQ_State": v["hq_st"],
        "OOS_HQ_with_SoCal_branches": "Yes" if v["hq_st"] != "CA" else "No",
        **{COL[c]: v["branches"][c] for c in COUNTIES},
        "Total_Branches_6cty": sum(v["branches"].values()),
        "Deposits_6cty_$K": v["deposits"],
        "Counties": "; ".join(counties), "Priority": pri,
        "v5_status": status, "Match_note": note,
        "Source_link": " | ".join(sorted(v["urls"])),
    })

rows.sort(key=lambda r: -r["Deposits_6cty_$K"])
fields = ["CERT","Institution","HQ_City","HQ_State","OOS_HQ_with_SoCal_branches",
          "Branches_LA","Branches_SB","Branches_Riv","Branches_OC","Branches_Ventura","Branches_SD",
          "Total_Branches_6cty","Deposits_6cty_$K","Counties","Priority","v5_status","Match_note","Source_link"]
with open(f"{BASE}/out/fdic_sod_census_6cty_2025.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

# stats
four = [r for r in rows if r["Priority"]=="PRIORITY-4CTY"]
print("Total institutions (6cty):", len(rows))
print("4-county institutions:", len(four))
percty = {c: len([r for r in rows if r[COL[c]]>0]) for c in COUNTIES}
print("Per county inst counts:", percty)
print("Branch totals per county:", {c: sum(r[COL[c]] for r in rows) for c in COUNTIES})
from collections import Counter
print("v5 status:", Counter(r["v5_status"] for r in rows))
print("OOS:", Counter(r["OOS_HQ_with_SoCal_branches"] for r in rows))
gaps = [r for r in rows if r["v5_status"]=="NEW_GAP"]
print("\nNEW_GAP top 20:")
for r in gaps[:20]:
    print(f"  {r['CERT']:>6} {r['Institution'][:55]:<55} {r['HQ_City']},{r['HQ_State']} br={r['Total_Branches_6cty']} dep={r['Deposits_6cty_$K']:,}")
print("\nPOSSIBLE_MATCH:")
for r in rows:
    if r["v5_status"]=="POSSIBLE_MATCH":
        print(f"  {r['CERT']:>6} {r['Institution'][:50]:<50} -> {r['Match_note'][:90]}")
