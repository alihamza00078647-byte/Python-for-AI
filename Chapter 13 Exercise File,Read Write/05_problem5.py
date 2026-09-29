n = int(input("Enter a Number: "))

l = [n*i for i in range(1,11)]
with open("Tables.txt", 'a') as f:
    f.write(f"{l} \n")

