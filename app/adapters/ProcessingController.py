from providers.route import route
from providers.get import get
from use_cases.http_client import HttpClient
from use_cases.extractor import Extractor

@route('/processing')
class ProcessingController:
  @get
  def index(self):
    # move it later
    http = HttpClient()
    response = http.get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02')
    extractor = Extractor()
    table = extractor.extract(response.text, 'tb_base tb_dados')
    print(table)
    return {'message': 'Hello, World!'}