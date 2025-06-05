#ciąg fib -> 0, 1, suma dwóch poprzednich...

def fib(a=1, b=1):
    while True:
        yield a
        a, b = b, a+b

wyjscie=fib()

for r in fib():
    print(r)
    if r == 4181:
        break