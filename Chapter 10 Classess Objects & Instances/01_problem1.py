class programmer:
    Company = "Microsoft"
    

    def __init__(self, name, salary, pin):
        print("Heres, the list of few programmers: ")
        self.name = name
        self.salary = salary
        self.pin = pin


pro = programmer("Ali Hamza", 150000, 2314)
print(f"The Name of the Employee {pro.name}\nSalary is {pro.salary}\nThe PinCode is {pro.pin}")