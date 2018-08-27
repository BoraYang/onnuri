import sys
from sign_in import *
from DBSingleton import *
from PyQt5 import QtSql
from view_list import *
if __name__ == "__main__":
    app = QApplication(sys.argv)

    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('../../db/onnuri.db')
    db.open()

    OnlyOne(db)

    mywin =ViewList()
    mywin.show()
    app.exec_()



