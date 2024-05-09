from app.modules.routing.annotations.route import route
from app.modules.routing.annotations.get import get
from app.use_cases.importing.importing_usecase import ImportingUsecase

@route('/importing')
class ImportingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = ImportingUsecase()
    return service.getImports(options)
