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

        # data = pd.DataFrame(np.array([[0, '0000', 0], [1, '0001', 1], [1, '0010', 2],
        #                      [1, '1000', 8], [2, '0011', 3], [2, '0110', 6],
        #                      [3, '0111', 7], [3, '1101', 11]]),
        #            columns=['Liczba jedynek', 'Liczba Binarna', 'Liczba Dziesiętna'])
        #
        # print(data)

        # self.model = TableModel(data)
        # self.tableView.setModel(self.model)

        self.lnDontCare.setEnabled(False)
        self.chbDontCare.setCheckState(Qt.Unchecked)
        self.chbDontCare.stateChanged.connect(self.ChangingState)

        self.btnFind.clicked.connect(self.GetData)


    def GetData(self, s):

        # sprawdzenie czy wprowadzono dane
        if self.lnMinterm.displayText() == '':
            button = QMessageBox.information(self, "Brak danych", "Podaj mintermy")
            return

        # przekazanie danych z formantów do metod
        getMinterm = self.lnMinterm.displayText()
        getDontCare = self.lnDontCare.displayText()

        if not self.chbDontCare.isChecked():
            getDontCare = ''

        print("TUTAJ")
        wynik = CreateTable(getMinterm, getDontCare).get_df()
        print("WYNIK: ", wynik)
        self.model = TableModel(wynik)
        self.tableView.setModel(self.model)



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
# palette = QPalette()
# palette.setColor(QPalette.Window, QColor(0, 128, 255))
# palette.setColor(QPalette.WindowText, Qt.white)

window.show()
app.exec_()

#===========================================














#

# print(wynik)
#
# data = pd.DataFrame(np.array([[0, '0000', 0], [1, '0001', 1], [1, '0010', 2],
#                               [1, '1000', 8], [2, '0011', 3], [2, '0110', 6],
#                               [3, '0111', 7], [3, '1101', 11]]),
#                     columns=['Liczba jedynek', 'Liczba Binarna', 'Liczba Dziesiętna'])
#
# list = data['Liczba Dziesiętna'].tolist()
# print(list)












