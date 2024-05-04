import pandas as pd

class ConverterAdapterHtmlToJson:
  def convert(self, element):
    df = pd.read_html(str(element[0]))[0]
    return df.to_json(orient='records')