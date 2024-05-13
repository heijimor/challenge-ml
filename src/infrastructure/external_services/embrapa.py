from infrastructure.modules.http.http_client import HttpClient
from infrastructure.modules.extracting.extractor import Extractor
from infrastructure.modules.converter.converter import Converter

class Embrapa:
  def get(self, options):
    http = HttpClient()
    params = { key: value for key, value in options.items() if value }
    response = http.get('http://vitibrasil.cnpuv.embrapa.br/index.php', params)
    extractor = Extractor()
    table = extractor.extract(response.text, 'tb_base tb_dados')
    converter = Converter()
    return converter.convert(table)