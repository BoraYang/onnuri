from PyQt5.QtWidgets import *

from add_family import AddFamily
from ui_view_member import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
from BibleStudyWindow import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap


class ViewMember(QMainWindow, Ui_ViewMember):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self,p_id):
        super().__init__()
        self.setupUi(self)
        self.p_id = p_id
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_save.released.connect(self.saveClicked)
        self.btn_show.released.connect(self.showClicked)
        self.tb_eng_name.setText(self.showEngName())
        self.tb_kor_name.setText(DBConnectSingleton.instance.getKorName(self.p_id))
        self.tb_email.setText(DBConnectSingleton.instance.getEmail(self.p_id))
        self.tb_phone.setText(str(DBConnectSingleton.instance.getPhone(self.p_id)))
        self.tb_address.setText(DBConnectSingleton.instance.getPhysicalAddress(self.p_id))
        self.tb_baptism_place.setText(self.showBaptismSite())
        self.tb_baptism_by.setText(self.showBaptizer())
        self.de_dob.setDate(QDate.fromString(DBConnectSingleton.instance.getBDate(self.p_id), "MM/dd/yyyy"))
        self.de_bap.setDate(QDate.fromString(self.showBaptismDate(), "MM/dd/yyyy"))
        self.de_reg.setDate(QDate.fromString(DBConnectSingleton.instance.getRDate(self.p_id), "MM/dd/yyyy"))
        self.cb_duty.addItem(DBConnectSingleton.instance.getDuty(self.p_id))
        new_comer_study = DBConnectSingleton.instance.getCStudy(self.p_id)
        if new_comer_study == 'True':
            self.chk_new_comer_study.setCheckState(QtCore.Qt.Checked)
        else:
            self.chk_new_comer_study.setCheckState(QtCore.Qt.Unchecked)
        new_family_study = DBConnectSingleton.instance.getMStudy(self.p_id)
        if new_family_study == 'True':
            self.chk_new_family_study.setCheckState(QtCore.Qt.Checked)
        else:
            self.chk_new_family_study.setCheckState(QtCore.Qt.Unchecked)
        self.chk_new_comer_study.setEnabled(False)
        self.chk_new_family_study.setEnabled(False)
        self.cb_group.addItem(DBConnectSingleton.instance.getGroup(self.p_id))
        self.cb_dept.addItem(DBConnectSingleton.instance.getDept(self.p_id))
        gender = DBConnectSingleton.instance.getGender(self.p_id)
        if gender == 'Male':
            self.rb_gender_male.setChecked(True)
            self.rb_gender_female.setChecked(False)
        else:
            self.rb_gender_male.setChecked(False)
            self.rb_gender_female.setChecked(True)
        self.rb_gender_male.setEnabled(False)
        self.rb_gender_female.setEnabled(False)
        self.btn_show_bible_study.released.connect(self.bStudyClicked)
        self.showPicture()

    @pyqtSlot()
    def bStudyClicked(self):
        first_name = DBConnectSingleton.instance.getFirstName(self.p_id)
        mid_name = DBConnectSingleton.instance.getMidName(self.p_id)
        last_name = DBConnectSingleton.instance.getLastName(self.p_id)
        name = first_name + " " + mid_name + " " + last_name
        self.ch_window = BibleStudyWindow(name, self.p_id, False)
        self.ch_window.show()

    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def saveClicked(self):
        print("save button clicked.")

    @pyqtSlot()
    def showClicked(self):
        self.family_viwer = AddFamily(self.p_id,self.last_name ,self.first_name ,DBConnectSingleton.instance.getBDate(self.p_id),True)
        self.family_viwer.show()


    def showEngName(self):
        first_name = DBConnectSingleton.instance.getFirstName(self.p_id)
        mid_name = DBConnectSingleton.instance.getMidName(self.p_id)
        last_name = DBConnectSingleton.instance.getLastName(self.p_id)
        self.last_name = last_name
        self.first_name = first_name
        if mid_name == None:
            return first_name + " " + last_name
        else:
            return first_name + " " + mid_name + " " + last_name


    def showBaptismSite(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        if(len(baptism) is 0):
            return ""
        baptismSite = baptism[1]
        return baptismSite

    def showBaptizer(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        if(len(baptism) is 0):
            return ""
        baptizer = baptism[2]
        return baptizer

    def showBaptismDate(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        if(len(baptism) is 0):
            return ""
        baptismDate = baptism[0]
        return baptismDate

    def showPicture(self):
        fileName = DBConnectSingleton.instance.getPicPath(self.p_id)
        if (len(fileName) is not 0):
            print(fileName)
        img = QImage(fileName)
        if(img.height() is 0 or img.width() is 0):
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("File open ERROR")
            msg.exec()
            return
        h = 155
        w = 201

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
        self.lbl_pic_view.setPixmap(QPixmap.fromImage(image))



