from use_cases.embrapa import Embrapa

class MarketingUsecase:
  def getMarketing(self):
    embrapa = Embrapa()
    return embrapa.get('04')