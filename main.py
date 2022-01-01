import sys
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
        self.SetShadowEffect(self.frame, blur=40)

        effectShadow = QGraphicsOpacityEffect(self.frame)
        effectShadow.setOpacity(0.8)
        self.frame.setGraphicsEffect(effectShadow)

        # Naciśnięcie button "GENERUJ"
        self.btnFind.clicked.connect(lambda: self.GetData(self.btnFind))

        self.btnShow.clicked.connect(lambda: self.ShowNewWindow(self.btnShow))

    # Naciśnięcie ENTER spowoduje wywołanie akcji dla btnFind
    def keyPressEvent(self, e: QKeyEvent):
        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.GetData(self.btnFind)
            self.lnMinterm.setFocus()

    @staticmethod
    def SetShadowEffect(label: Qt.Widget, blur: float = 15, offst: float = 2):
        effectShadow = QGraphicsDropShadowEffect(label)
        effectShadow.setBlurRadius(blur)
        effectShadow.setOffset(offst)
        label.setGraphicsEffect(effectShadow)

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

    # ODKOMENTOWAĆ
    # def init_schema(self, source):
    #     # print("init schema")
    #     try:
    #         self.schema = ViewSchema(source)
    #     except Exception:
    #         print("init graph")
    #
    #     self.stackedWidget.addWidget(self.schema.return_canvas())
    #     self.stackedWidget.setCurrentWidget(self.schema.return_canvas())


    def GetData(self, buttn):
        # sprawdzenie czy wprowadzono dane
        if self.lnMinterm.displayText() == '':
            button = QMessageBox.information(self, "Brak danych", "<font size = 8> Podaj Mintermy </font>")
            self.lnMinterm.setFocus()
            return

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

            countVariables = len(self.obj.getVariablesAsList())
            maxAcceptMinterm = pow(2, countVariables) - 1

            tab = [0,6,12,15]
            maxGiveNumber = max(tab)

            if maxGiveNumber > maxAcceptMinterm:
                print("Za duze liczby")
                button = QMessageBox.information(self, f"Niepoprawne dane", "Podano zbyt duże liczby. Dodaj zmienną lub "
                                                 f" wprowadź liczby w zakresie 0 - {maxAcceptMinterm}")
        except Exception:
            print("Problem z generowaniem obiektu InputData")

        try:
            self.ImportDataFrameToTruthTable(self.tblBinary, self.obj)
            self.ImportDataFrameToTableMinterm(self.tblMinterm, self.obj)
        except Exception:
            print("Problem z przekazaniem obiektu InputData do metody ImportDataFrame")

        # utworzenie Schema
        try:
            self.schema = Schema(self.ListVariable, self.obj.getImplicantsAsBinary(), self.obj.getTruthTable())
            self.schema.GenerateSchema()
        except Exception:
            print("Problem z wygenerowaniem obiektu Schema")

        pix = QPixmap('schema.png')
        pix = pix.scaled(self.lblSchemat.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.lblSchemat.setPixmap(pix)
        # self.lblSchemat.setScaledContents(True)

        obj_formula = ResultEntrance(self.obj.getImplicantsAsInput())
        str1 = obj_formula.GenerateAsMath()
        obj_formula.RenderImage()
        pix1 = QPixmap('formula.png')
        self.lblResultMath.setPixmap(pix1)
        self.btnShow.setEnabled(True)

    def ShowNewWindow(self, buttn):
        self.schema.ShowWithTruthTable()

    def CheckNumbersAndVariables(self):
        print()


    def ImportDataFrameToTruthTable(self, table: QTableView, obj: InputData):
        source = obj.getTruthTable().astype(str)
        model = TableModelBinary(source)
        table.setModel(model)

        vertHead = table.verticalHeader()
        vertHead.setDefaultSectionSize(35)
        vertHead.setMaximumWidth(50)
        vertHead.setDefaultAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        horiHead = table.horizontalHeader()
        horiHead.setDefaultSectionSize(40)
        horiHead.setFixedHeight(36)
        table.setColumnWidth(obj.getTruthTable().shape[1] - 1, 52)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        if obj.getTruthTable().shape[0] > 16:
            table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            table.setFixedWidth(310)
        else:
            table.setFixedWidth(250)
            table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def ImportDataFrameToTableMinterm(self, table: QTableView, obj: InputData):
        source = obj.getGroupImplicants()
        df = source.rename({"Liczba jedynek": "Grupa", "Liczba Binarna": "Binarnie", "Liczba Dziesiętna": "Dziesiętnie"}, axis=1)
        model = TableModelMinterm(df)

        table.setModel(model)
        column = table.horizontalHeader()
        row = table.verticalHeader()
        row.setDefaultSectionSize(40)
        column.setDefaultSectionSize(100)
        table.setColumnWidth(0, 150)
        table.setColumnWidth(1, 130)
        table.setColumnWidth(2, 100)
        table.setFixedWidth(402)
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
