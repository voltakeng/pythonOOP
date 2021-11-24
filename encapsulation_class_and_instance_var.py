class Employee: 
    #class variable
    _minSalary = 12000
    _maxSalary = 50000

    def __init__(self,name,salary,department): 
        #instance variable
        self.__name = name
        self.__salary = salary
        self._department = department 

    def showData(self): 
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = {}",format(self.__salary))
        print("ตำแหน่ง = {}",format(self._department))

obj = Employee("K",20000,"C")

print(Employee._maxSalary)