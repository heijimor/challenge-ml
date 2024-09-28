from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.bakery.bakery_usecase import BakeryUsecase

@route('/bakery/v1/train')
class BakeryTrainController:
  @get
  def index(self, requests):
    options = requests.query_params
    bakeryUseCase = BakeryUsecase()
    return bakeryUseCase.get(options)
