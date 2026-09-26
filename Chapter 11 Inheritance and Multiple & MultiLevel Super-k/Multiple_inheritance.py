class Employee:
    company = "Amazon"
    name = "Ali"
    def show(self):
        print(f"The Name of the Employee is {self.name} which is working at {self.company}")
class Programmer(Employee):
    company = "Nvidia"
    def showlanguage(self):
        print(f"The Name of the Company is {self.company}")

Emp = Programmer()
Coder = Employee()
Coder.show()
Emp.showlanguage()
# Programmer()

        