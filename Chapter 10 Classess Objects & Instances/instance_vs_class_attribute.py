class Employee:
    name = "Hamza"
    language = "C"
    salary = 120000

ali = Employee()
ali.language = "Rust"   #Instance/object attributes takes preference over class attributes
print(ali.language, ali.salary)