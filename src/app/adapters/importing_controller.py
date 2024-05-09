from providers.annotations.route import route
from providers.annotations.get import get
from use_cases.importing.importing_usecase import ImportingUsecase

@route('/importing')
class ImportingController:
  @get
  def index(self):
    service = ImportingUsecase()
    return service.getImports()
