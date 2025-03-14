for i in range (1, 11):
    for j in range (1, 11):
        print("%dx%d="%(i, j),end="")
        wynik=int(input())
        if wynik!=j*i:
            print("SPRÓBUJ JESZCZE RAZ")
            break
        if i==10 and j==10:
            print("SUKCES")
            break
    if wynik!=j*i:
        break
        
