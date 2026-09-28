import json
def save_report(report,path): open(path,"w",encoding="utf-8").write(json.dumps(report,ensure_ascii=False,indent=2))
