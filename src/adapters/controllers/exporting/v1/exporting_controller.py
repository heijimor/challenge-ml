from app.modules.routing.annotations.route import route
from app.modules.routing.annotations.get import get
from app.use_cases.exporting.exporting_usecase import ExportingUsecase

@route('/exporting')
class ExportingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = ExportingUsecase()
    return service.getExports(options)
