from app.modules.converter.converter_adapter_html_to_json import ConverterAdapterHtmlToJson

class Converter:
  def convert(self, element):
    adapter = ConverterAdapterHtmlToJson()
    return adapter.convert(element)