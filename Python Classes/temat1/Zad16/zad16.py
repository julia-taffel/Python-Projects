while True:
    err = False
    for i in range (1, 11):
        if(err): break
        for j in range (1, 11):
            if(err): break
            print("%dx%d="%(i, j),end="")
            wynik=int(input())
            if wynik!=j*i:    
                print("SPRÓBUJ JESZCZE RAZ")
                err = True
                break
        if err: break
    if err == False: break
print("SUKCES")
