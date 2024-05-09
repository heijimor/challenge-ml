from providers.annotations.route import route
from providers.annotations.get import get
from use_cases.production.production import Production

@route('/production')
class ProductionController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = Production()
    return service.getProduction(options)
