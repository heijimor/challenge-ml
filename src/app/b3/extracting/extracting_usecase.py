from infrastructure.external_services.embrapa import Embrapa

class ExportingUsecase:
  def getExports(self, options):
    embrapa = Embrapa()
    options['opcao'] = 'opt_06'
    return embrapa.get(options)