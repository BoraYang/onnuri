import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

mainwindow_class = uic.loadUiType("mainwindow.ui")[0]


class MyMainWindow(QMainWindow, mainwindow_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_push


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    app.exec_()
