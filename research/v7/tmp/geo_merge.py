import csv, json, math, time, urllib.request, urllib.parse

LAT0, LON0 = 34.133203, -117.456149
def hav(lat,lon):
    R=3958.761; p=math.pi/180
    a=math.sin((lat-LAT0)*p/2)**2+math.cos(LAT0*p)*math.cos(lat*p)*math.sin((lon-LON0)*p/2)**2
    return 2*R*math.asin(math.sqrt(a))

rows=json.load(open("/home/user/awake/research/v7/tmp/branches.json"))
coords={}
misses=[]
with open("/home/user/awake/research/v7/tmp/geo_out.csv",encoding="latin-1") as f:
    for line in csv.reader(f):
        idx=int(line[0]); status=line[2]
        if status=="Match":
            lon,lat=map(float,line[5].split(","))
            coords[idx]=(lat,lon,"census")
        else:
            misses.append(idx)

# index->key mapping reused for duplicates
keymap={}
for i,r in enumerate(rows):
    keymap[(r["addr"].upper(),r["city"].upper())]=keymap.get((r["addr"].upper(),r["city"].upper()),i)

def nominatim(q):
    url="https://nominatim.openstreetmap.org/search?"+urllib.parse.urlencode({"q":q,"format":"json","limit":1,"countrycodes":"us"})
    req=urllib.request.Request(url,headers={"User-Agent":"geo-research/1.0"})
    try:
        d=json.load(urllib.request.urlopen(req,timeout=20))
        if d: return float(d[0]["lat"]),float(d[0]["lon"])
    except Exception as e: print("ERR",e)
    return None

for idx in misses:
    r=rows[idx]
    res=nominatim(f"{r['addr']}, {r['city']}, CA {r['zip']}")
    time.sleep(1.1)
    if not res:
        res=nominatim(f"{r['addr']}, {r['city']}, CA"); time.sleep(1.1)
    if res: coords[idx]=(res[0],res[1],"nominatim")
    else: print("UNGEOCODED:",r["inst"],"|",r["addr"],r["city"],r["zip"])

out=[]
for i,r in enumerate(rows):
    key=(r["addr"].upper(),r["city"].upper())
    c=coords.get(keymap[key])
    if c:
        r["lat"],r["lon"],r["geosrc"]=c
        r["dist"]=round(hav(c[0],c[1]),2)
    else:
        r["dist"]=None
    out.append(r)
json.dump(out,open("/home/user/awake/research/v7/tmp/branches_geo.json","w"),indent=1)
ok=[r for r in out if r["dist"] is not None]
print(len(ok),"geocoded;", sum(1 for r in ok if r["dist"]<=8),"within 8mi")
for r in sorted(ok,key=lambda x:x["dist"])[:20]:
    print(f"{r['dist']:5.2f} {r['src']:4} {r['inst'][:40]:40} {r['addr']}, {r['city']}")
