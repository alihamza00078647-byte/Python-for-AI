n = int(input("Enter a Number to Calculate factorial: "))
fac= 1

for i in range(1, n+1):     #Maybe its confusing at first but heres the trick 
    fac = fac * i
 
print(f"The Factorial of {n} is {fac}")