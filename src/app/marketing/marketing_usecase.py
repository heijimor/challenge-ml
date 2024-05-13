from infrastructure.external_services.embrapa import Embrapa

class MarketingUsecase:
  def getMarketing(self, options):
    embrapa = Embrapa()
    options['opcao'] = 'opt_04'
    return embrapa.get(options)