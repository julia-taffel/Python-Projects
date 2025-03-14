err = False
for i in range (1, 11):
    if(err): break
    for j in range (1, 11):
        if(err): break
        print("%dx%d="%(i, j),end="")
        wynik=int(input())
        if wynik!=j*i: err = True
if(err): print("SPRÓBUJ JESZCZE RAZ")
else: print("SUKCES")
