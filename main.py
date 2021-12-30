import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import Qt
from MainWindow import Ui_MainWindow
from class_file.TableModel import TableModel
from class_file.Tablica_pokryc import DostepneMetody
from class_file.Reprezentacja_sumacyjna import *
from class_file.InputData import InputData
from class_file.ViewSchema import ViewSchema

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.obj = None
        self.schema = None
        self.ListVariable = None
        self.ListImplicants = None
        self.setupUi(self)
        self.secondWindow = None


        self.lnDontCare.setEnabled(False)
        self.chbDontCare.setCheckState(Qt.Unchecked)
        self.chbDontCare.stateChanged.connect(self.ChangingState)

        if self.lnMinterm.displayText() == '':
            self.btnDrawSchema.setEnabled(False)
        else:
            self.btnDrawSchema.setEnabled(True)

        self.btnFind.clicked.connect(lambda: self.GetData(self.btnFind))

        # self.btnFind.clicked.connect(self.GetData)

        self.btnDrawSchema.clicked.connect(self.DrawSchema)

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

        # init graph
        #
        # self.schema = None
        #
        # self.init_schema()




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

    def init_schema(self, source):
        # print("init schema")
        try:
            self.schema = ViewSchema(source)
            self.stackedWidget.addWidget(self.schema.return_canvas())
            self.stackedWidget.setCurrentWidget(self.schema.return_canvas())
        except Exception:
            print("init graph")

    def GetData(self, buttn):
        # sprawdzenie czy wprowadzono dane
        if self.lnMinterm.displayText() == '':
            button = QMessageBox.information(self, "Brak danych", "Podaj mintermy")
            return

        # przekazanie danych z formantów do metod
        getMinterm = str(self.lnMinterm.text())
        getDontCare = str(self.lnDontCare.text())
        getVariable = str(self.lnVariable.text())

        # jeżeli nie zaznaczono wartości nieokreślonych zignoruj wartości
        if not self.chbDontCare.isChecked():
            getDontCare = ''

        try:
            print(getMinterm)
            print(getDontCare)
            print(getVariable)
            self.obj = InputData(getVariable, getMinterm, getDontCare)
            self.ListVariable = self.obj.getVariables()
            self.ListImplicants = self.obj.getTestImplicant()
            # self.ListImplicants = obj.getGroupImplicants()
            print(self.ListVariable)
            print(self.ListImplicants)
        except Exception:
            print("ZMIENNE")

        try:
            self.ImportDataFrameToTruthTable(self.tblBinary, self.obj)
            self.ImportDataFrameToTableMinterm(self.tblMinterm, self.obj)
        except Exception:
            print("Import")

        #self.ImportDataFrameToTableMinterm(self.tblMinterm, getVariable, getMinterm, getDontCare)


        self.btnDrawSchema.setEnabled(True)
        self.init_schema(self.obj)
        # self.passingInfo(self.obj)


        # copy = tabBinary
        # print(copy)
    def passingInfo(self, object1):

        try:
            self.init_schema(object1)
        except Exception:
            print("passing Info")

        # self.secondWindow = str(self.lnVariable.text())



    def ImportDataFrameToTruthTable(self, table: QTableView, obj: InputData):
        source = obj.getTruthTable()
        self.model = TableModel(source)
        table.setModel(self.model)

    # def ImportDataFrameToTruthTable(self, table: QTableView, getVar: str, getMin: str, getDont: str):
    #     obj = InputData(getVar, getMin, getDont)
    #     source = obj.getTruthTable()
    #
    #     self.model = TableModel(source)
    #     table.setModel(self.model)

    # def ImportDataFrameToTableMinterm(self, table: QTableView, getVar: str, getMin: str, getDont: str):
    #     obj = InputData(getVar, getMin, getDont)
    #     source = obj.getGroupImplicants()
    #
    #     self.model = TableModel(source)
    #     table.setModel(self.model)
    #
    #     self.MergeRow(table, source['Liczba jedynek'].values)

    def ImportDataFrameToTableMinterm(self, table: QTableView, obj: InputData):
        source = obj.getGroupImplicants()

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


    def DrawSchema(self):
        # self.label_2.setPixmap(QPixmap("schema.png"))

        try:
            self.obj = InputData(self.lnVariable.text(), str(self.lnMinterm.text()), str(self.lnDontCare.text()))
        except Exception:
            print("Object")


        # variable = str(self.lnVariable.text())
        # implicants = ['000-', '-010', '011-']
        #
        # lista = [[]]
        # lista = self.obj.getImplicants()
        # print(lista)


        # try:
        #     implicants2 = )
        # except Exception:
        #     print("Implikanty")


        # getMinterm = str(self.lnMinterm.text())
        # getDontCare = str(self.lnDontCare.text())
        # getVariable = str(self.lnVariable.text())
        #
        # # jeżeli nie zaznaczono wartości nieokreślonych zignoruj wartości
        # if not self.chbDontCare.isChecked():
        #     getDontCare = ''
        # try:
        #     obj1 = InputData(getVariable, getMinterm, getDontCare)
        #     imp = obj1.getImplicants()
        # except Exception:
        #     print("Krystian")
        #
        #
        # try:
        #     variable = str(self.lnVariable)
        # except Exception:
        #     print("variable")

        # variable = 'a b c d'
        # implicants = [['B'], ['-B', '-D'], ['B', 'D'], ['C', '-E'], ['A']]

        try:
            values3a = 'a b c d e'
            self.secondWindow.tab = [1, 2, 3]
            # new_schema = Schema(variable, implicants)
            # new_schema.GenerateSchema()
        except Exception:
            print("schema crashed")



        # try:
        #     print(new_schema.listImplicants())
        # except Exception:
        #     print("Schemat")

        # graph = ViewSchema()
        #
        # print("SCHEMA: POCZĄTEK")

        # implicants = self.obj.getImplicants()
        # variable = self.obj.getVariables()
        #
        # # self.CreateSchema(implicants, variable)
        # self.new_schema = Schema(implicants, variable)
        # self.new_schema.save("schema2.png", False)
        #
        # # print(new_schema.elements)
        #
        # print("SCHEMA: KONIEC")

        # print(implicants)
        # print(variable)

    # def CreateSchema(self, implicants1, variables):
    #     self.new_schema = Schema(implicants1, variables)

        # def __init__(self, list_variable, list_implicant, line_width: int = 1):
        #
        # new_schema = Schema(

        # self.label_9.setText()


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
