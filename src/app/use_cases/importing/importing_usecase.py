from use_cases.embrapa import Embrapa

class ImportingUsecase:
  def getImports(self):
    embrapa = Embrapa()
    return embrapa.get('05')