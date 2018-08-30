# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/view_dept.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ViewDept(object):
    def setupUi(self, ViewDept):
        ViewDept.setObjectName("ViewDept")
        ViewDept.resize(402, 521)
        self.centralWidget = QtWidgets.QWidget(ViewDept)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cb_dept_name = QtWidgets.QComboBox(self.frame)
        self.cb_dept_name.setObjectName("cb_dept_name")
        self.gridLayout.addWidget(self.cb_dept_name, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.tv_list = QtWidgets.QTableView(self.centralWidget)
        self.tv_list.setObjectName("tv_list")
        self.verticalLayout.addWidget(self.tv_list)
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_go_back = QtWidgets.QPushButton(self.frame_2)
        self.btn_go_back.setObjectName("btn_go_back")
        self.gridLayout_2.addWidget(self.btn_go_back, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        ViewDept.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(ViewDept)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 402, 22))
        self.menuBar.setDefaultUp(True)
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        ViewDept.setMenuBar(self.menuBar)
        self.actionfiles = QtWidgets.QAction(ViewDept)
        self.actionfiles.setObjectName("actionfiles")
        self.actionnew = QtWidgets.QAction(ViewDept)
        self.actionnew.setObjectName("actionnew")
        self.actionedit = QtWidgets.QAction(ViewDept)
        self.actionedit.setObjectName("actionedit")
        self.menuMenu.addAction(self.actionfiles)
        self.menuMenu.addAction(self.actionnew)
        self.menuMenu.addAction(self.actionedit)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(ViewDept)
        QtCore.QMetaObject.connectSlotsByName(ViewDept)

    def retranslateUi(self, ViewDept):
        _translate = QtCore.QCoreApplication.translate
        ViewDept.setWindowTitle(_translate("ViewDept", "Add New Member"))
        self.label.setText(_translate("ViewDept", "Department Name"))
        self.btn_go_back.setText(_translate("ViewDept", "Go Back"))
        self.menuMenu.setTitle(_translate("ViewDept", "Menu"))
        self.actionfiles.setText(_translate("ViewDept", "files"))
        self.actionnew.setText(_translate("ViewDept", "new"))
        self.actionedit.setText(_translate("ViewDept", "edit"))

