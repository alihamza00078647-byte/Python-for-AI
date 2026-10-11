import numpy as np

"""
np.insert(array, index, value, axis)
array -- original Array
index -- index No where we want to push the Array
value -- Value We Want To Set 

**axis Cases
1. Axis None --> if axis=None then array will flatten then Append Data in Row
2. 2D Array Case --> if [axis=0 then data will set Row wise] else [axis=1 then data will set Column wise]
"""


arr = np.array([[12, 34], [30, 40]])
print(arr)

# Insert New Row at index #2
new_arr = np.insert(arr, 2, [210, 1000], axis=0) 
print(new_arr)

# Insert New Column at index #2
new_arr = np.insert(arr, 2, [210, 1000], axis=1) 
print(new_arr)

# if axis=None
new_arr = np.insert(arr, 2, [210, 1000], axis=None) 
print(new_arr)