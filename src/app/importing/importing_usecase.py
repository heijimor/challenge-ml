from infrastructure.external_services.embrapa import Embrapa

class ImportingUsecase:
  def getImports(self, options):
    embrapa = Embrapa()
    return embrapa.get(options)