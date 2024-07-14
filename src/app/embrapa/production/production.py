from infrastructure.external_services.embrapa import Embrapa

class Production:
  def getProduction(self, options):
    embrapa = Embrapa()
    options['opcao'] = 'opt_02'
    return embrapa.get(options)