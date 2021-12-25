import pylab
from typing import List
import schemdraw
import schemdraw.elements as elm
from schemdraw import logic
from schemdraw.parsing import logicparse
import string


class ResultEntrance:
    formula: List[List[str]] = []

    def __init__(self, formula):
        self.formula = formula

    def GenerateAsText(self):
        if len(self.formula) == 0:
            return
        out = 'Y = '
        for dis in self.formula:
            for con in dis:
                if con[0] == '-':
                    str1 = ''
                    out += '(' + (str1.join(con[1:])) + ")'"
                else:
                    out += con
                out += '\u00b7'
            out = out[:-1] + ' + '
        return out[:-3]

    # def GenerateAsMath(self):
    #     if len(self.formula) == 0:
    #         return
    #     out = '$Y = '
    #     for dis in self.formula:
    #         for con in dis:
    #             if con[0] == '-':
    #                 out += '\\overline{' + con[1] + '}\,'
    #                 if len(con) > 2:
    #                     str1 = ''
    #                     out += '_{' + (str1.join(con[2:])) + '}\,'
    #             else:
    #                 out += con[0] + '\,'
    #                 if len(con) > 1:
    #                     str1 = ''
    #                     out += '_{' + (str1.join(con[1:])) + '}\,'
    #         out += ' + '
    #     out = out[:-3] + '$'
    #     return out

    def GenerateAsMath(self):
        if len(self.formula) == 0:
            return
        out = '$Y = '
        for dis in self.formula:
            for con in dis:
                if con[0] == '-':
                    out += '\\bar{' + con[1] + '}'
                    if len(con) > 2:
                        str1 = ''
                        out += '_{' + (str1.join(con[2:])) + '}'
                else:
                    out += con[0]
                    if len(con) > 1:
                        str1 = ''
                        out += '_{' + (str1.join(con[1:])) + '}'
            out += ' + '
        out = out[:-3] + '$'
        return out


    def GenerateAsLogic(self):
        if len(self.formula) == 0:
            return
        out = '$Y = '
        for dis in self.formula:
            for con in dis:
                if con[0] == '-':
                    out += '\\bar{' + con[1] + '}'
                    if len(con) > 2:
                        str1 = ''
                        out += '_{' + (str1.join(con[2:])) + '}'
                else:
                    out += con[0]
                    if len(con) > 1:
                        str1 = ''
                        out += '_{' + (str1.join(con[1:])) + '}'
            out += ' + '
        out = out[:-3] + '$'
        return out

    # konwertuje wynik na math i zapisuje jako obraz
    # (spowalnie generowanie wyniku)

    def RenderImage(self):
        formula = self.GenerateAsMath()
        fig = pylab.figure()
        text = fig.text(0, 0, formula)

        dpi = 200
        fig.savefig('formula.png', dpi=dpi)

        bbox = text.get_window_extent()
        width, height = bbox.size / float(dpi) + 0.12
        fig.set_size_inches((3, height))
        dy = (bbox.ymin / float(dpi)) / height
        text.set_position((0.01, -dy+0.1))
        fig.savefig('formula.png', dpi=dpi)
        pylab.close()

    @staticmethod
    def RenderImageS(lista):
        obj = ResultEntrance(lista)
        formula = obj.GenerateAsMath()
        fig = pylab.figure()
        text = fig.text(0, 0, formula)

        dpi = 200
        fig.savefig('formula.png', dpi=dpi)

        bbox = text.get_window_extent()
        width, height = bbox.size / float(dpi) + 0.12
        fig.set_size_inches((3, height))
        dy = (bbox.ymin / float(dpi)) / height
        text.set_position((0.01, -dy+0.1))
        fig.savefig('formula.png', dpi=dpi)
        pylab.close()


lista = [['x1', '-x2', '-x3', 'x4'], ['x1', '-x2', 'x3', 'x4'], ['x1', '-x2', '-x3', '-x4']]
lista = [['A', 'B', '-C', 'D'], ['A', '-x2', 'x3', 'x4'], ['x1', '-x2', '-x3', '-x4']]
tmp = [['-x', '-x12', 'x1', 'x2'], ['x', '-x12', '-x']]

obj = ResultEntrance(tmp)
str1 = obj.GenerateAsMath()
print(str1)

out = '$Y = '
for dis in tmp:
    for con in dis:
        if con[0] == '-':
            # str1 = ''
            # out += '\\bar{' + con[1] + '}' + '_{' + (str1.join(con[2:])) + '}'
            out += '\\bar{' + con[1] + '}'
            if len(con) > 2:
                str1 = ''
                out += '_{' + (str1.join(con[2:])) + '}'
        else:
            out += con[0]
            if len(con) > 1:
                str1 = ''
                out += '_{' + (str1.join(con[1:])) + '}'
    out += ' + '
out = out[:-3] + '$'
print(out)

d = schemdraw.Drawing(unit=0.5)


# alphabet = list(string.ascii_uppercase)
# zmienne = ['x', 'y', 'z', 'a', 'b']
# print(alphabet)
#
# licznik = 1
#
# for x in range(0,4):
#     litera = alphabet[x]
#     d.here= (x+1,0)
#     out = "d += (" + litera + " := logic.Dot().label( " + "'" + zmienne[x] + "', fontsize=16)).color('red')"
#     exec(out)
#     d += logic.Line().down().length(0.4)
#     out = "d += (" + litera + f"{licznik} := logic.Dot())"
#     print(out)
#     exec(out)
#     d.push()
#     d += logic.Line().down().length(9)
#     d.pop()
#     d += logic.Line().right()
#     out = f"d += (not_{litera} := logic.Not()).scale(0.7).down()"
#     exec(out)
#     d += logic.Line().down().length(8)



d.here= (0,0)

d += (A := logic.Dot(radius=0).label('A', fontsize=18))
d += logic.Line().down().length(0.4)

d += (A1 := logic.Dot())
d.push()
d += logic.Line().down().length(9).linewidth(0.5)
d.pop()
d += logic.Line().right()
d += (not_A := logic.Not()).scale(0.7).down()
d += logic.Line().down().length(7.5)

d.here= (1,0)
d += (B := logic.Dot(radius=0).label('B', fontsize=20)).color('blue')
d += logic.Line().down().length(0.4)
d += (B1 := logic.Dot())
d.push()
d += logic.Line().down().length(9)
d.pop()
d += logic.Line().right()
d += logic.Line().down()
d += (not_B := logic.Not()).scale(0.7).linewidth(1)
d += logic.Line().down().length(7.5)

d.here= (2,0)
d += (C := logic.Dot().label('C'))
d += logic.Line().down().length(0.4)
d += (C1 := logic.Dot())
d.push()
d += logic.Line().down().length(9)
d.pop()
d += logic.Line().right()
d += logic.Line().down()
d += (not_C := logic.Not()).scale(0.7)
d += logic.Line().down().length(7.5)


d.here= (3,0)
d += (D := logic.Dot().label('D'))
d += logic.Line().down().length(0.4)
d += (D1 := logic.Dot())
d.push()
d += logic.Line().down().length(9)
d.pop()
d += logic.Line().right()
d += logic.Line().down()
d += (not_D := logic.Not()).scale(0.7)
d += logic.Line().down().length(7.5)






d.here = (4,-2)
d += (X := logic.And().right().anchor('in1').label('X', 'right'))
d += logic.Line().down().at(B.start).toy(X.in1)
d += logic.Dot()
d += logic.Line().to(X.in1)

d += logic.Line().down().at(not_B.end).toy(X.in2).color('red')
d += logic.Dot()
d += logic.Line().to(X.in2)


d.here = (4,-3.5)
d += (Y := logic.And(inputs=2).right().anchor('in1').label('Y$_{x}$', 'right'))
d += logic.Line().down().at(A.start).toy(Y.in1)
d += logic.Dot()
d += logic.Line().to(Y.in1)

d += logic.Line().down().at(not_A.end).toy(Y.in2).color('red')
d += logic.Dot()
d += logic.Line().to(Y.in2)

d.here = (4,-5)
d += (Z := logic.And().right().anchor('in1').label('Z', 'right'))
d += logic.Line().down().at(C1.start).toy(Z.in1)
d += logic.Dot()
d += logic.Line().to(Z.in1)

d += logic.Line().down().at(not_D.end).toy(Z.in2).color('red')
d += logic.Dot()
d += logic.Line().to(Z.in2)


d.here = (4,-6.5)
d += (W := logic.And(inputs=4).right().anchor('in1').label('W', 'right'))
d += logic.Line().down().at(C1.start).toy(W.in1)
d += logic.Dot()
d += logic.Line().to(W.in1)

d += logic.Line().down().at(not_C.end).toy(W.in2).color('red')
d += logic.Dot()
d += logic.Line().to(W.in2)

d += logic.Line().down().at(not_A.end).toy(W.in3).color('red')
d += logic.Dot()
d += logic.Line().to(W.in3)

d += (O1 := logic.Or(inputs=5).right().at((X.out[0]+2,(X.out[1]+W.out[1])/2)).label('Y$_{out}$', 'right')).scale(1.5)


d += logic.Line().right().at(X.out).tox(O1.in1).color('green')
d += logic.Line().to(O1.in1)

d += logic.Line().right().at(Y.out).toy(O1.in2).color('red')
d += logic.Line().right().length(0.9)
d += logic.Line().to(O1.in2)

d += logic.Line().right().at(Z.out).toy(O1.in3).color('red')
d += logic.Line().right().length(0.9)
d += logic.Line().to(O1.in3)

d += logic.Line().right().at(W.out).tox(O1.in5).color('blue')
d += logic.Line().to(O1.in5)




# d += logic.Line().down().at(not_A.end).toy(D.in2).color('red')
# d += logic.Dot()
# d += logic.Line().to(D.in2)


print('C$_{in}$')


d.draw()







