import pandas as pd
from typing import List, Tuple, Dict
from Reprezentacja_sumacyjna import CreateTable

def matched(num1: str, num2: str) -> bool:
    return sum(n1 != n2 for n1, n2 in zip(num1, num2)) == 1

assert matched('0000', '000x') == True
assert matched('0000', '0000') == False

def correct_pair(num1: str, num2: str) -> str:
    return ''.join(n1 if n1 == n2 else '-' for n1, n2 in zip(num1, num2))

assert correct_pair('0010', '0000') == '00-0'

def correct_tuple(tuple_elements: Tuple) -> Tuple:
    tup_element = tuple_elements
    # print(f"tupl_elem, {tup_element}")
    while any(isinstance(el, tuple) for el in tup_element):
        tup_element = sum(tup_element, ())
    tup_element = tuple(set(tup_element))
    return tup_element

assert correct_tuple(((1, 2), (3, 4))) == (1, 2, 3, 4)
assert correct_tuple((1, 2, 3, 4)) == (1, 2, 3, 4)

def elementy_laczone(df_input: pd.DataFrame) -> list:
    return pd.Series(df_input["Elemtny(łączone)"].values, index=df_input['Element']).to_dict()

def remove_element(dict_: dict, element):
    if element in dict_.keys():
        dict_.pop(element)

def compare_neighbours(df_input: pd.DataFrame, main: int, next_: int, dict_lacz: Dict[str, 'int']={}) \
        -> Tuple[pd.DataFrame, list]:
    # print(f"El_laczone = {el_lacz}")
    df_new = pd.DataFrame(columns=["Obiekt grupowany", "Elemtny(łączone)", "Element", "Użyty"])
    df_main = df_input.copy()
    # print each comparsion
    main_rows = df_main[df_main["Obiekt grupowany"] == main]
    next_rows = df_main[df_main["Obiekt grupowany"] == next_]
    # print(f"next->{next_rows}")

    for idx_main, row_main in main_rows.iterrows():
        for idx_, row_ in next_rows.iterrows():
            check1 = row_main['Element']
            check2 = row_['Element']
            if matched(check1, check2):
                # print(f"Matched! -{check1}- with {check2}")
                # print(f"nr -{row_main['Elemtny(łączone)']}- with {row_['Elemtny(łączone)']}")
                remove_element(dict_lacz, row_main["Element"])
                remove_element(dict_lacz, row_["Element"])
                if df_new.empty:
                    x = 0
                else:
                    x = df_new.index.max() + 1
                grupowy_tuple = correct_tuple(tuple([main]) + tuple([next_]))
                laczony_tuple = correct_tuple(tuple([row_main["Elemtny(łączone)"]]) + tuple([row_["Elemtny(łączone)"]]))
                df_new.loc[x] = [grupowy_tuple,
                                 laczony_tuple,
                                 correct_pair(check1, check2),
                                 False]
    return df_new, dict_lacz

def create_group(df_input: pd.DataFrame, dict_lacz: dict={}) -> pd.DataFrame:
    df_main = df_input.copy()
    df_out = pd.DataFrame()
    dict_lacz.update(elementy_laczone(df_input))
    unique_values = list(df_input['Obiekt grupowany'].unique())
    # print(f"Unique elements len = {len(unique_values)}")
    # print(f"Unique elements = {unique_values}")
    # print(f"Uprise group len = ->{len(unique_values) - 1}<-")
    for idx, el in enumerate(unique_values):
        if el == unique_values[-1]: continue
        df_tmp, dict_lacz = compare_neighbours(df_main, unique_values[idx], unique_values[idx+1], dict_lacz)
        df_out = pd.concat([df_out, df_tmp])
    df_out = df_out.drop_duplicates(subset='Element')
    return df_out.reset_index(drop=True), dict_lacz

def all_groups(df_input: pd.DataFrame):
    df_all: List[pd.DataFrame] = []
    df_out, dict_out = create_group(df_input, {})
    while not df_out.empty:
        df_out, dict_out = create_group(df_out, dict_out)
    # print(f"List out: {dict_out}")
    return dict_out

def przygotuj_tab_pokryc(postac_sumacyjna: List[int], implikanty_proste: dict):
    # print(f"Postac sumacyjna: {postac_sumacyjna}")
    # print("Słownik")
    # for key, item in implikanty_proste.items():
    #     print(f"key[{key}] = {item}")
    df_tab_pokryc = pd.DataFrame(
        columns=list(implikanty_proste.keys()),
        index=postac_sumacyjna,
        data=[['-'] * len(list(implikanty_proste.keys()))]
    )
    return df_tab_pokryc

def wypelnij_tab_pokryc(df_wstepna: pd.DataFrame, implikanty_proste: dict):
    for column, elements in implikanty_proste.items():
        # print(f"column = {column}")
        for element in elements:
            # print(f"element = {element}")
            if element in df_wstepna.index:
                df_wstepna.at[element, column] = '+'  # index, col
    return df_wstepna

def get_tab_pokryc(tab: CreateTable) -> pd.DataFrame:
    df = tab.get_df()
    df_grupowane = pd.DataFrame()
    df_grupowane[["Obiekt grupowany", "Elemtny(łączone)", "Element"]] = df[['Liczba jedynek', 'Liczba Dziesiętna', 'Liczba Binarna']]

    dict_out = all_groups(df_grupowane)
    print(f"Tab -> postac sum {tab.get_postac_sumacyjna()}")
    out_ = przygotuj_tab_pokryc(tab.get_postac_sumacyjna(), dict_out)
    return wypelnij_tab_pokryc(out_, dict_out)