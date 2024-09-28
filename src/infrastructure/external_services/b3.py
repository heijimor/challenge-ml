from infrastructure.modules.http.http_client import HttpClient
import base64
import json
import os
from infrastructure.modules.parquet.parquet import convert_csv_to_partitioned_parquet
from infrastructure.modules.stream.uploader import upload_to_s3

class B3:
  def get(self, options):
    http = HttpClient()
    params = { key: value for key, value in options.items() if value }
    # Realiza o download direto do site da B3
    url = 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetDownloadPortfolioSegment/eyJpbmRleCI6IklCT1YiLCJsYW5ndWFnZSI6InB0LWJyIn0='
    response = http.get(url, params, verify=False)
    # Decodifica de base64 para csv text
    decoded_bytes = base64.b64decode(response.text)
    # Como o arquivo está rodando local, está hard coded, em prod esses dados devem ser dinamicos
    folder_path = '/home/heijimor/Desktop/fiap/challenge-ml/temp'
    os.makedirs(folder_path, exist_ok=True)
    filename = os.path.join(folder_path, 'decoded_file.csv')
    # salvando em formato csv em temp folder
    with open(filename, 'wb') as f:
      f.write(decoded_bytes)

    # Converte para parquet
    convert_csv_to_partitioned_parquet(filename, folder_path)
    # Realiza o upload para o bucket s3
    upload_to_s3('tech-challenge-heijimor', 'output.parquet', f"{folder_path}/output.parquet", True)

    if (filename):
      response = {
        "status": "ok",
        "data": {
            "filename": filename
        }
      }
      return json.dumps(response)
    failed = {
      "status": "error",
      "data": {}
    }
    return json.dumps(failed)