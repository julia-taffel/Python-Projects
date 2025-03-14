def x(a, b, c):
    dis=b**2-4*a*c
    if dis<0:
        x1=None
        x2=None
        return x1, x2
    elif dis==0:
        x1=(-b)/(2*a)
        x2=None
        return x1, x2
    else:
        x1=(-b-dis**0.5)/(2*a)
        x2=(-b+dis**0.5)/(2*a)
        return x1, x2    

a=float(input())
b=float(input())
c=float(input())

print(x(a,b,c))
