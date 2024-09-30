import json

class BakeryMockApi:
  def getMarketingData(self):
    response = {
      "data": [
        {
          "marketingId": 1,
          "value": 10
        },
        {
          "marketingId": 2,
          "value": 15
        },
        {
          "marketingId": 3,
          "value": 20
        },
        {
          "marketingId": 4,
          "value": 25
        },
        {
          "marketingId": 5,
          "value": 30
        }
      ]
    }
    return json.dumps(response)
  
  def getOrders(self):
    response = {
      "data": [
        {
          "vendasId": 1,
          "marketingId:": 1,
          "value": 100
        },
        {
          "vendasId": 2,
          "marketingId:": 2,
          "value": 150
        },
        {
          "vendasId": 3,
          "marketingId:": 3,
          "value": 200
        },
        {
          "vendasId": 4,
          "marketingId:": 4,
          "value": 250
        },
        {
          "vendasId": 5,
          "marketingId:": 5,
          "value": 300
        }
      ]
    }
    return json.dumps(response)