from EmployeePack.Employee import Employee
from EmployeePack.Developer import Developer
from EmployeePack.Sales import Sales


#employ = Employee('Steve',1)
#print employ.calculate_salary()


employ1 = Developer('Tom',3,'python')
print employ1.description()
print employ1.description()

employ2 = Developer('James',2,'java')
print employ2.calculate_salary()
print employ2.description()


employ3 = Sales('David',4,'Dublin')
print employ3.calculate_salary()
print employ3.description()

employ4 = Sales('Frank',6,'NotDublin')
print employ4.calculate_salary()
print employ4.description()




