factorial = 1
n = int(input("Enter a Number to Calculate factorial: "))
i = 1
while i<= n:
    factorial = factorial * i
    i += 1


print(F'The Factorial of {n} is {factorial}')