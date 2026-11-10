# fibonachi series (0, 1 , 1, 2, 3, 5, 8, 13....)

n = int(input("Enter the ending number: "))
a , b = 0 , 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else: 
    number = 2
    while number < n:
        fibo = a + b
        print(a + b, fibo, end=" ")
        a , b = a + b , fibo
    print()