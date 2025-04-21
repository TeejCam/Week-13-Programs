from Employee import Employee

class Manager(Employee):
    def __init__(self, name, id, department, position, employees=None):
        super().__init__(name, id, department, position)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmployee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def removeEmployee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def printEmployees(self):
        for employee in self.employees:
            print('-->', employee.fullname())