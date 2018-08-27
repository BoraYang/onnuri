from PyQt5 import QtSql
from PyQt5.Qt import QSqlDatabase

db_driver = QtSql.QSqlDatabase.addDatabase('QSQLITE')

if not db_driver.isValid():
    print ("ERROR: Invalid database")

db = db_driver.setDatabaseName("../db/onnuri.db")

if not db.open():
    print ("ERROR: ", db.lastError().text())

class DBConnectSingleton:
    class __DBConnectSingleton:
        def __init__(self, db):
            self.db = db
        def __str__(self):
            return repr(self) + self.val

        # Get data from Person table
        def getInfo(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT * FROM Person WHERE id = '" + input_id + "';")
            query.exec()
            returnVal = []
            while query.next():
                returnVal.append(query.value(1))
                returnVal.append(query.value(2))
                returnVal.append(query.value(3))
                returnVal.append(query.value(4))
                returnVal.append(query.value(5))
                returnVal.append(query.value(6))
                returnVal.append(query.value(7))
                returnVal.append(query.value(8))
                returnVal.append(query.value(9))
                returnVal.append(query.value(10))
                returnVal.append(query.value(11))
                returnVal.append(query.value(12))
                returnVal.append(query.value(13))
                returnVal.append(query.value(14))
                returnVal.append(query.value(15))
                returnVal.append(query.value(16))
            return returnVal

        # Add data to Person table
        def addPerson(self, first_name, last_name, mid_name, kor_name, gender, b_date, r_date, email, phone, group, duty, baptism, family, c_study, m_study, b_study):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("INSERT INTO Person (first_name, last_name, mid_name, kor_name, gender, b_date, r_date, email, phone, group, duty, baptism, family, c_study, m_study, b_study) VALUES ('" + first_name + ", " + last_name + ", " + mid_name + ", " + kor_name + ", " + gender + ", " + b_date + ", " + r_date + ", " + email + ", " + phone + ", " + group + ", " + duty + ", " + baptism + ", " + family + ", " + c_study + ", " + m_study + ", " + b_study + ");")
            if not query.exec():
                return -1

        # Add data to Baptism Table
        def addBaptism(self, input_id, bap_date, location, admin):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("INSERT INTO Baptism (id, bap_date, location, admin) VALUES (" + input_id + ", " + bap_date + ", " + location + ", " + admin + ");")
            if not query.exec():
                return -1

        # Add data to Family Table
        def addFamily(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("INSERT INTO Family (id) VALUES (NULL);")
            if not query.exec():
                return -1

        # Update Baptism data of Person
        def updateBaptism(self, input_id, baptism_num):
            query = QtSql.QsqlQuery(self.db)
            query.prepare("UPDATE Person SET Baptism ='" + baptism_num + "' WHERE id ='" + input_id + "';")
            if not query.exec():
                return -1

        # Update Family data of Person
        def updateFamily(self, input_id, family_num):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET family = '" + family_num + "' WHERE id = '" + input_id + "';")
            if not query.exec():
                return -1

        # Convert Duty ID into duty name
        def getDutyID(self, input_duty):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT num FROM Duty WHERE name = '" + input_duty + "';")
            query.exec()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Convert Group ID into group name
        def getGroupID(self, input_group):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT num FROM ChurchGroup WHERE name = '" + input_group + "';")
            query.exec()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal


        # Return name list of Duty
        def getDutyName(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT name FROM Duty;")
            query.exec()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Return name list of Department
        def getDepartmentName(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT name FROM Department;")
            query.exec()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # def getFirstName(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT first_name FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getLastName(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT last_name FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getMidName(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT mid_name FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getKorName(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT kor_name FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getGender(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT gender FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getBDate(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT b_date FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getRDate(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT r_date FROM Person WHERE id = '" + input_id + "'")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getEmail(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT email FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getPhone(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT phone FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getGroup(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT group FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     group_id = None
        #     while query.next():
        #         group_id = query.value(0)
        #
        #     query.prepare("SELECT name FROM ChurchGroup WHERE group_num = '" + group_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        # def getDuty(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT duty FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     duty_id = None
        #     while query.next():
        #         duty_id = query.value(0)
        #
        #     query.prepare("SELECT name FROM Duty WHERE num = '" + duty_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal
        #
        #
        # def getBaptism(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT baptism FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     baptism_id = None
        #     while query.next():
        #         baptism_id = query.value(0)
        #
        #     query.prepare("SELECT bap_date, location, admin FROM Baptism WHERE num = '" + baptism_id + "';")
        #     query.exec()
        #     returnVal = []
        #     while query.next():
        #         returnVal.append(query.value(0))
        #         returnVal.append(query.value(1))
        #         returnVal.append(query.value(2))
        #     return returnVal
        #
        # def getFamily(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT family FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     family_id = None
        #     while query.next():
        #         family_id = query.value(0)
        #
        #     query.prepare("SELECT first_name, last_name, kor_name, b_date FROM Person WHERE id = '" + family_id + "';")
        #     query.exec()
        #     sublist = []
        #     returnVal = []
        #     while query.next():
        #         sublist.append(query.value(0))
        #         sublist.append(query.value(1))
        #         sublist.append(query.value(2))
        #         sublist.append(query.value(3))
        #         returnVal.append(sublist)
        #     return returnVal
        #
        # def getCStudy(self, input_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT c_study FROM Person WHERE id = '" + input_id + "';")
        #     query.exec()
        #     returnVal = None
        #     while query.next():
        #         returnVal = query.value(0)
        #     return returnVal

    instance = None
    def __init__(self, db):
        if not DBConnectSingleton.instance:
            DBConnectSingleton.instance = DBConnectSingleton.__DBConnectSingleton(db)
        else:
            DBConnectSingleton.instance.val = db
    def __getattr__(self, name):
        return getattr(self.instance, name)