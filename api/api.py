from http.server import BaseHTTPRequestHandler , HTTPServer


tasklist = ['Task 1', 'Task 2', 'Task 3', 'Task 4']


class requestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    """ will handle GET requests and send back the response """
    if self.path.endswith('/tasklist'):
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()

      output = ''
      output += '<html><body>'
      output += '<h1>Task List</h1>'
      output+= '<h3> <a href="/tasklist/new"> Add New Task </a> </h3>'
      for task in tasklist:
        output+= task
        output+= '</br>'
      output += '</body></html>'
      
      self.wfile.write(output.encode())
   
    if self.path.endswith('/tasklist/new'):
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()

      output = ''
      output += '<html><body>'
      output += '<h1>Add a new task</h1>'
      output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
      output += '<input name="task" type="text" placeholder="Add a new task">'
      output += '<input type="submit" value="Submit">'
      output += '</form>'
      output += '</body></html>'
      
      self.wfile.write(output.encode())
    
    

def main ():
    """ this function will start the server and listen for requests """
    PORT = 8080
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Started httpserver on port %s'% PORT)
    server.serve_forever() # will run forever until stopped by user (ctrl+c ) in the terminal


if __name__ == '__main__':
    main()