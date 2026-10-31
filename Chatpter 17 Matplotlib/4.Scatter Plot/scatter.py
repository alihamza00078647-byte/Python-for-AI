from matplotlib import pyplot as plt

"""
# Scatter Plot Syntax
plt.scatter(x, y, color="Color_Name", marker="marker style", label="label_Name")

Use Case := advertese vs sales,
"""

x = [1, 2, 3, 4, 5]
y = [24, 65, 76, 84, 32]

plt.scatter(x, y, color="red", marker="o", label="Data Learning")

plt.title("Scatter Plot")
plt.grid()
plt.xlabel('Days Of Weeks')
plt.ylabel('Test Marks')
# makes box
plt.legend()

plt.show()
