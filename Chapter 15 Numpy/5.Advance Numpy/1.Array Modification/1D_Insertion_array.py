import numpy as np

"""
np.insert(array, index, value, axis)
array -- original Array
index -- index No where we want to push the Array
value -- Value We Want To Set 

**axis Cases
1. Axis None --> if axis=None then array will flatten then Append Data in Row
2. 1D Array Case --> Simply Change row-wise
"""

arr = np.array([12, 34, 56])
new_arr = np.insert(arr, 3, 1000, axis=0) #By default axis=0 
print(new_arr)