from infrastructure.modules.routing.annotations.route import route
from app.bakery.bakery_usecase import BakeryUsecase
from infrastructure.modules.routing.annotations.post import post
from app.bakery.bakery_predict import BakeryPredictUsecase

@route('/bakery/v1/predict')
class BakeryPredictController:
  @post
  def index(self, requests):
    options = requests.query_params
    predictUsecase = BakeryPredictUsecase()
    predicted = predictUsecase.predict(requests.body)
    print(predicted)
    return { "data": "predicted" }
