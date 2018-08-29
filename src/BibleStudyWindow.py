from PyQt5.QtWidgets import *
from ui_biblestudywindow import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.Qt import QListWidgetItem
from PyQt5 import QtCore
from db_connect_singleton import *


class BibleStudyWindow(QMainWindow, Ui_BibleStudyWindow):
    def __init__(self , p_name , p_id = -1 , editable=True):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Bible Study")
        self.p_name = p_name
        self.gb_bible.setTitle("Name : "+p_name)
        self.p_id = p_id
        for i in self.getBibleStudyListFromDB():
            self.lv_bs_list.addItem(i)
        if p_name.lower() != "manage":
            self.list_bible = self.getAttendedBibleStudy(self.p_id)
            for i in range(0, self.lv_bs_list.count()):
                item = self.lv_bs_list.item(i)
                class_name = item.text()
                if editable:
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    if class_name in self.list_bible:
                        item.setCheckState(QtCore.Qt.Checked)
                    else:
                        item.setCheckState(QtCore.Qt.Unchecked)
                else:
                    item.setFlags(item.flags())
                    if class_name in self.list_bible:
                        item.setText(class_name + " : complete")
                    else:
                        item.setText(class_name + " : incomplete")
                    self.btn_add.setDisabled(True)
                    self.btn_save.setDisabled(True)


        else:
            self.btn_add.setDisabled(False)
            self.btn_save.setDisabled(True)
        self.lv_bs_list.itemChanged.connect(self.listItemChanged)
        self.btn_add.released.connect(self.btnAddClicked)
        self.btn_close.released.connect(self.btnCloseClicked)
        self.btn_save.released.connect(self.btnSaveClicked)

    @pyqtSlot(QListWidgetItem)
    def listItemChanged(self, item):
        print(self.gb_bible.title())
        if (item.checkState() == QtCore.Qt.Checked):
            print(item.text() + "checked")
        else:
            print(item.text() + "unchecked")

    @pyqtSlot()
    def btnSaveClicked(self):
        for i in range(0, self.lv_bs_list.count()):
            item = self.lv_bs_list.item(i)
            class_name = item.text()
            if class_name not in self.list_bible:
                self.updateBibleStudyDb(self.p_id,self.getBibleIdFromDB(class_name))

    @pyqtSlot()
    def btnCloseClicked(self):
        self.close()

    @pyqtSlot()
    def btnAddClicked(self):
        value , ok = QInputDialog.getText(self,"Input Study Title","input title")
        print(value,ok)
        if ok:
            self.addBibleClassToDB(value)
        else:
            return

    def getBibleStudyListFromDB(self):
        return DBConnectSingleton.instance.getBStudyList()

    def updateBibleStudyDb(self,p_id,b_id):
        pass

    def getAttendedBibleStudy(self,p_id):
        return DBConnectSingleton.instance.getBStudy(self.p_id)

    def addBibleClassToDB(self,name):
        DBConnectSingleton.instance.updateBibleClass(name)

    def getBibleIdFromDB(self,bible_name):
        return 2



