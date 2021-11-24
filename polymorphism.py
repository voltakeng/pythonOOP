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
        
class Accounting(Employee): 
    _departmentName = "บัญชี"
    def __init__(self,name,salary,age):
        # overriding method
        super().__init__(name,salary,self._departmentName)
        self._age = age

    def _showData(self): 
        # overriding method
        super()._showData()
        print("อายุ = "+str(self._age)) 

    def __str__(self):
        # overriding method
        return super().__str__()+" , อายุ = {}".format(self._age)       

class Programmer(Employee): 
    _departmentName = "โปรแกรม"
    def __init__(self,name,salary,experience,skill): 
        super().__init__(name,salary,self._departmentName)
        self._exp = experience
        self._skill = skill

    def _showData(self): 
        super()._showData()
        print("ประสบการณ์ = "+str(self._exp))   
        print("ทักษะ = "+self._skill)
    
    def __str__(self):
        return super().__str__()+" , ประสบการณ์ = {} , ทักษะ = {}".format(self._exp,self._skill)

class Sale(Employee): 
    _departmentName = "ขาย"
    def __init__(self,name,salary,area): 
        super().__init__(name,salary,self._departmentName)
        self._area = area
    
    def _showData(self): 
        super()._showData()
        print("พื้นที่ = "+self._area)   
    
    def __str__(self): 
        return super().__str__()+" , พื้นที่ = {}".format(self._area)

account = Accounting("ก้อง",10000,30)
print(account.__str__())
# เรียกใช้ overloading method
print("Income per year: "+str(account._getIncome(5000)))
programmer = Programmer("โจโจ้",40000,2,"python") 
print(programmer.__str__())
print("Income per year: "+str(account._getIncome(10000,500)))
sale = Sale("นัท",35000,"bkk")
print(sale.__str__())
print("Income per year: "+str(account._getIncome()))