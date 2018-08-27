# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/edit_group.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditGroup(object):
    def setupUi(self, EditGroup):
        EditGroup.setObjectName("EditGroup")
        EditGroup.resize(511, 432)
        self.centralWidget = QtWidgets.QWidget(EditGroup)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tv_group = QtWidgets.QTableView(self.centralWidget)
        self.tv_group.setObjectName("tv_group")
        self.verticalLayout.addWidget(self.tv_group)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_add_group = QtWidgets.QPushButton(self.frame)
        self.btn_add_group.setObjectName("btn_add_group")
        self.gridLayout_2.addWidget(self.btn_add_group, 0, 0, 1, 1)
        self.btn_remove_group = QtWidgets.QPushButton(self.frame)
        self.btn_remove_group.setObjectName("btn_remove_group")
        self.gridLayout_2.addWidget(self.btn_remove_group, 0, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.frame)
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_2.addWidget(self.btn_cancel, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        EditGroup.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(EditGroup)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 511, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        EditGroup.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(EditGroup)
        QtCore.QMetaObject.connectSlotsByName(EditGroup)

    def retranslateUi(self, EditGroup):
        _translate = QtCore.QCoreApplication.translate
        EditGroup.setWindowTitle(_translate("EditGroup", "Add New Member"))
        self.btn_add_group.setText(_translate("EditGroup", "Add Group"))
        self.btn_remove_group.setText(_translate("EditGroup", "Remove Group"))
        self.btn_cancel.setText(_translate("EditGroup", "Cancel"))
        self.menuMenu.setTitle(_translate("EditGroup", "Menu"))

