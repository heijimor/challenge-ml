from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.b3.extracting.extracting_usecase import ExtractingUsecase

@route('/b3/extracting')
class ExtractingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = ExtractingUsecase()
    return service.get(options)
