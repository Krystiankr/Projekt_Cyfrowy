import pandas as pd
import numpy as np
import re
from typing import List


class CreateTable:
    postac_sumacyjna: List[int]
    dont_care: List[int]
    wyjscie: List[int]
    df: pd.DataFrame = pd.DataFrame()

    def __init__(self, zmienne: str, postac_sumacyjna: str = '', dont_care: str = ''):
        # self.zmienne => 'x123 x23 x4 x5' -> ['x1', 'x2', 'x4', 'x5']
        self.zmienne = [el[:2] if len(el) > 2 else el for el in re.findall("\w+", zmienne)]
        self.postac_sumacyjna, self.dont_care, self.wyjscie \
        = self._filtr(postac_sumacyjna, dont_care)
        # self.wyjście => połączenie postac_sumacyjna i dont_care
        # e.g. self.postac_sumacyjna = [1, 2, 3]
        #      self.dont_care = [4, 5]
        #      self.wyjscie = [1, 2, 3, 4, 5]
        self._create_df_with_binary_nums()

    def get_postac_sumacyjna(self) -> List[int]:
        return sorted(self.postac_sumacyjna)

    def get_dont_care(self) -> List[int]:
        return sorted(self.dont_care)

    def _binary_length(self):
        max_element = max(self.wyjscie)
        binary_len = len(bin(max_element))-2  # bin(4) = '0b100'
        return binary_len

    def _create_df_with_binary_nums(self) -> None:
        # Tworzę df,
        # columny to podane zmienne
        # Pętla iteruje 2 ^ (ilosc zmiennych)
        # Kazdy wiersz to odpowiednio liczba binarna
        len_ = len(self.zmienne)
        self.df = pd.DataFrame(
            [[int(num)
              for num in f"{int(bin(x)[2:]):0{len_}d}"]  # 'repr bin' =  0000
             for x in range(0, 2 ** len_)],  # e.g. 3, from 000-111, e.g. 4, 0000-1111
            index=np.arange(0, 2 ** len_, 1),
            #columns=[chr(x) for x in range(ord('A'), ord('A')+bin_len)]  # [A, B, C, ..., A + bin_len]
            columns=self.zmienne
        )
        self._set_Y_column()

    def _set_Y_column(self) -> None:
        # Tworzę kolumne Y
        # Iteruje po każdym wierszu jeśli w self.wyjscie jest liczba to 1
        # W przeciwnym wypadku wstaw 0, Dodatkowo w miejsce dont_care wstawiam 'X'
        len_col = self.df.shape[0]
        self.df["Y"] = [1
                   if binary_num in self.wyjscie
                   else 0
                   for binary_num in range(len_col)]
        self.df.Y = list(map(lambda x: 'X' if x in self.get_dont_care() else self.df.at[x, 'Y'], self.df.Y.index))
        self._set_count_1()

    def _set_count_1(self) -> None:
        # Tworzę nową kolumne ilość jedynek, która będzie potrzebna do grupowania.
        # Jedynki są obliczane na podstawie jedynek w danym wierszu.
        self.df["count(1)"] = self.df.apply(lambda x: sum(x[:-1])
                                            if (x[-1] == 1 or x[-1] == 'X')
                                            else -1, axis=1)

    def get_pierwsza_grupa(self) -> pd.DataFrame:
        if self.df.empty:
            return pd.DataFrame()
        df2 = pd.DataFrame({})
        df_mix = self.df.apply(lambda x: [x[-1], ''.join(x[:-2].astype(str)), x[-2]], axis=1).reset_index()
        df2[['Liczba jedynek', 'Liczba Binarna', 'Y']] = df_mix[0].tolist()#, df_mix['index']
        df2["Liczba Dziesiętna"] = df_mix['index']
        df2 = df2[(df2.Y == 1) | (df2.Y == 'X')]
        df2.drop(columns='Y', inplace=True)
        df2 = df2.sort_values(by='Liczba jedynek')
        df2 = df2.reset_index(drop=True)
        return df2

    def return_df(self):
        return self.df

    @staticmethod
    def _filtr(min_term: str = '', dont_care: str = '') -> List[int]:
        # print(min_term, dont_care)

        def _str_to_list(tekst: str) -> List[int]:
            # Wyciągam wszystkie liczby z wejścia
            formated_tekst = re.findall(r'\d+', tekst)  # e.g. ['1', '3', '1', '1', ...]
            set_ = set(formated_tekst)
            list_ = list(set_)
            list_ = [int(x) for x in list_]
            return list_

        def _merge_list(l1: List[int] = [], l2: List[int] = []) -> List[int]:
            # Łącze już dwie gotowe listy, które mają elementy typu int
            # w jedną listę
            list_ = l1 + l2
            sorted_list = sorted(list_)
            # only values < 15
            sorted_list = [x for x in sorted_list if x <= 40]
            return sorted_list

        min_term_ = _str_to_list(min_term)
        dont_care_ = _str_to_list(dont_care)
        wejscie = _merge_list(min_term_, dont_care_)


        return min_term_, dont_care_, wejscie