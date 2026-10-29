from matplotlib import pyplot as plt

"""
plt.hist(data, bins="Number_of_Bins", color="color_Name", edgecolor="black")

"""

scores = [20, 30, 50, 89, 100, 76, 42, 13, 54, 72]

plt.hist(scores, bins=5, color="green", edgecolor="black")
plt.xlabel("years")
plt.ylabel("Scores of athletes")




plt.title("Histogram Chart")
plt.show()