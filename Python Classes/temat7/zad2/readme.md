Zadanie 2

Proszę napisać funkcję create_checker, która zwróci funkcję wykonującą test spójności danych na podanej bazie danych.

Obecna funkcja check_tables jest wadliwie napisana i wymaga podawania każdorazowo argumentu database, co może powodować problemy w przypadku łączenia się z wieloma bazami danych jednocześnie. W związku z tym, chcemy napisać własną funkcję, która będzie przyjmować połączenie z bazą danych jako argument i uniknąć podawania każdorazowo argumentu.

Funkcja create_checker powinna przyjąć połączenie z bazą danych jako argument, a następnie zwrócić funkcję, która będzie korzystać z tego połączenia do wykonania testu spójności danych. W ten sposób, możemy wykonywać testy na różnych bazach danych w różnych częściach programu, bez ryzyka konfliktów w użyciu globalnej zmiennej.

# Postać funkcji check_tables

def check_tables(database):
...
