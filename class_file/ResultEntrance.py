import pylab
from typing import List


class ResultEntrance:
    formula: List[List[str]]

    def __init__(self, formula):
        self.formula = formula

    def __repr__(self):
        return str(self.formula)

    def GenerateAsText(self) -> str:
        if len(self.formula) == 0:
            return ''
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

    def GenerateAsMath(self) -> str:
        if len(self.formula) == 0:
            return ''
        out = '$Y = '
        for dis in self.formula:
            for con in dis:
                if con[0] == '-':
                    out += '\\overline{' + con[1] + '}'
                    if len(con) > 2:
                        str1 = ''
                        out += '_{' + (str1.join(con[2:])) + '}'
                    out += '\,'
                else:
                    out += con[0]
                    if len(con) > 1:
                        str1 = ''
                        out += '_{' + (str1.join(con[1:])) + '}'
                    out += '\,'
            out += ' + '
        out = out[:-3] + '$'
        return out

    def GenerateAsMathBar(self):
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

    def GenerateAsLogic(self) -> str:
        if len(self.formula) == 0:
            return ''
        out = 'Y = ('
        for dis in self.formula:
            for con in dis:
                if con[0] == '-':
                    str1 = ''
                    out += 'not(' + (str1.join(con[1:])) + ")"
                else:
                    out += con
                out += ' and '
            out = out[:-5] + ') or ('
        return out[:-5]

    def RenderImage(self):
        # konwertuje wynik na math i zapisuje jako obraz
        formula = self.GenerateAsMath()
        fig = pylab.figure()
        text = fig.text(0, 0, formula)

        dpi = 200
        fig.savefig('png/formula.png', dpi=dpi)
        bbox = text.get_window_extent()
        width, height = bbox.size / float(dpi) + 0.12
        fig.set_size_inches((3, height))
        dy = (bbox.ymin / float(dpi)) / height
        text.set_position((0.01, -dy+0.1))
        fig.savefig('png/formula.png', dpi=dpi)
        pylab.close()

    # @staticmethod
    # def RenderImageS(lista):
    #     obj = ResultEntrance(lista)
    #     formula = obj.GenerateAsMath()
    #     fig = pylab.figure()
    #     text = fig.text(0, 0, formula)
    #
    #     dpi = 200
    #     fig.savefig('formula.png', dpi=dpi)
    #
    #     bbox = text.get_window_extent()
    #     width, height = bbox.size / float(dpi) + 0.12
    #     fig.set_size_inches((3, height))
    #     dy = (bbox.ymin / float(dpi)) / height
    #     text.set_position((0.01, -dy+0.1))
    #     fig.savefig('formula.png', dpi=dpi)
    #     pylab.close()


lista1 = [['x1', '-x2', '-x3', 'x4'], ['x1', '-x2', 'x3', 'x4'], ['x1', '-x2', '-x3', '-x4']]
lista2= [['A', 'B', '-C', 'D'], ['A', '-x2', 'x3', 'x4'], ['x1', '-x2', '-x3', '-x4']]
tmp = [['-x', '-x12', 'x1', 'x2'], ['x', '-x12', '-x']]

obj = ResultEntrance(lista1)
str1 = obj.GenerateAsMath()
obj.RenderImage()









