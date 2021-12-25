import pylab
from typing import List, Dict, Optional, Union
import schemdraw
import schemdraw.elements as elm
from schemdraw import logic
from schemdraw.parsing import logicparse
import string
import numpy as np


# Pomocnicza klasa do generowanie dynamicznych nazw zmiennych
class VariableDynamic:
    listIn = []
    listInNot = []
    listGates = []

class InputNode:
    node: schemdraw.Drawing
    name: str
    label: str

    def __init__(self, name: str, label: str):
        self.name = name
        self.label = label
        self.node = logic.Dot(radius=0).label("$" + label + "$", fontsize=18)


class Gate:
    connect: Dict[schemdraw.Drawing, List[schemdraw.Drawing]]

    def __init__(self):
        self.dictGates = dict()


class Schema:
    listVariable: List[str]
    listResult: List[List[str]]
    countIn: int
    listNodes: List[str]
    countNode: int
    listAnd: List[List[str]]
    countAnd: int

    dictGates: Dict[str, schemdraw.Drawing]
    dictInput: Dict[str, schemdraw.Drawing]

    # dictgates: Dict[int, schemdraw.logic.logic.Element]

    def __init__(self, list_val, list_res):
        self.listVariable = list_val
        self.listResult = list_res
        self.countIn = len(list_val)
        self.listAnd = []
        self.listNodes = []
        self.dictGates = {}
        self.dictInput = {}

        for implicant in range(0, len(list_res)):
            if len(list_res[implicant]) == 1:
                self.listNodes.append(list_res[implicant][0])
            else:
                self.listAnd.append(list_res[implicant])
        self.countNode = len(self.listNodes)
        self.countAnd = len(self.listAnd)


    def __repr__(self):
        out = ''
        out += f"zmienne: " + (' '.join(self.listVariable))
        out += f"\nWęzły: " + (' '.join(self.listNodes))
        out += f"\nBramki AND: " + (' '.join([str(x) for x in self.listAnd]))
        return out

    # type    1 - node,  2 - not
    def CreateInput(self, input: str, lbl: str, type: Optional[int] = 1) -> schemdraw.Drawing:
        if type == 1:
            new_node = logic.Dot(radius=0).label("$" + lbl + "$", fontsize=18)
            self.dictInput[input] = new_node
        else:
            new_node = logic.Not().scale(0.7).down()
            self.dictInput[input] = new_node

        return new_node


    def CreateGate(self, name: str, nr_in: Optional[int] = 2, type: Optional[int] = 1) -> Union[logic.And, logic.Dot]:
        if type == 1:
            new_gate = logic.And(inputs=nr_in).right().anchor('in1').linewidth(2)
            self.dictGates[name] = new_gate
        else:  # utworzenie node
            new_gate = logic.Dot(radius=0).linewidth(2)
            self.dictGates[name] = new_gate
        return new_gate


    def DrawSchema(self):
        alphabet = list(string.ascii_uppercase)
        count = 1
        d = schemdraw.Drawing(unit=0.5, lw=1)

        VarDyn = VariableDynamic()
        # globals()[f"A{x}"] = logic.Dot(radius=0).label(" + "'$" + tmp + "$', fontsize=18)

        # rysowanie wejść
        for x in range(0, self.countIn):
            mark = alphabet[x]
            variable = self.listVariable[x]
            lenDownLine = len(self.listResult) * 1.8

            # zaczynamy od 1, 0
            d.here = (x + 1, 0)

            # ustawiamy etykiete dla input
            tmp_label = variable[0] if len(variable) == 1 else variable[0] + '_{' + (('').join(variable[1:])) + '}'
            # new_input = InputNode(variable, tmp_label)
            # tworzymy nowy input
            new_input = self.CreateInput(variable, tmp_label)
            # dodajemy input do schematu
            d += new_input

            # rysujemy kreska w dol
            d += logic.Line().down().length(0.5)

            # dodajemy węzęł
            d += logic.Dot(radius=0.05)
            d.push()        # Pamiętamy położenie węzła
            d += logic.Line().down().length(lenDownLine)
            d.pop()         # powracamy do węzła
            # linia w prawo
            d += logic.Line().right()

            # utworzenie bramki not, dodanie do listy wejść i dodanie do schematu
            new_not = self.CreateInput(f'-{variable}', '', type=2)
            d += new_not
            d += logic.Line().down().length(lenDownLine-0.85)


        # dodawanie bramek do schematu
        drawStep = np.arange(-2, -20, -2)
        start = self.countIn * 1.4
        step = -2
        nrOR = 0

        for implicant in self.listResult:
            count = len(implicant)

            if (count == 1):           # Jeżeli node
                d.here = (start, step)
                step -= 0.8
                new_gate = self.CreateGate(f'OR{nrOR}', type=2)
                d += new_gate
            else:
                d.here = (start, step)
                step -= 1.5
                if count > 3:
                    step -= 0.8
                new_gate = self.CreateGate(f'OR{nrOR}', nr_in=len(implicant))
                d += new_gate


            # łączenie wejść bramek
            nr_in = 1
            for term in implicant:
                if isinstance(new_gate, schemdraw.logic.logic.And):
                    point = new_gate.__dict__['absanchors'][f'in{nr_in}']
                    d += logic.Line().down().at(self.dictInput[term].end).toy(point).linewidth(0)
                    d += logic.Dot(radius=0.05)
                    d += logic.Line().to(point)
                    nr_in += 1

                if isinstance(new_gate, schemdraw.elements.lines.Dot):
                    d += logic.Line().down().at(self.dictInput[term].end).toy(new_gate.end).linewidth(0)
                    d += logic.Dot(radius=0.05)
                    d += logic.Line().to(new_gate.end)


            nrOR += 1

        X = list(self.dictGates.values())[0]
        Y = list(self.dictGates.values())[-1]

        gate_OR = logic.Or(inputs=len(self.listResult)).right().at((X.out[0]+2,(X.out[1]+Y.out[1])/2)).label('$Y_{out}$', 'right', fontsize=20).scale(1.5)
        d += gate_OR

        nr_in = 1

        # for G_Out in self.dictGates.values():
        #     print(G_Out.__dict__.values())
        #     print(self.dictGates[G_Out])
        #     if len(G_Out) > 1:
        #         point = gate_OR.__dict__['absanchors'][f'in{nr_in}']
        #         d += logic.Line().right().at(G_Out.out).tox(point).color('red')
        #         d += logic.Line().to(point)







        # d += logic.Line().right().at(Y.out).toy(O1.in2).color('red')
        # d += logic.Line().right().length(0.9)
        # d += logic.Line().to(O1.in2)
        #
        # d += logic.Line().right().at(Z.out).toy(O1.in3).color('red')
        # d += logic.Line().right().length(0.9)
        # d += logic.Line().to(O1.in3)
        #
        # d += logic.Line().right().at(W.out).tox(O1.in5).color('blue')
        # d += logic.Line().to(O1.in5)

        d.draw()


values = ['A', 'B', 'C', 'D', 'E']
tmp = [['A', '-B', 'C', '-D'],['E'], ['A', '-B', 'C', '-D', 'A'], ['-A'], ['-B', '-C'], ['-A', '-B']]

obj = Schema(values, tmp)
obj.DrawSchema()
