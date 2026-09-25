from math import sqrt
class calculate:
    def __init__(self, n):
        self.n = n
    @staticmethod
    def greet():
        print("Hello, Here the list of the output: ")
    def square(self):
        print(f"The Square of the Number is {self.n*self.n}")
    def square_root(self):
        print(f"The Square Root of the Number is {sqrt(self.n)}")
    def cube(self):
        print(f"The Cube of the Number is {self.n*self.n*self.n}")

m = calculate(int(input("Enter a NUmber: ")))
m.square()
m.square_root()
m.cube()
m.greet()

