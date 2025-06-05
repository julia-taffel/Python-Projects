def only_strs(*args):
    for r in args:
        yield from (str(item) for item in r)
    
result = only_strs([1,2,3],(True,False),{"a","b","c"})

for i in result:
    print(i)