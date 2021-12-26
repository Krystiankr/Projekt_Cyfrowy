from typing import List, Dict, Optional, Union, Any
import schemdraw
import schemdraw.elements as elm
from schemdraw import logic
import string
import numpy as np


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

    def __init__(self, list_variable, list_implicant, line_width: int = 1):
        self.MainSchema = schemdraw.Drawing(unit=0.5, lw=line_width)
        self.listVariable = list_variable
        self.listResult = list_implicant
        self.countIn = len(list_variable)
        self.listAnd = []
        self.listNodes = []
        self.dictGates = {}
        self.dictInput = {}

        for implicant in range(0, len(list_implicant)):
            if len(list_implicant[implicant]) == 1:
                self.listNodes.append(list_implicant[implicant][0])
            else:
                self.listAnd.append(list_implicant[implicant])
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
            new_gate = logic.Dot(radius=0.05)
            self.dictGates[name] = new_gate
        return new_gate


    def DrawInputs(self, source: schemdraw.Drawing):
        # rysowanie wejść
        for x in range(0, self.countIn):
            variable = self.listVariable[x]
            lenDownLine = len(self.listResult) * 1.8

            # zaczynamy od 1, 0
            source.here = (x + 1, 0)

            # ustawiamy etykiete dla input
            tmp_label = variable[0] if len(variable) == 1 else variable[0] + '_{' + (('').join(variable[1:])) + '}'
            # new_input = InputNode(variable, tmp_label)
            # tworzymy nowy input
            new_input = self.CreateInput(variable, tmp_label)
            # dodajemy input do schematu
            source.add(new_input)

            # rysujemy kreska w dol
            source.add(logic.Line().down().length(0.5))

            # dodajemy węzęł
            # d += logic.Dot(radius=0.05)
            source.add(logic.Dot(radius=0.05))
            source.push()  # Pamiętamy położenie węzła
            source.add(logic.Line().down().length(lenDownLine))
            source.pop()  # powracamy do węzła
            # linia w prawo
            source.add(logic.Line().right())

            # utworzenie bramki not, dodanie do listy wejść i dodanie do schematu
            new_not = self.CreateInput(f'-{variable}', '', type=2)
            source.add(new_not)
            source.add(logic.Line().down().length(lenDownLine - 0.85))
        return source


    def DrawGatesAndInput(self, source: schemdraw.Drawing):
        drawStep = np.arange(-2, -20, -2)
        start = self.countIn * 1.4
        step = -2
        nrAND = 0

        for implicant in self.listResult:
            count = len(implicant)

            if (count == 1):           # Jeżeli node
                source.here = (start + 1.85, step)
                step -= 0.8
                new_gate = self.CreateGate(f'AND{nrAND}', type=2)
                source.add(new_gate)
            else:
                source.here = (start, step)
                step -= 1.5
                if count > 3:
                    step -= 0.8
                new_gate = self.CreateGate(f'AND{nrAND}', nr_in=len(implicant))
                source.add(new_gate)

           # łączenie  wejść   bramek
            nr_in = 1
            for term in implicant:
                if isinstance(new_gate, schemdraw.logic.logic.And):
                    point = new_gate.absanchors[f'in{nr_in}']
                    source.add(logic.Line().down().at(self.dictInput[term].end).toy(point).linewidth(0))
                    source.add(logic.Dot(radius=0.05))
                    source.add(logic.Line().to(point))
                    nr_in += 1

                if isinstance(new_gate, schemdraw.elements.lines.Dot):
                    source.add(logic.Line().down().at(self.dictInput[term].end).toy(new_gate.end).linewidth(0))
                    source.add(logic.Dot(radius=0.05))
                    source.add(logic.Line().to(new_gate.end)).color('red')

            nrAND += 1

        # rysowanie bramki OR



        return source

    def DrawGateOr(self):

        top = list(self.dictGates.values())[0]  # pierwsza bramka
        bottom = list(self.dictGates.values())[-1]  # ostatnia bramka

        top_point = top.end if isinstance(top, schemdraw.elements.lines.Dot) else top.out
        bottom_point = bottom.end if isinstance(bottom, schemdraw.elements.lines.Dot) else bottom.out

        gate_OR = logic.Or(inputs=len(self.listResult)).right().at(
            (top_point[0] * 1.3, (top_point[1] + bottom_point[1]) / 2)).label(
            '$Y_{out}$', 'right', fontsize=20).scale(1.5)
        source.add(gate_OR)



    def DrawSchema(self):
        alphabet = list(string.ascii_uppercase)
        count = 1
        d = schemdraw.Drawing(unit=0.5, lw=1)

        d = self.DrawInputs(d)
        d = self.DrawGatesAndInput(d)



        # gate_OR = logic.Or(inputs=len(self.listResult)).right().at((X.out[0]+2,(X.out[1]+Y.out[1])/2)).label('$Y_{out}$', 'right', fontsize=20).scale(1.5)
        # d += gate_OR
        #
        # nr_in = 1
        #
        # for G_Out in self.dictGates.values():
        #     print(G_Out.__dict__.values())
        #     print(self.dictGates[G_Out])
        #     if len(G_Out) > 1:
        #         point = gate_OR.__dict__['absanchors'][f'in{nr_in}']
        #         d += logic.Line().right().at(G_Out.out).tox(point).color('red')
        #         d += logic.Line().to(point)
        #
        #
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


# zrobić warunke aby sprawdzał zmienne z implikantami


values2 = ['x1', 'x2', 'x3', 'x4']
gates2 = [['-x2', 'x3'], ['x1','x4'], ['-x2'], ['-x4'], ['x1', 'x2', 'x3']]

values1 = ['A', 'B', 'C', 'D', 'E']
gates1 = [['B'], ['-B', '-D'], ['B','D'], ['C', '-E'], ['A']]

values3 = ['a', 'b', 'c', 'd', 'e']
gates3 = [['-a', '-b'], ['a','c'], ['-d'], ['-e']]


obj = Schema(values2, gates2)
obj.DrawSchema()
