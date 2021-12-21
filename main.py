from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import numpy as np
from typing import Any, List, Callable, Union
from fractions import Fraction
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QTextEdit

from MainWindow import Ui_MainWindow
from Create_Table import CreateTable
from Selekcja_Implikantow import SelekcjaImplikantow


import sys

# wejscie = pd.DataFrame(np.array([[0, '0000', 0], [1, '0001', 1], [1, '0010', 2],
#                              [1, '1000', 8], [2, '0011', 3], [2, '0110', 6],
#                              [3, '0111', 7], [3, '1101', 11]]),
#                    columns=['Liczba jedynek', 'Liczba Binarna', 'Liczba Dziesiętna'])

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
        # Note: self._data[index.row()][index.column()] will also work
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        data = pd.DataFrame(np.array([[0, '0000', 0], [1, '0001', 1], [1, '0010', 2],
                             [1, '1000', 8], [2, '0011', 3], [2, '0110', 6],
                             [3, '0111', 7], [3, '1101', 11]]),
                   columns=['Liczba jedynek', 'Liczba Binarna', 'Liczba Dziesiętna'])
        # data = np.array([[1, 9, 2], [1, 0, -1], [3, 5, 2], [3, 3, 2],
        #                  [5, 8, 9], ])

        print(data)
        self.model = TableModel(data)
        self.tableView.setModel(self.model)


        self.lnDontCare.setEnabled(False)
        self.chbDontCare.setCheckState(Qt.Unchecked)
        self.chbDontCare.stateChanged.connect(self.ChangingState)

        self.btnFind.clicked.connect(self.wypelnij)


    def wypelnij(self, s):
        if self.lnMinterm.displayText() == '':
            print("Nic nie ma")
            return
        wynik = self.lnMinterm.displayText()
        print(wynik)

        self.label_2.setText(str(wejscie))

    def ChangingState(self, s):
        s == Qt.Checked
        print(s)
        if s == 2:        # Checked
            self.lnDontCare.setEnabled(True)
        if s == 0:        # Unchecked
            self.lnDontCare.setEnabled(False)


app = QApplication(sys.argv)
#app.setStyle('Fusion')

window = MainWindow()
palette = QPalette()
palette.setColor(QPalette.Window, QColor(0, 128, 255))
palette.setColor(QPalette.WindowText, Qt.white)
app.setPalette(palette)
window.show()
app.exec_()





# lista1 = [1,2]
# lista2 = [4,5]
#
# wejscie = pd.DataFrame(np.array([[0, '0000', 0], [1, '0001', 1], [1, '0010', 2],
#                              [1, '1000', 8], [2, '0011', 3], [2, '0110', 6],
#                              [3, '0111', 7], [3, '1101', 11]]),
#                    columns=['Liczba jedynek', 'Liczba Binarna', 'Liczba Dziesiętna'])
#
# print(wejscie)

lista1 = "0,1,2,3,11"
lista2 = "4,5,9"
lista3 = "1,3"

wynik = CreateTable(lista1, lista2)
print(wynik.return_df())
print(wynik.get_df())
print()




# data = pd.DataFrame(np.array([[0, '0000', 0], [1, '0001', 1], [1, '0010', 2],
#                                          [1, '1000', 8], [2, '0011', 3], [2, '0110', 6],
#                                          [3, '0111', 7], [3, '1101', 11]]))
#
#
# for key, item in data.groupby(1):
#     print(key, item)
















