wejscie = ["Raz", "Dwa", "Trzy"]

with open("Zad2/wyjscie.txt", "w") as file:
    for line in wejscie:
        file.write(line + "\n")
        
print(file)