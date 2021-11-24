class Employee: 

    def __init__(self,name,salary,department): 
        self.__name = name
        self.__salary = salary
        self.__department = department 

    def showData(self): 
        print("ชื่อพนักงาน = {}",format(self.__name) )
        print("เงินเดือน = {}",format(self.__salary))
        print("ตำแหน่ง = {}",format(self.__department))

    def setSalary(self,newsalary):
        self.__salary = newsalary
    
    def getSalary(self): 
        return self.__salary

obj = Employee("K",20000,"C")

print(obj.getSalary())

obj.setSalary(50000) 
print(obj.getSalary())