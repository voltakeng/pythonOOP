from class_accounting import Accounting as ac
from class_programmer import Programmer as pg
from class_sale import Sale as sa

account = ac("ก้อง",10000,30)
print(account.__str__())
print("Income per year: "+str(account._getIncome(5000)))

programmer = pg("โจโจ้",40000,2,"python") 
print(programmer.__str__())
print("Income per year: "+str(account._getIncome(10000,500)))

sale = sa("นัท",35000,"bkk")
print(sale.__str__())
print("Income per year: "+str(account._getIncome()))