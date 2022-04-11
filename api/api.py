from http.server import BaseHTTPRequestHandler , HTTPServer


tasklist = ['Task 1', 'Task 2', 'Task 3', 'Task 4']


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    """ will handle GET requests and send back the response """
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(self.path[1:].encode()) # will show the path of whatever the user typed in the browser
    
    output = ""
    output += "<html><body>"
    output += "<h2>Task List</h2>"
    for task in tasklist:
      output+= task
      output+= "</br>"
    output += "</body></html>"
    self.wfile.write(output.encode())
    print(output)
    
    return

def main ():
    """ this function will start the server and listen for requests """
    port = 8080
    server = HTTPServer(('', port), handler)
    print('Started httpserver on port {}'.format(port))
    server.serve_forever() # will run forever until stopped by user (ctrl+c ) in the terminal


if __name__ == '__main__':
    main()