import json, csv, math

WTC = (33.767378164945, -118.199440918383)
def hav(lat,lon):
    R=3958.7613
    p1,p2 = math.radians(WTC[0]), math.radians(lat)
    dp = math.radians(lat-WTC[0]); dl = math.radians(lon-WTC[1])
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(a))

cands = json.load(open("candidates.json"))
coords = {}
with open("geo_batch_out.csv", newline="", encoding="latin-1") as f:
    for row in csv.reader(f):
        if len(row) >= 6 and row[2] == "Match":
            lon, lat = map(float, row[5].split(","))
            coords[int(row[0])] = (lat, lon, row[3])  # exact/non-exact in row[3]? actually row[3]=match type, row[4]=matched addr
unmatched = []
for i,r in enumerate(cands):
    if i in coords:
        lat,lon,_ = coords[i]
        r["lat"],r["lon"],r["geo"] = lat,lon,"census_batch"
        r["miles"] = round(hav(lat,lon),2)
    else:
        unmatched.append((i, r["addr"], r["city"], r["zip"]))
json.dump(cands, open("candidates.json","w"), indent=1)
print("unmatched:", len(unmatched))
for u in unmatched: print(u)
near = sorted([r for r in cands if r.get("miles") is not None and r["miles"]<=5], key=lambda r:r["miles"])
print("within 5mi so far:", len(near))
