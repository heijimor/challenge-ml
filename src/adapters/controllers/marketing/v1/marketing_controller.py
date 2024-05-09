from app.modules.routing.annotations.route import route
from app.modules.routing.annotations.get import get
from app.use_cases.marketing.marketing_usecase import MarketingUsecase

@route('/marketing')
class MarketingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = MarketingUsecase()
    return service.getMarketing(options)
