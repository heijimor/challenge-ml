import json
from http.server import BaseHTTPRequestHandler
from infrastructure.modules.routing.router import Router
from adapters.controllers.embrapa.processing.v1.processing_controller import ProcessingController
from adapters.controllers.embrapa.production.v1.production_controller import ProductionController
from adapters.controllers.embrapa.marketing.v1.marketing_controller import MarketingController
from adapters.controllers.embrapa.importing.v1.importing_controller import ImportingController
from adapters.controllers.embrapa.exporting.v1.exporting_controller import ExportingController
from adapters.controllers.b3.extracting.v1.extracting_controller import ExtractingController

class BaseRequestHandler(BaseHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    self.router = Router()
    self.router.register_controller(ProcessingController)
    self.router.register_controller(ProductionController)
    self.router.register_controller(MarketingController)
    self.router.register_controller(ImportingController)
    self.router.register_controller(ExportingController)
    self.router.register_controller(ExtractingController)
    super().__init__(*args, **kwargs)

  def do_GET(self):
    self.handle_request('GET')

  def do_POST(self):
    self.handle_request('POST')

  def handle_request(self, method):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()
    response = self.router.route_request(self.path, method)
    self.wfile.write(json.dumps(response).encode('utf-8'))