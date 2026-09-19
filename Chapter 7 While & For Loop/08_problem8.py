n = int(input("Enter a NUmber: "))

i = 1
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*i, end="")
    print("\n")
    # i += 1
