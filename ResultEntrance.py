import pylab
from typing import List

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
                    out += con[1] + "'"
                else:
                    out += con
            out += ' + '
        return out[:-3]

    def GenerateAsMath(self):
        if len(self.formula) == 0:
            return
        out = '$Y = '
        for dis in self.formula:
            for con in dis:
                if con[0] == '-':
                    out += '\\bar{' + con[1] + '}'
                else:
                    out += con
            out += ' + '
        out = out[:-3] + '$'
        return out

    # konwertuje wynik na math i zapisuje jako obraz
    # (spowalnie generowanie wyniku)
    # ZNALEŹC COŚ LEPSZEGO
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
        text.set_position((0, -dy))
        fig.savefig('formula.png', dpi=dpi)
        del fig

