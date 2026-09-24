# f = open("myfile.txt")
# data = f.read()
# print(data)
# f.close()


# The Same code can be written by using with statement:

with open("myfile.txt") as f:
    print(f.read())