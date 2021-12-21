from Create_Table import CreateTable


if __name__ == "__main__":
    # table.return.df() -> pierwsze columny to reprezentacja liczby binarnej, druga od konca to Y, ostatnia to count(1) liczba jedynek, tylko gdy Y == 1, inaczej Y == -1
    # table.first_group -> zwraca typ defaultdict, klucze to grupy, values: np. [-1, 0, 0, 1] gdzie -1 to 'x'
    # table.print_first_group() -> wypisuje w ładny sposob poszczególne grupy i ich elementy
    # wprowadzone jest ograniczenie liczb to max 40

    table = CreateTable()
    print(table.return_df())
    print(table.first_group())
    table.print_first_group()
