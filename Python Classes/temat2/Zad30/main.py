wejscie={'klucz1':(1, 3, 3), 'klucz2':(4, 5, 6)}

list = []
for key, tuple in wejscie.items():
    #print(f"key: {key}")
    for value in tuple:
        if value not in list:
            print(value)
            list.append(value)