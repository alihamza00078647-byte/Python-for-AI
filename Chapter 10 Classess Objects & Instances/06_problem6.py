from math import sqrt

class calculator:

    def __init__(slf, n):
        slf.n = n

    def square(slf):
        print(f"The Square of the Number is {slf.n*slf.n}")

    def cube(slf):
        print(f"The Cube of the Number is {slf.n*slf.n*slf.n}")
    def squareroot(slf):
        print(f"THe Square_Root of the Number is {sqrt(slf.n)}")
mathe = calculator(4)
mathe.square()
mathe.cube()
mathe.squareroot()




