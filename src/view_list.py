from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow , QHeaderView , QAbstractItemView
from ui_view_list import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSql import QSqlTableModel
from db_connect_singleton import *
from newmember import *
from view_member import ViewMember


class ViewList(QMainWindow , Ui_ViewList):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.btnCancelClicked)
        self.btn_add.released.connect(self.btnAddClicked)
        self.btn_delete.released.connect(self.btnDeleteClicked)
        self.btn_edit.released.connect(self.btnEditClicked)
        # self.btn_search.released.connect()
        self.model = QSqlTableModel(self,DBConnectSingleton.instance.getDB())
        self.model.setTable("Person")
        # self.model.
        self.model.select()


        # self.model.EditStrategy(QSqlTableModel.OnManualSubmit)
        h_list = ["First Name","Middle Name","Last Name","Korean Name","Gender","Address" ,"BirthDay","Day of Register","E-Mail","Phone","Group","Dept","Duty","Baptism","Family","NewComer Study","New Member Study","Picture"]
        # h_visible = [1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0]
        h_visible = [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]
        index = 1;
        for s in h_list:
            self.model.setHeaderData(index, QtCore.Qt.Horizontal, s)
            index+=1
        index = 0
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
        self.tv_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tv_list.clicked.connect(self.selecteditem)
        self.tv_list.show()
        self.tv_list.doubleClicked.connect(self.itemDoubleClicked)
        self.selected_id = -1

    @pyqtSlot(QModelIndex)
    def selecteditem(self,index:QModelIndex):
        select = self.tv_list.model().index(index.row(),0).data()
        self.selected_id = select

    @pyqtSlot(QModelIndex)
    def itemDoubleClicked(self,index):
        row_index = index.row()
        print(self.tv_list.model().index(row_index,0).data())
        self.viwer_window = ViewMember(self.tv_list.model().index(row_index,0).data())
        self.viwer_window.show()

    @pyqtSlot()
    def btnCancelClicked(self):
        self.close()
        return

    @pyqtSlot()
    def btnAddClicked(self):
        self.childWindow = NewMember()
        self.childWindow.myWindowCloseSignal.connect(self.tableViewUpdate)
        self.childWindow.show()
        return

    @pyqtSlot()
    def btnDeleteClicked(self):
        DBConnectSingleton.instance.removePerson(self.selected_id)
        self.tableViewUpdate()
        return

    @pyqtSlot()
    def btnEditClicked(self):
        if self.selected_id == -1:
            return
        self.edit_view = EditMember(self.selected_id)
        self.edit_view.myWindowCloseSignal.connect(self.tableViewUpdate)
        self.edit_view.show()
        return

    @pyqtSlot()
    def btnSearchClicked(self):
        print("search btn click")
        return

    @pyqtSlot()
    def tableViewUpdate(self):
        self.tv_list.model().select()
        self.tv_list.show()

