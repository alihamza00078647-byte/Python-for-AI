marks = int(input("Enter Your Marks: "))

if marks>=100 and marks>90:
    grade = "Excellent"
elif marks<=90 and marks>80:
    grade = "A"
elif marks<=80 and marks>70:
    grade = "B"
elif marks<=70 and marks>60:
    grade = "C"
else:
    grade = "Fail"
print("Your Grade is: ", grade)