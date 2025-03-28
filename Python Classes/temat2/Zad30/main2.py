wejscie={'klucz1':(1, 2, 3), 'klucz2':(3, 5, 6)}

tuple1 = set()
for tuple2 in wejscie.values():
    if tuple2 not in tuple1:            
        tuple1.add(tuple2)
        print(tuple2)