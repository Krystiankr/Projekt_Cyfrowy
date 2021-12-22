from Create_Table import CreateTable, CreateFirstGroup


if __name__ == "__main__":
    # table.return.df() -> pierwsze columny to reprezentacja liczby binarnej, druga od konca to Y, ostatnia to count(1) liczba jedynek, tylko gdy Y == 1, inaczej Y == -1
    # table.first_group -> zwraca typ defaultdict, klucze to grupy, values: np. [-1, 0, 0, 1] gdzie -1 to 'x'
    # table.print_first_group() -> wypisuje w ładny sposob poszczególne grupy i ich elementy
    # wprowadzone jest ograniczenie liczb to max 40
    # table.get_minterm() -> zwraca wejsciowy minterm w typie List[int]
    # table.get_dont_care() -> to samo co wyżej
    # table.get_df() -> wyswietla ladny widok df
    #
    table = CreateTable("4, 8, 10, 11, 12, 15", "9, 14")
    print(table)

    CreateFirstGroup("0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15")
# zmiana

