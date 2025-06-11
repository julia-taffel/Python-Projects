def bezbledny(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            print(f"Funkcja {func.__name__} wywołała błąd, ale jest jej bardzo przykro")
    return wrapper

@bezbledny
def funkcja(a, b):
    c=a+b
    return print("Oto ja, funkcja!")

funkcja(2)