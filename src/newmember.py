from PyQt5.QtWidgets import *
from ui_newmember import *
from PyQt5.QtCore import pyqtSlot

class NewMember(QMainWindow, Ui_NewMember):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.close)
        self.tb_kor_name.setReadOnly(False)

    @pyqtSlot()
    def close(self):
        exit()