def odwrotny_sumator(*args):
    return sum(1 / x for x in args)

wejscie = [
    [1, 3, 5 , 8, 0], 
    [5, 8, 9, 3, 4, 1]]

for r in wejscie:
    result = odwrotny_sumator(*filter(lambda x: x!=0, r))
    print(result)
        