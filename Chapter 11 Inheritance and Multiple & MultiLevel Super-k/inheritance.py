class Employee:
    company = "Google"
    def show(self):
        print(f"The Name is {self.name} and Language is {self.language}")
class programmer:
    company = "Amazon"
    def show(self):
        print(f"The Name is {self.name} and Language is {self.language}")
    def showLanguage(self):
        print(f"This Employee is Good in {self.language}")

a = Employee()
b = programmer()
print(a.company, b.company)