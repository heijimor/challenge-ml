from use_cases.embrapa import Embrapa

class ExportingUsecase:
  def getExports(self):
    embrapa = Embrapa()
    return embrapa.get('06')