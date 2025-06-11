def wiecej_wiecej(lista):
    def dekorator(func):
        def wrapper(*args, **kwargs):
            for i in lista:
                yield func(i, *args, **kwargs)
        return wrapper
    return dekorator

@wiecej_wiecej([1, 2, 3])
def funkcja(a, b):
    return a ** b

for i in funkcja(2):
    print(i)