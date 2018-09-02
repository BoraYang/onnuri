from PyQt5 import QtSql
from PyQt5.Qt import QSqlDatabase

class DBConnectSingleton:
    class __DBConnectSingleton:
        def __init__(self, db):
            self.db = db
        def __str__(self):
            return repr(self) + self.val

        def getDB(self):
            return self.db

        # Get data from Person table
        def getInfo(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT * FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec()
            returnVal = {}
            while query.next():
                row = query.record()
                for i in range(0,row.count()):
                    returnVal[row.fieldName(i)] = row.value(i)
            return returnVal

        # Get data from Person table
        def getPeopleByName(self, p_name):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT * FROM Person WHERE last_name = '" + str(p_name) + "';")
            query.exec()
            index = 0
            people = {}
            while query.next():
                row = query.record()
                returnVal = {}
                for i in range(0,row.count()):
                    returnVal[row.fieldName(i)] = row.value(i)
                people[index] = returnVal
                index +=1
            return people

        def verifyIdAndPasswd(self, id_, passwd):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("select password from User where id == '" + str(id_) + "'")
            if not query.exec_():
                return -1
            while query.next():
                passwd_db = query.value(0)
                if passwd_db == passwd:
                    return 1
                else:
                    return 0

        # Add data to Person table
        def addPerson(self, first_name="", last_name="", mid_name="", kor_name="", gender="", address="", b_date="",
                      r_date="",email="", phone="", group=-1,department=-1,duty = -1, baptism = -1, family = -1,
                      c_study = "", m_study = "", pic_path = ""):
            query = QtSql.QSqlQuery(self.db)
            query.prepare(
                "INSERT INTO Person " +
                "(first_name, last_name, mid_name, kor_name, gender, physical_address, b_date, r_date, email, phone, church_group, department, duty, baptism, family, c_study, m_study, picture_path) VALUES ('" + first_name + "', '" + last_name + "', '" + mid_name + "', '" + kor_name + "', '" + str(
                    gender) + "', '" + address + "', '" + b_date + "', '" + r_date + "', '" + email + "', '" + str(
                    phone) + "', '" + str(
                    group) + "', '" + str(department) + "', '" + str(duty) + "', '" + str(baptism) + "', '" + str(
                    family) + "', '" + str(c_study) + "', '" + str(m_study) + "', '" + str(pic_path) + "');")
            print(
                "INSERT INTO Person " +
                "(first_name, last_name, mid_name, kor_name, gender, physical_address, b_date, r_date, email, phone, church_group, department, duty, baptism, family, c_study, m_study, picture_path) VALUES ('" + first_name + "', '" + last_name + "', '" + mid_name + "', '" + kor_name + "', '" + str(
                    gender) + "', '" + address + "', '" + b_date + "', '" + r_date + "', '" + email + "', '" + str(
                    phone) + "', '" + str(
                    group) + "', '" + str(department) + "', '" + str(duty) + "', '" + str(baptism) + "', '" + str(
                    family) + "', '" + str(c_study) + "', '" + str(m_study) +"', '"+ str(pic_path) + "');")

            if not query.exec_():
                return -1
            query.clear()
            query.prepare(
                "select id from Person where first_name ='" + first_name + "' AND last_name ='" + last_name + "' AND mid_name = '" + mid_name + "'")
            if not query.exec_():
                return -1
            p_id = -1
            while query.next():
                p_id = query.value(0)
            return p_id

        # Add data to Baptism Table
        def addBaptism(self, input_id, bap_date, location, admin):
            query = QtSql.QSqlQuery(self.db)
            query.prepare(
                "INSERT INTO Baptism (id, bap_date, location, admin) VALUES ("+"'" +str(input_id)+"'"+ ", '"+str(
                    bap_date) + "', '"+location +"', '" + admin + "');")
            if not query.exec_():
                return -1
            query.clear()
            query.prepare("SELECT num FROM Baptism WHERE id = '" + str(input_id) + "'")
            if not query.exec_():
                return -1
            b_id = -1
            while query.next():
                b_id = query.value(0)
            return b_id

        # Add data to Group Table
        def addGroup(self, g_name, g_leader):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("INSERT INTO ChurchGroup (name, leader) VALUES ('" + g_name + "', " + g_leader + ")")
            if not query.exec_():
                return -1

        # Add data to Family Table
        def addFamily(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("INSERT INTO Family (id) VALUES (NULL);")
            if not query.exec_():
                return -1

        # Add physical address to Person table
        def addPhysicalAddress(self, input_id, physical_address):
            query = QtSql.QSqlQuery(self.db)
            query.prepare(
                "INSERT INTO Person (physical_address) VALUES ('" + str(physical_address) + "') WHERE id = '" + str(
                    input_id) + "';")
            if not query.exec_():
                return -1

        # Update first name for the given Person ID
        def updateFirstName(self, input_id, f_name):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET first_name = '" + f_name + "' WHERE id = " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update mid name for the given Person ID
        def updateMidName(self, input_id, m_name):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET mid_name = '" + m_name + "' WHERE id = " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update last name for the given Person ID
        def updateLastName(self, input_id, l_name):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET last_name = '" + l_name + "' WHERE id = " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update Korean name for the given Person ID
        def updateKorName(self, input_id, kor_name):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET kor_name = '" + kor_name + "' WHERE id = " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update gender for the given Person ID
        def updateGender(self, input_id, gender):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET gender = '" + gender + "' WHERE id = " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update address for the given Person ID
        def updatePhysicalAddress(self, input_id, address):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET physical_address = '" + address + "' WHERE id = " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update birthday for the given Person ID
        def updateBDate(self, input_id, birthday):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET b_date = '" + birthday + "' WHERE id = " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update registration date for the given Person ID
        def updateRDate(self, input_id, r_date):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET r_date = '" + r_date + "' WHERE id =" + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update email address for the given Person ID
        def updateEmail(self, input_id, e_mail):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET email = '" + e_mail + "' WHERE id =" + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update phone number for the given Person ID
        def updatePhone(self, input_id, num):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET phone = '" + str(num) + "' WHERE id =" + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update church group for the given Person ID
        def updateGroup(self, input_id, g_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET church_group = '" + str(g_id) + "' WHERE id =" + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update department for the given Person ID
        def updateDept(self, input_id, d_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET department = '" + str(d_id) + "' WHERE id =" + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update Duty for the given Person ID
        def updateDuty(self, input_id, d_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET duty = '" + str(d_id) + "' WHERE id =" + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update Newcomer study status for the given Person ID
        def updateCStudy(self, input_id, status):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET c_study = '" + str(status) + "' WHERE id =" + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update New Family study status for the given Person ID
        def updateMStudy(self, input_id, status):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET m_study = '" + str(status) + "' WHERE id =" + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update Baptism data of Person
        def updateBaptism(self, input_id, baptism_num):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET baptism = '" + str(baptism_num) + "' WHERE id ='" + str(input_id) + "';")
            if not query.exec_():
                return -1

        # Update Baptism location for the given Person ID
        def updateBapLocation(self, b_id, b_location):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Baptism SET location = '" + b_location + "' WHERE id ='" + str(b_id) + "';")
            if not query.exec_():
                return -1

        # Update Baptism date for the given Person ID
        def updateBapDate(self, b_id, b_date):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Baptism SET bap_date = '" + b_date + "' WHERE id ='" + str(b_id) + "';")
            if not query.exec_():
                return -1

        # Update Baptism administrator for the given Person ID
        def updateBapAdmin(self, b_id, b_admin):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Baptism SET admin = '" + b_admin + "' WHERE id ='" + str(b_id) + "';")
            if not query.exec_():
                return -1

        # Update Family data with the given family_num for the given Person ID
        def updateFamily(self, input_id, family_num):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET family = '" + str(family_num) + "' WHERE id = '" + str(input_id) + "';")
            if not query.exec_():
                return -1

        # Update picture file path for the given Person ID
        def updatePath(self, input_id, path):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET picture_path = '" + path + "' WHERE id = " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Update Group data into -1 before removing the given group
        def updateGroupToBeRemoved(self, g_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("UPDATE Person SET church_group = -1 WHERE church_group = " + str(g_id) + ";")
            if not query.exec_():
                return -1

        # Remove Group for the given group ID
        def removeGroup(self, g_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("DELETE FROM ChurchGroup WHERE num LIKE " + str(g_id) + ";")
            if not query.exec_():
                return -1

        # Remove info from Baptism for the given Person ID
        def removeBaptism(self, input_id):
            query= QtSql.QSqlQuery(self.db)
            query.prepare("DELETE FROM Baptism WHERE id LIKE " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Remove a member for the given Person ID
        def removePerson(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            if(self.removeBaptism(input_id) is -1):
                return -1
            if(self.removeBStudyHistory(input_id) is -1):
                return -1
            query.prepare("DELETE FROM Person WHERE id LIKE " + str(input_id)+";")
            if not query.exec_():
                return -1

        # Remove info from BibleStudyHistory for the given Person ID
        def removeBStudyHistory(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("DELETE FROM BibleStudyHistory WHERE p_id LIKE " + str(input_id) + ";")
            if not query.exec_():
                return -1

        # Add data to BibleStudy Table
        def addBStudy(self, input_name):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("INSERT INTO BibleStudy (name) VALUES ('" + str(input_name) + "');")
            if not query.exec_():
                return -1

        # Add bible study status for individual
        def addBStudyHistory(self, p_id, b_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("INSERT INTO BibleStudyHistory (p_id, b_id) VALUES ('" + str(p_id) + "', '" + str(b_id) +
                          "');")
            if not query.exec_():
                return -1

        # Return bible study status for individual in ID number
        def getBStudyHistory(self, p_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT b_id FROM BibleStudyHistory WHERE p_id = '" + str(p_id) + "';")
            query.exec_()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Return list of all department names
        def getDeptName(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT name FROM Department;")
            query.exec_()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Return department name for the given department ID
        def getDept(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT department FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            d_id = None
            while query.next():
                d_id = query.value(0)

            query.prepare("SELECT name FROM Department WHERE num = '" + str(d_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal  = query.value(0)
            return returnVal

        # Return Department ID for the given department name
        def getDeptID(self, d_name):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT num FROM Department WHERE name ='" + d_name + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal
        #
        # # Return list of people who are in the given department number
        # def getDeptNameList(self, d_id):
        #     query = QtSql.QSqlQuery(self.db)
        #     query.prepare("SELECT name FROM Person WHERE department = '" + str(d_id) + "';")
        #     query.exec_()
        #     returnVal = []
        #     while query.next():
        #         returnVal.append(query.value(0))
        #     return returnVal

        # Return list of birthday regarding to people who are in the given department number
        def getDeptDOBList(self, d_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT b_date FROM Person WHERE department = '" + str(d_id) + "';")
            query.exec_()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Convert Duty ID into duty name
        def getDutyID(self, input_duty):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT num FROM Duty WHERE name = '" + str(input_duty) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Convert Group ID into group name
        def getGroupID(self, input_group):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT num FROM ChurchGroup WHERE name = '" + str(input_group) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return physical address
        def getPhysicalAddress(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT physical_address FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return name list of Duty
        def getDutyName(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT name FROM Duty;")
            query.exec_()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Return first name
        def getFirstName(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT first_name FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return last name
        def getLastName(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT last_name FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return middle name
        def getMidName(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT mid_name FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return Korean name
        def getKorName(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT kor_name FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return list of all group names
        def getGroupList(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT name FROM ChurchGroup;")
            query.exec_()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Return group name for the given group number
        def getGroupName(self, g_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT name FROM ChurchGroup WHERE num = '" + str(g_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Return gender of the given person id
        def getGender(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT gender FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return date of birth
        def getBDate(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT b_date FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return registration date
        def getRDate(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT r_date FROM Person WHERE id = '" + str(input_id) + "'")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        def getEmail(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT email FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        def getPhone(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT phone FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        def getGroup(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT church_group FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            group_id = None
            while query.next():
                group_id = query.value(0)

            query.prepare("SELECT name FROM ChurchGroup WHERE num = '" + str(group_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return duty for individual
        def getDuty(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT duty FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            duty_id = None
            while query.next():
                duty_id = query.value(0)
            query.prepare("SELECT name FROM Duty WHERE num = '" + str(duty_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return Baptism status for individual
        def getBaptism(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT baptism FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            baptism_id = None
            while query.next():
                baptism_id = query.value(0)

            query.prepare("SELECT bap_date, location, admin FROM Baptism WHERE num = '" + str(baptism_id) + "';")
            query.exec_()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
                returnVal.append(query.value(1))
                returnVal.append(query.value(2))
            return returnVal

        # Return family ID for the given Person ID
        def getFamily(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT family FROM Person WHERE id = '" + input_id + "';")
            query.exec_()
            family_id = None
            while query.next():
                family_id = query.value(0)
            return family_id

            # query.prepare("SELECT first_name, last_name, kor_name, b_date FROM Person WHERE id = '" + family_id + "';")
            # query.exec_()
            # sublist = []
            # returnVal = []
            # while query.next():
            #     sublist.append(query.value(0))
            #     sublist.append(query.value(1))
            #     sublist.append(query.value(2))
            #     sublist.append(query.value(3))
            #     returnVal.append(sublist)
            # return returnVal

        # Return the highest ID number in Family Table
        def getHighestFamilyID(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT MAX(id) FROM Family;")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return status of Newcomer study
        def getCStudy(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT c_study FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return status of New Family study (a.k.a. New member study)
        def getMStudy(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT m_study FROM Person WHERE id = '" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return name list of the bible study
        def getBStudyList(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT name FROM BibleStudy;")
            query.exec_()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Return bible study status for individual with person ID
        def getBStudy(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT b_id FROM BibleStudyHistory WHERE p_id = '" + str(input_id) + "';")
            query.exec_()
            b_id_list = []
            returnVal = {}
            while query.next():
                b_id_list.append(query.value(0))

            query.clear()
            b_list = []
            for x in b_id_list:
                query.clear()
                query.prepare("SELECT name FROM BibleStudy WHERE num = '" + x + "';")
                query.exec_()
                while query.next():
                    b_list.append(query.value(0))

            for x in b_list:
                returnVal[x] = True
            return returnVal

        # Return all bible study names with BibleStudy ID
        def getBStudyName(self, b_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT name FROM BibleStudy WHERE num ='" + str(b_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal

        # Return list of bible study ID
        def getBStudyID(self):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT num FROM BibleStudy;")
            query.exec_()
            returnVal = []
            while query.next():
                returnVal.append(query.value(0))
            return returnVal

        # Return picture file path
        def getPicPath(self, input_id):
            query = QtSql.QSqlQuery(self.db)
            query.prepare("SELECT picture_path FROM Person WHERE id ='" + str(input_id) + "';")
            query.exec_()
            returnVal = None
            while query.next():
                returnVal = query.value(0)
            return returnVal


    instance:__DBConnectSingleton = None


    def __init__(self, db):
        if not DBConnectSingleton.instance:
            DBConnectSingleton.instance = DBConnectSingleton.__DBConnectSingleton(db)
        else:
            DBConnectSingleton.instance.val = db


    def __getattr__(self, name):
        return getattr(self.instance, name)
