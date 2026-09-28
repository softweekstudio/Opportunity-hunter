from agent import analyze_opportunity

def analyze(items):
    return [analyze_opportunity(item) for item in items]
