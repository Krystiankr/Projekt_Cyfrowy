from typing import List, Dict, Optional, Union, Any
import pandas as pd
import re
from Tablica_pokryc import DostepneMetody

class InputData:
    InputObject: DostepneMetody
    listVariables: str

    # firstGroup: pd.DataFrame
    # listImplicant: List[List[str]]
    # primeImplicantChart: pd.DataFrame

    def __init__(self, list_variable: str, minterm: str ='', dontcare: str =''):
        self.InputObject = DostepneMetody(list_variable, minterm, dontcare)
        self.listVariables = list_variable

        # self.truthTable = self.InputObject.get_tablica_prawdy()
        # self.firstGroup = self.InputObject.get_pierwsza_grupa()
        # self.listVariable = self.StrToList(listvariable)
        # self.listImplicant = self.SetListImplicant(self.InputObject.get_lista_implikantow())
        # self.primeImplicantChart = self.InputObject.get_tab_pokryc()

    def StrToList(self, text: str) -> List[str]:
        # z uprzejmości Pana Krystiana
        list_ = text.split(" ")
        # print(text)
        # formated_tekst = re.findall(r'\d+', text)  # e.g. ['1', '3', '1', '1', ...]
        # set_ = set(formated_tekst)
        # list_ = list(set_)
        # list_ = [int(x) for x in list_]
        # print(list_)
        return list_

    def getVariables(self) -> List[str]:
        return self.StrToList(self.listVariables)

    def getTruthTable(self) -> pd.DataFrame:
        return self.InputObject.get_tablica_prawdy()

    def getImplicants(self) -> List[List[str]]:
        variables = self.getVariables()
        implicants = self.InputObject.get_lista_implikantow()

        list_impl = [[char for char in implicants[i]] for i in range(0, len(implicants))]

        for implicant in list_impl:
            for term in range(0, len(implicant)):
                if implicant[term] == '1':
                    implicant[term] = variables[term]
                elif implicant[term] == '0':
                    implicant[term] = '-' + variables[term]
                else:
                    implicant[term] = ''

        tab_end = [[x for x in sub if x != ''] for sub in list_impl]
        return tab_end

    # def getGroupImplicants(self) -> pd.DataFrame:
    #     return self.InputObject.get_pierwsza_grupa()
    #
    #
    # def getTruthTableMark(self):
    #     return self.truthTable.to_markdown(index=False)





# variable = 'a b c d'
# sop = '1, 2, 3, 4, 5, 9, 12'
# dontcare = '0, 6'
#
# obj = InputData(variable, sop, dontcare)
# print(obj.getImplicants())
