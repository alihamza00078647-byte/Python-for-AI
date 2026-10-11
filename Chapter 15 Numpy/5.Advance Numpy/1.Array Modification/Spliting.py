import numpy as np

"""
=== ** Methods ** ===
1. np.split() -> Split into equal Parts
1. Note ---> Pay heed On Value Error ( Agar Array Equally Split Nahi Ho Raha)


** 2D Split ** 
2. np.vsplit() -> vertically Split Array [ Column Wise ]
3. np.hsplit() -> horizontally Split Array [ Row Wise ]

"""

arr = np.array([1, 2, 3, 4, 5, 6])
# Split Into Equal Parts Same AS JS Split
print(np.split(arr, 2))



# Split Vertically Columns into Equal Parts 
arr2 = np.array([[1, 2, 3], [40, 50, 60], [610, 201, 1000], [61, 21, 100]])
print(np.vsplit(arr2, 2))


# Horizontally Split
arr3 = np.array([[1, 2, 3, 4], [40, 50, 60, 70], [610, 201, 1000, 312], [61, 21, 100, 32]])
print(np.hsplit(arr3, 2))
