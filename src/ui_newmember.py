# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/newmember.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewMember(object):
    def setupUi(self, NewMember):
        NewMember.setObjectName("NewMember")
        NewMember.resize(599, 924)
        self.centralWidget = QtWidgets.QWidget(NewMember)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_photo_view = QtWidgets.QLabel(self.groupBox)
        self.lbl_photo_view.setAutoFillBackground(True)
        self.lbl_photo_view.setText("")
        self.lbl_photo_view.setObjectName("lbl_photo_view")
        self.gridLayout.addWidget(self.lbl_photo_view, 9, 1, 2, 1)
        self.lbl_email = QtWidgets.QLabel(self.groupBox)
        self.lbl_email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_email.setObjectName("lbl_email")
        self.gridLayout.addWidget(self.lbl_email, 7, 3, 1, 1)
        self.tb_email = QtWidgets.QLineEdit(self.groupBox)
        self.tb_email.setObjectName("tb_email")
        self.gridLayout.addWidget(self.tb_email, 7, 4, 1, 1)
        self.lbl_gender = QtWidgets.QLabel(self.groupBox)
        self.lbl_gender.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_gender.setObjectName("lbl_gender")
        self.gridLayout.addWidget(self.lbl_gender, 0, 3, 1, 1)
        self.lbl_last_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_last_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_last_name.setObjectName("lbl_last_name")
        self.gridLayout.addWidget(self.lbl_last_name, 4, 3, 1, 1)
        self.lbl_photo_loc = QtWidgets.QLabel(self.groupBox)
        self.lbl_photo_loc.setMaximumSize(QtCore.QSize(253, 16))
        self.lbl_photo_loc.setScaledContents(True)
        self.lbl_photo_loc.setObjectName("lbl_photo_loc")
        self.gridLayout.addWidget(self.lbl_photo_loc, 9, 3, 1, 2)
        self.lbl_mid_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_mid_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_mid_name.setObjectName("lbl_mid_name")
        self.gridLayout.addWidget(self.lbl_mid_name, 4, 0, 1, 1)
        self.tb_mid_name = QtWidgets.QLineEdit(self.groupBox)
        self.tb_mid_name.setObjectName("tb_mid_name")
        self.gridLayout.addWidget(self.tb_mid_name, 4, 1, 1, 1)
        self.lbl_phone = QtWidgets.QLabel(self.groupBox)
        self.lbl_phone.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_phone.setObjectName("lbl_phone")
        self.gridLayout.addWidget(self.lbl_phone, 7, 0, 1, 1)
        self.btn_sel_photo = QtWidgets.QPushButton(self.groupBox)
        self.btn_sel_photo.setObjectName("btn_sel_photo")
        self.gridLayout.addWidget(self.btn_sel_photo, 10, 4, 1, 1)
        self.tb_first_name = QtWidgets.QLineEdit(self.groupBox)
        self.tb_first_name.setObjectName("tb_first_name")
        self.gridLayout.addWidget(self.tb_first_name, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        self.lbl_first_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_first_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_first_name.setObjectName("lbl_first_name")
        self.gridLayout.addWidget(self.lbl_first_name, 3, 0, 1, 1)
        self.tb_phone = QtWidgets.QLineEdit(self.groupBox)
        self.tb_phone.setObjectName("tb_phone")
        self.gridLayout.addWidget(self.tb_phone, 7, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rb_gender_male = QtWidgets.QRadioButton(self.frame_3)
        self.rb_gender_male.setObjectName("rb_gender_male")
        self.horizontalLayout.addWidget(self.rb_gender_male)
        self.rb_gender_female = QtWidgets.QRadioButton(self.frame_3)
        self.rb_gender_female.setObjectName("rb_gender_female")
        self.horizontalLayout.addWidget(self.rb_gender_female)
        self.gridLayout.addWidget(self.frame_3, 0, 4, 1, 1)
        self.de_dob = QtWidgets.QDateEdit(self.groupBox)
        self.de_dob.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.de_dob.setCalendarPopup(True)
        self.de_dob.setObjectName("de_dob")
        self.gridLayout.addWidget(self.de_dob, 3, 4, 1, 1)
        self.tb_last_name = QtWidgets.QLineEdit(self.groupBox)
        self.tb_last_name.setObjectName("tb_last_name")
        self.gridLayout.addWidget(self.tb_last_name, 4, 4, 1, 1)
        self.tb_kor_name = QtWidgets.QLineEdit(self.groupBox)
        self.tb_kor_name.setObjectName("tb_kor_name")
        self.gridLayout.addWidget(self.tb_kor_name, 0, 1, 1, 1)
        self.lbl_kor_name = QtWidgets.QLabel(self.groupBox)
        self.lbl_kor_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_kor_name.setObjectName("lbl_kor_name")
        self.gridLayout.addWidget(self.lbl_kor_name, 0, 0, 1, 1)
        self.lbl_birthday = QtWidgets.QLabel(self.groupBox)
        self.lbl_birthday.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_birthday.setObjectName("lbl_birthday")
        self.gridLayout.addWidget(self.lbl_birthday, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.tb_address = QtWidgets.QLineEdit(self.groupBox)
        self.tb_address.setObjectName("tb_address")
        self.gridLayout.addWidget(self.tb_address, 8, 1, 1, 4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chk_new_comer_study = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_new_comer_study.setObjectName("chk_new_comer_study")
        self.gridLayout_2.addWidget(self.chk_new_comer_study, 9, 1, 1, 1)
        self.de_reg = QtWidgets.QDateEdit(self.groupBox_2)
        self.de_reg.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.de_reg.setCalendarPopup(True)
        self.de_reg.setObjectName("de_reg")
        self.gridLayout_2.addWidget(self.de_reg, 0, 1, 1, 1)
        self.lbl_baptism_place = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_baptism_place.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_baptism_place.setObjectName("lbl_baptism_place")
        self.gridLayout_2.addWidget(self.lbl_baptism_place, 3, 0, 1, 1)
        self.lbl_baptism_by = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_baptism_by.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_baptism_by.setObjectName("lbl_baptism_by")
        self.gridLayout_2.addWidget(self.lbl_baptism_by, 4, 0, 1, 1)
        self.tb_baptism_place = QtWidgets.QLineEdit(self.groupBox_2)
        self.tb_baptism_place.setObjectName("tb_baptism_place")
        self.gridLayout_2.addWidget(self.tb_baptism_place, 3, 1, 1, 1)
        self.lbl_new_family_study = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_new_family_study.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_new_family_study.setObjectName("lbl_new_family_study")
        self.gridLayout_2.addWidget(self.lbl_new_family_study, 10, 0, 1, 1)
        self.tb_baptism_by = QtWidgets.QLineEdit(self.groupBox_2)
        self.tb_baptism_by.setObjectName("tb_baptism_by")
        self.gridLayout_2.addWidget(self.tb_baptism_by, 4, 1, 1, 1)
        self.btn_show_bible_study = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_show_bible_study.setObjectName("btn_show_bible_study")
        self.gridLayout_2.addWidget(self.btn_show_bible_study, 11, 1, 1, 1)
        self.cb_duty = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_duty.setObjectName("cb_duty")
        self.gridLayout_2.addWidget(self.cb_duty, 5, 1, 1, 1)
        self.lbl_duty = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_duty.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_duty.setObjectName("lbl_duty")
        self.gridLayout_2.addWidget(self.lbl_duty, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 11, 0, 1, 1)
        self.chk_baptism = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_baptism.setObjectName("chk_baptism")
        self.gridLayout_2.addWidget(self.chk_baptism, 1, 1, 1, 1)
        self.lbl_new_comer_study = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_new_comer_study.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_new_comer_study.setObjectName("lbl_new_comer_study")
        self.gridLayout_2.addWidget(self.lbl_new_comer_study, 9, 0, 1, 1)
        self.chk_new_family_study = QtWidgets.QCheckBox(self.groupBox_2)
        self.chk_new_family_study.setObjectName("chk_new_family_study")
        self.gridLayout_2.addWidget(self.chk_new_family_study, 10, 1, 1, 1)
        self.de_bap = QtWidgets.QDateEdit(self.groupBox_2)
        self.de_bap.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.de_bap.setCalendarPopup(True)
        self.de_bap.setObjectName("de_bap")
        self.gridLayout_2.addWidget(self.de_bap, 2, 1, 1, 1)
        self.lbl_register_date = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_register_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_register_date.setObjectName("lbl_register_date")
        self.gridLayout_2.addWidget(self.lbl_register_date, 0, 0, 1, 1)
        self.lbl_baptism_date = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_baptism_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_baptism_date.setObjectName("lbl_baptism_date")
        self.gridLayout_2.addWidget(self.lbl_baptism_date, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.cb_dept = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_dept.setEditable(False)
        self.cb_dept.setObjectName("cb_dept")
        self.gridLayout_2.addWidget(self.cb_dept, 7, 1, 1, 1)
        self.cb_group = QtWidgets.QComboBox(self.groupBox_2)
        self.cb_group.setObjectName("cb_group")
        self.gridLayout_2.addWidget(self.cb_group, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 8, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_show_family = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_show_family.setObjectName("btn_show_family")
        self.verticalLayout_3.addWidget(self.btn_show_family)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_2)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.btn_save = QtWidgets.QPushButton(self.frame_2)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        NewMember.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(NewMember)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 599, 22))
        self.menuBar.setDefaultUp(True)
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        NewMember.setMenuBar(self.menuBar)
        self.actionfiles = QtWidgets.QAction(NewMember)
        self.actionfiles.setObjectName("actionfiles")
        self.actionnew = QtWidgets.QAction(NewMember)
        self.actionnew.setObjectName("actionnew")
        self.actionedit = QtWidgets.QAction(NewMember)
        self.actionedit.setObjectName("actionedit")
        self.menuMenu.addAction(self.actionfiles)
        self.menuMenu.addAction(self.actionnew)
        self.menuMenu.addAction(self.actionedit)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(NewMember)
        QtCore.QMetaObject.connectSlotsByName(NewMember)
        NewMember.setTabOrder(self.tb_kor_name, self.tb_first_name)
        NewMember.setTabOrder(self.tb_first_name, self.tb_mid_name)
        NewMember.setTabOrder(self.tb_mid_name, self.tb_last_name)
        NewMember.setTabOrder(self.tb_last_name, self.tb_phone)
        NewMember.setTabOrder(self.tb_phone, self.tb_email)
        NewMember.setTabOrder(self.tb_email, self.de_dob)
        NewMember.setTabOrder(self.de_dob, self.rb_gender_male)
        NewMember.setTabOrder(self.rb_gender_male, self.rb_gender_female)
        NewMember.setTabOrder(self.rb_gender_female, self.btn_sel_photo)
        NewMember.setTabOrder(self.btn_sel_photo, self.de_reg)
        NewMember.setTabOrder(self.de_reg, self.de_bap)
        NewMember.setTabOrder(self.de_bap, self.tb_baptism_place)
        NewMember.setTabOrder(self.tb_baptism_place, self.tb_baptism_by)
        NewMember.setTabOrder(self.tb_baptism_by, self.cb_duty)
        NewMember.setTabOrder(self.cb_duty, self.chk_new_family_study)
        NewMember.setTabOrder(self.chk_new_family_study, self.chk_new_comer_study)
        NewMember.setTabOrder(self.chk_new_comer_study, self.btn_show_bible_study)
        NewMember.setTabOrder(self.btn_show_bible_study, self.btn_show_family)
        NewMember.setTabOrder(self.btn_show_family, self.btn_cancel)
        NewMember.setTabOrder(self.btn_cancel, self.btn_save)

    def retranslateUi(self, NewMember):
        _translate = QtCore.QCoreApplication.translate
        NewMember.setWindowTitle(_translate("NewMember", "Add New Member"))
        self.groupBox.setTitle(_translate("NewMember", "Personal Information"))
        self.lbl_email.setText(_translate("NewMember", "E-Mail"))
        self.lbl_gender.setText(_translate("NewMember", "Gender"))
        self.lbl_last_name.setText(_translate("NewMember", "Last Name"))
        self.lbl_photo_loc.setText(_translate("NewMember", "Photo Location"))
        self.lbl_mid_name.setText(_translate("NewMember", "Middle Name"))
        self.lbl_phone.setText(_translate("NewMember", " Phone"))
        self.btn_sel_photo.setText(_translate("NewMember", "Select Photo"))
        self.label_2.setText(_translate("NewMember", "Photo"))
        self.lbl_first_name.setText(_translate("NewMember", "First Name"))
        self.rb_gender_male.setText(_translate("NewMember", "Male"))
        self.rb_gender_female.setText(_translate("NewMember", "Female"))
        self.de_dob.setDisplayFormat(_translate("NewMember", "MM/dd/yyyy"))
        self.lbl_kor_name.setText(_translate("NewMember", "Korean Name"))
        self.lbl_birthday.setText(_translate("NewMember", "Date of Birth"))
        self.label_3.setText(_translate("NewMember", "Address"))
        self.groupBox_2.setTitle(_translate("NewMember", "Additional Information"))
        self.chk_new_comer_study.setText(_translate("NewMember", "Completed"))
        self.de_reg.setDisplayFormat(_translate("NewMember", "MM/dd/yyyy"))
        self.lbl_baptism_place.setText(_translate("NewMember", "Baptism Site"))
        self.lbl_baptism_by.setText(_translate("NewMember", "Baptizer"))
        self.lbl_new_family_study.setText(_translate("NewMember", "New Family Study"))
        self.btn_show_bible_study.setText(_translate("NewMember", "Show"))
        self.lbl_duty.setText(_translate("NewMember", "Duty"))
        self.label_12.setText(_translate("NewMember", "Bible Study"))
        self.chk_baptism.setText(_translate("NewMember", "Received"))
        self.lbl_new_comer_study.setText(_translate("NewMember", "Newcomer Study"))
        self.chk_new_family_study.setText(_translate("NewMember", "Completed"))
        self.de_bap.setDisplayFormat(_translate("NewMember", "MM/dd/yyyy"))
        self.lbl_register_date.setText(_translate("NewMember", "Registration Date"))
        self.lbl_baptism_date.setText(_translate("NewMember", "Baptism Date"))
        self.label_4.setText(_translate("NewMember", "Department"))
        self.label_5.setText(_translate("NewMember", "Baptism"))
        self.label.setText(_translate("NewMember", "Group"))
        self.groupBox_3.setTitle(_translate("NewMember", "Family Information"))
        self.btn_show_family.setText(_translate("NewMember", "Show"))
        self.btn_cancel.setText(_translate("NewMember", "Cancel"))
        self.btn_save.setText(_translate("NewMember", "Save"))
        self.menuMenu.setTitle(_translate("NewMember", "Menu"))
        self.actionfiles.setText(_translate("NewMember", "files"))
        self.actionnew.setText(_translate("NewMember", "new"))
        self.actionedit.setText(_translate("NewMember", "edit"))

