import pandas as pd
import numpy as np
from collections import Counter, defaultdict
from Reprezentacja_sumacyjna import ReprezentacjaFormyKanonicznejSumacyjnej


class SelekcjaImplikantow:
    df: pd.DataFrame

    def __init__(self, postac_sumacyjna):
        rep = ReprezentacjaFormyKanonicznejSumacyjnej(postac_sumacyjna)
        self.df = rep.return_df()

    def return_df(self):
        return self.df


postac_sum = [0, 2, 3, 5, 6, 7 ,8 ,9 ,10, 11, 12, 13, 14, 15]
sel = SelekcjaImplikantow(postac_sum)
df = sel.return_df()


def check_row(row):
    if row[-1] == 1:  # Y == 1
        return len(row[:-1].nonzero()[0])  # count(1) in row


df_values = list(map(check_row, df.values))
print(Counter(df_values))