import string

text = str(input())

def check_text(text):
    check = False
    for char in text:
        if char not in string.ascii_letters:
            check = True
    if check == True:
        print("TAK")
    else: print("NIE")
            
check_text(text)