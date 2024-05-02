from bs4 import BeautifulSoup

class Extractor:

  # def Extractor(self):
    # self.uri = 'http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01'

  def extract(self, text, className):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.findAll(class_= className)