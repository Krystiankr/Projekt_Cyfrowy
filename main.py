import sys
from typing import List
import ResultEntrance
from random import *

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt



from Create_Table import CreateTable
from MainWindow import Ui_MainWindow
from TableModel import TableModel
from ResultEntrance import ResultEntrance


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
        # self.label_2.resize(self.renderer.defaultSize())
        # self.painter = QtGui.QPainter(self.label_2)
        # self.painter.restore()
        # self.renderer.render(self.painter)
        # self.label_2.show()
        # # widget.show()



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
                print(f"{start}, 0, {count}, 1")
            start = x


    def GetData(self):
        # sprawdzenie czy wprowadzono dane
        if self.lnMinterm.displayText() == '':
            button = QMessageBox.information(self, "Brak danych", "Podaj mintermy")
            return

        # przekazanie danych z formantów do metod
        getMinterm = self.lnMinterm.displayText()
        getDontCare = self.lnDontCare.displayText()

        # jeżeli nie zaznaczono wartości nieokreślonych zignoruj wartości
        if not self.chbDontCare.isChecked():
            getDontCare = ''

        # utworzenie DataFrame z klasy CreateTable(konstruktor).metoda()
        wynik = CreateTable(getMinterm, getDontCare).get_df()

        # utworzenie formanta TableView i przekazanie danych
        self.model = TableModel(wynik)
        self.tableView.setModel(self.model)
        self.MergeRow(self.tableView, wynik['Liczba jedynek'].values)

        tabBinary = CreateTable(getMinterm, getDontCare).return_df()
        self.model1 = TableModel(tabBinary)
        self.tblBinary.setModel(self.model1)

        copy = tabBinary
        print(copy)

        trial = [[0 for x in range(randint(2, 5))] for y in range(randint(2, 5))]
        for x in range(0, len(trial)):
            for y in range(0, len(trial[x])):
                if randint(1, 10) % 2 == 0:
                    trial[x][y] = '-' + chr(randint(65, 70))
                else:
                    trial[x][y] = chr(randint(65, 70))
        print(trial)

        self.img = ResultEntrance(trial).RenderImage()
        self.label_2.setPixmap(QPixmap('formula.png'))


    def ChangingState(self, s):
        s == Qt.Checked
        if s == 2:  # Checked
            self.lnDontCare.setEnabled(True)
        if s == 0:  # Unchecked
            self.lnDontCare.setEnabled(False)


# ============================================================================================


app = QApplication(sys.argv)

window = MainWindow()

window.show()
app.exec_()

# ===========================================

