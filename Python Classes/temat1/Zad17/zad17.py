h=int(input())
for i in range(1,h+1):
    x = int(2*i-1)
    z = int(h-i)
    print(" "*z, end="")
    print("*"*x)
