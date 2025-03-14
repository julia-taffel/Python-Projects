liczba=int(input())
if liczba==1:
    print("TAK")
else:
    while liczba%2==0:
        if liczba!=1:
            liczba=liczba/2
        if liczba==1:
            print("TAK")
            break
    else:
        print("NIE")
