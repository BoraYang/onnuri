from PyQt5.QtWidgets import *
from ui_view_member import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap


class ViewMember(QMainWindow, Ui_ViewMember):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_save.released.connect(self.saveClicked)
        self.btn_show.released.connect(self.showClicked)
        self.tb_eng_name.setText(self.showEngName())
        self.tb_kor_name.setText(DBConnectSingleton.instance.getKorname())
        self.tb_email.setText(DBConnectSingleton.instance.getEmail())
        self.tb_phone.setText(DBConnectSingleton.instance.getPhone())


    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def saveClicked(self):
        print("save button clicked.")

    @pyqtSlot()
    def showClicked(self):
        print("show button clicked.")

    @pyqtSlot()
    def showEngName(self):
        first_name = DBConnectSingleton.instance.getFirstName()
        mid_name = DBConnectSingleton.instance.getMidName()
        last_name = DBConnectSingleton.instance.getLastName()
        if mid_name == None:
            return first_name + " " + last_name
        else:
            return first_name + " " + mid_name + " " + last_name




