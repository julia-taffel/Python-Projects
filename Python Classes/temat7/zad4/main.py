wejscie = [{1 : 6453, 2 : 534}, {1 : 4545, 2 : 634}]

def count_refluxibility(a1, a2, a3, a4, position):
    return print(a1, a2, a3, a4, position)

wyjscie = []

for i in wejscie:
    def reflux(par):
        return lambda position: count_refluxibility(**par, position=position)
    new_i = dict(i)
    new_i["count_refluxibility"] = reflux(i)
    wyjscie.append(new_i)