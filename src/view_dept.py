from PyQt5.QtWidgets import *
from ui_view_dept import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap

class Home(QMainWindow, Ui_ViewDept):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_go_back.released.connect(self.closeClicked)
        for e in DBConnectSingleton.instance.getDeptName():
            self.cb_dept_name.addItem(e)

        @pyqtSlot()
        def closeClicked(self):
            self.close()