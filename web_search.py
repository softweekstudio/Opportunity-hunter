"""
Placeholder for V2 web browsing/search integration.

V1 deliberately does not scrape websites or access accounts.
The function below accepts results supplied by the user or another
approved research layer.
"""

def normalize_results(results):
    normalized = []
    for r in results:
        normalized.append({
            "name": r.get("name", ""),
            "description": r.get("description", ""),
            "demand": r.get("demand", ""),
            "competition": r.get("competition", ""),
            "price": r.get("price", ""),
            "source": r.get("source", ""),
            "next_step": r.get("next_step", "")
        })
    return normalized
