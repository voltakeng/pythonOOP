from class_employee import Employee

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