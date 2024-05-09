from urllib.parse import urlparse, parse_qs
from app.modules.routing.router_request import RouterRequest

class Router:
  def __init__(self):
      self.controllers = {}

  def register_controller(self, controller):
      name = controller.__name__
      path = controller.path
      self.controllers[path] = controller()
      print(f'registering controller.. {controller} by name {name} and path {path}')

  def route_request(self, path, method):
      parsed_url = urlparse(path)
      main_path = parsed_url.path
      controller = self.controllers.get(main_path)
      print(f'controller found.. {controller} by incoming path {main_path}')

      if controller and hasattr(controller, 'path') and controller.path == main_path:
          for attr_name in dir(controller):
              attr = getattr(controller, attr_name)
              if hasattr(attr, 'method') and attr.method == method:
                  query_params = parse_qs(parsed_url.query)
                  requests = RouterRequest(query_params)
                  return attr(requests)
      return {'error': 'Endpoint not found'}