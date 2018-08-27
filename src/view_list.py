from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow , QHeaderView
from ui_view_list import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import QSqlTableModel
from DBSingleton import *

class ViewList(QMainWindow , Ui_ViewList):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.btn_cancel.released.connect()
        # self.btn_add.released.connect()
        # self.btn_delete.released.connect()
        # self.btn_edit.released.connect()
        # self.btn_search.released.connect()
        self.model = QSqlTableModel(self,OnlyOne.instance.getDB())
        self.model.setTable("Person")
        self.model.select()

        # self.model.EditStrategy(QSqlTableModel.OnManualSubmit)
        h_list = ["First Name","Middle Name","Last Name","Korean Name","Gender","BirthDay","Day of Register",        "E-Mail","Phone","Group","Duty","Baptism","Family","NewComer Study","New Member Study","BibleStudy"]
        h_visible = [1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0]
        index = 1;
        for s in h_list:
            self.model.setHeaderData(index, QtCore.Qt.Horizontal,s)
            index+=1
        index =0
        self.tv_list.setModel(self.model)
        for i in h_visible:
            visible = False
            if i is 1:
                visible = False
            else:
                visible = True
            self.tv_list.setColumnHidden(index , visible)
            index+=1

        self.tv_list.setSortingEnabled(True)

        self.tv_list.show()

    @pyqtSlot()
    def btnCancelClicked(self):
        self.close()
        return

    @pyqtSlot()
    def btnAddClicked(self):
        print("add btn click")
        return

    @pyqtSlot()
    def btnDeleteClicked(self):
        print("del btn click")
        return

    @pyqtSlot()
    def btnEditClicked(self):
        print("del btn click")
        return

    @pyqtSlot()
    def btnSearchClicked(self):
        print("search btn click")
        return