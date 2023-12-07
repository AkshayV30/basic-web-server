import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
   
        html_content = "<html><body><h1>Hello, World!</h1></body></html>"
        self.wfile.write(html_content.encode())

port = 8000

with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Serving on port {port}")

    httpd.serve_forever()
