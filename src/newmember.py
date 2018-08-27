from PyQt5.QtWidgets import *
from ui_newmember import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QDate


class NewMember(QMainWindow, Ui_NewMember):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_save.released.connect(self.saveClicked)
        self.btn_show.released.connect(self.showClicked)
        self.tb_kor_name.setReadOnly(False)
        self.rb_gender_male.setChecked(True)
        self.de_bap.setDate(QDate.currentDate())
        self.de_dob.setDate(QDate.currentDate())
        self.de_reg.setDate(QDate.currentDate())
        for i in self.getDutyListFromDB():
            self.cb_duty.addItem(i)


    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def saveClicked(self):
        print("save button clicked.")

    @pyqtSlot()
    def showClicked(self):
        self.person()
        print("show button clicked.")

    def person(self):
        first_name = self.tb_first_name.text()
        mid_name = self.tb_mid_name.text()
        last_name = self.tb_last_name.text()
        kor_name = self.tb_kor_name.text()
        phone = self.tb_phone.text()
        gender =self.getGender()
        email = self.tb_email.text()
        dob = self.de_dob.date().toString()  # birth
        doreg = self.de_reg.date().toString()  # register
        dobap = self.de_bap.date().toString() # baptism
        biptism_site = self.tb_baptism_place.text()
        biptism_by = self.tb_baptism_by.text()
        duty = self.cb_duty.currentText()
        new_c_s = self.chk_new_comer_study.isChecked()
        new_f_s = self.chk_new_comer_study.isChecked()
        s_john = self.chk_john.isChecked() #boolean
        s_romans = self.chk_romans.isChecked() #boolean
        s_timothy = self.chk_timothy.isChecked() #boolean


    def getGender(self):
        if(self.rb_gender_male):
            return "male"
        else:
            return "female"

    def getDutyListFromDB(self):
        duties = ("목사","전도사","평신도")
        return duties
