def powitanie(nazwisko, imie):
    print(f"Witaj, {imie} {nazwisko}!")

user_name = input("Podaj swoje imię: ")
user_surname = input("Podaj swoje nazwisko: ")

powitanie(imie = user_name, nazwisko = user_surname)