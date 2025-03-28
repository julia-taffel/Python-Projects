wejscie = {1, 2, 3, 4}
wyjscie = set()

def set_gen(set1, set2=[]):
    wyjscie.add(frozenset(set2))
    for i in range(len(set1)):
        set_gen(set1[i+1:], set2 + [set1[i]])

set_gen(list(wejscie))
print(*wyjscie, sep="\n")