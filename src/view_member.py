from PyQt5.QtWidgets import *
from ui_view_member import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate
from db_connect_singleton import *
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
        self.tb_kor_name.setText(DBConnectSingleton.instance.getKorname(self.p_id))
        self.tb_email.setText(DBConnectSingleton.instance.getEmail(self.p_id))
        self.tb_phone.setText(DBConnectSingleton.instance.getPhone(self.p_id))
        self.tb_baptism_place.setText(self.showBaptismSite())
        self.tb_baptism_by.setText(self.showBaptizer())
        self.de_dob.setDate(DBConnectSingleton.instance.getBDate(self.p_id))
        self.de_bap.setDate(self.showBaptismDate())
        self.de_reg.setDate(DBConnectSingleton.instance.getRDate(self.p_id))
        self.cb_duty.setCurrentText(DBConnectSingleton.instance.getDuty(self.p_id))
        self.chk_new_comer_study.setCheckState(QtCore.Qt.Checked)
        self.chk_new_family_study.setCheckState(QtCore.Qt.Checked)
        self.lbl_group_info.setText(DBConnectSingleton.instance.getGroup(self.p_id))
        self.rb_gender_male.setChecked(QtCore.Qt.Checked)
        self.rb_gender_female.setChecked(QtCore.Qt.Checked)
        #self.gv_pic.set

    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def saveClicked(self):
        print("save button clicked.")

    @pyqtSlot()
    def showClicked(self):
        print("show button clicked.")

    @pyqtSlot()
    def showEngName(self):
        first_name = DBConnectSingleton.instance.getFirstName(self.p_id)
        mid_name = DBConnectSingleton.instance.getMidName(self.p_id)
        last_name = DBConnectSingleton.instance.getLastName(self.p_id)
        if mid_name == None:
            return first_name + " " + last_name
        else:
            return first_name + " " + mid_name + " " + last_name

    @pyqtSlot()
    def showBaptismSite(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        baptismSite = baptism[3]
        return baptismSite

    @pyqtSlot()
    def showBaptizer(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        baptizer = baptism[4]
        return baptizer

    @pyqtSlot()
    def showBaptismDate(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        baptismDate = baptism[2]
        return baptismDate

    @pyqtSlot()
    def showPicture(self):
        fileName = DBConnectSingleton.instance.getPicPath(self.p_id)
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
        imag = img.scaledToHeight(img_h)
        # img.scaledToWidth(img_w)
        self.lbl_photo_view.setPixmap(QPixmap.fromImage(imag))


