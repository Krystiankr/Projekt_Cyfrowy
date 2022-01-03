import sys

import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from MainWindow import Ui_MainWindow
from class_file.TableModel import TableModelMinterm, TableModelBinary
from class_file.Reprezentacja_sumacyjna import *
from class_file.InputData import InputData
from class_file.Schema import Schema
from class_file.ResultEntrance import ResultEntrance


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.obj = None
        self.schema = None
        self.ListVariable = None
        self.ListImplicants = None
        self.setupUi(self)
        self.secondWindow = None

        # ustawienie czcionek
        font = QFont("Script MT Bold")
        self.lblQuine.setFont(font)
        font = QFont("Open Sans")
        self.btnFind.setFont(font)

        # ustawienia początkowe
        self.lnDontCare.setEnabled(False)
        self.chbDontCare.setCheckState(Qt.Unchecked)
        self.chbDontCare.stateChanged.connect(self.ChangingState)

        self.btnShow.setEnabled(False)

        # ustawienie shadow
        self.SetShadowEffect(self.lblQuine, blur=10)
        self.SetShadowEffect(self.lnMinterm)
        self.SetShadowEffect(self.lnVariable)
        self.SetShadowEffect(self.lnDontCare)
        self.SetShadowEffect(self.btnFind, blur=30)
        self.SetShadowEffect(self.tblMinterm, blur=30)
        self.SetShadowEffect(self.tblBinary, blur=40)
        self.SetShadowEffect(self.frame, blur=40, offst=2)

        # Akcję dla przycisków"
        self.btnFind.clicked.connect(lambda: self.GenerateData(self.btnFind))
        self.btnShow.clicked.connect(lambda: self.ShowWindowSchema(self.btnShow))

    # Naciśnięcie ENTER spowoduje wywołanie akcji dla btnFind
    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.GenerateData(self.btnFind)
            self.lnMinterm.setFocus()

    @staticmethod
    def SetShadowEffect(label: Qt.Widget, blur: float = 15, offst: float = 2):
        ''' Dodanie efektu cienia dla przekazanego widgetu
            Args:
                label: widget, na którym dodajemy cień
                blur: wielkość rozmycia
                offst: odległość
        '''
        effectShadow = QGraphicsDropShadowEffect(label)
        effectShadow.setBlurRadius(blur)
        effectShadow.setOffset(offst)
        label.setGraphicsEffect(effectShadow)

    # Metoda scala komórki w kolumnie Liczba jedynek
    # Przyjmuje formant TableView, w którym sprawdzamy wiersze oraz tablice z danymi
    def MergeRow(self, Table: QTableView, tab: [List]):
        ''' Metoda scala komórki w kolumnie Liczba jedynek w tablicy wektorów
            Przyjmuje widget TableView, w którym sprawdza wiersze oraz tablice z danymi,
            a następnie łączy komórki o tych samych wartościach
        '''
        Table.clearSpans()           # usunięcie aktualnych scalan
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

    def GenerateData(self, buttn) -> bool:
        ''' Metoda przyjmuje dane wpisane od użytkownika i wykonuje wszystkie czynności
                    potrzebne do wyświetlenia wyniku
        '''

        # sprawdzenie czy wprowadzono dane
        if self.lnMinterm.displayText() == '':
            button = QMessageBox.information(self, "Brak danych", "<font size = 8> Podaj Mintermy </font>")
            self.lnMinterm.setFocus()
            return False

        self.lnMinterm.setFocus()

        # przekazanie danych z formantów do metod
        getMinterm = str(self.lnMinterm.text())
        getDontCare = str(self.lnDontCare.text())
        getVariable = str(self.lnVariable.text())

        # jeżeli nie zaznaczono wartości nieokreślonych zignoruj wartości
        if not self.chbDontCare.isChecked():
            getDontCare = ''

        try:
            self.obj = InputData(getVariable, getMinterm, getDontCare)
            self.ListVariable = self.obj.getVariablesAsString()
            self.ListImplicants = self.obj.getTestImplicant()

            # sprawdzenie czy liczba wpisanych liczb odpawiada (ilością) wpisanym zmiennych
            countVariables = len(self.obj.getVariablesAsList())
            maxAcceptMinterm = pow(2, countVariables) - 1
            tab = self.obj.getInitNumbers()
            maxGiveNumber = max(tab)
            if maxGiveNumber > maxAcceptMinterm:
                button = QMessageBox.information(self, f"Niepoprawne dane", "Podano zbyt duże liczby. Dodaj zmienną lub "
                                                 f" wprowadź liczby w zakresie 0 - {maxAcceptMinterm}")
                return False

        except Exception:
            print("Problem z generowaniem obiektu InputData")

        try:
            self.ImportDataFrameToTruthTable(self.tblBinary, self.obj)
            self.ImportDataFrameToTableMinterm(self.tblMinterm, self.obj)
        except Exception:
            print("Problem z utworzeniem tabel (ImportDataFrame)")

        # utworzenie Schema
        try:
            self.schema = Schema(self.ListVariable, self.obj.getImplicantsAsBinary(), self.obj.getTruthTable())
            f = self.schema.GenerateSchema(truth_table=False)
        except Exception:
            print("Problem z wygenerowaniem obiektu Schema")

        pix = QPixmap('schema.png')
        pix = pix.scaled(self.lblSchemat.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.lblSchemat.setPixmap(pix)
        # self.lblSchemat.setScaledContents(True)

        obj_formula = ResultEntrance(self.obj.getImplicantsAsInput())
        obj_formula.RenderImage()
        pix1 = QPixmap('formula.png')
        self.lblResultMath.setPixmap(pix1)
        self.btnShow.setEnabled(True)

        return True

    def ShowWindowSchema(self, buttn):
        f = self.schema.GenerateSchema(truth_table=True, draw=True, save_schem=False)

    def ImportDataFrameToTruthTable(self, table: QTableView, obj: InputData) -> None:
        source = obj.getTruthTable().astype(str)
        model = TableModelBinary(source)
        table.setModel(model)

        vertHead = table.verticalHeader()
        vertHead.setDefaultSectionSize(34)
        vertHead.setDefaultAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        horiHead = table.horizontalHeader()
        horiHead.setDefaultSectionSize(10)
        horiHead.setFixedHeight(36)

        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        if obj.getTruthTable().shape[0] > 16:
            table.setColumnWidth(obj.getTruthTable().shape[1] - 1, 40)
            table.setFixedWidth(290)
            table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        else:
            table.setColumnWidth(obj.getTruthTable().shape[1] - 1, 50)
            table.setFixedWidth(248)
            table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # if obj.getTruthTable().shape[0] > 16:
        #     table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #
        # else:
        #     table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # if obj.getTruthTable().shape[0] > 16:
        #     table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #     table.setFixedWidth(310)
        # else:
        #     table.setFixedWidth(250)
        #     table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def ImportDataFrameToTableMinterm(self, table: QTableView, obj: InputData) -> None:
        source = obj.getGroupImplicants()
        df = source.rename({"Liczba jedynek": "Grupa", "Liczba Binarna": "Binarnie", "Liczba Dziesiętna": "Dziesiętnie"}, axis=1)
        model = TableModelMinterm(df)

        table.setModel(model)
        column = table.horizontalHeader()
        row = table.verticalHeader()
        row.setDefaultSectionSize(40)
        column.setDefaultSectionSize(100)
        table.setColumnWidth(0, 120)
        table.setColumnWidth(1, 100)
        table.setColumnWidth(2, 100)
        table.setFixedWidth(343)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.verticalHeader().hide()

        self.MergeRow(table, df['Grupa'].values)

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

    def DrawSchema(self):
        try:
            self.obj = InputData(self.lnVariable.text(), str(self.lnMinterm.text()), str(self.lnDontCare.text()))
            print(self.obj.getTruthTable())
        except Exception:
            print("Object")

        try:
            values3a = 'a b c d e'
            self.secondWindow.tab = [1, 2, 3]
            # new_schema = Schema(variable, implicants)
            # new_schema.GenerateSchema()
        except Exception:
            print("schema crashed")

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
