from infrastructure.modules.http.http_client import HttpClient
import base64
import csv
import os

class B3:
  def get(self, options):
    http = HttpClient()
    params = { key: value for key, value in options.items() if value }
    url = 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetDownloadPortfolioDay/eyJpbmRleCI6IklCT1YiLCJsYW5ndWFnZSI6InB0LWJyIn0='
    response = http.get(url, params, verify=False)
    decoded_bytes = base64.b64decode(response.text)

    # Folder path where you want to save the CSV file on the server
    folder_path = '/home/heijimor/Desktop/fiap/challenge-ml/temp'

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Filename for the decoded CSV file
    filename = os.path.join(folder_path, 'decoded_file.csv')

    # Write the decoded bytes to a CSV file
    with open(filename, 'wb') as f:
        f.write(decoded_bytes)

    print(f"Decoded CSV file saved successfully to {filename}")