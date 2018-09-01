from PyQt5.QtWidgets import *
from ui_add_group import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap


class AddGroup(QMainWindow, Ui_AddGroup):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_save.released.connect(self.saveClicked)

    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def saveClicked(self):
        self.saveToDb()
        print("Save button clicked.")

    def saveToDb(self):
        group_name = self.cb_group_name.currentText()
        leader_id = self.tb_leader_id.text()

        DBConnectSingleton.instance.addGroup(group_name, leader_id)
        self.close()

