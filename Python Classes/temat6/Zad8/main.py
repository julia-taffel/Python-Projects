def dzielniki(a):
    while a != 1:
        yield a%2
        a //= 2
    #yield 1
    
a = int(input())

for no in dzielniki(a):
    print(no)