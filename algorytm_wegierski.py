from cmath import inf
import copy
import numpy as np
from termcolor import cprint


#funkcja wypisująca w ładny sposób podaną macierz
def wypisywanie_macierzy(macierz):
    for i in macierz:
        for j in i:
            print("%3s" %(j),end=" ")
        print()

#odejmowanie minimum z wierszy i kolumn
def przeksztalcenie_macierzy_minimum(macierz):
    N=len(macierz)
    macierz_min= np.array(macierz)

    min_el_wiersz=0
    for k in range(N):
        min_el_wiersz=macierz[k][0]
        for i in macierz[k]:
            if min_el_wiersz>i:
                min_el_wiersz=i
        for j in range(N):
            macierz_min[k][j]-=min_el_wiersz

    min_el_kolumna=0
    for k in range(N):
        min_el_kolumna=macierz[0][k]
        for i in macierz:
            if min_el_kolumna>i[k]:
                min_el_kolumna=i[k]
        for j in range(N):
            macierz_min[j][k]-=min_el_kolumna

    return macierz

#pomocnicza funkcja szukająca zer niezależnych w macierzy
def pomocnicza_szukanie_zer(zera_macierz,N):
    zera_niezalezne = []
    while 1 in zera_macierz:
        minimum=inf
        indeks_min=-1
        for k in range(N):
            ile=sum((zera_macierz[k]==1))
            if 1 in zera_macierz[k] and minimum>ile:
                minimum=ile
                indeks_min=k
            
        for i in range(N):
            if zera_macierz[indeks_min,i]==1:
                    zera_niezalezne.append((indeks_min,i))
                    zera_macierz[indeks_min, :] = 0
                    zera_macierz[:,i] = 0
                    break
    return zera_niezalezne

#pomocnicza funkcja szukająca optymalnego wykreślenia lini na wierszach i kolumnach
def pomocnicza_szukanie_lini(macierz_zer,niezaznaczone_wiersze,zera_niezalezne,N):
    zaznaczone_kolumny = []
    zaznaczone_wiersze =[]
    czy_zaznaczone = True
    while czy_zaznaczone:
            czy_zaznaczone = False
            for i in range(len(niezaznaczone_wiersze)):
                wiersz = macierz_zer[niezaznaczone_wiersze[i], :]
                for j in range(N):
                    if j not in zaznaczone_kolumny and wiersz[j] == 1:
                        zaznaczone_kolumny.append(j)
                        czy_zaznaczone = True

            for w, k in zera_niezalezne:
                if w not in niezaznaczone_wiersze and w not in zaznaczone_wiersze and k in zaznaczone_kolumny:
                    niezaznaczone_wiersze.append(w)
                    czy_zaznaczone = True

    for i in list(range(N)):
        if i not in niezaznaczone_wiersze:
            zaznaczone_wiersze.append(i)

    return zaznaczone_kolumny,zaznaczone_wiersze

#funkcja wyznaczająca linie wierszy i kolumn z zerami niezależnymi
def wyznaczanie_lini(macierz):
    N=len(macierz)
    zera=[[0]*N for i in range(N)]
    macierz_zer= np.array(zera)
    for i in range(N):
        for j in range(N):
            if macierz[i][j]==0:
                macierz_zer[i][j]=1
    zera_macierz = copy.deepcopy(macierz_zer)   
    zera_niezalezne=pomocnicza_szukanie_zer(zera_macierz,N)
    zera_niezalezne_wiersz = []
    for i in range(len(zera_niezalezne)):
            zera_niezalezne_wiersz.append(zera_niezalezne[i][0])
    niezaznaczone_wiersze = []   
    for i in list(range(N)):
        if i not in zera_niezalezne_wiersz:
            niezaznaczone_wiersze.append(i)
    zaznaczone_kolumny,zaznaczone_wiersze=pomocnicza_szukanie_lini(macierz_zer,niezaznaczone_wiersze,zera_niezalezne,N)  
    liczba_zer_niezaleznych = len(zaznaczone_wiersze) + len(zaznaczone_kolumny)
    return zera_niezalezne, zaznaczone_wiersze, zaznaczone_kolumny,liczba_zer_niezaleznych

#funkcja przekształcająca macierz poprzez zwiększanie ilości zer niezależnych
def zwiekszanie_liczby_zer_niezaleznych(macierz,wiersze,kolumny):
    N=len(macierz)
    macierz_ulepszona=copy.deepcopy(macierz)
    macierz_lini=[[0]*N for i in range(N)]
    linie= np.array(macierz_lini)
    for i in wiersze:
        for j in range(N):
            linie[i][j]+=1
    for i in range(N):
        for j in kolumny:
            linie[i][j]+=1

    minimum = inf
    for i in range(N):
        for j in range(N):
            if linie[i][j]==0:
                minimum=min(minimum,macierz_ulepszona[i][j])
    for i in range(N):
        for j in range(N):
            if linie[i][j]==0:
                macierz_ulepszona[i][j]-=minimum
            elif linie[i][j]==2:
                macierz_ulepszona[i][j]+=minimum
    return macierz_ulepszona

#algorytm węgierski krok po  kroku
def metoda_wegierska(macierz):
    N=len(macierz)
    #krok 1
    macierz_zer = przeksztalcenie_macierzy_minimum(macierz)
    liczba_zer_niezaleznych = 0
    while liczba_zer_niezaleznych < N:
        #krok 2
        wynik, zaznaczone_wiersze, zaznaczone_kolumny ,liczba_zer_niezaleznych= wyznaczanie_lini(macierz_zer)
        #krok 3
        if liczba_zer_niezaleznych < N:
            #krok 4
            macierz_zer = zwiekszanie_liczby_zer_niezaleznych(macierz_zer, zaznaczone_wiersze, zaznaczone_kolumny)
        
    macierz_wynikowa=[[0]*N for i in range(N)]
    for w,k in wynik:
        macierz_wynikowa[w][k]=1
    return macierz_wynikowa,wynik

#funkcja wypisująca orginalną macierz z zaznaczonym optymalnym przydziałem 
def wypisywanie_wyniku(macierz,wyniki):
    N=len(macierz)
    print("Optymalny przydział zadań:")

    for i in range(N):
        for j in range(N):
            if wyniki[i][j]:
                cprint("%3s" %(macierz[i][j]),end=" ",color='blue')
            else:
                print("%3s" %(macierz[i][j]),end=" ")
        print()
    print()

#funkcja sumująca koszt
def wypisywanie_kosztu(macierz_orginalna,wynik):
    N=len(macierz_orginalna)
    suma_kosztow = 0
    print("Optymalny koszt:")
    k=0
    for m in wynik:
        k+=1
        print(macierz_orginalna[m[0], m[1]],end=" ")
        suma_kosztow+=macierz_orginalna[m[0], m[1]]
        if k==(N):
            print(" = ",end=" ")
        else:
            print(" + ",end=" ")
    print(suma_kosztow)
    

