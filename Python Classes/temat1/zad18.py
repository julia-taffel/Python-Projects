suma=float(0)
ilo=float(1)
ary=float(0)
geo=float(0)
i=1
while True:
    h=float(input())
    if h<=0: break
    suma=suma+h
    ilo=ilo*h
    ary=(suma)/i
    geo=ilo**(1/i)
    i=i+1
print(suma)
print(ilo)
print(ary)        
print(geo)        
        
