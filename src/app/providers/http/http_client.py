from requests import get

class HttpClient:
  def get(self, uri, params):
    return get(uri, params)