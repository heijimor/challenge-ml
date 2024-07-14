from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.embrapa.processing.processing import Processing

@route('/processing')
class ProcessingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = Processing()
    return service.getProcessing(options)
