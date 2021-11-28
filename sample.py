import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

    # application
app = QApplication(sys.argv)

win = QWidget()
    # placement of window x,y,w,h
win.setGeometry(200,150,800,500)
win.setWindowTitle('HELLO WORLD!')

    # making label
label_1 = QLabel(win)
label_1.setText("This is the first pyqt5 application")
label_1.setToolTip("HELLOOOOO")
label_1.move(1,150)
    # show windows
win.show()

    # exit system
sys.exit(app.exec_())