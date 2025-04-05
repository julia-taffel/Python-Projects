wyjscie = []

file = open("Zad1/wejscie.txt", "r")

for line in file:
    wyjscie.append(line)
file.close()
print(wyjscie)