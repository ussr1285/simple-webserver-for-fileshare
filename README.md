- index.html 파일이 있는 위치에서 아래 명령어 실행
- index.html 이 없으면 파일 구조로 나옴.
```zsh
python3 -m http.server 80
```

- 혹은 아래 파일을 만들고 `python 파일명`으로 실행.
```zsh
import http.server
import socketserver

PORT = 80  # 원하는 포트 번호로 변경 가능

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()

```

