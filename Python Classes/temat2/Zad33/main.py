wejscie={1:{"Maths":[3, 5, 2], "English":[6, 3, 5]}, 2:{"Maths":[5, 3, 6], "English":[1, 3, 2]}, 3:{"Maths":[2, 3, 1], "English":[5, 4, 4]}}
wyjscie = {}
ave=float()

def average(list1=[]):
    n = len(list1)
    if n == 0:
        return 0
    ave = sum(list1)/n
    return ave

for key, value1 in wejscie.items():
    list1=[]
    for value2 in value1.values():
        list1.extend(value2)
        #print(list1)    
    wyjscie[key] = average(list1)
    
print(wyjscie)