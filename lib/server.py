#!/usr/bin/env python3
from lib import logger, arguments
from http.server import BaseHTTPRequestHandler, HTTPServer

args = arguments.get_args()

class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logger.request(self)
        self._set_response()

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",str(self.path), str(self.headers), post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    def log_message(self,format,*args):
        return

def start_server(server_class=HTTPServer, handler_class=RequestHandler):
    host = args.server_address
    port = args.server_port
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        logger.msg('Listening @ ',f'http://{host}:{port}','green')
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    finally:
        httpd.server_close()

