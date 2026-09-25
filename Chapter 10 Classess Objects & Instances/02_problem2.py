from math import sqrt

class calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The Square of the Number is {self.n*self.n}")

    def cube(self):
        print(f"The Cube of the Number is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"THe Square_Root of the Number is {sqrt(self.n)}")
mathe = calculator(4)
mathe.square()
mathe.cube()
mathe.squareroot()




