import matplotlib.pyplot as plt


"""
# plt.subplot(nRows, nColumns, index)

"""
x = [1, 2, 3, 4, 5]
y = [24, 65, 76, 84, 32]


plt.subplot(1, 2, 1)
plt.plot(x, y)

plt.show()

x = [1, 2, 3, 4, 5]
y = [24, 65, 76, 84, 32]


plt.subplot(1, 2, 1)
plt.bar(x, y)

plt.show()
