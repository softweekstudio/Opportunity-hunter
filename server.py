import json
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlparse,parse_qs
from agent import research
class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        u=urlparse(self.path)
        if u.path=="/api/research":
            q=parse_qs(u.query).get("q",[""])[0].strip()
            try: body=json.dumps(research(q) if q else {"error":"Missing query."},ensure_ascii=False).encode()
            except Exception as e: body=json.dumps({"error":str(e)}).encode()
            self.send_response(200);self.send_header("Content-Type","application/json; charset=utf-8");self.send_header("Content-Length",str(len(body)));self.end_headers();self.wfile.write(body);return
        super().do_GET()
print("AI Agent V1.5: http://127.0.0.1:8080") if __name__=="__main__" else None
if __name__=="__main__": ThreadingHTTPServer(("127.0.0.1",8080),H).serve_forever()
