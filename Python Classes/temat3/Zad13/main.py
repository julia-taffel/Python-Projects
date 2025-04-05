import string

text = str(input())

def check_whitespaces(text):
    check = False
    for char in text:
        if char in string.whitespace:
            check = True
    if check == True:
        print("TAK")
    else: print("NIE")
            
check_whitespaces(text)