import matplotlib.pyplot as plt


"""
#fig, ax = plt.subplot(nrows, ncols, figsize=(height, width))
"""
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

x = [1, 2, 3, 4]
y = [10, 20, 40, 89]


ax[0].plot(x, y, color="red")
ax[0].set_title("1st Chart")


ax[1].bar(x, y, color="green")
ax[1].set_title("2nd Chart")

# Give a Common Name
plt.suptitle('Camparison of Two Charts')

# Tight Layout will auto adjust
plt.tight_layout()

plt.show()


