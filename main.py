import copy
import random
from graf import rysuj_graf, rysuj_graf_z_przydzialem
from algorytm_wegierski import wypisywanie_macierzy,metoda_wegierska,wypisywanie_kosztu,wypisywanie_wyniku
import numpy as np

def main():
    klucz=input(
'''
########################################
        Algorytm węgierkski 
########################################

Wybierz opcję: 
1. Podaj macierz kosztów ręcznie
2. Załaduj macierz z pliku "dane.txt"
3. Stwórz pseudolosową macierz (rozmiar 3-10)

Wprowadź numer opcji: ''')
    macierz_kosztow=[]
    if(klucz =="1"):
            try:
                N=int(input("Podaj rozmiar macierzy: "))
                if N<=0:
                    raise ValueError
            except ValueError:
                print("Podałeś złą wartość!")
                raise  SystemExit
            except:
                print("Inny błąd!")
                raise  SystemExit
            wiersz=[]
            for i in range(N):
                print(f"Podaj {i+1} wiersz macierzy (elementy odzielone spacjami):")
                w=input().split(" ")
                for j in range(N):
                    try:
                        wiersz.append(int(w[j]))
                    except IndexError:
                        print("Nie podałeś wystarczającej liczby elementów!")
                        raise  SystemExit
                    except ValueError:
                        print("Nie podałeś liczby całkowitej!")
                        raise  SystemExit
                    except:
                        print("Inny błąd!")
                        raise  SystemExit

                macierz_kosztow.append(list(wiersz))
                wiersz.clear()

    elif(klucz =="2"):
            print("Wczytano macierz z pliku")
            plik="dane.txt"
            f = open(plik, "r")
            lines = f.readlines()
            wiersz=[]
            N=int(lines[0])
            for line in lines[1:]:
                w=line.split(" ")
                for j in range(N):
                    try:
                        wiersz.append(int(w[j]))
                    except IndexError:
                        print("Plik nie zawiera wystarczającej liczby elementów!")
                        wiersz.append(0)
                    except ValueError:
                        print("Plik nie zawiera wszystkich liczb całkowitych!")
                        raise  SystemExit
                    except:
                        print("Inny błąd!")
                        raise  SystemExit
                macierz_kosztow.append(list(wiersz))
                wiersz.clear()
            f.close()
    elif(klucz =="3"):
            print("Stworzono pseudolosową macierz")
            wiersz = []
            N=random.randint(3,10)
            print("Rozmiar macierzy: " +str(N))
            for i in range(N): 
                for j in range(N):
                    n = random.randint(1,200)
                    wiersz.append(n)
                macierz_kosztow.append(list(wiersz))
                wiersz.clear()
            
    else:
            print("Zły numer")
            raise  SystemExit

    macierz_kosztow = np.array(macierz_kosztow)
    print("Macierz")
    wypisywanie_macierzy(macierz_kosztow)
    print()
    rysuj_graf(macierz_kosztow)

    MinMax=input(
'''
Wybierz akcję: 
1. Minimalizacja kosztów
2. Maksymalizacja efektów

Wprowadź numer opcji: ''')
    macierz_kopia=copy.deepcopy(macierz_kosztow)
    if MinMax=='2':
        macierz_kopia=-macierz_kopia

    macierz_wynikowa, wynik=metoda_wegierska(macierz_kopia)
    print()

    wypisywanie_wyniku(macierz_kosztow,macierz_wynikowa)
    wypisywanie_kosztu(macierz_kosztow,wynik)
    rysuj_graf_z_przydzialem(macierz_kosztow,wynik)


if __name__ == "__main__":
    main()


