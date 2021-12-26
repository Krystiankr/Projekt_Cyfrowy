import pandas as pd
import numpy as np
import re
from collections import defaultdict
from typing import List


class CreateTable:
    postac_sumacyjna: List[int]
    dont_care: List[int]
    wyjscie: List[int]
    df: pd.DataFrame = pd.DataFrame()

    def __init__(self, postac_sumacyjna: str = '', dont_care: str = ''):
        self.postac_sumacyjna, self.dont_care, self.wyjscie \
        = self._filtr(postac_sumacyjna, dont_care)
        self.create_df_with_binary_nums()

    def get_postac_sumacyjna(self) -> List[int]:
        return sorted(self.postac_sumacyjna)

    def _binary_length(self):
        max_element = max(self.wyjscie)
        binary_len = len(bin(max_element))-2  # bin(4) = '0b100'
        return binary_len

    def create_df_with_binary_nums(self) -> None:
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
        self._set_count_1()

    def _set_count_1(self) -> None:
        self.df["count(1)"] = self.df.apply(lambda x: sum(x[:-1])
                                            if x[-1] == 1
                                            else -1, axis=1)

    def get_df(self) -> pd.DataFrame:
        if self.df.empty:
            return pd.DataFrame()
        df2 = pd.DataFrame({})
        df_mix = self.df.apply(lambda x: [x[-1], ''.join(x[:-2].astype(str)), x[-2]], axis=1).reset_index()
        df2[['Liczba jedynek', 'Liczba Binarna', 'Y']] = df_mix[0].tolist()#, df_mix['index']
        df2["Liczba Dziesiętna"] = df_mix['index']
        df2 = df2[df2.Y == 1]
        df2.drop(columns='Y', inplace=True)
        df2 = df2.sort_values(by='Liczba jedynek')
        df2 = df2.reset_index(drop=True)
        return df2

    def first_group(self) -> pd.DataFrame:
        df_first_group = self.get_df()
        df_first_group["Checked"] = False
        return df_first_group

    def grouped_dict(self):
        group_dict = defaultdict(list)
        df2 = self.df[self.df["count(1)"] != -1]
        df2_sorted = df2.sort_values(by=['count(1)'])
        # print(f"Unique elements {group_len}")
        flag = 0
        for row in df2_sorted.values:
            if row[-1] == flag:
                # print(f"Group[{row[-1]}]")
                flag += 1
            group_dict[row[-1]].append(row[:-2])
        # print(group_dict)
        return group_dict

    def print_dict(self, dict_):
        for key, items in dict_.items():
            print(f"Group {key}")
            print(f"Items:")
            for item in items:
                print(item)

    @staticmethod
    def check_pair(bin1: np.ndarray, bin2: np.ndarray) -> bool:
        return False if np.abs(bin2 - bin1).sum() > 1 else True

    @staticmethod
    def return_list_with_x(bin1: np.ndarray, bin2: np.ndarray) -> int:
        new = bin1.copy()
        idx = (bin1 == bin2).argmin()
        new[idx] = '-1'
        return new

    def first_group_list(self):
        df = self.first_group()
        print(df["count(1)"].unique())

    def combine_each_group(self, dict_):
        licznik = 0
        result_dict = defaultdict(List[List[int]])
        group_dict = dict_
        for key, items in group_dict.items():
            if key + 1 in group_dict.keys():
                result_dict[(key, key+1)] = []
                # print(f"Group[{key}]")
            for item_g in items:
                #  print(f"Main item {item_g}")
                if key + 1 in group_dict.keys():
                    # result_dict[(key, key+1)] = []
                    for item in group_dict[key + 1]:
                        if self.check_pair(item_g, item):
                            # print(f"Found pair! {item_g} {item}")
                            # print(f"{self.return_list_with_x(item_g, item)}")
                            result_dict[(key, key+1)].append(self.return_list_with_x(item_g, item))
        return result_dict

    def return_df(self):
        return self.df

    @staticmethod
    def _filtr(min_term: str = '', dont_care: str = '') -> List[int]:
        print(min_term, dont_care)

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