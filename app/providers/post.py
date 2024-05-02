from functools import wraps

def post(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.method = 'POST'
    return wrapper