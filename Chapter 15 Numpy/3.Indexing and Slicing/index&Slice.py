import numpy as np 

"""
array[index] -> 1d Array
array[row, column] -> 2d & 3d Array
**
Slice ArrName[start:stop:step]
Can Also Use Negative indexing
"""
arr = np.array([12, 34, 56, 78, 90])

print(arr[0])  #1st Element 


# Slicing at Python
arrSlice = np.array([12, 34, 56, 78, 90])

# print(arrSlice[0:3])
# print(arrSlice[-3:-1])
# print(arrSlice[::2])  # Take Steps of provided Number
print(arrSlice[::-1])  # Will reverse the Array




