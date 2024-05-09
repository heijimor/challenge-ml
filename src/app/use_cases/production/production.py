from use_cases.embrapa import Embrapa

class Production:
  def getProduction(self):
    embrapa = Embrapa()
    return embrapa.get('02')