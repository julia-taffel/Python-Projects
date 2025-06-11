def przywitanie_funkcji(func):
    def wrapper(*args, **kwargs):
        print(f"Funkcja {func.__name__} czuje się kochana")
        return func(*args, **kwargs)
    return wrapper

@przywitanie_funkcji
def multi(a, b):
    return a*b
    
multi(2, 3)