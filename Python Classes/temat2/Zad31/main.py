wejscie={'klucz1':[1, 2, 3], 'klucz2':[3, 5, 6]}

list1 = []
for key, list2 in wejscie.items():
    #print(f"key: {key}")
    for value in list2:
        if value not in list1:
            print(value)
            list1.append(value)
