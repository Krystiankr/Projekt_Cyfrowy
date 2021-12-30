from typing import List
import pandas as pd
import re

from class_file.Tablica_pokryc import DostepneMetody

class InputData:
    InputObject: DostepneMetody
    listVariables: str
    listMinterms: str
    listDontCare: str

    def __init__(self, list_variable: str, minterm: str ='', dontcare: str =''):
        self.InputObject = DostepneMetody(list_variable, minterm, dontcare)
        self.listVariables = list_variable
        self.listMinterms = minterm
        self.listDontCare = dontcare

    def getVariablesAsList(self) -> List[str]:
        return StrToList(self.listVariables)

    def getVariablesAsString(self) -> str:
        return self.listVariables

    def getMintermsAsList(self) -> List[str]:
        return StrToList(self.listMinterms)

    def getDontCareAsList(self) -> List[str]:
        return StrToList(self.listDontCare)

    def getTruthTable(self) -> pd.DataFrame:
        return self.InputObject.get_tablica_prawdy()

    def getImplicantsAsBinary(self) -> List[str]:
        return self.InputObject.get_prime_implicants()

    def getImplicantsAsInput(self) -> List[List[str]]:
        # Generowanie implikantów w formie [['-b', '-c', 'd'], ['-a', '-b']]
        variables = self.getVariablesAsList()
        implicants = self.getImplicantsAsBinary()
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

    def getGroupImplicants(self):
        return self.InputObject.get_pierwsza_grupa()

    def getTestImplicant(self):
        return ['000-', '-010', '011-']


def StrToList(text: str) -> List[str]:
    tab = re.findall('\w+', text)  # e.g. ['1', '3', '1', '1', ...]
    return tab
