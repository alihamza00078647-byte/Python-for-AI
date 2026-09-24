# f = open("log.txt", "r")

# line = f.readline()
# print(line)
# f.close()

with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"YES, Python is present. Line No: {lineno}")
        break
    lineno += 1

else:
    print("No, Python is not present")