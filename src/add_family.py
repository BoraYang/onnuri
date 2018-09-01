from PyQt5.QtCore import *
from ui_add_family import *
from PyQt5.QtWidgets import *
from db_connect_singleton import *

class AddFamily(QMainWindow,Ui_AddFamily):

    def __init__(self):
        super().__init__()
        self.setupUi()

    @pyqtSlot()
    def btnSearchClicked(self):
        f_name = self.tb_fam_name.text()
        pass


