class Employee: 
    minSalary = 12000
    maxSalary = 50000
    def __init__(self,name,salary,department): 
        self.name = name
        self.salary = salary
        self.department = department 

    def showData(self): 
        print("ชื่อพนักงาน = {}",format(self.name) )
        print("เงินเดือน = {}",format(self.salary))
        print("ตำแหน่ง = {}",format(self.department))

class Accounting(Employee): 
    def __init__(self):
        pass

class Programmer(Employee): 
    pass

class Sale(Employee): 
    _departmentName = "ฝ่ายขาย"

ac = Accounting() 
print(ac.maxSalary)

pg = Programmer("K",20000,"C") 
print(pg.salary)


