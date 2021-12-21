from typing import List, Union
import re
import pandas as pd
from Selekcja_Implikantow import SelekcjaImplikantow


class CreateTable:

    table: Union[SelekcjaImplikantow, int] = 0

    def __init__(self, min_term: str = '', dont_care: str = '') -> None:
        self.minterm = self._str_to_list(min_term)
        self.dont_care = self._str_to_list(dont_care)
        wejscie = self._merge_list(self.minterm, self.dont_care)
        if wejscie:
            self.table = SelekcjaImplikantow(wejscie)

    def get_df(self):
        df2 = pd.DataFrame({})
        df_mix = self.table.return_df().apply(lambda x: [x[-1], ''.join(x[:-2].astype(str)), x[-2]], axis=1).reset_index()
        df2[['Liczba jedynek', 'Liczba Binarna', 'Y']] = df_mix[0].tolist()#, df_mix['index']
        df2["Liczba Dziesiętna"] = df_mix['index']
        df2 = df2[df2.Y == 1]
        df2.drop(columns='Y', inplace=True)
        df2 = df2.sort_values(by='Liczba jedynek')
        df2 = df2.reset_index(drop=True)
        return df2

    def return_df(self):
        if self.table:
            return self.table.return_df()
        return 0

    def get_minterm(self):
        return self.minterm

    def get_dont_care(self):
        return self.dont_care

    def first_group(self):
        if self.table:
            return self.table.combine_each_group()
        return 0

    def print_first_group(self):
        if self.table:
            self.table.print_final_first_group()
        return 0

    def _merge_list(self, l1: List[int] = [], l2: List[int] = []) -> List[int]:
        list_ = l1 + l2
        sorted_list = sorted(list_)
        # only values < 15
        sorted_list = [x for x in sorted_list if x <= 40]
        return sorted_list

    @staticmethod
    def _str_to_list(tekst: str) -> List[int]:
        formated_tekst = re.findall(r'\d+', tekst)  # e.g. ['1', '3', '1', '1', ...]
        set_ = set(formated_tekst)
        list_ = list(set_)
        list_ = [int(x) for x in list_]
        return list_
