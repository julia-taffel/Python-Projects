wyjscie_1 = []

for i in range(0,10):
    a = []
    for j in range(0,10):
        a.append(int(0))
    wyjscie_1.append(a)
        
wyjscie_2 = [[0]*10]*10

wyjscie_1[0][0]=1
wyjscie_2[0][0]=1

print(wyjscie_1[1][0] == wyjscie_2[1][0])
print(wyjscie_1[1][0])
print(wyjscie_2[1][0])