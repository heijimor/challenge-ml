from providers.http.http_client import HttpClient
from providers.extracting.extractor import Extractor
from providers.converter.converter import Converter

class Embrapa:
  def get(self, opt):
    http = HttpClient()
    response = http.get(f'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_{opt}')
    extractor = Extractor()
    table = extractor.extract(response.text, 'tb_base tb_dados')
    converter = Converter()
    return converter.convert(table)