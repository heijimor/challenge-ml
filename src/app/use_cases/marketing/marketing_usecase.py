from providers.http.http_client import HttpClient
from providers.extracting.extractor import Extractor
from providers.converter.converter import Converter
from use_cases.embrapa import Embrapa

class MarketingUsecase:
  def getMarketing(self):
    embrapa = Embrapa()
    return embrapa.get('04')