import http.server
import os

page=open("index.html").read()

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_respones(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(page.encode())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))   # Use PORT if it's there.
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, Shortener)
    httpd.serve_forever()