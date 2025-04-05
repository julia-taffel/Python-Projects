def file_creator(input_file="Zad5/wejscie.txt", output_file="Zad5/wyjscie.txt"):
    try:
        with open(input_file, "r") as file1:
            inside = file1.read()
            upside_down = inside[::-1]
            
        with open(output_file, "w") as file2:
            file2.write(upside_down)
                
    except FileNotFoundError:
        print(f"Error: File '{input_file}' does not exist")
        
file_creator()