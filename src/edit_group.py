from PyQt5.QtWidgets import *
from ui_edit_group import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap


class EditGroup(QMainWindow, Ui_EditGroup):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
