import numpy as np

# nan_to_num(array, Replacing_Value) default -> nan=0

arr = np.array([1,2,np.nan, 4, 8, np.nan])

# return a new Array
res = np.nan_to_num(arr, nan=981)
print(res) 