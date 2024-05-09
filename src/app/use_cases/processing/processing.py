from use_cases.embrapa import Embrapa

class Processing:
  def getProcessing(self):
    embrapa = Embrapa()
    return embrapa.get('03')