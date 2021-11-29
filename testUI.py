import sys
from PyQt5 import QtWidgets, uic

import resources

app = QtWidgets.QApplication(sys.argv)

w = uic.loadUi("qtdesignerUI.ui")

w.show()
app.exec()