import pandas as pd
from typing import List
import numpy as np
from collections import defaultdict
from Reprezentacja_sumacyjna import ReprezentacjaFormyKanonicznejSumacyjnej


class SelekcjaImplikantow:
    df: pd.DataFrame
    len_binary: int

    def __init__(self, min_term: List[int]):
        rep = ReprezentacjaFormyKanonicznejSumacyjnej(min_term)
        self.df = rep.return_df()
        self.len_binary = self.df.shape[1] - 1
        self.first_group_col()

    def return_df(self):
        return self.df

    def first_group_col(self):
        self.df["count(1)"] = self.df.apply(lambda x: sum(x[:-1])
                                            if x[-1] == 1
                                            else -1, axis=1)

    def not_finished_first_group(self):
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

    @staticmethod
    def check_pair(bin1: np.ndarray, bin2: np.ndarray) -> bool:
        return False if np.abs(bin2 - bin1).sum() > 1 else True

    @staticmethod
    def return_list_with_x(bin1: np.ndarray, bin2: np.ndarray) -> int:
        new = bin1.copy()
        idx = (bin1 == bin2).argmin()
        new[idx] = '-1'
        return new

    def combine_each_group(self):
        result_dict = defaultdict(List[List[int]])
        group_dict = self.not_finished_first_group()
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

    #  Koniec mojego etapu, wypisanie pasujących par jako 'x' wybralem -1
    def print_final_first_group(self):
        final_dict = self.combine_each_group()
        # print(final_dict)
        for key, items in final_dict.items():
            print(f"Group {key}")
            print(f"Items:")
            for item in items:
                print(item)
