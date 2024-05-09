from app.use_cases.embrapa import Embrapa

class ExportingUsecase:
  def getExports(self, options):
    embrapa = Embrapa()
    return embrapa.get(options)