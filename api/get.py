import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer


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
            output += '<h3> <a href="/tasklist/new"> Add New Task </a> </h3>'
            for task in tasklist:
                output += task
                output += '<a/ href = "tasklist/%s/remove">X</a>' % task
                output += '</br>'
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
            
            
        if self.path.endswith('/remove'):
            listIDPath  = self.path.split('/')[2]
            print(listIDPath)
            
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            # tasklist.remove(listIDPath)
            output = ''
            output += '<html><body>'
            output += '<h1>Remove Task: %s</h1>' % listIDPath.replace('%20', ' ')
            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/%s/remove">' % listIDPath
            output += '<input type="submit" value="Remove">'
            output += '</form>'
            output += '<a href="/tasklist">Cancel</a>'
            output += '</body></html>'

            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/tasklist/new'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len      
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_task = fields.get('task')

                tasklist.append(new_task[0])
            
            
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()

        if self.path.endswith('/remove'):
            listIDPath  = self.path.split('/')[2]
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            if ctype == 'multipart/form-data':
                list_item = listIDPath.replace('%20', ' ') 
                tasklist.remove(list_item)
                
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()
                
                
def main():
    """ this function will start the server and listen for requests """
    PORT = 9000
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print('Started httpserver on port %s' % PORT)
    server.serve_forever()  # will run forever until stopped by user (ctrl+c ) in the terminal


if __name__ == '__main__':
    main()
