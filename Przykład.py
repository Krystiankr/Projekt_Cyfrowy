import pandas as pd

from Reprezentacja_sumacyjna import CreateTable
from Tablica_pokryc import get_tab_pokryc, get_tablica_prawdy, get_pierwsza_grupa, generuj_funkcje, get_lista_implikantow

if __name__ == "__main__":
    # tab = CreateTable("0, 1, 2, 8, 11, 15, 20, 23, 24, 27, 28", "3, 22, 29, 31")
    # zmienne=['D', 'C', 'B', 'A']
    tab = CreateTable(zmienne='x1 x2 x3 x4 x51 x8 x9',postac_sumacyjna="0, 2, 3, 5 6 7 8 9 10 11 12 13 14 15")
    print()
    # print(get_pierwsza_grupa(tab)) ok
    print(get_tab_pokryc(tab)) # ok
    # print(generuj_funkcje(tab))
    print(generuj_funkcje(tab))
    print(get_tablica_prawdy(tab)) #  ok
    print(get_lista_implikantow(tab))

