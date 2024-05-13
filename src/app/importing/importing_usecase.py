from infrastructure.external_services.embrapa import Embrapa

class ImportingUsecase:
  def getImports(self, options):
    embrapa = Embrapa()
    options['opcao'] = 'opt_05'
    return embrapa.get(options)