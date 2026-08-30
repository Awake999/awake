# -*- coding: utf-8 -*-
"""LANE 4 — Conversation Hub: one local portal page with every contact's FULL
GHL thread (calls / SMS / email / activities / notes, inbound + outbound) plus
a per-contact summary and deep links to the same view in GHL.
Output: ops/archive/ghl/CONVERSATION_HUB.html  (local + private repo only —
message bodies never go to the hosted artifact, per the pseudonymization rule).
"""
import json, sys, datetime, pathlib, re
from collections import Counter

DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
REPO = pathlib.Path(__file__).resolve().parent.parent.parent
RAW = REPO / "ops" / "archive" / "ghl" / DATE / "raw"
OUT = REPO / "ops" / "archive" / "ghl" / "CONVERSATION_HUB.html"
J = lambda n: json.load(open(RAW / f"{n}.json", encoding="utf-8"))
LOC = "WFkoNzKa9J9PxhngsLfl"

contacts = J("contacts")
convs = J("conversations")
msgs = J("messages_by_conversation")
appts = J("appointments_by_contact")
opps = J("opportunities")
pipes = {p["id"]: p for p in J("pipelines")["pipelines"]}
try:
    notes = J("notes_by_contact")
except FileNotFoundError:
    notes = {}

opp_by_contact = {}
for o in opps:
    opp_by_contact.setdefault(o.get("contactId"), []).append(o)
conv_by_contact = {}
for cvid, cv in convs.items():
    conv_by_contact.setdefault(cv.get("contactId"), []).append(cvid)

def stage_name(o):
    p = pipes.get(o.get("pipelineId"), {})
    s = next((x["name"] for x in p.get("stages", []) if x["id"] == o.get("pipelineStageId")), "?")
    return re.sub(r"[^\w /&+-]", "", s).strip()

data = []
for c in contacts:
    cid = c["id"]
    nm = f'{c.get("firstNameRaw") or c.get("firstName") or ""} {c.get("lastNameRaw") or c.get("lastName") or ""}'.strip() or "(no name)"
    events = []
    convids = conv_by_contact.get(cid, [])
    for cvid in convids:
        for m in msgs.get(cvid, []):
            t = m.get("messageType") or ""
            meta = m.get("meta") or {}
            call = meta.get("call") or {}
            email = meta.get("email") or {}
            events.append({
                "ts": m.get("dateAdded"), "kind": t.replace("TYPE_", ""),
                "dir": m.get("direction") or "", "status": m.get("status") or "",
                "body": ((email.get("subject") + " — ") if isinstance(email.get("subject"), str) else "") + (m.get("body") or "")[:4000],
                "dur": call.get("duration"),
            })
    for n in notes.get(cid, []):
        events.append({"ts": n.get("dateAdded"), "kind": "NOTE", "dir": "", "status": "",
                       "body": (n.get("body") or "")[:4000], "dur": None})
    events.sort(key=lambda e: str(e["ts"]))
    ct = Counter(e["kind"] for e in events)
    ap = [{"ts": e.get("startTime"), "st": e.get("appointmentStatus"), "title": e.get("title")} for e in appts.get(cid, [])]
    oo = opp_by_contact.get(cid, [])
    data.append({
        "id": cid, "name": nm, "created": str(c.get("dateAdded"))[:10],
        "tags": c.get("tags") or [], "src": c.get("source") or "",
        "counts": dict(ct), "n": len(events),
        "last": events[-1]["ts"] if events else None,
        "opp": (stage_name(oo[0]) + " (" + oo[0].get("status", "") + ")") if oo else "",
        "appts": ap, "convids": convids, "events": events,
    })
data.sort(key=lambda d: str(d["last"] or ""), reverse=True)

html = """<title>APW Conversation Hub</title>
<style>
:root{--bg:#0F1214;--surface:#171B1E;--raised:#1E2428;--line:#2A3136;--ink:#E9ECEA;--ink2:#9AA4A0;--ink3:#667069;
--gold:#EDDA9C;--cyan:#33C1E8;--green:#3DDC97;--purple:#B44BE8;--link:#6FD0EC}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 "Archivo","Helvetica Neue",Arial,sans-serif;color-scheme:dark}
a{color:var(--link);text-decoration:none}a:hover{text-decoration:underline}
.app{display:grid;grid-template-columns:290px 1fr;height:100vh}
.side{border-right:1px solid var(--line);overflow-y:auto;background:var(--surface)}
.side .hd{padding:14px 14px 8px;position:sticky;top:0;background:var(--surface);border-bottom:1px solid var(--line)}
.side h1{font-size:15px;margin:0 0 8px;color:var(--gold)}
.side input{width:100%;background:var(--raised);border:1px solid var(--line);color:var(--ink);border-radius:6px;padding:7px 10px;font:inherit}
.person{padding:9px 14px;border-bottom:1px solid var(--line);cursor:pointer;display:flex;justify-content:space-between;gap:8px}
.person:hover,.person.on{background:var(--raised)}
.person .nm{font-weight:600;font-size:13.5px}.person .mt{color:var(--ink3);font-size:11.5px;white-space:nowrap}
.main{overflow-y:auto;padding:20px 26px}
.sumhead{border-bottom:2px solid var(--gold);padding-bottom:12px;margin-bottom:14px}
.sumhead h2{margin:0 0 4px;font-size:20px}
.sumhead .links a{margin-right:14px;font-size:12.5px}
.sum{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:12.5px;color:var(--ink2);margin:8px 0 2px}
.sum b{color:var(--ink)}
.chip{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:1px 7px;border-radius:999px;background:var(--raised);border:1px solid var(--line);color:var(--ink2)}
.ev{display:grid;grid-template-columns:88px 26px 1fr;gap:10px;padding:8px 0;border-bottom:1px dashed var(--line);align-items:start}
.ev .ts{color:var(--ink3);font-size:11.5px;font-family:Consolas,monospace;padding-top:2px}
.ev .ic{font-size:15px;text-align:center}
.ev .bd{font-size:13px;color:var(--ink2);word-break:break-word;max-width:88ch}
.ev .bd .who{font-weight:700;font-size:11px;letter-spacing:.06em;text-transform:uppercase;margin-right:8px}
.in .who{color:var(--green)}.out .who{color:var(--cyan)}
.ev.NOTE .bd{background:rgba(237,218,156,.06);border-left:3px solid var(--gold);padding:6px 10px;border-radius:4px;color:var(--ink)}
.ev.CALL .bd b{color:var(--ink)}
.empty{color:var(--ink3);padding:40px;text-align:center}
.mono{font-family:Consolas,monospace}
</style>
<div class="app">
<div class="side"><div class="hd"><h1>APW Conversation Hub</h1>
<input id="q" type="search" placeholder="Search __N__ contacts…"></div>
<div id="list"></div></div>
<div class="main" id="main"><div class="empty">Pick a contact ← &nbsp;every call, text, email, activity and note, oldest first.<br>Snapshot __DATE__ · refreshes with each local GHL pull.</div></div>
</div>
<script>
var DATA=__DATA__;
var LOC="__LOC__";
var GHLC="https://app.gohighlevel.com/v2/location/"+LOC+"/contacts/detail/";
var GHLV="https://app.gohighlevel.com/v2/location/"+LOC+"/conversations/conversations/";
var ICONS={SMS:"💬",EMAIL:"✉️",CALL:"📞",NOTE:"📝",ACTIVITY_OPPORTUNITY:"🎯",ACTIVITY_APPOINTMENT:"📅",ACTIVITY_CONTACT:"⚙️",SMS_REACTION:"👍"};
function esc(s){var d=document.createElement("div");d.textContent=s==null?"":String(s);return d.innerHTML}
var list=document.getElementById("list"),main=document.getElementById("main"),q=document.getElementById("q");
function renderList(){
  var needle=(q.value||"").toLowerCase();
  list.innerHTML=DATA.map(function(d,i){
    if(needle&&(d.name+" "+d.tags.join(" ")).toLowerCase().indexOf(needle)<0)return"";
    return '<div class="person" data-i="'+i+'"><span class="nm">'+esc(d.name)+'</span><span class="mt">'+d.n+' · '+esc(String(d.last||"").slice(0,10))+'</span></div>';
  }).join("");
}
function show(i){
  var d=DATA[i];
  document.querySelectorAll(".person").forEach(function(p){p.classList.toggle("on",p.getAttribute("data-i")==String(i))});
  var counts=Object.keys(d.counts).map(function(k){return (ICONS[k]||"")+" "+k.toLowerCase()+" <b>"+d.counts[k]+"</b>"}).join(" · ");
  var ap=d.appts.map(function(a){return esc(String(a.ts).slice(0,10))+" <b>"+esc(a.st||"?")+"</b>"}).join(" · ")||"none";
  var h='<div class="sumhead"><h2>'+esc(d.name)+'</h2>'
   +'<div class="links"><a href="'+GHLC+d.id+'">GHL contact ↗</a>'
   +d.convids.map(function(cv,ix){return '<a href="'+GHLV+cv+'">GHL conversation'+(d.convids.length>1?" "+(ix+1):"")+' ↗</a>'}).join("")
   +'</div>'
   +'<div class="sum"><span>added <b>'+esc(d.created)+'</b></span><span>source <b>'+esc(d.src||"—")+'</b></span>'
   +'<span>opportunity <b>'+esc(d.opp||"—")+'</b></span><span>'+counts+'</span></div>'
   +'<div class="sum"><span>appointments: '+ap+'</span></div>'
   +'<div class="sum">'+d.tags.map(function(t){return '<span class="chip">'+esc(t)+'</span>'}).join(" ")+'</div></div>';
  h+=d.events.map(function(e){
    var body=e.body;
    if(e.kind==="CALL")body="<b>"+(e.dir==="inbound"?"Inbound":"Outbound")+" call</b> · "+esc(e.status||"?")+(e.dur!=null?" · "+e.dur+"s":"");
    else body=esc(body);
    var who=e.dir?'<span class="who">'+(e.dir==="inbound"?"IN":"OUT")+"</span>":"";
    return '<div class="ev '+e.kind+' '+(e.dir==="inbound"?"in":"out")+'"><span class="ts">'+esc(String(e.ts||"").replace("T"," ").slice(0,16))+'</span><span class="ic">'+(ICONS[e.kind]||"•")+'</span><span class="bd">'+who+body+'</span></div>';
  }).join("");
  main.innerHTML=h;main.scrollTop=0;
}
list.addEventListener("click",function(ev){var p=ev.target.closest(".person");if(p)show(+p.getAttribute("data-i"))});
q.addEventListener("input",renderList);
renderList();
</script>
"""
payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
html = html.replace("__DATA__", payload).replace("__LOC__", LOC).replace("__N__", str(len(data))).replace("__DATE__", DATE)
OUT.write_text(html, encoding="utf-8")
print(f"hub: {len(data)} contacts, {sum(d['n'] for d in data)} events -> {OUT} ({OUT.stat().st_size//1024} KB)")
