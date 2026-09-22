def natural(i, n):
    sum = 0
    while i <= n:
        i = i + 1
        sum = sum + i
    return sum








c = natural(1, n = int(input("Enter a Number: ")))
print(c)