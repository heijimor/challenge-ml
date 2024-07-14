from infrastructure.external_services.b3 import B3
from infrastructure.external_services.embrapa import Embrapa

class ExtractingUsecase:
  def get(self, options):
    b3 = B3()
    print(b3.get(options))
    embrapa = Embrapa()
    return embrapa.get(options)