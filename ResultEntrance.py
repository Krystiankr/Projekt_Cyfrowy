import matplotlib
import pylab
from typing import Any, Optional, Dict, List


class ResultEntrance:
    formula: List[List[str]] = []

    def __init__(self, formula):
        self.formula = formula


    def printAsText(self):
        print(self.formula)
        out = 'Y = '
        for dis in self.formula:
            for con in dis:
                if con[0] == '-':
                    out += con[1] + "'"
                else:
                    out += con
            out += ' + '

        return out[:-3]



    # def saveImage(self):


#
# lista = [['A', '-B', 'C', '-D'], ['-A', 'B', 'C'], ['-B', '-C'], ['A', 'B']]
# tmp = ResultEntrance(lista)
#
# print(tmp.formula)
#
#
# print(len(lista))
#
# out = '$Y = '
# for dis in lista:
#     for con in dis:
#         if con[0] == '-':
#             out += '\\bar{' + con[1] + '}'
#         else:
#             out += con
#         # out += ' * '
#     out += ' + '
# out += '$'
# print(out)
#
#
# formula = r'$Y = \bar{A}\bar{B}\bar{C}D + A\bar{B}C, %s$' % ('test' * 2)
# print(formula)
#
# formula = r'$x=3^2, y = \frac{1}{\frac{2}{3}}, %s$' % ('test' * 20)
# formula = out
# fig = pylab.figure()
# text = fig.text(0, 0, formula)
#
# # Saving the figure will render the text.
# dpi = 300
# fig.savefig('formula.png', dpi=dpi)
#
# # Now we can work with text's bounding box.
# bbox = text.get_window_extent()
#
# width, height = bbox.size / float(dpi) + 0.12
# # Adjust the figure size so it can hold the entire text.
# fig.set_size_inches((3, height))
#
# # Adjust text's vertical position.
# dy = (bbox.ymin/float(dpi))/height
# text.set_position((0, -dy))
#
# # Save the adjusted text.
# fig.savefig('formula.png', dpi=dpi)