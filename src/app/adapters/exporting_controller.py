from providers.annotations.route import route
from providers.annotations.get import get
from use_cases.exporting.exporting_usecase import ExportingUsecase

@route('/exporting')
class ExportingController:
  @get
  def index(self, requests):
    print('requests >>>>>>>>>>>>>>>>>>>>>>>>>>>..')
    print(requests.query_params)
    service = ExportingUsecase()
    return service.getExports()
