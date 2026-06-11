import json, math, re, time, urllib.parse, urllib.request

WTC = (33.767378164945, -118.199440918383)
def hav(lat,lon):
    R=3958.7613; import math
    dp=math.radians(lat-WTC[0]); dl=math.radians(lon-WTC[1])
    a=math.sin(dp/2)**2+math.cos(math.radians(WTC[0]))*math.cos(math.radians(lat))*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(a))

def census_oneline(q):
    url="https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address="+urllib.parse.quote(q)+"&benchmark=Public_AR_Current&format=json"
    try:
        d=json.load(urllib.request.urlopen(url, timeout=30))
        m=d["result"]["addressMatches"]
        if m: c=m[0]["coordinates"]; return c["y"],c["x"],"census_oneline"
    except Exception as e: pass
    return None

def nominatim(q):
    url="https://nominatim.openstreetmap.org/search?format=json&limit=1&q="+urllib.parse.quote(q)
    req=urllib.request.Request(url, headers={"User-Agent":"geo-research/1.0 (nguyenalan95@gmail.com)"})
    try:
        d=json.load(urllib.request.urlopen(req, timeout=30))
        if d: return float(d[0]["lat"]),float(d[0]["lon"]),"nominatim"
    except Exception: pass
    return None

cands=json.load(open("candidates.json"))
for r in cands:
    if r.get("lat"): continue
    clean=re.sub(r'(?i)[,]?\s*(ste|suite|unit|bldg|#)\s*\S*','',r["addr"]).strip().rstrip(',')
    q=f'{clean}, {r["city"]}, CA {r["zip"]}'
    res=census_oneline(q)
    if not res:
        time.sleep(1.1); res=nominatim(q)
        time.sleep(1.1)
    if res:
        r["lat"],r["lon"],r["geo"]=res
        r["miles"]=round(hav(res[0],res[1]),2)
        print("OK", r["geo"], r["addr"], r["city"], r["miles"])
    else:
        print("FAIL", r["addr"], r["city"], r["zip"])
json.dump(cands, open("candidates.json","w"), indent=1)
print("still missing:", sum(1 for r in cands if not r.get("lat")))
