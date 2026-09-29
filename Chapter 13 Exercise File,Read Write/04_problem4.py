# a = 3
# b = int(int(input("Enter the Value of b: ")))

try:
    a = 3
    b = int(int(input("Enter the Value of b: ")))
    print(a/b)

except ZeroDivisionError as e:
    print("Infinite")