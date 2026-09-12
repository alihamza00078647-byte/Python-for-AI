name = input("Enter Your Name: ")
math = int(input("Enter Maths marks: "))
physics = int(input("Enter Physics Marks: "))
eng = int(input("Enter Engish marks: "))

marks = ((math + physics + eng) * 100) / 300

if (math >= 33 and physics >= 33 and eng>=33 and marks>= 40):
    print(f"Congratulates, {name} You are passed with {marks}%")

else:
    print(f'Oop! You are Fail {name} with {marks}')