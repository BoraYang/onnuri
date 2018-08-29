from PyQt5.QtWidgets import *
from ui_home import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap
from view_list import *
from edit_group import *
from BibleStudyWindow import *

class Home(QMainWindow, Ui_Home):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_quit.released.connect(self.closeClicked)
        self.btn_member.released.connect(self.memberClicked)
        self.btn_group.released.connect(self.groupClicked)
        self.btn_bible_study.released.connect(self.bibleStudyClicked)

    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def memberClicked(self):
        self.childWindow = ViewList()
        self.childWindow.show()

    @pyqtSlot()
    def groupClicked(self):
        self.childWindow = EditGroup()
        self.childWindow.show()

    @pyqtSlot()
    def bibleStudyClicked(self):
        self.childWindow = BibleStudyWindow('manage', p_id = -1 , editable=True)
        self.childWindow.show()
