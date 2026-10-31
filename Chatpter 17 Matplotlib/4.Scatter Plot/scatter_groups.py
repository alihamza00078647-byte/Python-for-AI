from matplotlib import pyplot as plt

"""
# Scatter Plot Syntax
plt.scatter(x, y, color="Color_Name", marker="marker style", label="label_Name")

Use Case := advertese vs sales,
"""

# 1st Group
grp1x = [1, 2, 3, 4, 5]
grp1y = [24, 65, 76, 84, 32]

# 2nd Group
grp2x = [1, 2, 3, 4, 5]
grp2y = [90, 89, 36, 33, 42]


plt.scatter(grp1x, grp1y, color="red", marker="o", label="Data Learning")
plt.scatter(grp2x, grp2y, color="blue", marker="^", label="Data Learning")

plt.title("Class Camparison")
plt.grid()
plt.xlabel('Days Of Weeks')
plt.ylabel('Test Marks')
# makes box
plt.legend()

plt.show()
