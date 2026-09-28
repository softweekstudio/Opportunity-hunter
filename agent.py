import json
from datetime import datetime
from pathlib import Path
from web_search import search_web

ROOT=Path(__file__).parent
CFG=ROOT/"config.json"; MEM=ROOT/"data"/"memory.json"; REP=ROOT/"data"/"reports"
REP.mkdir(parents=True,exist_ok=True)

def load(p,d):
    try:return json.loads(p.read_text(encoding="utf-8"))
    except (FileNotFoundError,json.JSONDecodeError):return d
def save(p,d):
    p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")

def analyze(x):
    t=(x.get("title","")+" "+x.get("snippet","")).lower()
    demand=["need","how to","template","planner","tracker","printable","organizer","checklist","guide","problem","help","looking for"]
    market=["free","etsy","amazon","shop","seller","best"]
    dh=sum(w in t for w in demand); mh=sum(w in t for w in market)
    return {**x,"score":max(0,min(100,50+min(25,dh*5)-min(20,mh*4))),
            "reasons":[f"Demand signals: {dh}.",f"Market/competition signals: {mh}."]}

def research(query,n=8):
    raw=search_web(query,n); results=[analyze(x) for x in raw]; now=datetime.now().isoformat(timespec="seconds")
    mem=load(MEM,{"research":[],"runs":[]}); mem["research"].extend(results); mem["runs"].append({"timestamp":now,"query":query,"result_count":len(results)}); save(MEM,mem)
    report={"created_at":now,"objective":load(CFG,{}).get("objective",""),"query":query,"results":results}
    save(REP/f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",report); return report

if __name__=="__main__":
    q=input("What should I research? ").strip()
    print(json.dumps(research(q),ensure_ascii=False,indent=2) if q else "No query entered.")
