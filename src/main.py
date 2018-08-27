import sys
from sign_in import *
from db_connect_singleton import *
from PyQt5 import QtSql
from view_list import *

if __name__ == "__main__":
    app = QApplication(sys.argv)

    db_driver = QtSql.QSqlDatabase.addDatabase('QSQLITE')

    if not db_driver.isValid():
        print("ERROR: Invalid database")

    db_driver.setDatabaseName("../../db/onnuri.db")

    if not db_driver.open():
        print("ERROR: ", db_driver.lastError().text())

    DBConnectSingleton(db_driver)

    mywin =Singin()
    mywin.show()
    app.exec_()



