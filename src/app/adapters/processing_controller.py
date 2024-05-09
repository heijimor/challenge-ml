from providers.annotations.route import route
from providers.annotations.get import get
from use_cases.processing.processing import Processing

@route('/processing')
class ProcessingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = Processing()
    return service.getProcessing(options)
