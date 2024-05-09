from io import StringIO
import pandas as pd

class ConverterAdapterHtmlToJson:
  def convert(self, element):
    df = pd.read_html(StringIO(str(element[0])))[0]
    return df.to_dict(orient='records')