class Employee:
    salary = 12000
    def salaryafterincrement(self):
        return ((25 * self.salary ) / 100) + self.salary
        # print(f"The Salary of the Employee is {self.salary + increment}")

Emp = Employee()
print(Emp.salaryafterincrement())