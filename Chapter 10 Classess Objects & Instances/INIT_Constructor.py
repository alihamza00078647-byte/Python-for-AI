class Employee:
    name = "Hamza"
    language = "C"
    salary = 120000

    def __init__(self, name, language, salary):
        self.name = name
        self.salary = salary
        self.language = language 
        print("I am in the class")

ali = Employee("Ali", 100202002, "C++")
# ali.language = "Rust"   #Instance/object attributes takes preference over class attributes
ali

print(ali.name, ali.salary, ali.language)