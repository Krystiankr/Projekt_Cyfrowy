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
        MainWindow.resize(1890, 834)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 60, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 70, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 255, 255, 255), stop:0.373979 rgba(255, 255, 255, 255), stop:0.373991 rgba(33, 30, 255, 255), stop:0.624018 rgba(33, 30, 255, 255), stop:0.624043 rgba(255, 0, 0, 255), stop:1 rgba(255, 0, 0, 255));\n"
"font: 700 36pt \"Script MT Bold\";")
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, -20, 851, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btnFind = QtWidgets.QPushButton(self.centralwidget)
        self.btnFind.setGeometry(QtCore.QRect(230, 360, 121, 41))
        self.btnFind.setStyleSheet(":active\n"
"{\n"
"font: 500 12pt \"Open Sans\";\n"
"-webkit-border-radius: 12px;\n"
"-moz-border-radius: 12px;\n"
"border-radius: 12px;\n"
"background-color: rgb(15, 111, 198);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255)}\n"
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
        self.label_3.setGeometry(QtCore.QRect(60, 180, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.label_3.setObjectName("label_3")
        self.lnMinterm = QtWidgets.QLineEdit(self.centralwidget)
        self.lnMinterm.setGeometry(QtCore.QRect(180, 230, 221, 41))
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
        self.lnVariable.setGeometry(QtCore.QRect(180, 180, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lnVariable.setFont(font)
        self.lnVariable.setStyleSheet("border: 3px solid #1C6EA4;\n"
"border-radius: 12px;")
        self.lnVariable.setInputMask("")
        self.lnVariable.setAlignment(QtCore.Qt.AlignCenter)
        self.lnVariable.setObjectName("lnVariable")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 280, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.label_7.setObjectName("label_7")
        self.lnDontCare = QtWidgets.QLineEdit(self.centralwidget)
        self.lnDontCare.setGeometry(QtCore.QRect(180, 300, 221, 41))
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
        self.chbDontCare.setGeometry(QtCore.QRect(40, 290, 21, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chbDontCare.setFont(font)
        self.chbDontCare.setMouseTracking(True)
        self.chbDontCare.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.chbDontCare.setText("")
        self.chbDontCare.setObjectName("chbDontCare")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 230, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("border-color: None;\n"
"background-color: None;")
        self.label.setObjectName("label")
        self.tblBinary = QtWidgets.QTableView(self.centralwidget)
        self.tblBinary.setGeometry(QtCore.QRect(450, 210, 391, 381))
        self.tblBinary.setStyleSheet("border-top: 3px solid #1C6EA4;\n"
"border-radius: 12px;\n"
"border-top-color: rgb(255, 85, 127);\n"
"\n"
"")
        self.tblBinary.setLineWidth(3)
        self.tblBinary.setObjectName("tblBinary")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 160, 851, 631))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(220, 220, 220);\n"
"border-radius: 12px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(760, 10, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.lblResultMath = QtWidgets.QLabel(self.frame)
        self.lblResultMath.setGeometry(QtCore.QRect(60, 540, 751, 71))
        self.lblResultMath.setStyleSheet("border-color: None;")
        self.lblResultMath.setObjectName("lblResultMath")
        self.tblMinterm = QtWidgets.QTableView(self.frame)
        self.tblMinterm.setGeometry(QtCore.QRect(20, 260, 391, 221))
        self.tblMinterm.setStyleSheet("border: None")
        self.tblMinterm.setObjectName("tblMinterm")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 510, 311, 51))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 600, 75, 24))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 600, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.btnDrawSchema = QtWidgets.QPushButton(self.frame)
        self.btnDrawSchema.setGeometry(QtCore.QRect(570, 460, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.btnDrawSchema.setFont(font)
        self.btnDrawSchema.setStyleSheet(":active\n"
"{\n"
"font: 500 12pt \"Open Sans\";\n"
"-webkit-border-radius: 12px;\n"
"-moz-border-radius: 12px;\n"
"border-radius: 12px;\n"
"background-color: rgb(15, 111, 198);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255, 255, 255)}\n"
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
"")
        self.btnDrawSchema.setObjectName("btnDrawSchema")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 130, 241, 31))
        self.label_9.setObjectName("label_9")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 400, 231, 161))
        self.label_2.setObjectName("label_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(870, 160, 991, 621))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.frame.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.btnFind.raise_()
        self.label_3.raise_()
        self.lnMinterm.raise_()
        self.lnVariable.raise_()
        self.label_7.raise_()
        self.lnDontCare.raise_()
        self.chbDontCare.raise_()
        self.label.raise_()
        self.tblBinary.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.lnVariable)
        self.label.setBuddy(self.lnMinterm)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lnMinterm, self.chbDontCare)
        MainWindow.setTabOrder(self.chbDontCare, self.lnDontCare)
        MainWindow.setTabOrder(self.lnDontCare, self.btnFind)
        MainWindow.setTabOrder(self.btnFind, self.tblMinterm)
        MainWindow.setTabOrder(self.tblMinterm, self.tblBinary)
        MainWindow.setTabOrder(self.tblBinary, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lnVariable)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "metodą"))
        self.label_6.setText(_translate("MainWindow", "Quine’a-McCluskeya"))
        self.label_4.setText(_translate("MainWindow", "Minimalizacja"))
        self.btnFind.setText(_translate("MainWindow", "Generuj"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Zmienne:</p></body></html>"))
        self.lnMinterm.setPlaceholderText(_translate("MainWindow", "1, 2, 5, 9, 12"))
        self.lnVariable.setText(_translate("MainWindow", "A, B, C, D"))
        self.lnVariable.setPlaceholderText(_translate("MainWindow", "a, b, c, d"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">wartości <br/>nieokreślone</p></body></html>"))
        self.lnDontCare.setPlaceholderText(_translate("MainWindow", "0, 6"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mintermy:</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Wyjście"))
        self.lblResultMath.setText(_translate("MainWindow", "Y = WYNIK"))
        self.label_8.setText(_translate("MainWindow", "Forma zminimalizowana:"))
        self.pushButton_2.setText(_translate("MainWindow", "TEX"))
        self.pushButton_3.setText(_translate("MainWindow", "Tekst"))
        self.btnDrawSchema.setText(_translate("MainWindow", "Rysuj"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
