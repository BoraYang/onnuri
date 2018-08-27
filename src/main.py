import sys
from sign_in import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = Singin()
    mywin.show()
    app.exec_()
