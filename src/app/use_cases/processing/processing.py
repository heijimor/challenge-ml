from app.use_cases.embrapa import Embrapa

class Processing:
  def getProcessing(self, options):
    embrapa = Embrapa()
    return embrapa.get(options)