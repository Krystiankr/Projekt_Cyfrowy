import pandas as pd

from Reprezentacja_sumacyjna import CreateTable
from Tablica_pokryc import get_tab_pokryc, get_tablica_prawdy, get_pierwsza_grupa

if __name__ == "__main__":
    tab = CreateTable("0, 1, 2, 3, 5, 9, 12, 14, 15", "4, 8, 11")

    # print(get_tab_pokryc(tab))
    # print(get_tablica_prawdy(tab))
    print(get_pierwsza_grupa(tab))

