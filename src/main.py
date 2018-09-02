import sys

from family_view import FamilyView
from sign_in import *
from db_connect_singleton import *
from PyQt5 import QtSql
from view_list import *
from BibleStudyWindow import *
from home import *
from add_group import *
from view_member import *
from edit_group import *



if __name__ == "__main__":
    app = QApplication(sys.argv)
    db_driver = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    if not db_driver.isValid():
        print("ERROR: Invalid database")
    db_driver.setDatabaseName("../../db/onnuri.db")
    if not db_driver.open():
        print("ERROR: ", db_driver.lastError().text())

    DBConnectSingleton(db_driver)

    # mywin = BibleStudyWindow("youngtak cho",editable=True)
    # mywin = ViewMember(1)
    mywin = EditGroup()
    mywin.show()
    app.exec_()