from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.embrapa.marketing.marketing_usecase import MarketingUsecase

@route('/marketing')
class MarketingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = MarketingUsecase()
    return service.getMarketing(options)
