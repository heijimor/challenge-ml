from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.embrapa.importing.importing_usecase import ImportingUsecase

@route('/importing')
class ImportingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = ImportingUsecase()
    return service.getImports(options)
