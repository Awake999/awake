import json, csv, re

FOCUS = {"FONTANA","RIALTO","BLOOMINGTON","RANCHO CUCAMONGA","ONTARIO","SAN BERNARDINO",
         "RIVERSIDE","JURUPA VALLEY","COLTON","UPLAND","EASTVALE","MIRA LOMA","GLEN AVON",
         "PEDLEY","GRAND TERRACE","MUSCOY","CLAREMONT","POMONA","MONTCLAIR","CHINO"}

rows=[]
for cty in ["San_Bernardino","Riverside","Los_Angeles"]:
    d=json.load(open(f"/home/user/awake/research/v6/out/sod_2025_{cty}.json"))
    for rec in d["data"]:
        r=rec["data"]
        if str(r.get("CITYBR","")).upper() in FOCUS:
            rows.append({"src":"SOD","inst":r["NAMEFULL"],"cert":r["CERT"],
                "addr":r["ADDRESBR"],"city":r["CITYBR"],"zip":str(r["ZIPBR"]).zfill(5),
                "branch":r.get("NAMEBR",""),"hq":f"{r['CITY']}, {r['STALP']}"})

with open("/home/user/awake/research/v6/out/cr202603/Credit Union Branch Information.txt", encoding="latin-1") as f:
    for r in csv.DictReader(f):
        if r["PhysicalAddressStateCode"]=="CA" and r["PhysicalAddressCity"].strip().upper() in FOCUS:
            rows.append({"src":"NCUA","inst":r["CU_NAME"],"cert":r["CU_NUMBER"],
                "addr":r["PhysicalAddressLine1"],"city":r["PhysicalAddressCity"].title(),
                "zip":r["PhysicalAddressPostalCode"][:5],"branch":r["SiteName"],"hq":""})

print(len(rows),"branches")
json.dump(rows,open("/home/user/awake/research/v7/tmp/branches.json","w"),indent=1)
# batch geocode input
seen={}
with open("/home/user/awake/research/v7/tmp/geo_in.csv","w",newline="") as f:
    w=csv.writer(f)
    for i,r in enumerate(rows):
        key=(r["addr"].upper(),r["city"].upper())
        if key in seen: continue
        seen[key]=i
        w.writerow([i,r["addr"],r["city"],"CA",r["zip"]])
print(len(seen),"unique addresses")
from collections import Counter
print(Counter([r["city"].upper() for r in rows]))
