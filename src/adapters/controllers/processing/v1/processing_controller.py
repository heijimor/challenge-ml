from app.modules.routing.annotations.route import route
from app.modules.routing.annotations.get import get
from app.use_cases.processing.processing import Processing

@route('/processing')
class ProcessingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = Processing()
    return service.getProcessing(options)
