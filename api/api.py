from http.server import BaseHTTPRequestHandler , HTTPServer

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(self.path[1:].encode())
    return

def main ():
    port = 8080
    server = HTTPServer(('', port), handler)
    print('Started httpserver on port {}'.format(port))
    server.serve_forever()


if __name__ == '__main__':
    main()