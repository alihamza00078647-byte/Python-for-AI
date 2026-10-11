import numpy as np

"""
1. 1d Array --> np.delete(arr, index, axis=None) None means => Flatten Array
2. 2d Array -->  np.delete(arr, index of Array, axis=0) -- delete row-wise 

"""

# Delete from 1d Array
arr = np.array([1, 2, 3, 4, 5])
# print(np.delete(arr, 0, axis=None))


# Delete from 2d Array as Row

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.delete(arr_2d, 1, axis=0))

# Delete from 2d Array as column
print(np.delete(arr_2d, 0, axis=1))
