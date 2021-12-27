from typing import List, Dict, Optional, Union, Any
import schemdraw
import schemdraw.elements as elm
from schemdraw import logic
import math
import string
import numpy as np
import pandas as pd
import re
from Tablica_pokryc import DostepneMetody

class Schema:
    MainSchema = schemdraw.Drawing
    listVariable: List[str]
    listResult: List[List[str]]
    countIn: int
    listNodes: List[str]
    countNode: int
    listAnd: List[List[str]]
    countAnd: int

    dictGates: Dict[str, schemdraw.Drawing]
    dictInput: Dict[str, schemdraw.Drawing]
    gateOR: schemdraw.Drawing



    def __init__(self, list_variable, list_implicant, line_width: int = 1):
        self.MainSchema = schemdraw.Drawing(unit=0.5, lw=line_width)
        #self.listVariable = list_variable
        self.listVariable = self.StrToList(list_variable)
        #self.listResult = list_implicant
        self.listResult = self.SetListImplicant(list_implicant)
        self.countIn = len(list_variable)
        self.listAnd = []
        self.listNodes = []
        self.dictGates = {}
        self.dictInput = {}
        self.gateOR = schemdraw.Drawing


        # for implicant in range(0, len(list_implicant)):
        #     if len(list_implicant[implicant]) == 1:
        #         self.listNodes.append(list_implicant[implicant][0])
        #     else:
        #         self.listAnd.append(list_implicant[implicant])
        # self.countNode = len(self.listNodes)
        # self.countAnd = len(self.listAnd)


    def __repr__(self):
        out = ''
        out += f"zmienne: " + (' '.join(self.listVariable))
        out += f"\nWęzły: " + (' '.join(self.listNodes))
        out += f"\nBramki AND: " + (' '.join([str(x) for x in self.listAnd]))
        return out

    def StrToList(self, source: Any):
        if isinstance(source, list):
            return source
        else:
            # z uprzejmości Pana Krystiana
            # Wyciągam wszystkie liczby z wejścia
            formated_tekst = re.findall(r'\d+', source)  # e.g. ['1', '3', '1', '1', ...]
            set_ = set(formated_tekst)
            list_ = list(set_)
            list_ = [int(x) for x in list_]
            return list_

    def SetListImplicant(self, listImp: Any):

        # sprawdzenie czy podano w formie: ['0-0-0', '000-0', '-00--', '0-00-']
                                #         czy [['-x2', 'x3'], ['x1','x4'], ['-x2']]

        all_term = [item.replace("-", "") for sublist in listImp for item in sublist]
        check_if_exist = all(item in self.listVariable for item in all_term)

        if check_if_exist:
            return listImp

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
        print(type(tab_end))
        return tab_end

    def CheckVariableAndImplicants(self) -> bool:

        all_term = [item.replace("-", "") for sublist in self.listResult for item in sublist]
        check_if_exist = all(item in self.listVariable for item in all_term)

        return True if check_if_exist else False


    # type    1 - node,  2 - not
    def CreateInput(self, input: str, lbl: str, type: Optional[int] = 1) -> schemdraw.Drawing:
        if type == 1:
            new_node = logic.Dot(radius=0).label("$" + lbl + "$", fontsize=16)
            self.dictInput[input] = new_node
        else:
            new_node = logic.Not().scale(0.7).down()
            self.dictInput[input] = new_node

        return new_node


    def CreateGate(self, name: str, nr_in: Optional[int] = 2, type: Optional[int] = 1) -> Union[logic.And, logic.Dot]:
        if type == 1:
            new_gate = logic.And(inputs=nr_in).right().anchor('in1')
            self.dictGates[name] = new_gate
        else:  # utworzenie node
            new_gate = logic.Dot(radius=0.05).color('red')
            self.dictGates[name] = new_gate
        return new_gate

    def CreateNode(self, name: str) -> logic.Dot:
        new_node = logic.Dot(radius=0.05).color('red')
        self.dictGates[name] = new_node

        return new_node


    def DrawInputs(self) -> None:
        # rysowanie wejść
        for x in range(0, self.countIn):
            variable = self.listVariable[x]
            lenDownLine = len(self.listResult) * 2

            # zaczynamy od 1, 0
            self.MainSchema.here = (x + 1, 0)

            # ustawiamy etykiete dla input
            tmp_label = variable[0] if len(variable) == 1 else variable[0] + '_{' + (('').join(variable[1:])) + '}'
            # new_input = InputNode(variable, tmp_label)
            # tworzymy nowy input
            new_input = self.CreateInput(variable, tmp_label)
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
            new_not = self.CreateInput(f'-{variable}', '', type=2)
            self.MainSchema.add(new_not)
            self.MainSchema.add(logic.Line().down().length(lenDownLine - 0.85))


    def DrawGatesAndInput(self):
        drawStep = np.arange(-2, -20, -2)
        start = self.countIn * 1.4
        step = -2
        nrAND = 0

        for implicant in self.listResult:
            count = len(implicant)

            if (count == 1):           # Jeżeli node
                self.MainSchema.here = (start + 1.85, step)
                step -= 0.8
                new_gate = self.CreateNode(f'AND{nrAND}')
                self.MainSchema.add(new_gate)
            else:
                self.MainSchema.here = (start, step)
                step -= 1.5
                if count > 3:
                    step -= 0.8
                new_gate = self.CreateGate(f'AND{nrAND}', nr_in=len(implicant))
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


    def DrawGateOr(self):

        top = list(self.dictGates.values())[0]  # pierwsza bramka
        bottom = list(self.dictGates.values())[-1]  # ostatnia bramka

        top_point = top.end if isinstance(top, schemdraw.elements.lines.Dot) else top.out
        bottom_point = bottom.end if isinstance(bottom, schemdraw.elements.lines.Dot) else bottom.out

        gate_OR = logic.Or(inputs=len(self.listResult)).right().at(
            (top_point[0] * 1.3, (top_point[1] + bottom_point[1]) / 2)).label(
            '$Y_{out}$', 'right', fontsize=20).scale(1.5)
        self.MainSchema.add(gate_OR)

        # przypisanie adresu bramki do atrybutu klasy
        self.gateOR = gate_OR

        # łączenie input z wyjściami OR
        self.ConnectInputswithOr(gate_OR)

    def ConnectInputswithOr(self, gate: schemdraw.Drawing):

        # utworzenie listy ze współrzędnymi (obiekt Point) wejść bramki OR (ze słownika gate_OR.absanchors)

        coordInOr = [v for k, v in gate.absanchors.items() if k.startswith('in')]
        print(coordInOr)
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
        distance = coordInOr[0][0] - coordOutGates[0][0]            # dystans X wyjść bramek do wejścia OR
        decrease = 1

        for step in range(0, limitFor):
            # jeżeli środkowy element w liscie nieparzystej
            if not (len(coordInOr) % 2 == 0) and (step == limitFor - 1):
                self.MainSchema.add(logic.Line().right().at(coordOutGates[step]).length(distance * decrease))
                if coordOutGates[step][1] < coordInOr[step][1]:     # jeżeli wejście leży poniżej wyjścia OR, linia w góre
                    self.MainSchema.add(logic.Line().up().length(abs(coordInOr[step][1] - coordOutGates[step][1])))
                if coordOutGates[step][1] > coordInOr[step][1]:     # linia w dół
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


    def GetTruthTableMark(self, source: pd.DataFrame):
        return source.to_markdown(index=False)

    def DrawTruthTable(self, df: pd.DataFrame):
        table = self.GetTruthTableMark(df)
        print(table)





    # def DrawKmap(self):
    #     if self.listVariable > 4:
    #         print("Obsługa tylko do 4 zmiennych")
    #         return



    def DrawSchema(self):

        checkYourData = self.CheckVariableAndImplicants()

        if checkYourData:
            self.DrawInputs()
            self.DrawGatesAndInput()
            self.DrawGateOr()

            self.MainSchema.move(7, 0)

            self.MainSchema.add(logic.Kmap(names='ABCD',
           truthtable=[('1100', '1'),
                       ('1101', '1'),
                       ('1111', '1'),
                       ('1110', '1'),
                       ('0101', '1'),
                       ('0111', 'X'),
                       ('1101', '1'),
                       ('1111', '1'),
                       ('0000', '1'),
                       ('1000', '1')],
           groups={'11..': {'color': 'red', 'fill': '#ff000033'},
                   '.1.1': {'color': 'blue', 'fill': '#0000ff33'},
                   '.000': {'color': 'green', 'fill': '#00ff0033'}}))

            # table = '''
            #  A | B | C
            # ---|---|---
            #  0 | 1 | 1
            #  0 | X | 0
            #  1 | 0 | 0
            #  1 | 1 | 1
            # '''
            # self.MainSchema.add(logic.Table(table, colfmt='cc||c'))






            #
            #
            #
            # find = self.dictGates['AND2']
            # print(find)
            #
            # print(self.MainSchema.elements.index(find))
            # print(self.MainSchema.elements[43])
            #
            # self.MainSchema.elements.pop(45)
            # self.MainSchema.elements.pop(46)
            #
            # self.MainSchema.add(logic.Line().down().at(self.dictInput['-x2'].end).toy(self.gateOR.in3).linewidth(1))
            # self.MainSchema.add(logic.Dot(radius=0.05))
            # self.MainSchema.add(logic.Line().to(self.gateOR.in3))
            #
            df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                               columns=['a', 'b', 'c'])
            #
            #
            # mark = df2.to_markdown(index=False)



            table = '''
            |  h |  a   |   b |   c |
            |----|----:|-----|-----|
            |  0 |   1 |   2 |   3 |
            |  1 |   4 |   5 |   6 |
            |  2 |   7 |   8 |   9 |
            '''

            # self.MainSchema.add(logic.Table(mark, colfmt='cc||c'))






            self.MainSchema.draw()
            # self.MainSchema.save("schema.png", False)



        else:
            print("Błędne dane. Sprawdź zmienne i implikanty")
            return




values2 = ['x1', 'x2', 'x3', 'x4', 'x5']
gates2 = [['-x2', 'x3'], ['x1','x4'], ['-x2'], ['-x4'], ['x1', 'x2', 'x3']]

values1 = ['A', 'B', 'C', 'D', 'E']
gates1 = [['B'], ['-B', '-D'], ['B','D'], ['C', '-E'], ['A']]

values3 = ['a', 'b', 'c', 'd', 'e']
gates3 = [['-a']]


impl = ['0-0-0', '101-1', '-00--', '1-11-']
obj = Schema(values3, impl)
obj.DrawSchema()
print(obj.listResult)



