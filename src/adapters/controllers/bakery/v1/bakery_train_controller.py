from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.bakery.bakery_usecase import BakeryUsecase
from infrastructure.modules.routing.annotations.post import post

@route('/bakery/v1/train')
class BakeryTrainController:
  @get
  def index(self, requests):
    options = requests.query_params
    bakeryUseCase = BakeryUsecase()
    return bakeryUseCase.train_model()
  
  @post
  def predict(self, requests):
    body = requests.body
    bakeryUseCase = BakeryUsecase()
    budget = float(body.get('budget'))
    price = float(body.get('price'))
    sales = bakeryUseCase.predict_sales(budget)
    financial = bakeryUseCase.predict_financial_return(sales, price)
    
    return {
      'predicted_sales': sales, # vendas
      'predicted_financial_return': financial # lucro reais
    }