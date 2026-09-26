class Employee:
    a = 1

class Programmer(Employee):
    b = 2
class Coder(Programmer):
    c = 3

# object1 = Employee()
# object2 = Programmer()
object3 = Coder()
print(object3.a, object3.b, object3.c)