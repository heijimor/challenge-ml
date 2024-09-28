from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.b3.extracting.extracting_usecase import ExtractingUsecase
import json

@route('/bakery/v1')
class BakeryController:
  @get
  def index(self, requests):
    options = requests.query_params
    return {
      "message": "Hello, World!",
      "status": "success"
    }
