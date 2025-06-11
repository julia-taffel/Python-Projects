import time
import obserwatorzy

def obserwuj(func):
    def wrapper(*args, **kwargs):
        nazwa_funkcji = func.__name__
        wynik = func(*args, **kwargs)
        aktualny_czas = time.time()
        komunikat = f"Funkcja {nazwa_funkcji} została wywołana o czasie {aktualny_czas} i życzy smacznej kawusi."
        
        kto_obserwuje = obserwatorzy.obserwatorzy[nazwa_funkcji]
        for imie, chce_obserwowac in  kto_obserwuje.items():
            if chce_obserwowac:
                if imie == "Beatka":
                    informuj_beatke(komunikat)
                if imie == "Anetka":
                    informuj_anetke(komunikat)
                if imie == "Cześka":
                    informuj_czeske(komunikat)
                if imie == "Danka":
                    informuj_danke(komunikat)
                if imie == "Elka":
                    informuj_elke(komunikat)
            
        return wynik
    return wrapper


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
 
@obserwuj
def funkcja_testowa():
    print("To jest test funkcji!")

    
funkcja_testowa()
#informuj_beatke(komunikat)
