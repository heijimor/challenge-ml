from requests import get
import requests

class HttpClient:
  def get(self, uri, params):
    try:
      response = get(uri, params)
      response.raise_for_status()
      return response
    except requests.exceptions.HTTPError as http_error:
      status_code = response.status_code if response else None
      return {'error': f'HTTP Error {status_code}: {http_error}'}
    except requests.exceptions.RequestException as req_error:
      return {'error': f'Request Error: {req_error}'}
    except Exception as error:
      return {'error': str(error)}