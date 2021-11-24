from class_employee import Employee

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