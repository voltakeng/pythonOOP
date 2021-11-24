class Employee: 
    __minSalary = 12000
    maxSalary = 50000
    companyName = "xyz"
    def __init__(self,name,salary,department): 
        self.__name = name
        self.__salary = salary
        self._department = department 

    def _showData(self): 
        print("ชื่อพนักงาน = " + self.__name )
        print("เงินเดือน = ",format(self.__salary))
        print("ตำแหน่ง = ",format(self._department))

    def _getIncome(self,bonus=0,ot=0): 
        return self.__salary *12 +bonus+ot
    
    def __str__(self): 
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {}".format(self.__name,self._department,self.__salary))