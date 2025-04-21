from Employee import Employee
from Manager import Manager

emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
mgr1 = Manager("Sue Sylvester", 12345, "HR", "Manager", [emp1])
print(mgr1.getName()) # inherited method
mgr1.printEmployees()



