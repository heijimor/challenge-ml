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

    return {
        marketing: marketing,
        orders: orders,
    }
