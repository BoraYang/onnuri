# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/family_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FamilyView(object):
    def setupUi(self, FamilyView):
        FamilyView.setObjectName("FamilyView")
        FamilyView.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(FamilyView)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.btnclose = QtWidgets.QPushButton(self.centralwidget)
        self.btnclose.setObjectName("btnclose")
        self.verticalLayout.addWidget(self.btnclose)
        FamilyView.setCentralWidget(self.centralwidget)

        self.retranslateUi(FamilyView)
        QtCore.QMetaObject.connectSlotsByName(FamilyView)

    def retranslateUi(self, FamilyView):
        _translate = QtCore.QCoreApplication.translate
        FamilyView.setWindowTitle(_translate("FamilyView", "MainWindow"))
        self.btnclose.setText(_translate("FamilyView", "Close"))

