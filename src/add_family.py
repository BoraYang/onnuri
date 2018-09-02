from PyQt5.QtCore import *
from ui_add_family import *
from PyQt5.QtWidgets import *
from db_connect_singleton import *

class AddFamily(QMainWindow,Ui_AddFamily):

    def __init__(self,id_ = -1 ,last_name="" , first_name = "",b_date="",show = False):
        super().__init__()
        self.setupUi(self)
        if(not show):
            self.btn_search.released.connect(self.btnSearchClicked)
            self.lv_search_result.itemDoubleClicked.connect(self.searchItemDoubleClicked)
            self.lv_be_added_family.itemDoubleClicked.connect(self.beAddedItemDoubleClicked)
            self.btn_add.released.connect(self.btnSaveClicked)
        else:
            self.btn_search.setEnabled(False)
            self.btn_add.setEnabled(False)
            self.groupBox_2.setTitle("Family Member")
        self.btn_cancel.released.connect(self.btnClosedclicked)
        if id_ is not -1:
            self.lv_be_added_family.addItem(str(id_) + " : " + first_name +", "+last_name+ " : " + b_date)
            f_id = DBConnectSingleton.instance.getFamily(id_)
            if(f_id is not -1):
                people_ids = DBConnectSingleton.instance.getFamilyMembers(f_id)
                for i in people_ids:
                    if(id_ is i):
                        continue
                    person = DBConnectSingleton.instance.getInfo(i)
                    self.lv_be_added_family.addItem(
                        str(person['id']) + " : " + person['first_name'] + ", " + person[
                            'last_name'] + " : " + str(person['b_date']))


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
            exist_f_id = DBConnectSingleton.instance.getHighestFamilyID()
        for person in people:
            DBConnectSingleton.instance.updateFamily(person[0],exist_f_id)



    @pyqtSlot()
    def btnSearchClicked(self):
        l_name = self.tb_fam_name.text()
        self.lv_search_result.clear()
        people = DBConnectSingleton.instance.getPeopleByName(l_name)
        for i in people:
            self.lv_search_result.addItem(str(people[i]['id'])+" : "+people[i]['first_name']+", "+people[i]['last_name']+" : "+str(people[i]['b_date']))

    @pyqtSlot(QListWidgetItem)
    def searchItemDoubleClicked(self, item: QListWidgetItem):
        text = item.text()
        self.lv_be_added_family.addItem(text)

    @pyqtSlot(QListWidgetItem)
    def beAddedItemDoubleClicked(self, item: QListWidgetItem):
        index = self.lv_be_added_family.indexFromItem(item)
        self.lv_be_added_family.takeItem(index.row())
        text = item.text().split(" : ")
        p_id = text[0]
        DBConnectSingleton.instance.updateFamily(p_id,-1)
