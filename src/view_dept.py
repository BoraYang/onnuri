from PyQt5.QtWidgets import *
from ui_view_dept import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.QtSql import QSqlTableModel
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap

class ViewDept(QMainWindow, Ui_ViewDept):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for e in DBConnectSingleton.instance.getDeptName():
            self.cb_dept_name.addItem(e)

        self.cb_changed(self.cb_dept_name.currentText())
        self.btn_go_back.released.connect(self.closeClicked)
        self.cb_dept_name.currentTextChanged.connect(self.cb_changed)



    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot(str)
    def cb_changed(self, name):
        id_ = DBConnectSingleton.instance.getDeptID(name)
        self.model = QSqlTableModel(self, DBConnectSingleton.instance.getDB())
        self.model.setTable('Person')
        self.model.setFilter("department like "+str(id_))
        self.model.select()
        self.tv_list.setModel(self.model)


        h_list = ["First Name", "Middle Name", "Last Name", "Korean Name", "Gender", "Address", "BirthDay",
                  "Day of Register", "E-Mail", "Phone", "Group", "Dept", "Duty", "Baptism", "Family", "NewComer Study",
                  "New Member Study", "Picture"]

        h_visible = [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        index = 1;
        for s in h_list:
            self.model.setHeaderData(index, QtCore.Qt.Horizontal, s)
            index += 1
        index = 0
        self.tv_list.setModel(self.model)
        for i in h_visible:
            visible = False
            if i is 1:
                visible = False
            else:
                visible = True
            self.tv_list.setColumnHidden(index, visible)
            index += 1

        self.tv_list.setSortingEnabled(True)

        self.tv_list.show()

