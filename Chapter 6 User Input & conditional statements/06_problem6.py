marks = int(input("Enter your marks: "))
# total = 1100
percentage_marks = (marks / 1100) * 100

if (percentage_marks>=90 and percentage_marks>80):
    print("Excellent", percentage_marks)
elif (percentage_marks>=80 and percentage_marks<70):
    print('A')






else:
    print("You Are Fail")