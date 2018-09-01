from PyQt5.QtWidgets import *
from ui_edit_group import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QModelIndex
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QHeaderView
from add_group import *

class EditGroup(QMainWindow, Ui_EditGroup):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_add_group.released.connect(self.addClicked)
        self.btn_remove_group.released.connect(self.removeClicked)
        self.tv_group.clicked.connect(self.tableViewClicked)
        self.viewTable()

    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def addClicked(self):
        self.ch_window = AddGroup()
        self.ch_window.show()

    @pyqtSlot()
    def removeClicked(self):
        return

    def viewTable(self):
        # group_list = DBConnectSingleton.instance.getGroupList()
        self.model = QSqlTableModel(self, DBConnectSingleton.instance.getDB())
        self.model.setTable('Department')
        # self.model.setFilter("department = '" + str(id_) + "';")
        self.model.select()
        self.tv_group.setModel(self.model)


        h_list = ["Name", "Leader"]

        h_visible = [0, 1, 0]

        index = 1;
        for s in h_list:
            self.model.setHeaderData(index, QtCore.Qt.Horizontal, s)
            index += 1
        index = 0
        self.tv_group.setModel(self.model)
        for i in h_visible:
            visible = False
            if i is 1:
                visible = False
            else:
                visible = True
            self.tv_group.setColumnHidden(index, visible)
            index += 1

        self.tv_group.setSortingEnabled(True)
        for i in range(0,len(h_visible)):
            self.tv_group.setColumnWidth(i,326)
        self.tv_group.show()
asdasd
    @pyqtSlot(QModelIndex)
    def tableViewClicked(self, index):
        print('hi')
    #
    # def setTableWidth(self):
    #     width = self.tv_group.verticalHeader().width()
    #     width += self.tv_group.horizontalHeader().length()
    #     if self.tv_group.verticalScrollBar().isVisible():
    #         width += self.tv_group.verticalScrollBar().width()
    #     self.tv_group.setFixedWidth(width)
    #     width += self.tv_group.frameWidth() * 2
