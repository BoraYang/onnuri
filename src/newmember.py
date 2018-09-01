from PyQt5.QtWidgets import *

from BibleStudyWindow import BibleStudyWindow
from ui_newmember import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtCore import QDate , Qt
from db_connect_singleton import *
from PyQt5.Qt import QImage, QFile, QFileDialog, QPixmap
from person import *
from add_family import *

file_dir = "../../onnuri_photo"


class NewMember(QMainWindow, Ui_NewMember):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.img = None
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_save.released.connect(self.saveClicked)
        self.btn_show_bible_study.released.connect(self.btnBibleStudyShowClicked)
        self.btn_sel_photo.released.connect(self.btn_sel_photo_clicked)
        self.btn_show_family.setEnabled(False)
        self.photo = None

        self.rb_gender_male.setChecked(True)
        self.chk_baptism.stateChanged.connect(self.baptism_enable)

        if not self.chk_baptism.isChecked():
            self.de_bap.setEnabled(False)
            self.tb_baptism_by.setEnabled(False)
            self.tb_baptism_place.setEnabled(False)

        self.de_bap.setDate(QDate.currentDate())
        self.de_dob.setDate(QDate.currentDate())
        self.de_reg.setDate(QDate.currentDate())
        for i in self.getDutyListFromDB():
            self.cb_duty.addItem(i)


        for i in DBConnectSingleton.instance.getGroupList():
            self.cb_group.addItem(i)


        for i in DBConnectSingleton.instance.getDeptName():
            self.cb_dept.addItem(i)
        self.btn_show_bible_study.setEnabled(False)


    def setDuty(self,id_):
        index = 0;
        duty_name = DBConnectSingleton.instance.getDuty(id_)
        for i in self.getDutyListFromDB():
            self.cb_duty.addItem(i)
            if(i != duty_name):
                self.cb_duty.setCurrentIndex(index)
            index +=1

    def setGroup(self,id_):
        index = 0
        group_name = DBConnectSingleton.instance.getGroup(id_)
        for i in DBConnectSingleton.instance.getGroupList():
            self.cb_group.addItem(i)
            if (i != group_name):
                self.cb_group.setCurrentIndex(index)
            index += 1

    def setDept(self,dept_id):
        index = 0
        dept_name = DBConnectSingleton.instance.getDeptName(dept_id)
        for i in DBConnectSingleton.instance.getDeptName():
            self.cb_dept.addItem(i)
            if(dept_name == i):
                self.cb_dept.setCurrentIndex(index)
            index+=1
        self.btn_show_bible_study.setEnabled(False)


    def closeEvent(self, event):
        self.myWindowCloseSignal.emit()
        event.accept()

    @pyqtSlot(int)
    def baptism_enable(self,checked):
        if(checked == Qt.Checked):
            self.de_bap.setEnabled(True)
            self.tb_baptism_by.setEnabled(True)
            self.tb_baptism_place.setEnabled(True)
        else:
            self.de_bap.setEnabled(False)
            self.tb_baptism_by.setEnabled(False)
            self.tb_baptism_place.setEnabled(False)

    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def saveClicked(self):
        self.saveToDb()
        print("save button clicked.")

    @pyqtSlot()
    def btnBibleStudyShowClicked(self):
        pass

    @pyqtSlot()
    def btnFamilyShowClicked(self):
        pass


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
        address =self.tb_address.text()
        email = self.tb_email.text()
        dob = self.de_dob.date().toString("MM/dd/yyyy")  # birth
        doreg = self.de_reg.date().toString("MM/dd/yyyy")  # register
        dobap = ""
        biptism_site =""
        biptism_by = ""
        if(self.chk_baptism.isChecked()):
            dobap = self.de_bap.date().toString("MM/dd/yyyy")  # baptism
            biptism_site = self.tb_baptism_place.text()
            biptism_by = self.tb_baptism_by.text()
        duty = self.cb_duty.currentText()
        group = self.cb_group.currentText()
        group = DBConnectSingleton.instance.getGroupID(group)
        new_c_s = self.chk_new_comer_study.isChecked()
        new_f_s = self.chk_new_comer_study.isChecked()

        dept = self.cb_dept.currentText()
        dept_id = DBConnectSingleton.instance.getDeptID(dept)

        duty_id = self.getDutyId(duty)
        f_name = first_name+mid_name+last_name+str(phone)
        file_path = self.savePhoto(f_name)
        # add to db with no baptism id and get personal id
        p_id = DBConnectSingleton.instance.addPerson(first_name=first_name, last_name=last_name,
                                                     mid_name=mid_name,kor_name=kor_name,
                                                     gender=gender,address=address,
                                                     b_date=dob, r_date=doreg, email = email,phone=phone,
                                                     group=group,department=dept_id,duty=duty_id, baptism=-1,
                                                     family=-1, c_study=new_c_s, m_study=new_f_s , pic_path=file_path)
        if(self.chk_baptism.isChecked()):
            # add baptism id to db anf get baptism id
            b_id = DBConnectSingleton.instance.addBaptism(input_id=p_id, bap_date=dobap, location=biptism_site,
                                                          admin=biptism_by)
            # update personal information with baptism id
            DBConnectSingleton.instance.updateBaptism(input_id=p_id, baptism_num=b_id)




    def savePhoto(self,name):
        if(self.img is not None):
            self.img = self.img.scaled(600,600 , Qt.KeepAspectRatio)
            self.img.save(file_dir+"/"+name+".png")
            return ""+file_dir+"/"+name+".png"
        else:
            return "None"

    def setPhototoView(self,img):
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


    @pyqtSlot()
    def btn_sel_photo_clicked(self):
        fileName = QFileDialog.getOpenFileName(self, caption="Select Photo", filter="Image Files (*.png *.jpg *.bmp)")
        if (len(fileName) is not 0):
            print(fileName[0])
        self.file_path = fileName[0]
        img = QImage(fileName[0])
        self.img = img.copy()

        self.setPhototoView(img)
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


class EditMember(QMainWindow, Ui_NewMember):
    myWindowCloseSignal = pyqtSignal()

    def __init__(self, p_id):
        super().__init__()
        self.setupUi(self)
        self.p_id = p_id
        self.bapsite = False
        self.btn_cancel.released.connect(self.closeClicked)
        self.btn_save.released.connect(self.saveClicked)
        # self.btn_show.released.connect(self.showClicked)
        self.tb_first_name.setText(DBConnectSingleton.instance.getFirstName(self.p_id))
        self.tb_mid_name.setText(DBConnectSingleton.instance.getMidName(self.p_id))
        self.tb_last_name.setText(DBConnectSingleton.instance.getLastName(self.p_id))
        self.btn_sel_photo.released.connect(self.btn_sel_photo_clicked)

        self.tb_kor_name.setText(DBConnectSingleton.instance.getKorName(self.p_id))
        self.tb_email.setText(DBConnectSingleton.instance.getEmail(self.p_id))
        self.tb_phone.setText(str(DBConnectSingleton.instance.getPhone(self.p_id)))
        self.tb_address.setText(DBConnectSingleton.instance.getPhysicalAddress(self.p_id))
        self.tb_baptism_place.setText(self.showBaptismSite)
        self.tb_baptism_by.setText(self.showBaptizer())
        self.de_dob.setDate(QDate.fromString(DBConnectSingleton.instance.getBDate(self.p_id), "MM/dd/yyyy"))
        if len(self.tb_baptism_place.text()) is not 0:
            self.no_baptism = False
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

        self.cb_group.addItem(DBConnectSingleton.instance.getGroup(self.p_id))
        self.cb_dept.addItem(DBConnectSingleton.instance.getDept(self.p_id))
        gender = DBConnectSingleton.instance.getGender(self.p_id)
        if gender == 'Male':
            self.rb_gender_male.setChecked(True)
            self.rb_gender_female.setChecked(False)
        else:
            self.rb_gender_male.setChecked(False)
            self.rb_gender_female.setChecked(True)
        self.btn_show_bible_study.released.connect(self.bStudyClicked)
        self.showPicture()
        self.btn_show_family.released.connect(self.btnFamilyEditClicked)

    @pyqtSlot()
    def btnFamilyEditClicked(self):
        self.fmaily_window = AddFamily()
        self.fmaily_window.show()

    @property
    def showBaptismSite(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        if (len(baptism) is 0):
            return ""
        baptismSite = baptism[1]
        return baptismSite

    def showBaptizer(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        if (len(baptism) is 0):
            return ""
        baptizer = baptism[2]
        return baptizer

    def showBaptismDate(self):
        baptism = DBConnectSingleton.instance.getBaptism(self.p_id)
        if (len(baptism) is 0):
            return ""
        self.chk_baptism.setChecked(True)
        baptismDate = baptism[0]
        return baptismDate

    def showPicture(self):
        fileName = DBConnectSingleton.instance.getPicPath(self.p_id)
        self.lbl_photo_loc.setText(fileName)
        if (len(fileName) is not 0):
            print(fileName)
        img = QImage(fileName)
        if(img.width() is 0 or img.height() is 0):
            msgBox = QMessageBox()
            msgBox.setText("The file is not exist.");
            msgBox.exec();
            return
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
        self.lbl_photo_view.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot()
    def bStudyClicked(self):
        first_name = DBConnectSingleton.instance.getFirstName(self.p_id)
        mid_name = DBConnectSingleton.instance.getMidName(self.p_id)
        last_name = DBConnectSingleton.instance.getLastName(self.p_id)
        name = first_name + " " + mid_name + " " + last_name
        self.ch_window = BibleStudyWindow(name, self.p_id, True)
        self.ch_window.show()

    def setPhototoView(self,img):
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


    @pyqtSlot()
    def btn_sel_photo_clicked(self):
        fileName = QFileDialog.getOpenFileName(self, caption="Select Photo", filter="Image Files (*.png *.jpg *.bmp)")
        if (len(fileName) is not 0):
            print(fileName[0])
        self.file_path = fileName[0]
        img = QImage(fileName[0])
        self.img = img.copy()
        self.setPhototoView(img)
        arr = fileName[0].split("/")
        index = len(arr) - 1
        self.lbl_photo_loc.setText(file_dir+"/"+arr[index])

    def update_info(self):
        pass
        # DBConnectSingleton.instance
    @pyqtSlot()
    def closeClicked(self):
        self.close()

    @pyqtSlot()
    def saveClicked(self):
        DBConnectSingleton.instance.updateFirstName(self.p_id, self.tb_first_name.text())
        DBConnectSingleton.instance.updateMidName(self.p_id, self.tb_mid_name.text())
        DBConnectSingleton.instance.updateLastName(self.p_id, self.tb_last_name.text())
        DBConnectSingleton.instance.updateKorName(self.p_id,self.tb_kor_name.text())
        DBConnectSingleton.instance.updateBDate(self.p_id, self.de_dob.date().toString("MM/dd/yyyy"))
        DBConnectSingleton.instance.updateGender(self.p_id,self.getGender())
        DBConnectSingleton.instance.updateEmail(self.p_id,self.tb_email.text())
        DBConnectSingleton.instance.updatePhone(self.p_id,self.tb_phone.text())
        DBConnectSingleton.instance.updatePhysicalAddress(self.p_id,self.tb_address.text())

        DBConnectSingleton.instance.updateBDate(self.p_id, self.de_dob.date().toString("MM/dd/yyyy"))

        if(len(self.lbl_photo_loc.text()) is not 0):
            DBConnectSingleton.instance.updatePath(self.p_id,self.lbl_photo_loc.text())
        DBConnectSingleton.instance.updateBDate(self.p_id, self.de_dob.date().toString("MM/dd/yyyy"))

        dept = DBConnectSingleton.instance.getDeptID(self.cb_dept.currentText())
        DBConnectSingleton.instance.updateDept(self.p_id,dept)
        if(self.no_baptism):

            if (len(self.tb_baptism_place.text()) is not 0):
                dobap = self.de_dob.date().toString("MM/dd/yyyy")
                biptism_site = self.tb_baptism_place.text()
                biptism_by = self.tb_baptism_by
                b_id = DBConnectSingleton.instance.addBaptism(input_id=self.p_id, bap_date=dobap, location=biptism_site,
                                                              admin=biptism_by)
                # update personal information with baptism id
                DBConnectSingleton.instance.updateBaptism(input_id=self.p_id, baptism_num=b_id)
        else:
            DBConnectSingleton.instance.updateBapAdmin(self.p_id,self.tb_baptism_by.text())
            DBConnectSingleton.instance.updateBapLocation(self.p_id, self.tb_baptism_by.text())
            DBConnectSingleton.instance.updateBapDate(self.p_id, self.de_bap.date().toString("MM/dd/yyyy"))

        duty_id = DBConnectSingleton.instance.getDutyID(self.cb_duty.currentText())
        DBConnectSingleton.instance.updateDuty(self.p_id, duty_id)

        dept_id = DBConnectSingleton.instance.getDeptID(self.cb_dept.currentText())
        DBConnectSingleton.instance.updateDept(self.p_id, dept_id)

        group_id = DBConnectSingleton.instance.getGroupID(self.cb_group.currentText())
        DBConnectSingleton.instance.updateGroup(self.p_id, group_id)
        3
        new_c_s = self.chk_new_comer_study.isChecked()
        new_f_s = self.chk_new_comer_study.isChecked()
        DBConnectSingleton.instance.updateCStudy(self.p_id, new_c_s)
        DBConnectSingleton.instance.updateMStudy(self.p_id, new_f_s)


    def getGender(self):
        if (self.rb_gender_male):
            return "Male"
        else:
            return "Female"