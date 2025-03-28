from functools import reduce

wejscie = [1, 2, 3, 4, 5]

def add(x, y):
    return x + y

result = reduce(add, wejscie)
print(result)