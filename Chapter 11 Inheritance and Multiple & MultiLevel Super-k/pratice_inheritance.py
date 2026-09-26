class Employee:
    company = "Google"
    def show(self):
        print(f"The Name is {self.name} and Language is {self.language}")
class programmer(Employee):
    company = "Amazon"
    id = 762576
    def show(self):
        print(f"The ID of the Employee is {self.id}")
#     def showLanguage(self):
#         print(f"This Employee is Good in {self.language}")



# a = Employee()
b = programmer()
b.show()
print(f"The Employee is the worker of", b.company)