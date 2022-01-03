from typing import List, Dict, Optional, Union, Any

import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm
from schemdraw import logic
import math
import numpy as np
import pandas as pd
import re

from class_file.Tablica_pokryc import DostepneMetody
from class_file.ResultEntrance import ResultEntrance
from class_file.InputData import InputData

import matplotlib
from matplotlib import rcParams
matplotlib.use('Qt5Agg')
rcParams['mathtext.default'] = 'it'
rcParams['mathtext.fontset'] = 'stix'


class Schema:
    MainSchema = schemdraw.Drawing
    truthTable = pd.DataFrame
    listVariable: List[str]
    listResult: List[List[str]]
    listImplicants: List[str]
    dictGates: Dict[str, schemdraw.Drawing]
    dictInput: Dict[str, schemdraw.Drawing]

    def __init__(self, list_variable: str, list_implicant: List[str], df: pd.DataFrame = None, line_width: int = 1):
        self.MainSchema = schemdraw.Drawing(unit=0.5, lw=line_width)
        self.truthTable = df
        self.listVariable = self.StrToList(list_variable)
        self.listResult = self.SetListImplicant(list_implicant)
        self.listImplicants = list_implicant
        self.dictGates = {}
        self.dictInput = {}

    def GetCountIn(self) -> int:
        return len(self.listVariable)

    @staticmethod
    def StrToList(source: Any) -> Union[List, str]:
        if isinstance(source, list):
            return source
        else:
            formated_tekst = re.findall('\w+', source)  # e.g. ['1', '3', '1', '1', ...]
            return formated_tekst

    def SetListImplicant(self, listImp: Any) ->List[List[str]]:
        ''' Konwersja prowadzonych implikantów ['--10', '1--0'...]
                    na odpowiadające im wejścia: [['c', '-d'], ['a', '-d'], ... ]
        '''
        if len(listImp) == 0:
            print("Brak implikantów...")
            return []
        if not(len(self.listVariable) == len(listImp[0])):
            print("Zmienne nie odpowiadają podanym implikantom")
            return []

        list_impl = [[char for char in listImp[i]] for i in range(0, len(listImp))]

        for implicant in list_impl:
            for term in range(0, len(implicant)):
                if implicant[term] == '1':
                    implicant[term] = self.listVariable[term]
                elif implicant[term] == '0':
                    implicant[term] = '-' + self.listVariable[term]
                else:
                    implicant[term] = ''

        tab_end = [[x for x in sub if x != ''] for sub in list_impl]
        return tab_end

    def CheckVariableAndImplicants(self) -> bool:
        ''' Sprawdzenie podanych danych
                    Porónywanie uzyskanych implikanótw ze zmiennymi
        '''
        all_term = [item.replace("-", "") for sublist in self.listResult for item in sublist]
        check_if_exist = all(item in self.listVariable for item in all_term)

        if check_if_exist and not(len(self.listResult)) == 0:
            return True
        else:
            if len(self.listResult) == 0:
                print("Nie wygenerowano żadnych implikantów.")
                return False
            else:
                print("Nieokreślony błąd.")
                return False

    def CreateInput(self, input: str, lbl: str, type: Optional[int] = 1) -> schemdraw.Drawing:
        ''' Tworzenie wejść i ich negacji
             Args:
                 input: nazwa obiektu
                 lbl: ustawienie etykiety
                 type:
                        1: utworzenie węzła
                        0: utworzenie negacji
        '''
        if type == 0:
            new_node = logic.Not().scale(0.7).down()
            self.dictInput[input] = new_node
        elif type == 1:
            new_node = logic.Dot(radius=0).label("$" + lbl + "$", fontsize=20)
            self.dictInput[input] = new_node
        else:
            print("Niezidentyfikowany obiekt...")
            new_node = None
        return new_node

    def CreateGateAnd(self, name: str, nr_in: Optional[int] = 2) -> Union[logic.And, logic.Dot]:
        ''' Utworzenie bramki AND
             Args:
                 name: nazwa obiektu
                 nr_in: liczba wejść bramki AND
        '''

        new_gate = logic.And(inputs=nr_in).right().anchor('in1')
        self.dictGates[name] = new_gate
        return new_gate

    def CreateNode(self, name: str) -> logic.Dot:
        ''' Utworzenie węzła
             Args:
                 name: nazwa obiektu
        '''
        new_node = logic.Dot(radius=0)
        self.dictGates[name] = new_node
        return new_node

    def GetLengthDownLine(self) -> float:
        ''' Ustawienie długości dolnej linii wychodzącej z Input '''

        length = 2.5
        for impl in self.listResult:
            if len(impl) > 1:
                length += len(impl) * 0.45
            else:
                length += 0.6 + 0.5
        return length

    def DrawInputs(self) -> None:
        ''' Rysowanie wszystkich wejść i ich negacji '''
        # rysowanie wejść
        for x in range(0, self.GetCountIn()):
            variable = self.listVariable[x]
            lenDownLine = self.GetLengthDownLine()
            # zaczynamy od 1, 0
            self.MainSchema.here = (x + 1, 0)
            # ustawiamy etykiete dla input
            tmp_label = variable[0] if len(variable) == 1 else variable[0] + '_{' + (('').join(variable[1:])) + '}'
            # new_input = InputNode(variable, tmp_label)
            # tworzymy nowy input
            new_input = self.CreateInput(variable, tmp_label, type=1)
            # dodajemy input do schematu
            self.MainSchema.add(new_input)

            # rysujemy kreska w dol
            self.MainSchema.add(logic.Line().down().length(0.5))

            # dodajemy węzęł
            self.MainSchema.add(logic.Dot(radius=0.05))
            self.MainSchema.push()  # Pamiętamy położenie węzła
            self.MainSchema.add(logic.Line().down().length(lenDownLine))
            self.MainSchema.pop()  # powracamy do węzła
            # linia w prawo
            self.MainSchema.add(logic.Line().right())

            # utworzenie bramki not, dodanie do listy wejść i dodanie do schematu
            new_not = self.CreateInput(f'-{variable}', '', type=0)
            self.MainSchema.add(new_not)
            self.MainSchema.add(logic.Line().down().length(lenDownLine - 0.85))

    def DrawGatesAndInput(self) -> None:
        ''' Rysowanie bramek(węzłów) i łączenie z ich wejściami wejść (zmiennych) '''
        # start - odległość pozioma bramek od linii wejść
        start = self.GetCountIn() * 1.4
        # step - odległość pomiędzy bramkami AND
        step = -2
        nrAND = 0

        for implicant in self.listResult:
            count = len(implicant)
            if (count == 1):  # Jeżeli node
                # (+1.85) dodanie node na wysokości wyjść bramek AND
                self.MainSchema.here = (start + 1.85, step)
                step -= 0.8
                new_gate = self.CreateNode(f'AND{nrAND}')
                self.MainSchema.add(new_gate)
            else:
                self.MainSchema.here = (start, step)
                step -= 1.5
                if count > 3:
                    step -= 0.8
                new_gate = self.CreateGateAnd(f'AND{nrAND}', nr_in=len(implicant))
                self.MainSchema.add(new_gate)

            # łączenie  wejść   bramek
            nr_in = 1
            for term in implicant:
                if isinstance(new_gate, schemdraw.logic.logic.And):
                    point = new_gate.absanchors[f'in{nr_in}']
                    self.MainSchema.add(logic.Line().down().at(self.dictInput[term].end).toy(point).linewidth(0))
                    self.MainSchema.add(logic.Dot(radius=0.05))
                    self.MainSchema.add(logic.Line().to(point))
                    nr_in += 1

                if isinstance(new_gate, schemdraw.elements.lines.Dot):
                    self.MainSchema.add(logic.Line().down().at(self.dictInput[term].end).toy(new_gate.end).linewidth(0))
                    self.MainSchema.add(logic.Dot(radius=0.05))
                    self.MainSchema.add(logic.Line().to(new_gate.end))
            nrAND += 1

    def DrawGateOr(self) -> None:
        ''' Rysowanie bramki OR i połączenie jej z bramkami AND '''
        top = list(self.dictGates.values())[0]  # pierwsza bramka
        bottom = list(self.dictGates.values())[-1]  # ostatnia bramka

        top_point = top.end if isinstance(top, schemdraw.elements.lines.Dot) else top.out
        bottom_point = bottom.end if isinstance(bottom, schemdraw.elements.lines.Dot) else bottom.out

        gate_OR = logic.Or(inputs=len(self.listResult)).right().at(
            (top_point[0] * 1.3, (top_point[1] + bottom_point[1]) / 2)).label(
            '$Y$', 'right', fontsize=20).scale(1.5)
        self.MainSchema.add(gate_OR)
        self.MainSchema.pop()
        self.MainSchema.push()
        # łączenie input z wyjściami OR
        self.ConnectInputswithOr(gate_OR)
        self.MainSchema.pop()

    def ConnectInputswithOr(self, gate: schemdraw.Drawing) -> None:
        ''' Łączęnie wejść bramki OR z wyjściami bramek AND '''
        # utworzenie listy ze współrzędnymi (obiekt Point) wejść bramki OR (ze słownika gate_OR.absanchors)
        self.MainSchema.push()      # zapamiętanie pozycji wyjścia bramki OR
        coordInOr = [v for k, v in gate.absanchors.items() if k.startswith('in')]
        coordInOr.reverse()

        # utworzenie listy ze współrzędnymi wyjść wszystkich bramek i node
        coordOutGates = [v.out if isinstance(v, schemdraw.logic.logic.And) else v.end for k, v in
                         self.dictGates.items()]

        if not (len(coordInOr) == len(coordOutGates)):
            print("Niepoprawna liczba elementów tablic Point")
            return

        # FOR, przechodzi od pierwszego ostatniego elementu
        # czyli dla [1, 2, 3, 4, 5, 6] przechodzi przez [1, 6]->[2,5]->[3,4]

        limitFor = math.ceil(len(coordInOr) / 2)
        distance = coordInOr[0][0] - coordOutGates[0][0]  # dystans X wyjść bramek do wejścia OR
        decrease = 1

        for step in range(0, limitFor):
            # jeżeli środkowy element w liscie nieparzystej
            if not (len(coordInOr) % 2 == 0) and (step == limitFor - 1):
                self.MainSchema.add(logic.Line().right().at(coordOutGates[step]).length(distance * decrease))
                if coordOutGates[step][1] < coordInOr[step][1]:  # jeżeli wejście leży poniżej wyjścia OR, linia w góre
                    self.MainSchema.add(logic.Line().up().length(abs(coordInOr[step][1] - coordOutGates[step][1])))
                if coordOutGates[step][1] > coordInOr[step][1]:  # linia w dół
                    self.MainSchema.add(logic.Line().down().length(abs(coordInOr[step][1] - coordOutGates[step][1])))
                # łączymy linię z wejściem OR
                self.MainSchema.add(logic.Line().to(coordInOr[step]))
            else:
                self.MainSchema.add(logic.Line().right().at(coordOutGates[step]).length(distance * decrease))
                if coordOutGates[step][1] < coordInOr[step][1]:
                    self.MainSchema.add(logic.Line().up().length(abs(coordInOr[step][1] - coordOutGates[step][1])))
                if coordOutGates[step][1] > coordInOr[step][1]:
                    self.MainSchema.add(logic.Line().down().length(abs(coordInOr[step][1] - coordOutGates[step][1])))
                self.MainSchema.add(logic.Line().to(coordInOr[step]))

                self.MainSchema.add(logic.Line().right().at(coordOutGates[-step - 1]).length(distance * decrease))
                if coordOutGates[-step - 1][1] < coordInOr[-step - 1][1]:
                    self.MainSchema.add(
                        logic.Line().up().length(abs(coordInOr[-step - 1][1] - coordOutGates[-step - 1][1])))
                if coordOutGates[-step - 1][1] > coordInOr[-step - 1][1]:
                    self.MainSchema.add(
                        logic.Line().down().length(abs(coordInOr[-step - 1][1] - coordOutGates[-step - 1][1])))
                self.MainSchema.add(logic.Line().to(coordInOr[-step - 1]))
            # zmniejszamy długość linii od wyjść bramek
            decrease -= 0.35

        self.MainSchema.pop()       # powrót do wyjścia bramki OR

    def DrawKmap(self) -> None:
        ''' Rysowanie mapki Karnaugha. TYLKO DLA 4 ZMIENNYCH '''
        # Generowanie siatki Karnaugha dla 4 zmiennych
        if len(self.listVariable) <= 4:
            truthTab = self.truthTable.astype(str)
            num = truthTab.shape[1] - 1
            numBin = truthTab.iloc[:, 0:num].to_records(index=None)
            yValue = list(truthTab.iloc[:, -1])
            kmapData = list(map(lambda x, y: (''.join(x), y), numBin, yValue))

            implikants = self.listImplicants
            implikants = [term.replace('-', '.') for term in implikants]

            tabColor = ['red', 'blue', 'green', 'magenta', 'orange', 'darkorchid', 'slategray']
            # tabFill = ['#ff000033', '#0000ff33', '#00ff0033', '#ffea00', '#e0aaff', '#ffa6c1', 'c9e4ca']
            tablw = [2.5, 2.2, 2.0, 1.6, 1.2, 1.0, 0.8]
            group = dict(
                map(lambda implikant, color, lw: (implikant, {'color': color, 'lw': lw}), implikants, tabColor, tablw))

            namesK = ''
            for idx in self.listVariable:
                namesK += idx[0] if len(idx) == 1 else idx[1]

            self.MainSchema.push()
            self.MainSchema.move(2.5, 0)
            self.MainSchema.add(logic.Kmap(names=namesK, truthtable=kmapData, groups=group))
            self.MainSchema.pop()
        else:
            print("Siatka Karnaugha generuje się tylka dla 4 zmiennych")

    def DrawTruthTable(self) -> None:
        ''' Rysowanie tablicy prawdy '''
        self.MainSchema.push()
        if(self.GetCountIn() > 4):
            self.MainSchema.move(2, 5)
        else:
            self.MainSchema.move(8, 6)
        table = self.truthTable.to_markdown(index=False)
        form = (self.truthTable.shape[1] - 1) * "c" + "||" + "c"

        if self.GetCountIn() > 4:
            self.MainSchema.move(1, 2)
            self.MainSchema.add(logic.Table(table, colfmt=form, fontsize=10).scale(0.8))
        else:
            self.MainSchema.add(logic.Table(table, colfmt=form))
        self.MainSchema.pop()

    def DrawFormula(self) -> None:
        ''' Rysowanie funkcji wyjścia '''
        lbl = ResultEntrance(self.listResult).GenerateAsMathBar()
        if isinstance(list(self.dictGates.values())[-1], schemdraw.logic.logic.And):
            startFrom = list(self.dictGates.values())[-1].out
        else:
            startFrom = list(self.dictGates.values())[-1].end
        # self.MainSchema.here = (startFrom[0]+3, startFrom[1])
        self.MainSchema.move(-2, -1.5)
        self.MainSchema.add(logic.Dot(radius=0).label(lbl, fontsize=20, halign='left', valign='top', color='navy'))

    def DrawSOP(self) -> None:
        ''' Rysowanie kanonicznej postaci sumacyjnej funkcji '''
        self.MainSchema.push()      # zapamiętanie pozycji wyjścia bramki OR
        df = self.truthTable
        minterm = df.index[df.Y == 1].tolist()
        dontcare = df.index[df.Y == 'X'].tolist()

        lblMin = ', '.join([str(int) for int in minterm])
        lblDont = ', '.join([str(int) for int in dontcare])
        lblVar = ''
        for idx in self.listVariable:
            lblVar += idx[0] if len(idx) == 1 else idx[0] + '_{' + (('').join(idx[1:])) + '}'
            lblVar += ', '
        text = "$f\,(" + lblVar[:-2] + ") = \\sum\,m(" + lblMin + ")$"
        if len(dontcare) > 0:
            text += "$\,+\,d(" + lblDont + ")$"

        if self.GetCountIn() > 4:
            self.MainSchema.here = (2, 2.2)
        else:
            self.MainSchema.here = (2, 2.8)

        self.MainSchema.add(logic.Dot(radius=0).label(text,
                                                        fontsize=24,
                                                        halign='left',
                                                        valign='top'))
        self.MainSchema.pop()  # powrót do pozycji wyjścia bramki OR

    def SaveSchema(self, filename: str) -> None:
        ''' Zapisanie schematu w pliku o nazwie - filename, format: "schemat.png" '''
        if bool(self.MainSchema.elements):
            f = self.MainSchema.save(filename, transparent=False, dpi=300)
            plt.close(f)
            print(f"Zapisano schemat w pliku \"{filename}\"")
        else:
            print("Nie zapisano schematu. Brak elementów.")

    def DrawSchema(self):
        ''' Wyświetlenie schematu '''
        self.MainSchema.draw()

    def GenerateSchema(self,
                            sop: bool = True,
                            kmap: bool = True,
                            truth_table: bool = True,
                            save_schem: bool = True,
                            formula: bool = False,
                            draw: bool = False) -> None:
        ''' Generowanie schematu z wybranymi elementami

            Args:
                kmap: [True/False] - rysowanie siatki Karnaugha (Tylko dla czterech zmiennych)
                truth_table: [True/False] - rysowanie tablicy prawdy
                save_schem: [True/False] - zapis schematu w formacie png
                draw: [True/False] - wyświetlenie schematu na ekranie
        '''

        try:
            checkYourData = self.CheckVariableAndImplicants()
            if checkYourData:
                self.DrawInputs()
                self.DrawGatesAndInput()
                self.DrawGateOr()
                # Opcjonalne:
                if sop:
                    self.DrawSOP()
                if kmap:
                    self.DrawKmap()
                if truth_table:
                    self.DrawTruthTable()
                if formula:
                    self.DrawFormula()
                if draw:
                    self.DrawSchema()
                if save_schem:
                    self.SaveSchema("png/schema.png")
            else:
                print("Błędne dane. Sprawdź zmienne i implikanty!")
        except Exception:
            print(self.listResult)
            print("[Wyjątek] Nie wygenerowano schematu")


if __name__ == "__main__":
    variable = 'A, B, C, D'
    sop = '0,1,2,7,9,11,12,13,14'
    dontcare = ''

    data = InputData(variable, sop, dontcare)
    schema = Schema(variable, data.getImplicantsAsBinary(), data.getTruthTable())
    schema.GenerateSchema1()


# variable = 'A, B, C, D'
# sop = '0,1,2,7,9,11,12,13,14'
# dontcare = ''
#
# tmp2 = InputData(variable, sop, dontcare)
# tmp = DostepneMetody(variable, sop, dontcare)
# print(tmp.get_prime_implicants())
#
# schema = Schema(variable, tmp2.getImplicantsAsBinary(), tmp2.getTruthTable())
# schema.GenerateSchema()
#
# print(schema.listImplicants)

# d = schemdraw.Drawing()
# d.add(elm.Resistor())
# schemfig = d.draw()
# schemfig.ax.axvline(.5, color='purple', ls='--')
# schemfig.ax.axvline(2.5, color='orange', ls='-', lw=3)
# schemfig.show()

