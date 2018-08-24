import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from mainwindow import Ui_MainWindow

mainwindow_class = Ui_MainWindow


class MyMainWindow(QMainWindow, mainwindow_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.close)

    @pyqtSlot()
    def close(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainWindow()
    mywin.show()
    app.exec_()
