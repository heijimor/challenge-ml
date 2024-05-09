from http.server import HTTPServer
from app.modules.routing.base_request_handler import BaseRequestHandler

def run_server():
  port = 8000
  server_address = ('', port)
  httpd = HTTPServer(server_address, BaseRequestHandler)
  print(f'Starting server... {port}')
  httpd.serve_forever()
