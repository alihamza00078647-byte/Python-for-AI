class animals:
    pass

class Pets(animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow!!!")

d = Dog()
d.bark()