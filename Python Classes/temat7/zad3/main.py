def f(a, b):
    return a + b
    
wyjscie = []

for i in range(100):
    def loop(x):
        return lambda b: f(x, b)
    wyjscie.append(loop(i))

print(wyjscie)