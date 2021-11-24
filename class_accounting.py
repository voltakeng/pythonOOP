from class_employee import Employee

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