import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


def the_window_style(win):
        # x, y, w, h
    win.setGeometry(300,200,800,500)
    win.setWindowTitle('HELLO WORLD!')
    win.setStyleSheet('background:#89d5c2')
        
        # frameless
    win.setWindowFlags(QtCore.Qt.FramelessWindowHint)


def button_launch(win):
    button = QPushButton(win)
    button.setText('LAUNCH')
    button.move(450,150)

def button_register(win):
    button = QPushButton(win)
    button.setText('REGISTER A FACE')
    button.move(450,200)

def button_records(win):
    button = QPushButton(win)
    button.setText('RECORDS')
    button.move(600,150)

def button_logs(win):
    button = QPushButton(win)
    button.setText('LOGS')
    button.move(600,200)

def button_get_started(win):
    button = QPushButton(win)
    button.setText('GET STARTED')
    button.move(525,250)



def label_title(win):
    label = QLabel(win)
    label.setText('UNMASKED')


def label_footer(win):
    label = QLabel(win)
    label.setText('Powered by CloverByte, 2021')
    label.move(300,480)

def run_application():
    app = QApplication(sys.argv)
    win = QDialog()

        # window style
    the_window_style(win)

        # window title
    label_title(win)

    button_launch(win)
    button_register(win)
    button_records(win)
    button_logs(win)
    button_get_started(win)
    
    label_footer(win)

    win.show()
    sys.exit(app.exec_())
    


    # run application
run_application()