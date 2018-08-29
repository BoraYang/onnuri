from PyQt5.QtWidgets import *
from ui_newmember import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap


class NewMember(QMainWindow, Ui_NewMember):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_save.released.connect(self.saveClicked)
        self.btn_show_bible_study.released.connect(self.showClicked)
        self.rb_gender_male.setChecked(True)
        self.de_bap.setDate(QDate.currentDate())
        self.de_dob.setDate(QDate.currentDate())
        self.de_reg.setDate(QDate.currentDate())
        self.btn_sel_photo.released.connect(self.btn_sel_photo_clicked)
        self.photo = None

        for i in self.getDutyListFromDB():
            self.cb_duty.addItem(i)

    def closeEvent(self, event):
        self.myWindowCloseSignal.emit()
        event.accept()

    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def saveClicked(self):
        self.saveToDb()
        print("save button clicked.")

    @pyqtSlot()
    def showClicked(self):
        print("show button clicked.")

    def saveToDb(self):
        first_name = self.tb_first_name.text()
        mid_name = self.tb_mid_name.text()
        last_name = self.tb_last_name.text()
        kor_name = self.tb_kor_name.text()
        if(len(self.tb_phone.text()) is 0):
            phone = ""
        else:
            phone = int(self.tb_phone.text())
        gender = self.getGender()
        email = self.tb_email.text()
        dob = self.de_dob.date().toString()  # birth
        doreg = self.de_reg.date().toString()  # register
        dobap = self.de_bap.date().toString()  # baptism
        biptism_site = self.tb_baptism_place.text()
        biptism_by = self.tb_baptism_by.text()
        duty = self.cb_duty.currentText()
        group = self.cb_group.currentText()
        new_c_s = self.chk_new_comer_study.isChecked()
        new_f_s = self.chk_new_comer_study.isChecked()
        s_john = self.chk_john.isChecked()  # boolean
        s_romans = self.chk_romans.isChecked()  # boolean
        s_timothy = self.chk_timothy.isChecked()  # boolean

        duty_id = self.getDutyId(duty)
        # add to db with no baptism id and get personal id
        p_id = DBConnectSingleton.instance.addPerson(first_name=first_name, last_name=last_name,
                                                     mid_name=mid_name,gender=gender, email=email,
                                                     b_date=dob, r_date=doreg, kor_name=kor_name, phone=phone,
                                                     group=group,duty=duty_id, baptism=-1,
                                                     family=-1, c_study=new_c_s, m_study=new_f_s)
        # add baptism id to db anf get baptism id
        b_id = DBConnectSingleton.instance.addBaptism(input_id=p_id, bap_date=dobap, location=biptism_site,
                                                      admin=biptism_by)
        # update personal information with baptism id
        DBConnectSingleton.instance.updateBaptism(input_id=p_id, baptism_num=b_id)


    @pyqtSlot()
    def btn_sel_photo_clicked(self):
        fileName = QFileDialog.getOpenFileName(self, caption="Select Photo", filter="Image Files (*.png *.jpg *.bmp)")
        if (len(fileName) is not 0):
            print(fileName[0])
        img = QImage(fileName[0])
        h = self.lbl_photo_view.height()
        w = self.lbl_photo_view.width()

        img_h = img.height()
        img_w = img.width()
        if (img_h > img_w):
            scale_factor = h / img_h
            img_h = h
            img_w *= scale_factor
        else:
            scale_factor = w / img_w
            img_w = w
            img_h *= scale_factor
        image = img.scaledToHeight(img_h)
        # img.scaledToWidth(img_w)
        self.lbl_photo_view.setPixmap(QPixmap.fromImage(image))
        arr = fileName[0].split("/")
        index = len(arr) - 1

        self.lbl_photo_loc.setText("" + arr[index])

    # def insertBiptismInfo(self, dobap , biptism_site , biptism_by):
    #     id_ = DBConnectSingleton.instance.insertBiptismInfo(dobap ,biptism_site,biptism_by)
    #     return id_

    def getDutyId(self, duty_str):
        id_ = DBConnectSingleton.instance.getDutyID(duty_str)
        if -1 == id_:
            print("Cannot search Duty ID")
        return id_

    def getGroupId(self, group_str):
        id_ = DBConnectSingleton.instance.getGroupID(group_str)
        if -1 == id_:
            print("Cannot search Group ID")
        return id_

    def getGender(self):
        if (self.rb_gender_male):
            return "Male"
        else:
            return "Female"

    def getDutyListFromDB(self):
        duties = DBConnectSingleton.instance.getDutyName()
        return duties
