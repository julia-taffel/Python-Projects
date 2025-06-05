Zadanie 15

Napisz funkcję egzekutor, która przyjmuje dowolną liczbę argumentów pozycyjnych i dowolną liczbę argumentów opcjonanych. Każdy argument pozycyjny to funkcja dwuargumentowa. Funkcja egzekutor wywołuje każdą z przekazanych funkcji na każdym kluczu i wartości przekazanych jako argumenty opcjonalne.

Przykład:

egzekutor(lambda x,y:x+y, lambda x,y:y+x, a="b", b="c")
"ab"
"ba"
"bc"
"cb"