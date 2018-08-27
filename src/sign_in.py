from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from ui_sign_in import Ui_SignIn
from db_connect_singleton import *
from newmember import *
import re


class Singin(QMainWindow,Ui_SignIn):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_cancel.released.connect(self.cancelClicked)
        self.btn_sign_in.released.connect(self.signinClicked)
        self.tb_password.textChanged.connect(self.chkpasswd)
        self.tb_password.setEchoMode(QLineEdit.Password)
        self.regex = re.compile("""^[A-Za-z0-9_!@#$%^&*-]{6,18}$""")
        self.btn_sign_in.setEnabled(False)


    @pyqtSlot(str)
    def chkpasswd(self,passwd):
        print(passwd)
        if not self.regex.match(passwd):
            self.btn_sign_in.setEnabled(False)
        else:
            self.btn_sign_in.setEnabled(True)

    @pyqtSlot()
    def cancelClicked(self):
        self.close()

    @pyqtSlot()
    def signinClicked(self):
        id_str = self.tb_id.text()
        pass_str = self.tb_password.text()
        ischeck = DBConnectSingleton.instance.verifyIdAndPasswd(id_str, pass_str)
        self.window = None
        if ischeck == 1 or ischeck == 0: # for Test
        # if ischeck == 1 # for release
            self.window = NewMember()
            self.window.show()
            self.close()
            print("log in")
        elif ischeck == 0:
            print("log fail")
        elif ischeck == -1:
            print("DB ERROR")
