with open("this.txt", "r") as f:
    content = f.read()

with open("log.txt") as f:
    data = f.read()

if content == data:
    print("Yes Both Files have Same Content")
else:
    print("No, Both Files have  not Same Content")