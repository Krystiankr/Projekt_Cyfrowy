import pandas as pd

from Reprezentacja_sumacyjna import CreateTable
from Tablica_pokryc import get_tab_pokryc

if __name__ == "__main__":
    tab = CreateTable("1, 2, 3, 5, 9, 12, 14, 15", "4, 8, 11")

    print(get_tab_pokryc(tab))

