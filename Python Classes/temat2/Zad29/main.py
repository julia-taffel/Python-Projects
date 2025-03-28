wejscie_1 = {'klucz1':1, 'klucz2':2}
wejscie_2 ={'klucz3': 3, 'klucz4':4}

wejscie=wejscie_1.copy()
wejscie.update(wejscie_2)

print(*[f"{x} {y}" for x, y in wejscie.items()], sep="\n", end="")
print("abc")