class Person:
    id = 0
    first_name = ""
    last_name = ""
    mid_name = ""
    kor_name = ""
    gender = ""
    birth_day = ""
    reg_date = ""
    email = ""
    phone = 0
    group = 0
    duty = 0
    family = 0
    newcomer = ""
    newFamily = ""
    address = ""
    dept = ""
    def __init__(self, first_name="", last_name="", mid_name="", kor_name="", gender="", birth_day="", reg_date="",
                 email="",dept = "" ,  phone=0, group=0, duty=0, family=0, newcomer="", newFamily="" , address = ""):
        self.address = address
        self.dept = dept
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.mid_name = mid_name
        self.kor_name = kor_name
        self.gender = gender
        self.birth_day = birth_day
        self.reg_date = reg_date
        self.email = email
        self.phone = phone
        self.group = group
        self.duty = duty
        self.family = family
        self.newcomer = newcomer
        self.newFamily = newFamily

    def toSqlQurey(self):
        return "(" + self.id + "," + self.first_name + "," + self.last_name + "," + self.mid_name + "," + self.kor_name + "," + self.gender + "," + self.birth_day + "," + self.reg_date + "," + self.email + "," + self.phone + "," + self.group + "," + self.duty + "," + self.family + "," + self.newcomer + "," + self.newFamily + "," + self.b_study+")"
