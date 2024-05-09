from providers.annotations.route import route
from providers.annotations.get import get
from use_cases.marketing.marketing_usecase import MarketingUsecase

@route('/marketing')
class MarketingController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = MarketingUsecase()
    return service.getMarketing(options)
