#from http.server import HTTPServer, SimpleHTTPRequestHandler
#
#httpd = HTTPServer(("localhost", 8888), SimpleHTTPRequestHandler)
#httpd.serve_forever()

#import http.server
#import socketserver
#
#PORT = 8000
#Handler = http.server.SimpleHTTPRequestHandler
#
#with socketserver.TCPServer(("", PORT), Handler) as httpd:
#    print("serving at port", PORT)
#    httpd.serve_forever()

#from http.server import HTTPServer, SimpleHTTPRequestHandler
#
#host = 'localhost'
#port = 8000
#httpd = HTTPServer((host, port), SimpleHTTPRequestHandler)
#print('serving at port', port)
#httpd.serve_forever()

from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        print(self)
        body = b'Hello World'
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

host = 'localhost'
port = 8000
httpd = HTTPServer((host, port), MyHandler)
print('serving at port', port)
httpd.serve_forever()
