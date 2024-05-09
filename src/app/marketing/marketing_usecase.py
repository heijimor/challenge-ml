from infrastructure.external_services.embrapa import Embrapa

class MarketingUsecase:
  def getMarketing(self, options):
    embrapa = Embrapa()
    return embrapa.get(options)