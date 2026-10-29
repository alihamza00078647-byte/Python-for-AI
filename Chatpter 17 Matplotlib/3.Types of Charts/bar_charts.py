import matplotlib.pyplot as plt

"""
# Bar chart
plt.bar(x, height(y), color="Color Name", width=value, lable="Lable Name")
"""


product = ["A", "B", "C", "D", "E", "F"]
sales = [12, 43, 45, 65, 2, 90]


# plt.barh(product, sales, color="red")

# vertical bar 
plt.bar(product, sales, color="red")
plt.title("xyz Company Sales data")
plt.xlabel("Products Names")
plt.ylabel("Sales Units")


plt.legend()
plt.show()