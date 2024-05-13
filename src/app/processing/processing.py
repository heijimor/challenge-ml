from infrastructure.external_services.embrapa import Embrapa

class Processing:
  def getProcessing(self, options):
    embrapa = Embrapa()
    options['opcao'] = 'opt_03'
    return embrapa.get(options)