import random

def file_creator():
    #Tworzenie pliku do testowania kodu
    with open("Zad3/wejscie.txt", "w") as file:
        for _ in range(100):
            number = random.randint(1, 1000)
            file.write(str(number) + "\n")
            
def suma(file="Zad3/wejscie.txt"):
    suma = 0
    try:
        with open(file, "r") as file:
            for line in file:
                try:
                    number = int(line.strip())
                    #print(number)
                    suma += number
                except ValueError:
                    print(f"Error: Wrong number in line {line.strip()}")
        print(suma)
    except FileNotFoundError:
        print(f"Error: File '{file}' does not exist")
        
suma()