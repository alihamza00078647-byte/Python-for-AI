import numpy as np

"""
Aggregation functions in Numpy
min, max, sum, avg, mean, std ,var
"""

arr = np.array([12, 33, 44, 55, 66, 12])

print("Sum is  = ", np.sum(arr))
print("Min is = ", np.min(arr))
print("Max is = ", np.max(arr))

print("Standard Deviation = ", np.std(arr))

print("Variance is = ", np.var(arr))

print("mean is = ", np.mean(arr))
# print(np.avg(arr))
