import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
    # window
win = QDialog()

def button_clicked():
    print('Button just clicked')
    

button_1 = QPushButton(win)
button_1.setText('Name')
    # button clicked
button_1.clicked.connect(button_clicked)

button_2 = QPushButton(win)
button_2.setText('Age')
button_2.move(0,50)


    # placement and size of window
win.setGeometry(500,300,500,500)
    # show window
win.show()
    # exit application
sys.exit(app.exec_())