x1=None
x2=None

def x(a, b, c):
    global x1, x2
    dis=b**2-4*a*c
    if dis>0:
        x1=(-b-dis**0.5)/(2*a)
        x2=(-b+dis**0.5)/(2*a)
    elif dis==0:
        x1=(-b)/(2*a)

a=float(input())
b=float(input())
c=float(input())

x(a, b, c)
print(x1, x2)
