from providers.route import route
from providers.get import get

@route('/processing')
class ProcessingController:
  @get
  def index(self):
    return {'message': 'Hello, World!'}