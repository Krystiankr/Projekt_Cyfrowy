import pandas as pd
import numpy as np
import re
from typing import List


class CreateTable:
    postac_sumacyjna: List[int]
    dont_care: List[int]
    wyjscie: List[int]
    df: pd.DataFrame = pd.DataFrame()

    def __init__(self, postac_sumacyjna: str = '', dont_care: str = ''):

        self.postac_sumacyjna, self.dont_care, self.wyjscie \
        = self._filtr(postac_sumacyjna, dont_care)
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
        len_ = self._binary_length()
        bin_len = 4 if len_ <= 4 else len_
        self.df = pd.DataFrame(
            [[int(num)
              for num in f"{int(bin(x)[2:]):0{bin_len}d}"]  # 'repr bin' =  0000
             for x in range(0, 2 ** len_)],  # e.g. 3, from 000-111, e.g. 4, 0000-1111
            index=np.arange(0, 2 ** len_, 1),
            columns=[chr(x) for x in range(ord('A'), ord('A')+bin_len)]  # [A, B, C, ..., A + bin_len]
        )
        self._set_Y_column()

    def _set_Y_column(self) -> None:
        len_col = self.df.shape[0]
        self.df["Y"] = [1
                   if binary_num in self.wyjscie
                   else 0
                   for binary_num in range(len_col)]
        self.df.Y = list(map(lambda x: 'X' if x in self.get_dont_care() else self.df.at[x, 'Y'], self.df.Y.index))
        self._set_count_1()

    def _set_count_1(self) -> None:
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

    @staticmethod
    def return_list_with_x(bin1: np.ndarray, bin2: np.ndarray) -> int:
        new = bin1.copy()
        idx = (bin1 == bin2).argmin()
        new[idx] = '-1'
        return new

    def return_df(self):
        return self.df

    @staticmethod
    def _filtr(min_term: str = '', dont_care: str = '') -> List[int]:
        # print(min_term, dont_care)

        def _str_to_list(tekst: str) -> List[int]:
            formated_tekst = re.findall(r'\d+', tekst)  # e.g. ['1', '3', '1', '1', ...]
            set_ = set(formated_tekst)
            list_ = list(set_)
            list_ = [int(x) for x in list_]
            return list_

        def _merge_list(l1: List[int] = [], l2: List[int] = []) -> List[int]:
            list_ = l1 + l2
            sorted_list = sorted(list_)
            # only values < 15
            sorted_list = [x for x in sorted_list if x <= 40]
            return sorted_list

        min_term_ = _str_to_list(min_term)
        dont_care_ = _str_to_list(dont_care)
        wejscie = _merge_list(min_term_, dont_care_)
        return min_term_, dont_care_, wejscie