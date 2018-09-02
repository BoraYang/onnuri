# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/home.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Home(object):
    def setupUi(self, Home):
        Home.setObjectName("Home")
        Home.resize(701, 469)
        self.centralWidget = QtWidgets.QWidget(Home)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.homeFrame = QtWidgets.QFrame(self.centralWidget)
        self.homeFrame.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.homeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homeFrame.setObjectName("homeFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.homeFrame)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_bible_study = QtWidgets.QPushButton(self.homeFrame)
        self.btn_bible_study.setObjectName("btn_bible_study")
        self.gridLayout.addWidget(self.btn_bible_study, 1, 1, 1, 1)
        self.btn_quit = QtWidgets.QPushButton(self.homeFrame)
        self.btn_quit.setObjectName("btn_quit")
        self.gridLayout.addWidget(self.btn_quit, 4, 1, 1, 1)
        self.btn_group = QtWidgets.QPushButton(self.homeFrame)
        self.btn_group.setObjectName("btn_group")
        self.gridLayout.addWidget(self.btn_group, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.btn_member = QtWidgets.QPushButton(self.homeFrame)
        self.btn_member.setObjectName("btn_member")
        self.gridLayout.addWidget(self.btn_member, 0, 1, 1, 1)
        self.btn_department = QtWidgets.QPushButton(self.homeFrame)
        self.btn_department.setObjectName("btn_department")
        self.gridLayout.addWidget(self.btn_department, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.homeFrame)
        Home.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Home)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 701, 22))
        self.menuBar.setDefaultUp(True)
        self.menuBar.setObjectName("menuBar")
        self.menuMenu = QtWidgets.QMenu(self.menuBar)
        self.menuMenu.setObjectName("menuMenu")
        Home.setMenuBar(self.menuBar)
        self.actionfiles = QtWidgets.QAction(Home)
        self.actionfiles.setObjectName("actionfiles")
        self.actionnew = QtWidgets.QAction(Home)
        self.actionnew.setObjectName("actionnew")
        self.actionedit = QtWidgets.QAction(Home)
        self.actionedit.setObjectName("actionedit")
        self.menuMenu.addAction(self.actionfiles)
        self.menuMenu.addAction(self.actionnew)
        self.menuMenu.addAction(self.actionedit)
        self.menuBar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        _translate = QtCore.QCoreApplication.translate
        Home.setWindowTitle(_translate("Home", "Onnuri All Nations Baptist Church Register"))
        self.btn_bible_study.setText(_translate("Home", "Bible Study"))
        self.btn_quit.setText(_translate("Home", "Quit"))
        self.btn_group.setText(_translate("Home", "Group"))
        self.btn_member.setText(_translate("Home", "Member"))
        self.btn_department.setText(_translate("Home", "Department"))
        self.menuMenu.setTitle(_translate("Home", "Menu"))
        self.actionfiles.setText(_translate("Home", "files"))
        self.actionnew.setText(_translate("Home", "new"))
        self.actionedit.setText(_translate("Home", "edit"))

