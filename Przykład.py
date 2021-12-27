import pandas as pd

from Reprezentacja_sumacyjna import CreateTable
from Tablica_pokryc import get_tab_pokryc, get_tablica_prawdy, get_pierwsza_grupa, generuj_funkcje

if __name__ == "__main__":
    # tab = CreateTable("0, 1, 2, 8, 11, 15, 20, 23, 24, 27, 28", "3, 22, 29, 31")
    tab = CreateTable(postac_sumacyjna="0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15")
    print(get_tablica_prawdy(tab)) #  ok
    # print(get_pierwsza_grupa(tab)) ok
    print(get_tab_pokryc(tab)) # ok
    # print(generuj_funkcje(tab))

