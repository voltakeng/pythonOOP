class Employee: 

    # constructor
    def __init__(self,name,salary,department): 
        self.name = name
        self.salary = salary
        self.department = department 

    def showData(self): 
        print("ชื่อพนักงาน = {}",format(self.name) )
        print("เงินเดือน = {}",format(self.salary))
        print("ตำแหน่ง = {}",format(self.department))

    # destructor
    def __del__(self): 
        pass

obj = Employee("K",20000,"C")

# เช็คว่า object นี้ถูกสร้างจาก class นี้หรือไม่
print(isinstance(obj,Employee))

# เช็คว่าใน class มีอะไรบ้าง
print(dir())

# ดูว่ามาจาก class ไหน
print(obj.__class__)

# คืนแรม
del obj

