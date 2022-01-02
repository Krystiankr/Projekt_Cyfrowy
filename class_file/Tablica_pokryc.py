import pandas as pd
import numpy as np
from typing import List, Tuple, Dict
from collections import Counter
from class_file.Reprezentacja_sumacyjna import CreateTable


class DostepneMetody:
    _tab: CreateTable

    def __init__(self, zmienne: str, postac_sumacyjna: str = '', dont_care: str = ''):
        self._tab = CreateTable(zmienne, postac_sumacyjna, dont_care)


    @staticmethod
    def _matched(num1: str, num2: str) -> bool:
        return sum(n1 != n2 for n1, n2 in zip(num1, num2)) == 1
    # assert matched('0000', '000x') == True
    # assert matched('0000', '0000') == False

    @staticmethod
    def _correct_pair(num1: str, num2: str) -> str:
        return ''.join(n1 if n1 == n2 else '-' for n1, n2 in zip(num1, num2))
    # assert correct_pair('0010', '0000') == '00-0'

    @staticmethod
    def _correct_tuple(tuple_elements: Tuple) -> Tuple:
        tup_element = tuple_elements
        # print(f"tupl_elem, {tup_element}")
        while any(isinstance(el, tuple) for el in tup_element):
            tup_element = sum(tup_element, ())
        tup_element = tuple(set(tup_element))
        return tup_element
    # assert correct_tuple(((1, 2), (3, 4))) == (1, 2, 3, 4)
    # assert correct_tuple((1, 2, 3, 4)) == (1, 2, 3, 4)

    @staticmethod
    def _elementy_laczone(df_input: pd.DataFrame) -> list:
        return pd.Series(df_input["Elemtny(łączone)"].values, index=df_input['Element']).to_dict()
    # e.g.
    # (0, 2, 8, 10): -0-0'
    # (2, 3, 6, 7, 10, 11, 14 ,15): '--1-'

    @staticmethod
    def _remove_element(dict_: dict, element):
        if element in dict_.keys():
            dict_.pop(element)

    def _compare_neighbours(self, df_input: pd.DataFrame, main: int, next_: int, dict_lacz: Dict[str, 'int']={}) \
            -> Tuple[pd.DataFrame, list]:
        # Metoda odpowiada za porównanie danego elementu z grupy np. 0
        # Ze wszystkimi elementami grupy następnej np (0, 2), (0, 8)
        df_new = pd.DataFrame(columns=["Obiekt grupowany", "Elemtny(łączone)", "Element", "Użyty"])
        df_main = df_input.copy()
        main_rows = df_main[df_main["Obiekt grupowany"] == main]
        next_rows = df_main[df_main["Obiekt grupowany"] == next_]

        for idx_main, row_main in main_rows.iterrows():
            for idx_, row_ in next_rows.iterrows():
                check1 = row_main['Element']
                check2 = row_['Element']
                if self._matched(check1, check2):
                    # Jeśli porównywane elementy różnią się na dokładnie jednym bicie
                    # to odznacz, że są użyte \/ (usuwam ze słownika)
                    self._remove_element(dict_lacz, row_main["Element"])
                    self._remove_element(dict_lacz, row_["Element"])

                    if df_new.empty:
                        # Jeśli df jest pusta to pierwszy indeks to 0
                        x = 0
                    else:
                        # w przeciwym wypadku, wstaw nowy wiersz w max(index) + 1
                        x = df_new.index.max() + 1
                    grupowy_tuple = self._correct_tuple(tuple([main]) + tuple([next_]))
                    laczony_tuple = self._correct_tuple(tuple([row_main["Elemtny(łączone)"]]) + tuple([row_["Elemtny(łączone)"]]))
                    df_new.loc[x] = [grupowy_tuple,
                                     laczony_tuple,
                                     self._correct_pair(check1, check2),
                                     False]
        return df_new, dict_lacz

    def _create_group(self, df_input: pd.DataFrame, dict_lacz: dict={}) -> pd.DataFrame:
        # Tworze cały etap grupowania np. cały etap2 lub cały etap3
        # Dla każdego elementu z grupy l.jedynek == 1, wykonaj porównanie z grupą następna (to zadanie zlecam compare_neighbours)
        # Plus muszę przekazać df, ponieważ łącze porównania grup
        # DF1 = (0, 2), (0, 8),
        # DF2 = (2, 3), (2,6), (2, 10), ....
        # DF3 = (7, 15), (11, 15), (13, 15), (14, 15)
        # wyjsciem tej metody jest połączenie wszystkich powyższych df = DF1 + DF2 + DF3 + DF4

        df_main = df_input.copy()
        df_out = pd.DataFrame()
        dict_lacz.update(self._elementy_laczone(df_input))
        unique_values = list(df_input['Obiekt grupowany'].unique())
        for idx, el in enumerate(unique_values):
            if el == unique_values[-1]: continue
            df_tmp, dict_lacz = self._compare_neighbours(df_main, unique_values[idx], unique_values[idx+1], dict_lacz)
            df_out = pd.concat([df_out, df_tmp])
        df_out = df_out.drop_duplicates(subset='Element')
        return df_out.reset_index(drop=True), dict_lacz

    def _all_groups(self, df_input: pd.DataFrame):
        # Metoda ta odpowiada, za stworzenie każdej grupy do momentu, aż nie powstanie żadna nowa grupa.
        # I na końcu wypuszcza wszystkie zebrane stąd implikanty.
        # Te, które nie zostały użyte, i wszystkie z ostatniej grupy.
        df_all: List[pd.DataFrame] = []
        df_out, dict_out = self._create_group(df_input, {})
        while not df_out.empty:
            df_out, dict_out = self._create_group(df_out, dict_out)
        return dict_out

    def _przygotuj_tab_pokryc(self, postac_sumacyjna: List[int], implikanty_proste: dict):
        # Tworzę DF na powstawie implikantow.
        # print(f"Postac sumacyjna: {postac_sumacyjna}")
        # print("Słownik")
        # for key, item in implikanty_proste.items():
            # print(f"key[{key}] = {item}")

        df_tab_pokryc = pd.DataFrame(
            columns=list(implikanty_proste.keys()),
            index=postac_sumacyjna,
            data=[['-'] * len(list(implikanty_proste.keys()))]
        )
        return df_tab_pokryc

    def _wypelnij_tab_pokryc(self, df_wstepna: pd.DataFrame, implikanty_proste: dict):
        # Wstawiam + w odpowiednie miejsca w tablicy pokryc.
        for column, elements in implikanty_proste.items():
            # print(f"column = {column}")
            if isinstance(elements, int):
                if elements in df_wstepna.index:
                    df_wstepna.at[elements, column] = '+'  # index, col
            else:
                # print(f"elements: {elements}, {len(elements)=}")
                for element in elements:
                    # print(f"element = {element}")
                    if element in df_wstepna.index:
                        df_wstepna.at[element, column] = '+'  # index, col
        for col in df_wstepna.columns:
            if not '+' in Counter(df_wstepna[col]):
                del df_wstepna[col]
        return df_wstepna

    def get_lista_implikantow(self):
        return list(self.get_tab_pokryc().columns)

    def get_tab_pokryc(self) -> pd.DataFrame:
        df = self._tab.get_pierwsza_grupa().copy()
        df_grupowane = pd.DataFrame()
        df_grupowane[["Obiekt grupowany", "Elemtny(łączone)", "Element"]] = df[['Liczba jedynek', 'Liczba Dziesiętna', 'Liczba Binarna']]

        dict_out = self._all_groups(df_grupowane).copy()
        # print(f"Tab -> postac sum {tab.get_postac_sumacyjna()}")
        out_ = self._przygotuj_tab_pokryc(self._tab.get_postac_sumacyjna(), dict_out)
        return self._wypelnij_tab_pokryc(out_, dict_out)

    def get_tablica_prawdy(self) -> pd.DataFrame:
        return self._tab.return_df().iloc[:, :-1]

    def get_pierwsza_grupa(self) -> pd.DataFrame:
        return self._tab.get_pierwsza_grupa()

    def get_odebrane_dane(self) -> List[int]:
        return self._tab.get_postacsum_dontcare()

    def generuj_funkcje(self) -> str:
        # Generuje funkcje na podstawie poprzednich wyników.
        # Nazwy zmiennych są brane z nazw zmiennych podanych na początku.
        df = self.get_tab_pokryc()
        f_out = 'Y = '
        nazwy = list(self.get_tablica_prawdy().iloc[:, :-1].columns)
        for i, el in enumerate(df.columns):
            for idx, char in enumerate(el):
                if char == '-': continue
                if char == '0':
                    f_out += f"({nazwy[idx]})'"
                if char == '1':
                    f_out += nazwy[idx]
            if i != len(df.columns) - 1:
                f_out += ' + '
        return f_out

    def get_prime_implicants(self):
        df = self.get_tab_pokryc()
        primes = []
        for col in df.columns:
            # print(col)
            arr1 = np.array(list(df[col]))
            indeks = list(np.where(arr1=='+')[0])
            # print(indeks)
            prime = [len(np.where(df.iloc[idx, :]=='+')[0]) for idx in indeks].count(1) != 0
            if prime:
                primes.append(col)
                # print(f"PRIME! {col}")
        return primes


if __name__ == "__main__":
    tab = DostepneMetody(zmienne='x1 x2 x3 x4',
                           postac_sumacyjna='1 2 3 4',
                           dont_care='5 6')
    print(tab.get_odebrane_dane())
