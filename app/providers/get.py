from functools import wraps

def get(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.method = 'GET'
    return wrapper