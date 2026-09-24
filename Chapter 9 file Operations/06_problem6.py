with open("log.txt") as f:
    data = f.read()

if "python" in data:
    print("YES, Python is present")
else:
    print("No, Python is not present")