from bs4 import BeautifulSoup

class Extractor:
  def extract(self, text, className):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.findAll(class_= className)