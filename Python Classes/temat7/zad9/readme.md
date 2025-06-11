Zadanie 9

Dane jest pięć funkcji: informuj_anetke, informuj_beatke, informuj_czeske, informuj_danke i informuj_elke. Każda z nich przyjmuje jeden argument komunikat, który w magiczny sposób przekazuje do właściwej osoby. W programie, nad którym pracuje twój zespół, znajduje się już ponad 100 modułów a w nich wiele różnych funkcji. Dla celów kontrolnych Anetka, Beatka, Cześka, Danka i Elka muszą mieć odnotowane wywołanie określonych funkcji oraz czas, w którym to wywołanie nastąpiło. Jednakże każda z nich ma inny zasób funkcji, które obserwuje. Początkowo każda z nich miała przypisany własny dekorator i programiści dekorowali odpowiednie funkcje, które dana pani miała obserwować. Niestety, niektóre funkcje muszą być obserwowane przez kilka osób. Zrezygnowano więc z tego rozwiązania i zastąpiono to jednym dekoratorem parametrycznym, który przyjmował informacje, które panie mają otrzymywać informacje. W ten sposób każda z obserwowanych funkcji miała tylko jeden dekorator z imionami odpowiednich pań. Niestety, kolejne etapy testów aplikacji wymagają ciągłych zmian. Mimo że te same funkcje są obserwowane, to cały czas zmienia się zasób każdej z pań. Tym samym programiści musieli cały czas przesukiwać wszystkie moduły i ręcznie zmieniać parametry dekoratora przy każdej z funkcji.
Wraz z kolegami i koleżankami programistami uznaliście, że tak dalej być nie może. Po długiej naradzie uznaliście, że spalenie na stosie działu kontroli, jakości, testów i picia kawy nie wchodzi w grę. Dostałeś zatem bojowe zadanie by najpisać jeden dekorator, by wszystkimi rządzić. Każda z obserwowanych funkcji zostanie udekorowana przy pomocy @obserwuj. Ty natomiast masz sprawić, by dekorator rozpoznał, jaka to funkcja i komu przekazać stosowne informacje. W tym celu wyposażono cię w słownik obserwatorzy dostępny w module obserwatorzy. Kluczami tegoż słownika są nazwy funkcji a wartościami kolejne słowniki, z których każdy zawiera imiona określonych pań oraz wartości True / False, zależnie od tego, czy dana pani chce tę funkcję akurat obserwować. Twój dekorator musi pobrać ten słownik, rozpoznać z którą funkcją ma do czynienia, zdecydować, którym paniom przekazać informacje i oczywiście to zrobić. Jako komunikat napisz Funkcja tu wstaw nazwę została wywołana o czasie tu czas i życzy smacznej kawusi. Czas uzyskaj poprzez funkcję time z pakietu time. Pamiętaj, że dekorator musi oczywiście tę funkcję również wywołać i zwrócić jej wartość.

Do testów możesz wykorzystać następujące implementacje pięciu funkcji:

def informuj_anetke(komunikat):
print(komunikat, "Anetka życzy miłego dzionka")

def informuj_beatke(komunikat):
print(komunikat, "Beatka życzy miłego dzionka")

def informuj_czeske(komunikat):
print(komunikat, "Cześka życzy miłego dzionka")

def informuj_danke(komunikat):
print(komunikat, "Danka życzy miłego dzionka")

def informuj_elke(komunikat):
print(komunikat, "Elka życzy miłego dzionka i prosi o twój numer telefonu")
