Zadanie 10

Napisz funkcję czas, która zwraca generator. Funkcja ta liczy i zwraca czas między kolejnymi yieldami. Funkcję tę można zastosować jako licznik czasu między kolejnymi etapami wykonywania programu.
Podpowiedź: Zaimportuj funkcję time z pakietu time.

Przykład zastosowania funkcji czas:

czasomierz = czas()
do_something()
print(next(czasomierz))
do_something_else()
print(next(czasomierz))

W odróżnieniu od standardowych sposobów na mierzenie tego, funkcja ta pozwala zastosować oddzielne, niezależne liczniki.