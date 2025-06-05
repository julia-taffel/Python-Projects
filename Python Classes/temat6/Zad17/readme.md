Zadanie 17

Napisz funkcję only_strs, która przyjmuje dowolną liczbę argumentów pozycyjnych. Każdy argument jest obiektem iterowalnym (listą, krotką, zbiorem, generatorem itp.). Funkcja ma zwracać generator, który przekaże wszystkie kolejne elementy przekazanych przez argumenty obiektów iterowalnych, skonwertowane na typ str. Innymi słowy, funkcja ta konkatenuje wszystkie przekazane obiekty i konwertuje ich elementy na str.

Sugestia: Warto w rozwiązaniu spróbować wykorzystać yield from dla przećwiczenia, choć nie jest to jedyne rozwiązanie. Przykładowo only_strs([1,2,3],(True,False),{"a","b","c"}) zwraca kolejno "1","2","3","True","False","a","b","c". Oczywiście, w przypadku zbiorów, kolejność może być inna.