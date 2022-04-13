from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib import parse
import platform
from datetime import datetime

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        """ will handle GET requests and send back the response """
        path = self.path
        url_components = parse.urlparse(path)
        query_string = parse.parse_qsl(url_components.query)
        dic = dict(query_string)
        name = dic.get('name')
        if name:
            message = f'Hi, {name}!\n'
        else:
            message = 'Hi, Stranger!\n'

        message += f"\n Greetings from Python Version {platform.python_version()} on {platform.system()} {platform.release()} \n"
        
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # will show the path of whatever the user typed in the browser
        self.wfile.write(message.encode())
        self.wfile.write(self.path[1:].encode())

        return


def main():
    """ this function will start the server and listen for requests """
    port = 8080
    server = HTTPServer(('', port), handler)
    print('Started httpserver on port {}'.format(port))
    server.serve_forever()  # will run forever until stopped by user (ctrl+c ) in the terminal


if __name__ == '__main__':
    main()
