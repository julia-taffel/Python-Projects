def silnia(x):
    #4! = 4 * 3 * 2 * 1 = 24
    if x < 0:
        return ValueError
    if x == 0:
        return 1
    return x * silnia(x-1)

print(silnia(4))