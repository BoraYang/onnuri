# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/sign_in.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignIn(object):
    def setupUi(self, SignIn):
        SignIn.setObjectName("SignIn")
        SignIn.resize(314, 198)
        self.centralWidget = QtWidgets.QWidget(SignIn)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frm_sign_in = QtWidgets.QFrame(self.centralWidget)
        self.frm_sign_in.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frm_sign_in.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_sign_in.setObjectName("frm_sign_in")
        self.gridLayout = QtWidgets.QGridLayout(self.frm_sign_in)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_id = QtWidgets.QLabel(self.frm_sign_in)
        self.lbl_id.setObjectName("lbl_id")
        self.gridLayout.addWidget(self.lbl_id, 0, 0, 1, 1)
        self.tb_password = QtWidgets.QLineEdit(self.frm_sign_in)
        self.tb_password.setObjectName("tb_password")
        self.gridLayout.addWidget(self.tb_password, 1, 1, 1, 1)
        self.tb_id = QtWidgets.QLineEdit(self.frm_sign_in)
        self.tb_id.setObjectName("tb_id")
        self.gridLayout.addWidget(self.tb_id, 0, 1, 1, 1)
        self.lbl_password = QtWidgets.QLabel(self.frm_sign_in)
        self.lbl_password.setObjectName("lbl_password")
        self.gridLayout.addWidget(self.lbl_password, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frm_sign_in)
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_cancel = QtWidgets.QPushButton(self.frame_2)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_sign_in = QtWidgets.QPushButton(self.frame_2)
        self.btn_sign_in.setObjectName("btn_sign_in")
        self.horizontalLayout.addWidget(self.btn_sign_in)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        SignIn.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(SignIn)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 314, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        SignIn.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(SignIn)
        QtCore.QMetaObject.connectSlotsByName(SignIn)

    def retranslateUi(self, SignIn):
        _translate = QtCore.QCoreApplication.translate
        SignIn.setWindowTitle(_translate("SignIn", "Add New Member"))
        self.lbl_id.setText(_translate("SignIn", "ID"))
        self.lbl_password.setText(_translate("SignIn", "Password"))
        self.btn_cancel.setText(_translate("SignIn", "Cancel"))
        self.btn_sign_in.setText(_translate("SignIn", "Sign in"))
        self.menuMenu.setTitle(_translate("SignIn", "Menu"))

