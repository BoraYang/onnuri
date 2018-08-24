import sys
from PyQt5.QtWidgets import *

from PyQt5.QtCore import pyqtSlot


class MyMainWindow(QMainWindow, mainwindow_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chk_john.setEnable(false)

    @pyqtSlot()
    def close(self):
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow_class = uic.loadUi("../gui/newmember.ui")[0]
    mywin = MyMainWindow()
    mywin.show()
    app.exec_()
