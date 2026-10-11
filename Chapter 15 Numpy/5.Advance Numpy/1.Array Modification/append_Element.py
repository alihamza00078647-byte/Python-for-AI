import numpy as np


"""
append() --> add Element at the end of Array ( Create New Array )
.concatenate() --> merge 2 or more Arrays along with Axis.
"""

arr = np.array([1,2,4,5])
# Append New Value or Whole Array
new_arr = np.append(arr, [20, 30])
# print(new_arr)

# Merge Two Arrays
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])

merge_arr = np.concatenate((arr1, arr2), axis=0) #axis=0 row-wise & axis=1 column-wise
print(merge_arr)


