"""
AI Agent V1 - Opportunity Hunter
Offline-first controller. It can analyze manually supplied research data
and create structured opportunity reports.

This V1 intentionally does NOT:
- spend money
- send messages
- publish content
- log into accounts
- execute arbitrary browser actions

A future V2 can add approved tools behind explicit permission checks.
"""
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent
CONFIG = ROOT / "config.json"
MEMORY = ROOT / "data" / "memory.json"
REPORTS = ROOT / "data" / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)

def load_json(path, default):
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def analyze_opportunity(item):
    text = " ".join(str(item.get(k, "")) for k in ("name", "description", "demand", "competition"))
    demand = str(item.get("demand", "")).lower()
    competition = str(item.get("competition", "")).lower()

    score = 50
    reasons = []

    if any(x in demand for x in ("high", "alta", "strong", "forte")):
        score += 20
        reasons.append("Demand is described as strong.")
    elif any(x in demand for x in ("low", "bassa", "weak", "debole")):
        score -= 15
        reasons.append("Demand is described as weak.")

    if any(x in competition for x in ("low", "bassa", "weak", "debole")):
        score += 15
        reasons.append("Competition is described as relatively low.")
    elif any(x in competition for x in ("high", "alta", "strong", "forte")):
        score -= 15
        reasons.append("Competition is described as strong.")

    score = max(0, min(100, score))
    return {
        "name": item.get("name", "Unnamed opportunity"),
        "score": score,
        "source": item.get("source", ""),
        "description": item.get("description", ""),
        "demand": item.get("demand", ""),
        "competition": item.get("competition", ""),
        "price": item.get("price", ""),
        "reasons": reasons,
        "next_step": item.get("next_step", "Research the opportunity further before creating anything.")
    }

def run(items):
    memory = load_json(MEMORY, {"research": [], "runs": []})
    results = [analyze_opportunity(x) for x in items]
    now = datetime.now().isoformat(timespec="seconds")

    memory["research"].extend(results)
    memory["runs"].append({"timestamp": now, "count": len(results)})
    save_json(MEMORY, memory)

    report = {
        "created_at": now,
        "objective": load_json(CONFIG, {}).get("objective", ""),
        "results": results
    }
    filename = REPORTS / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    save_json(filename, report)
    return report

if __name__ == "__main__":
    demo = [{
        "name": "Example digital planner",
        "description": "A hypothetical example for testing the agent.",
        "demand": "high",
        "competition": "medium",
        "price": "€5-€12",
        "source": "manual test",
        "next_step": "Validate demand with current marketplace research."
    }]
    print(json.dumps(run(demo), ensure_ascii=False, indent=2))
