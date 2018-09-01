from ui_home import *
from view_list import *
from edit_group import *
from BibleStudyWindow import *
from view_dept import *

class Home(QMainWindow, Ui_Home):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_quit.released.connect(self.closeClicked)
        self.btn_member.released.connect(self.memberClicked)
        self.btn_group.released.connect(self.groupClicked)
        self.btn_bible_study.released.connect(self.bibleStudyClicked)
        self.btn_department.released.connect(self.deptClicked)

        # Back ground
        # ui.frame->setStyleSheet("background-image: url(:/images/menu_background.png);" "background-repeat: repeat;");


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

    @pyqtSlot()
    def deptClicked(self):
        self.childWindow = ViewDept()
        self.childWindow.show()