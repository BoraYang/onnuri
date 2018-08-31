from PyQt5.QtWidgets import *
from ui_view_dept import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap

class ViewDept(QMainWindow, Ui_ViewDept):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_go_back.released.connect(self.closeClicked)
        for e in DBConnectSingleton.instance.getDeptName():
            self.cb_dept_name.addItem(e)
        self.cb_dept_name.currentTextChanged.connect(self.cb_changed)

    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot(str)
    def cb_changed(self, name):
        id_ = DBConnectSingleton.instance.getDeptID(name)
        self.tv_list.model.filter("department = '" + id_ + "';")
        self.tv_list.model.select()
        self.tv_list.show()
