# class Businessman:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The Value of class Attribute a is {cls.a}")

class Employee:
        @property     
        def name(self):        
            return self.ename

        @name.setter
        def name(self,value):
            self.ename = value
# man = Businessman()
# man.a = 23
# man.show()
e = Employee()
e.name = "ALi"
property(e.name)