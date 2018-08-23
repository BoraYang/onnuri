import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

mainwindow_class = uic.loadUiType("../gui/mainwindow.ui")[0]


class MyMainWindow(QMainWindow, mainwindow_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    app.exec_()
