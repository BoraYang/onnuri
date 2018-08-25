import sys
from PyQt5.QtWidgets import *
from ui_newmember import *
from sign_in import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = Singin()
    mywin.show()
    app.exec_()
