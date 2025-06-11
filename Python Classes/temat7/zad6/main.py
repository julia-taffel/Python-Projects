def stringer(func):
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs))
    return wrapper

@stringer
def Liczby():
    return print(123)

Liczby()