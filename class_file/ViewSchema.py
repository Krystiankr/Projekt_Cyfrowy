import sys

from matplotlib.backends.qt_compat import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import matplotlib
from class_file.InputData import InputData

# matplotlib.use("Qt5Agg")

if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas,
        NavigationToolbar2QT as NavigationToolbar,
    )
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas,
        NavigationToolbar2QT as NavigationToolbar,
    )
from matplotlib.figure import Figure

import schemdraw
import schemdraw.elements as elm
from MainWindow import Ui_MainWindow
from class_file.Schema import Schema

class ViewSchema(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, objectFromMain):
        super().__init__()
        self.object = objectFromMain
        self.objSchema = None
        self._main = QtWidgets.QWidget()

        values3a = 'a b c d'
        impl = ['0-1-', '10-0']
        print("TAB ==>:")
        print(self.object.getVariables())
        #
        try:
            self.objSchema = Schema(self.object.getVariables(), impl)
            self.objSchema.GenerateSchema()
        except Exception:
            print("VARIABLES crashed")
        #
        # obj.GenerateSchema()

        # napis = self.parent.lnVariable.text()

        # layout = QtWidgets.QVBoxLayout(self._main)


        self.canvas = FigureCanvasQTAgg(plt.Figure(figsize=(10, 10),
                                                   facecolor=(240 / 255, 240 / 255, 240 / 255),
                                                   constrained_layout=True,
                                                   dpi = 200))

        self.canvas1 = FigureCanvas(Figure(figsize=(5, 3)))

        #
        # layout.addWidget(self.canvas1)

        # self.addToolBar(NavigationToolbar(self.canvas1, self))
        # toolbar = NavigationToolbar(self.canvas1, self)
        layout = QtWidgets.QVBoxLayout(self._main)
        # layout.addWidget(toolbar)
        layout.addWidget(self.canvas)
        self.setCentralWidget(self._main)

        ax = self.canvas.figure.subplots()

        # d = schemdraw.Drawing(fontsize=10)
        # d.add(elm.Capacitor())
        # r = d.add(elm.Resistor(theta=40))
        # d.add(elm.Diode(label="D1"))
        # d.add(elm.Diode)
        # d.add(elm.Diode)
        self.objSchema.MainSchema.draw(ax=ax, show=False, showframe=True)
        self.objSchema.MainSchema.interactive(True)
        # d.draw(ax=ax, show=False)


    def return_canvas(self):
        return self.canvas


if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()













