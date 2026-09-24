with open("old.txt") as f:
    variable = f.read()

with open("renamed_python.txt", "w") as f:
    f.write(variable)