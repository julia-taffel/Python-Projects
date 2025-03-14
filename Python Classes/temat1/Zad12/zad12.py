ile=0
while ile>=0:
    liczba=input()
    if liczba=="STOP":
        break
    liczba=int(liczba)
    if liczba%2==0:
        ile+=1
print(ile)