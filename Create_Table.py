from typing import List, Union
import re
from Selekcja_Implikantow import SelekcjaImplikantow


class CreateTable:

    table: Union[SelekcjaImplikantow, int] = 0

    def __init__(self, min_term: str = '', dont_care: str = '') -> None:
        wejscie = self._merge_list(str(min_term), str(dont_care))
        if wejscie:
            self.table = SelekcjaImplikantow(wejscie)

    def return_df(self):
        if self.table:
            return self.table.return_df()
        return 0

    def first_group(self):
        if self.table:
            return self.table.combine_each_group()
        return 0

    def print_first_group(self):
        if self.table:
            self.table.print_final_first_group()
        return 0

    def _merge_list(self, l1: str = '', l2: str = '') -> List[int]:
        list_ = self._str_to_list(l1) + self._str_to_list(l2)
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
