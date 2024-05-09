class Router:
  def __init__(self):
      self.controllers = {}

  def register_controller(self, controller):
      name = controller.__name__
      path = controller.path
      self.controllers[path] = controller()
      print(f'registering controller.. {controller} by name {name} and path {path}')

  def route_request(self, path, method):
      controller = self.controllers.get(path)
      print(f'controller found.. {controller} by incoming path {path}')

      if controller and hasattr(controller, 'path') and controller.path == path:
          for attr_name in dir(controller):
              attr = getattr(controller, attr_name)
              if hasattr(attr, 'method') and attr.method == method:
                  return attr()
      return {'error': 'Endpoint not found'}