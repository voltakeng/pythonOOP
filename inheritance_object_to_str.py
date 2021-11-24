class Employee: 
    minSalary = 12000
    maxSalary = 50000
    def __init__(self,name,salary,department): 
        self.__name = name
        self.__salary = salary
        self._department = department 

    def showData(self): 
        print("ชื่อพนักงาน = " + self.__name )
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = ",format(self._department))

    def _getIncome(self): 
        return self.__salary *12
    
    def __str__(self): 
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {}".format(self.__name,self._department,self.__salary))
        
class Accounting(Employee): 
    _departmentName = "บัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self._departmentName)

class Programmer(Employee): 
    _departmentName = "โปรแกรม"
    def __init__(self,name,salary): 
        super().__init__(name,salary,self._departmentName)

class Sale(Employee): 
    _departmentName = "ขาย"
    def __init__(self,name,salary): 
        pass
        super().__init__(name,salary,self._departmentName)

account = Accounting("ก้อง",10000)
print(account.__str__())
programmer = Programmer("โจโจ้",40000) 
print(programmer.__str__())
sale = Sale("นัท",35000)
print(sale.__str__())