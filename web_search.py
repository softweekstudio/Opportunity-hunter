from html.parser import HTMLParser
from urllib.parse import urlencode,unquote
from urllib.request import Request,urlopen
import re
URL="https://html.duckduckgo.com/html/"
class P(HTMLParser):
    def __init__(self): super().__init__(); self.r=[]; self.c=None; self.title=False; self.snip=False
    def handle_starttag(self,t,a):
        a=dict(a); c=a.get("class","")
        if t=="a" and "result__a" in c:self.c={"title":"","url":a.get("href",""),"snippet":""};self.title=True
        elif self.c and "result__snippet" in c:self.snip=True
    def handle_endtag(self,t):
        if t=="a" and self.title:self.title=False
        if t=="div" and self.snip:self.snip=False
    def handle_data(self,d):
        d=" ".join(d.split())
        if self.c and d:
            if self.title:self.c["title"]+=d
            elif self.snip:self.c["snippet"]+=d
    def close(self):
        super().close()
        if self.c and self.c["title"]:self.r.append(self.c);self.c=None
def clean(u):
    m=re.search(r"[?&]uddg=([^&]+)",u or ""); return unquote(m.group(1)) if m else u
def search_web(q,max_results=8):
    req=Request(URL+"?"+urlencode({"q":q}),headers={"User-Agent":"Mozilla/5.0 (Android; Termux) OpportunityHunter/1.5"})
    with urlopen(req,timeout=20) as r: html=r.read().decode("utf-8","ignore")
    p=P();p.feed(html);p.close()
    return [{"title":x["title"].strip(),"url":clean(x["url"]),"snippet":x["snippet"].strip()} for x in p.r[:max_results]]
