class RouterRequest:
  def __init__(self, query_params):
      self.query_params = query_params

  def query_params(self, key):
      return self.query_params.get(key)