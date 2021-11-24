class Employee: 

    def __init__(self,name,salary,department): 

        # public attribute
        self.name = name

        # protected attribute
        self._salary = salary

        # private attribute
        self.__department = department 
        # เรียก private ในนี้ได้
        self.__showName()

    # public method
    def showData(self): 
        print("ชื่อพนักงาน = {}",format(self.name) )
        print("เงินเดือน = {}",format(self._salary))
        print("ตำแหน่ง = {}",format(self.__department))

    # private method
    def __showName(self): 
        print("ชื่อพนักงาน = {}",format(self.name) )


obj = Employee("K",20000,"C")

#public
obj.name = "โจโจ้"
obj.showData() 

#protected
obj.salary = 50000
obj.showData() 
obj._salary = 40000
obj.showData()

#private
# obj.__department = "G"
# จะทำไม่ได้
# และ
# เรียก private ในนี้ไม่ได้
# obj.__showName()


