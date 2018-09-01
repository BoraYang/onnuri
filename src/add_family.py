from PyQt5.QtCore import *
from ui_add_family import *
from PyQt5.QtWidgets import *
from db_connect_singleton import *

class AddFamily(QMainWindow,Ui_AddFamily):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_search.released.connect(self.btnSearchClicked)
        self.lv_search_result.itemDoubleClicked.connect(self.searchItemDoubleClicked)
        self.lv_be_added_family.itemDoubleClicked.connect(self.beAddedItemDoubleClicked)
        self.btn_add
        self.btn_cancel.released.connect()

    @pyqtSlot()
    def btnClosedclicked(self):
        self.close()
    @pyqtSlot()
    def btnSaveClicked(self):
        people = []
        exist_f_id = -1
        for i in range(0,self.lv_be_added_family.count()):
            item = self.lv_be_added_family.item(i)
            text = item.text().split(" : ")
            people.append(text)
        for person in people:
            id = person[0]
            f_id = DBConnectSingleton.instance.getInfo(id)["family"]
            if(f_id is not -1):
                exist_f_id = f_id
        if exist_f_id is -1:
            DBConnectSingleton.instance.addFamily()

    @pyqtSlot()
    def btnSearchClicked(self):
        f_name = self.tb_fam_name.text()
        self.lv_search_result.clear()
        people = DBConnectSingleton.instance.getPeopleByName(f_name)
        for i in people:
            self.lv_search_result.addItem(people[i]['id']+" : "+people[i]['last_name']+" : "+people[i]['b_date'])

    @pyqtSlot(QListWidgetItem)
    def searchItemDoubleClicked(self, item: QListWidgetItem):
        text = item.text()
        self.lv_be_added_family.addItem(text)

    @pyqtSlot(QListWidgetItem)
    def beAddedItemDoubleClicked(self, item: QListWidgetItem):
        index = self.lv_be_added_family.indexFromItem(item)
        self.lv_be_added_family.takeItem(index.row())