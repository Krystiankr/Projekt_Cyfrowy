# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1890, 830)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblMetoda = QtWidgets.QLabel(self.centralwidget)
        self.lblMetoda.setGeometry(QtCore.QRect(730, 30, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.lblMetoda.setFont(font)
        self.lblMetoda.setObjectName("lblMetoda")
        self.lblQuine = QtWidgets.QLabel(self.centralwidget)
        self.lblQuine.setGeometry(QtCore.QRect(1150, 20, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        self.lblQuine.setFont(font)
        self.lblQuine.setStyleSheet("font: 700 36pt \"Script MT Bold\";\n"
"background-color: None;")
        self.lblQuine.setObjectName("lblQuine")
        self.lblMinimalizacja = QtWidgets.QLabel(self.centralwidget)
        self.lblMinimalizacja.setGeometry(QtCore.QRect(0, -20, 851, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.lblMinimalizacja.setFont(font)
        self.lblMinimalizacja.setStyleSheet("")
        self.lblMinimalizacja.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMinimalizacja.setObjectName("lblMinimalizacja")
        self.btnFind = QtWidgets.QPushButton(self.centralwidget)
        self.btnFind.setGeometry(QtCore.QRect(230, 300, 121, 41))
        self.btnFind.setStyleSheet(":active\n"
"{\n"
"font: 500 12pt \"Open Sans\";\n"
"-webkit-border-radius: 12px;\n"
"-moz-border-radius: 12px;\n"
"border-radius: 12px;\n"
"background-color: rgb(15, 111, 198);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255)\n"
"}\n"
":!active\n"
"{\n"
"font: 500 12pt \"Open Sans\";\n"
"-webkit-border-radius: 12px;\n"
"-moz-border-radius: 12px;\n"
"border-radius: 12px;\n"
"background-color: rgb(15, 111, 198);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255)\n"
"}\n"
"\n"
"\n"
":pressed\n"
"{\n"
"    background-color: rgb(0, 85, 255);\n"
"    border-style: inset\n"
"}\n"
":hover\n"
" {\n"
"    border: 2px solid rgb(0, 0, 0)\n"
"}\n"
":focus\n"
" {\n"
"    border: 2px solid rgb(0, 0, 255)\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btnFind.setAutoDefault(True)
        self.btnFind.setObjectName("btnFind")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 120, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.label_3.setObjectName("label_3")
        self.lnMinterm = QtWidgets.QLineEdit(self.centralwidget)
        self.lnMinterm.setGeometry(QtCore.QRect(180, 170, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lnMinterm.setFont(font)
        self.lnMinterm.setStyleSheet("border: 3px solid #1C6EA4;\n"
"border-radius: 12px;")
        self.lnMinterm.setText("")
        self.lnMinterm.setFrame(True)
        self.lnMinterm.setAlignment(QtCore.Qt.AlignCenter)
        self.lnMinterm.setDragEnabled(True)
        self.lnMinterm.setObjectName("lnMinterm")
        self.lnVariable = QtWidgets.QLineEdit(self.centralwidget)
        self.lnVariable.setGeometry(QtCore.QRect(180, 120, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lnVariable.setFont(font)
        self.lnVariable.setStyleSheet("border: 3px solid #1C6EA4;\n"
"border-radius: 12px;")
        self.lnVariable.setInputMask("")
        self.lnVariable.setAlignment(QtCore.Qt.AlignCenter)
        self.lnVariable.setObjectName("lnVariable")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 220, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.label_7.setObjectName("label_7")
        self.lnDontCare = QtWidgets.QLineEdit(self.centralwidget)
        self.lnDontCare.setGeometry(QtCore.QRect(180, 240, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lnDontCare.setFont(font)
        self.lnDontCare.setStyleSheet(":active\n"
"{\n"
"border: 3px solid #1C6EA4;\n"
"border-radius: 12px;\n"
"}\n"
":disabled\n"
"{\n"
"    \n"
"    background-color: rgb(234, 234, 234);\n"
"    border: 2px solid rgb(172, 172, 172);\n"
"    border-radius: 12px;\n"
"\n"
"}")
        self.lnDontCare.setAlignment(QtCore.Qt.AlignCenter)
        self.lnDontCare.setObjectName("lnDontCare")
        self.chbDontCare = QtWidgets.QCheckBox(self.centralwidget)
        self.chbDontCare.setGeometry(QtCore.QRect(40, 230, 21, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chbDontCare.setFont(font)
        self.chbDontCare.setMouseTracking(True)
        self.chbDontCare.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.chbDontCare.setText("")
        self.chbDontCare.setObjectName("chbDontCare")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 170, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.label.setObjectName("label")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 241, 31))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(730, 0, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-color: None;\n"
"font: 500 18pt \"Open Sans\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(940, 100, 75, 24))
        self.pushButton_2.setStyleSheet(":active\n"
"{\n"
"font: 500 10pt \"Open Sans\";\n"
"-webkit-border-radius: 12px;\n"
"-moz-border-radius: 12px;\n"
"border-radius: 12px;\n"
"background-color: None;\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(208, 208, 208)}\n"
":pressed\n"
"{\n"
"    background-color: rgb(0, 85, 255);\n"
"}\n"
":hover\n"
" {\n"
"    border: 2px solid rgb(0, 0, 0)\n"
"}\n"
":!hover\n"
" {\n"
"    border: 2px solid rgb(208, 208, 208)\n"
"}\n"
"\n"
":released\n"
" {\n"
"    border: 2px solid rgb(208, 208, 208)\n"
"}\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1050, 100, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lblResultMath = QtWidgets.QLabel(self.centralwidget)
        self.lblResultMath.setGeometry(QtCore.QRect(800, 730, 751, 71))
        self.lblResultMath.setStyleSheet("border-color: None;")
        self.lblResultMath.setObjectName("lblResultMath")
        self.tblMinterm = QtWidgets.QTableView(self.centralwidget)
        self.tblMinterm.setGeometry(QtCore.QRect(20, 390, 402, 421))
        self.tblMinterm.setStyleSheet("QTableView {\n"
"        gridline-color: black;\n"
"        selection-background-color: blue;\n"
"        text-align: center;\n"
"        font: 14pt;\n"
"    border: 3px solid #1C6EA4;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QHeaderView\n"
"{\n"
"    font: 600 11pt \"Open Sans\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(15, 111, 198);\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 4px;\n"
"    border-style: solid;\n"
"    border-bottom: 1px solid #fffff8;\n"
"    border-right: 1px solid #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: None;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border-left: 1px solid #fffff8;\n"
"}")
        self.tblMinterm.setObjectName("tblMinterm")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(350, 660, 191, 151))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 350, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.label_4.setObjectName("label_4")
        self.tblBinary = QtWidgets.QTableView(self.centralwidget)
        self.tblBinary.setGeometry(QtCore.QRect(490, 160, 281, 601))
        self.tblBinary.setStyleSheet("QHeaderView::section\n"
"{\n"
"            border-top:0px solid #D8D8D8;\n"
"            border-left:0px solid #D8D8D8;\n"
"            border-right:1px solid black;\n"
"            border-bottom: 1px solid #D8D8D8;\n"
"            background-color:white;\n"
"            padding:4px;\n"
"            font: 12pt;\n"
"\n"
"}\n"
"\n"
"QTableView {\n"
"        border-collapse: collapse;\n"
"        gridline-color: black;\n"
"        selection-background-color: blue;\n"
"        text-align: center;\n"
"        font: 12pt;\n"
"            border: 3px ridge  rgb(136, 136, 136) ;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"font: 12pt;\n"
"    border-top: None;\n"
"    border-bottom: 2px solid rgb(0, 0, 0);\n"
"    border-collapse: collapse;\n"
"}\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"            border-top: 0px solid black;\n"
"           border-left: 0px solid black;\n"
"            border-right: 2px solid black;\n"
"            border-bottom: 2px solid black;\n"
"           background-color: white;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"    font: 10pt;\n"
"    border-top: None;\n"
"    border-bottom: 1px solid ;\n"
"    border-right: 2px solid black;\n"
"    border-collapse: collapse;\n"
"}")
        self.tblBinary.setLineWidth(3)
        self.tblBinary.setObjectName("tblBinary")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(480, 110, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.label_5.setObjectName("label_5")
        self.lblSchemat = QtWidgets.QLabel(self.centralwidget)
        self.lblSchemat.setGeometry(QtCore.QRect(780, 160, 1091, 541))
        self.lblSchemat.setObjectName("lblSchemat")
        self.lblMetoda.raise_()
        self.lblQuine.raise_()
        self.lblMinimalizacja.raise_()
        self.btnFind.raise_()
        self.label_3.raise_()
        self.lnMinterm.raise_()
        self.lnVariable.raise_()
        self.label_7.raise_()
        self.lnDontCare.raise_()
        self.chbDontCare.raise_()
        self.label.raise_()
        self.label_9.raise_()
        self.label_8.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.lblResultMath.raise_()
        self.tblMinterm.raise_()
        self.stackedWidget.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.tblBinary.raise_()
        self.lblSchemat.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.setBuddy(self.lnVariable)
        self.label.setBuddy(self.lnMinterm)
        self.label_4.setBuddy(self.lnVariable)
        self.label_5.setBuddy(self.lnVariable)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lnMinterm, self.chbDontCare)
        MainWindow.setTabOrder(self.chbDontCare, self.lnDontCare)
        MainWindow.setTabOrder(self.lnDontCare, self.btnFind)
        MainWindow.setTabOrder(self.btnFind, self.tblBinary)
        MainWindow.setTabOrder(self.tblBinary, self.lnVariable)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblMetoda.setText(_translate("MainWindow", "metodą"))
        self.lblQuine.setText(_translate("MainWindow", "Quine’a-McCluskeya"))
        self.lblMinimalizacja.setText(_translate("MainWindow", "Minimalizacja"))
        self.btnFind.setText(_translate("MainWindow", "Generuj"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Zmienne:</p></body></html>"))
        self.lnMinterm.setPlaceholderText(_translate("MainWindow", "1, 2, 5, 9, 12"))
        self.lnVariable.setText(_translate("MainWindow", "A, B, C, D"))
        self.lnVariable.setPlaceholderText(_translate("MainWindow", "a, b, c, d"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">wartości <br/>nieokreślone</p></body></html>"))
        self.lnDontCare.setPlaceholderText(_translate("MainWindow", "0, 6"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mintermy:</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "Forma zminimalizowana:"))
        self.pushButton_2.setText(_translate("MainWindow", "TEX"))
        self.pushButton_3.setText(_translate("MainWindow", "Tekst"))
        self.lblResultMath.setText(_translate("MainWindow", "Y = WYNIK"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Wektory:</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Tablica prawdy:</p></body></html>"))
        self.lblSchemat.setText(_translate("MainWindow", "TextLabel"))
