import sys
from PyQt5.QtWidgets import *
from ui_newmember import *
from newmember import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = NewMember()
    mywin.show()
    app.exec_()
