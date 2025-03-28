wejscie = {1, 2, 3, 4}
wyjscie = set()

elementy = list(wejscie)
n = len(elementy)

#przesunięcie bitu 1 o n pozycji w lewo 
for i in range(1 << n): 
    set1 = set()
    for j in range(n):
        #czy j-ty bit liczby i jest ustawiony na 1
        if (i >> j) & 1:
            set1.add(elementy[j])
    wyjscie.add(frozenset(set1))

print(*wyjscie, sep="\n")