# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/biblestudywindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BibleStudyWindow(object):
    def setupUi(self, BibleStudyWindow):
        BibleStudyWindow.setObjectName("BibleStudyWindow")
        BibleStudyWindow.resize(267, 329)
        self.centralwidget = QtWidgets.QWidget(BibleStudyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_bible = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_bible.setObjectName("gb_bible")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_bible)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lv_bs_list = QtWidgets.QListWidget(self.gb_bible)
        self.lv_bs_list.setObjectName("lv_bs_list")
        self.verticalLayout_2.addWidget(self.lv_bs_list)
        self.verticalLayout.addWidget(self.gb_bible)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setObjectName("btn_close")
        self.gridLayout.addWidget(self.btn_close, 0, 3, 1, 1)
        self.btn_add = QtWidgets.QPushButton(self.frame)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 0, 0, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        BibleStudyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BibleStudyWindow)
        QtCore.QMetaObject.connectSlotsByName(BibleStudyWindow)
        BibleStudyWindow.setTabOrder(self.lv_bs_list, self.btn_add)
        BibleStudyWindow.setTabOrder(self.btn_add, self.btn_close)

    def retranslateUi(self, BibleStudyWindow):
        _translate = QtCore.QCoreApplication.translate
        BibleStudyWindow.setWindowTitle(_translate("BibleStudyWindow", "Bible Study"))
        self.gb_bible.setTitle(_translate("BibleStudyWindow", "Manage"))
        self.btn_close.setText(_translate("BibleStudyWindow", "Close"))
        self.btn_add.setText(_translate("BibleStudyWindow", "Add"))
        self.btn_save.setText(_translate("BibleStudyWindow", "Save"))

