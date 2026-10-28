import matplotlib.pyplot as plt

"""
plt.plot(x-axis, y-axis, color="red", linestyle="-", marker="circle|square", lable="lable_Name")
plt.title("Your Title")
plt.legend(location where we set box, size of box(fontsize))
plt.grid(color="red", linestyle=":", linewidth=3)
plt.xlim := Set axis limit to zoom/magnify the important data.
plt.ylim := Set axis limit to zoom/magnify the important data.
"""


x = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"] #x-axis
y = [100, 210, 129, 90, 70, 2, 130] #y-axis

plt.plot(x, y, color="green", linestyle="-", linewidth=2, marker="o")

# Set Title 
plt.title("Sales Data")
# Create a box at (upper left, lower right) cornor.
plt.legend(loc="lower right", fontsize=53)

plt.xlabel("Days of Weeks")
plt.ylabel("Sales Items")
# draw lines at back.
plt.grid(color="brown", linestyle=":", linewidth=1)

# Set limit on x-y axis
plt.xlim(1, 4)
plt.ylim(0, 220)

# Replace the lables
plt.xticks([1, 2, 3], ["M1", "M2", "M3", "M4"])
# plt.yticks()

# Show Graph 
plt.show()