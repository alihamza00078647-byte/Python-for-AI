n = int(input("Enter a Number: "))

l = [str(n*i) for i in range(1, 11)]
vertical_table = "\n".join(l)
print(f"{vertical_table}")
