class Employee:
    salary = 12000
    def pay(self):
        increment = (25 * self.salary ) / 100
        print(f"The Salary of the Employee is {self.salary + increment}")

Emp = Employee()
Emp.pay()