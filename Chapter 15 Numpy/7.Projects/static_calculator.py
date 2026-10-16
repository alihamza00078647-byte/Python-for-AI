import numpy as np

# Take user input number
user_num = input('Enter List of Numbers Separated by spaces: ')

# change into array also sata type
arr = np.array(user_num.split(), dtype=int)

# Calculate mean
mean = np.mean(arr)

# calculate standard deviation
std_dev = np.std(arr)


# array leta hai aur percentage leta hai, aur wo VALUE batata hai
# jiske NEECHE utna % data hota hai
percen = np.percentile(arr, 90)

print(round(percen, 2))
