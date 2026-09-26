class Employee:
    def __init__(self):
        print("Contructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2
class Coder(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Coder")
    c = 3

# object1 = Employee()
# object2 = Programmer()
object3 = Coder()
# print(object1.a)
# print(object2.a, object2.b)
print(object3.c)