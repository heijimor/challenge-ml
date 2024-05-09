def route(path):
    def decorator(cls):
        cls.path = path
        return cls
    return decorator