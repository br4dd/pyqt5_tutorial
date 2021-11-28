import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def the_button_1(win):
    button = QPushButton(win)
    button.setText("Name")
    button.setToolTip("YOU HAVE DISCOVERED THE HIDDEN TREASURE")



def the_window_style(win):
        # x, y, w, h
    win.setGeometry(200,200,800,500)
    win.setWindowTitle('HELLO WORLD!')
    win.setStyleSheet('background:#89d5c2')
        
        # frameless
    #win.setWindowFlags(QtCore.Qt.FramelessWindowHint)


def the_title(win):
    label = QLabel(win)
    label.setText('HELLO WORLD')


def run_application():
    app = QApplication(sys.argv)
    win = QDialog()

        # window style
    the_window_style(win)

        # window title
    the_title(win)

    win.show()
    sys.exit(app.exec_())

    
    # run application
run_application()