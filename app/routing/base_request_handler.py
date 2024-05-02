import json
from http.server import BaseHTTPRequestHandler
from routing.router import Router
from adapters.ProcessingController import ProcessingController

class BaseRequestHandler(BaseHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    self.router = Router()
    self.router.register_controller(ProcessingController)
    super().__init__(*args, **kwargs)

  def do_GET(self):
    self.handle_request('GET')

  def do_POST(self):
    self.handle_request('POST')

  def handle_request(self, method):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    response = self.router.route_request(self.path, method)
    self.wfile.write(json.dumps(response).encode('utf-8'))