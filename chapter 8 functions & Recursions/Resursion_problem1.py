def recursion(n):
    if n==1 or n==0:
        return 1

    else:
        return n* recursion(n-1)






# fac = recursion(7)
fac = recursion(int(input("Enter a number: ")))
print(f"The factorial is {fac}")