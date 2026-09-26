class Businessman:
    a = 1
    @classmethod
    def show(cls):
        print(f"The Value of class Attribute a is {cls.a}")

man = Businessman()
man.a = 23
man.show()