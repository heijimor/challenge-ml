from app.modules.routing.annotations.route import route
from app.modules.routing.annotations.get import get
from app.use_cases.production.production import Production

@route('/production')
class ProductionController:
  @get
  def index(self, requests):
    options = requests.query_params
    service = Production()
    return service.getProduction(options)
