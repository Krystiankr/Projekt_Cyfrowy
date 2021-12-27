import sys
from typing import List

import pandas as pd

import ResultEntrance
from random import *

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from MainWindow import Ui_MainWindow
from TableModel import TableModel
from TableModel import PandasModel
from ResultEntrance import ResultEntrance

from Tablica_pokryc import *
from Reprezentacja_sumacyjna import *
from InputData import InputData
from Tablica_pokryc import DostepneMetody


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.lnDontCare.setEnabled(False)
        self.chbDontCare.setCheckState(Qt.Unchecked)
        self.chbDontCare.stateChanged.connect(self.ChangingState)

        self.btnFind.clicked.connect(self.GetData)

        # ustawienie czcionek
        font = QFont("Script MT Bold")
        self.label_6.setFont(font)

        font = QFont("Open Sans")
        self.btnFind.setFont(font)

        # formatowanie tablic

        font = QFont("Open Sans", 12)
        self.tblBinary.setFont(font)

        column = self.tblBinary.horizontalHeader()
        row = self.tblBinary.verticalHeader()

        row.setDefaultSectionSize(40)
        column.setDefaultSectionSize(40)

        row.setStyleSheet("border-color: None;\n"
                          "background-color: None;")

        column.setStyleSheet("border-color: None;\n"
                             "background-color: None;")

        row.setFixedWidth(35)
        column.setFixedHeight(50)

        # self.tblBinary.horizontalHeader().setFixedHeight(50)
        # self.tblBinary.verticalHeader().setFixedWidth(35)

        # self.tblBinary.setStyleSheet("QTableWidget::item {padding-left: 5px; border: 3px}")

        # TUTAJ ZACZNIJ!!!!!!!!!!!
        self.tblBinary.horizontalHeader().setStyleSheet("QHeaderView::section {padding-left: 10px; border: 0px}")
        self.tblBinary.setStyleSheet("QTableWidget::item {padding-left: 10px; border: 0px}")

        self.tblBinary.horizontalHeader().setFont(QFont("Open Sans", 12))
        self.tblBinary.verticalHeader().setFont(QFont("Open Sans", 12))

        self.tblBinary.verticalHeader().setMaximumWidth(100)

        self.tblBinary.horizontalHeader().setDefaultAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.tblBinary.verticalHeader().setDefaultAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        # self.renderer = QSvgRenderer('Zeichen.svg')
        # self.lblResultMath.resize(self.renderer.defaultSize())
        # self.painter = QtGui.QPainter(self.lblResultMath)
        # self.painter.restore()
        # self.renderer.render(self.painter)
        # self.lblResultMath.show()
        # # widget.show()

        self.pushButton_2.clicked.connect(self.tryingCopy)

    # Metoda scala komórki w kolumnie Liczba jedynek
    # Przyjmuje formant TableView, w którym sprawdzamy wiersze oraz tablice z danymi
    def MergeRow(self, Table: QTableView, tab: [List]):
        # usunięcie aktualnych scalan
        Table.clearSpans()

        start = 0
        stop = len(tab)

        while start < stop - 1:
            num = tab[start]
            count = 1
            for x in range(start + 1, stop):
                if (tab[x] == num):
                    count += 1
                else:
                    break
            if count > 1:
                Table.setSpan(start, 0, count, 1)
            start = x


    def GetData(self):
        # sprawdzenie czy wprowadzono dane
        if self.lnMinterm.displayText() == '':
            button = QMessageBox.information(self, "Brak danych", "Podaj mintermy")
            return

        # przekazanie danych z formantów do metod
        getMinterm = self.lnMinterm.text()
        getDontCare = self.lnDontCare.text()
        getVariable = self.lnVariable.text()

        # jeżeli nie zaznaczono wartości nieokreślonych zignoruj wartości
        if not self.chbDontCare.isChecked():
            getDontCare = ''

        self.ImportDataFrameToTruthTable(self.tblBinary, getVariable, getMinterm, getDontCare)
        self.ImportDataFrameToTableMinterm(self.tblMinterm, getVariable, getMinterm, getDontCare)


        # copy = tabBinary
        # print(copy)

    def ImportDataFrameToTruthTable(self, table: QTableView, getVar: str, getMin: str, getDont: str):
        obj = InputData(getVar, getMin, getDont)
        source = obj.getTruthTable()

        self.model = TableModel(source)
        table.setModel(self.model)

    def ImportDataFrameToTableMinterm(self, table: QTableView, getVar: str, getMin: str, getDont: str):
        obj = DostepneMetody(getVar, getMin, getDont)
        source = obj.get_pierwsza_grupa()

        self.model = TableModel(source)
        table.setModel(self.model)

        self.MergeRow(table, source['Liczba jedynek'].values)

    def ChangingState(self, s):
        s == Qt.Checked
        if s == 2:  # Checked
            self.lnDontCare.setEnabled(True)
        if s == 0:  # Unchecked
            self.lnDontCare.setEnabled(False)

    def tryingCopy(self, s):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.label_9.text(), mode=cb.Clipboard)


# ============================================================================================

app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec_()

# ===========================================

#
# variable = 'a, b, c, d'
# sop = '1, 2, 3, 4, 5, 9, 12'
# dontcare = '0, 6'
#
# dane = InputData(variable, sop, dontcare)
# print(dane.truthTable)
# print(dane.listImplicant)
# print(dane.firstGroup)
#
