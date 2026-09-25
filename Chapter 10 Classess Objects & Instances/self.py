class Employee:
    name = "Hamza"
    language = "C"
    salary = 120000
# if we dont wnat to use self/other variable naeme then
    def getinfo(self):
        print(f"The Language is {self.language}\nThe Salary is {self.salary}")
    @staticmethod
    def greet():
        print("Hello Good Morning")
ali = Employee()
# ali.language = "Rust"
ali.getinfo()
ali.greet()
# print(ali.language, ali.salary)