class RouterRequest:
  def __init__(self, query_params, body):
    self.query_params = query_params
    self.body = body

  def query_params(self, key):
    return self.query_params.get(key)

  def body(self, key):
    return self.body.get(key)