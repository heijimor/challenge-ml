from providers.http.http_client import HttpClient
from providers.extracting.extractor import Extractor
from providers.converter.converter import Converter

class Processing:
  def getProcessing(self):
    http = HttpClient()
    response = http.get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02')
    extractor = Extractor()
    table = extractor.extract(response.text, 'tb_base tb_dados')
    converter = Converter()
    return converter.convert(table)