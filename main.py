import http.server
import socketserver

PORT = 80  # 원하는 포트 번호로 변경 가능

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
