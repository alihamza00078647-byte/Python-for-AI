import matplotlib.pyplot as plt

"""
** Pie Chart **

plt.pie(values, lables="lable_list", colors=color_list, autopct="%1.1f%%") // auto-percentage (%, %%)

"""
regions = ["South", "North", "East", "West"]
revenue = [1233, 4311, 3244, 4900]


plt.pie(revenue, labels=regions, autopct="%1.1f%%", colors=["red", "green", "blue", "orange"])
plt.title("Mera Title")

# Only use to show graphs.
plt.show()