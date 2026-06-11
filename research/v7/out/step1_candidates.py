import json, csv, re

CITIES = {"LONG BEACH","SIGNAL HILL","LAKEWOOD","CARSON","SAN PEDRO","WILMINGTON",
"SEAL BEACH","LOS ALAMITOS","HAWAIIAN GARDENS","BELLFLOWER","PARAMOUNT","COMPTON",
"HARBOR CITY","ROSSMOOR","TERMINAL ISLAND","RANCHO DOMINGUEZ","CYPRESS","ARTESIA",
"CERRITOS","NORWALK","DOWNEY","TORRANCE","LOMITA","GARDEN GROVE","WESTMINSTER","STANTON","BUENA PARK","LA PALMA","HUNTINGTON BEACH"}
# wide net; distance filter happens after geocoding

rows = []
for cty in ("Los_Angeles","Orange"):
    d = json.load(open(f"/home/user/awake/research/v6/out/sod_2025_{cty}.json"))
    for rec in d["data"]:
        r = rec["data"]
        if (r.get("CITYBR") or "").upper().strip() in CITIES:
            rows.append({"src":"SOD","inst":r["NAMEFULL"],"id":str(r["CERT"]),
                "branch":r.get("NAMEBR",""),"addr":r.get("ADDRESBR","").strip(),
                "city":r["CITYBR"].strip(),"state":"CA","zip":str(r.get("ZIPBR","")).zfill(5),
                "hq":f'{r.get("CITY","")}, {r.get("STALP","")}'})

with open("/home/user/awake/research/v6/out/cr202603/Credit Union Branch Information.txt", encoding="latin-1") as f:
    rd = csv.DictReader(f)
    for r in rd:
        if r["PhysicalAddressStateCode"]=="CA" and (r["PhysicalAddressCity"] or "").upper().strip() in CITIES:
            rows.append({"src":"NCUA","inst":r["CU_NAME"].strip(),"id":r["CU_NUMBER"],
                "branch":r["SiteName"].strip(),"addr":r["PhysicalAddressLine1"].strip(),
                "city":r["PhysicalAddressCity"].strip(),"state":"CA",
                "zip":r["PhysicalAddressPostalCode"][:5],"hq":""})

json.dump(rows, open("/home/user/awake/research/v7/out/candidates.json","w"), indent=1)
# batch geocoder input: id, street, city, state, zip
with open("/home/user/awake/research/v7/out/geo_batch_in.csv","w",newline="") as f:
    w = csv.writer(f)
    for i,r in enumerate(rows):
        w.writerow([i, r["addr"], r["city"], r["state"], r["zip"]])
print(len(rows), "candidate branches;", sum(1 for r in rows if r['src']=='SOD'),"SOD /", sum(1 for r in rows if r['src']=='NCUA'),"NCUA")
