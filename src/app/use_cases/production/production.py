from app.use_cases.embrapa import Embrapa

class Production:
  def getProduction(self, options):
    embrapa = Embrapa()
    return embrapa.get(options)