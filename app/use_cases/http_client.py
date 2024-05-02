from requests import get

class HttpClient:
  def get(self, uri):
    return get(uri)