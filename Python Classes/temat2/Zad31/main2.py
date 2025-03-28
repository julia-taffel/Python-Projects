wejscie={'klucz1':[1, 2, 3], 'klucz2':[3, 5, 6]}

list1 = []
for list2 in wejscie.values():
    tuple1 = tuple(list2)
    
    if tuple1 not in list1:            
        list1.append(tuple1)
        print(list2)