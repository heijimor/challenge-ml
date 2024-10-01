from infrastructure.modules.routing.annotations.route import route
from infrastructure.modules.routing.annotations.get import get
from app.b3.extracting.extracting_usecase import ExtractingUsecase

import os
import json
from infrastructure.external_services.bakery.mock_api import BakeryMockApi

@route('/bakery/v1/extracting')
class BakeryExtractingController:
  @get
  def index(self, requests):
    options = requests.query_params

    mockApi = BakeryMockApi()
    marketing = mockApi.getMarketingData() 
    orders = mockApi.getOrders()

    # should upload to s3
    # in s3 should merge this date and simplify into data like this
    # {
        # 'gasto_marketing': [10, 15, 20, 25, 30],
        # 'vendas': [100, 150, 200, 250, 300]
    # }

    return {
        marketing: marketing,
        orders: orders,
    }
