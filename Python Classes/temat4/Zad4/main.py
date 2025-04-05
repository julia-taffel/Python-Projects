def deletion(file="Zad4/wejscie.txt"):
    try:
        with open(file, "r") as file1:
            lines = file1.readlines()
        
        first_A = [line for line in lines if line.startswith("A")]
        
        with open(file, "w") as file2:
            file2.writelines(first_A)
            
    except FileNotFoundError:
        print(f"Error: File '{file}' does not exist")
        
deletion()