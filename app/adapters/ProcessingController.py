from providers.route import route
from providers.get import get
from use_cases.http_client import HttpClient

@route('/processing')
class ProcessingController:
  @get
  def index(self):
    # move it later
    http = HttpClient()
    response = http.get('http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02')
    print(response.text)
    return {'message': 'Hello, World!'}