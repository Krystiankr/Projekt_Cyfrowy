from Tablica_pokryc import DostepneMetody

if __name__ == "__main__":
    # tab = CreateTable("0, 1, 2, 8, 11, 15, 20, 23, 24, 27, 28", "3, 22, 29, 31")
    # zmienne=['D', 'C', 'B', 'A']
    tab = DostepneMetody(zmienne='x1 x2 x3 x4 x51 x8 x9',postac_sumacyjna="0, 2, 3, 5 6 7 8 9 10 11 12 13 14 15", dont_care='')
    print()
    print(tab.get_pierwsza_grupa())  #  ok
    print(tab.get_tab_pokryc())  # ok
    print(tab.generuj_funkcje())
    print(tab.get_tablica_prawdy())  #  ok
    print(tab.get_lista_implikantow())


