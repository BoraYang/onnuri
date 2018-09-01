from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from ui_family_view import *
from db_connect_singleton import *
class FamilyView(QMainWindow,Ui_FamilyView):
    def __init__(self,f_id):
        super().__init__()
        self.setupUi(self)
        self.f_id =f_id
        self.setWindowTitle("Family Viewer")
        self.btnclose.released.connect(self.btnCloseClicked)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.model = QSqlTableModel(self,DBConnectSingleton.instance.getDB())
        self.model.setTable("Person")
        self.model.setFilter("family like "+str(f_id))
        self.model.select()
        self.tableView.setModel(self.model)
        h_list = ["First Name", "Middle Name", "Last Name", "Korean Name", "Gender", "Address", "BirthDay",
                  "Day of Register", "E-Mail", "Phone", "Group", "Dept", "Duty", "Baptism", "Family", "NewComer Study",
                  "New Member Study", "Picture"]
        # h_visible = [1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0]
        h_visible = [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        index = 1;
        for s in h_list:
            self.model.setHeaderData(index, QtCore.Qt.Horizontal, s)
            index += 1
        index = 0
        self.tableView.setModel(self.model)
        for i in h_visible:
            visible = False
            if i is 1:
                visible = False
            else:
                visible = True
            self.tableView.setColumnHidden(index, visible)
            index += 1

    @pyqtSlot()
    def btnCloseClicked(self):
        self.close()