# 14. Aggregation # ka matlab hai ek class dosri class ka reference rakhti hai lekin dono ka object apni jaga alag alag hota hai.
# Assignment:Create a class Department and a class Employee. Use aggregation by having a Department object store a reference
# to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.empName = name

class Department:
    def __init__(self, employee):
        self.deptEmployee = employee

emp = Employee("Kashan")
dept = Department(emp)
print(dept.deptEmployee.empName)
