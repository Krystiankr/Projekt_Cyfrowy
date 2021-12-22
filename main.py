import sys
from typing import List

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



from Create_Table import CreateTable
from MainWindow import Ui_MainWindow


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
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.lnDontCare.setEnabled(False)
        self.chbDontCare.setCheckState(Qt.Unchecked)
        self.chbDontCare.stateChanged.connect(self.ChangingState)

        self.btnFind.clicked.connect(self.GetData)


        # self.btnFind.setStyleSheet("background-color: blue")
        # self.tableView.setStyleSheet("border: 1px solid black")

        # wejscie = pd.DataFrame(np.array([[0, '0000', 0], [1, '0001', 1], [1, '0010', 2],
        #                              [1, '1000', 8], [2, '0011', 3], [2, '0110', 6],
        #                              [3, '0111', 7], [3, '1101', 11]]),
        #                    columns=['Liczba jedynek', 'Liczba Binarna', 'Liczba Dziesiętna'])
        #
        #
        # # formatowanie tableView
        # self.tableView.setFrameShape(QFrame.HLine)
        # self.model = TableModel(wejscie)
        # self.tableView.setModel(self.model)

        # self.tableView.setSpan(0,0,2,1)
        # header = QTableView.horizontalHeader(self.tableView)
        # header.setFrameStyle(QFrame.Box | QFrame.Plain)
        # header.setLineWidth(1)
        # self.tableView.setHorizontalHeader(header)

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

        tmp = Table.rowSpan(0,0)
        print(f"Span: {tmp}")

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

    def ChangingState(self, s):
        s == Qt.Checked
        print(s)
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


#

#
#
# data = pd.DataFrame(np.array([[0, '0000', 0], [1, '0001', 1], [1, '0010', 2],
#                               [1, '1000', 8], [2, '0011', 3], [2, '0110', 6],
#                               [3, '0111', 7], [3, '1101', 11]]),
#                     columns=['Liczba jedynek', 'Liczba Binarna', 'Liczba Dziesiętna'])
#
# print(data['Liczba jedynek'].values)
#
# listaJedynek = data['Liczba jedynek'].values
#
#
# start = 0
# count = 0
# stop = len(listaJedynek)
#
# while start < stop:
#     num = listaJedynek[start]
#     count = 1
#     for x in range(start+1, stop):
#         if (listaJedynek[x] == num):
#             count += 1
#         else:
#             break
#     if(count > 1):
#         print(f"{start}, 0, {count}, 1")
#     start = x
#
# print("KONIEC")
#
