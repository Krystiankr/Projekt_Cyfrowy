import pandas as pd
import numpy as np
from typing import List


class ReprezentacjaFormyKanonicznejSumacyjnej:
    postac_sumacyjna: List[int]

    def __init__(self, postac_sumacyjna):
        self.postac_sumacyjna = postac_sumacyjna

    def binary_length(self):
        max_element = max(self.postac_sumacyjna)
        binary_len = len(bin(max_element))-2  # bin(4) = '0b100'
        return binary_len

    def df_binary_all_combinations(self):
        len_ = self.binary_length()
        bin_len = 4 if len_ <= 4 else len_
        df = pd.DataFrame(
            [[int(num)
              for num in f"{int(bin(x)[2:]):0{bin_len}d}"]  # 'repr bin' =  0000
             for x in range(0, 2 ** len_)],  # e.g. 3, from 000-111, e.g. 4, 0000-1111
            index=np.arange(0, 2 ** len_, 1),
            columns=[chr(x) for x in range(ord('A'), ord('A')+bin_len)]  # [A, B, C, ..., A + bin_len]
        )
        return df

    def set_Y_column(self):
        df = self.df_binary_all_combinations()
        len_col = df.shape[0]
        df["Y"] = [1
                   if binary_num in self.postac_sumacyjna
                   else 0
                   for binary_num in range(len_col)]
        return df

    def return_df(self):
        return self.set_Y_column()
