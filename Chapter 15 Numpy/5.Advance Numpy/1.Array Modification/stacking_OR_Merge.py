import numpy as np

"""
**Methods
1. vstack() -> vertically Stack or Merge Arrays  [ Column Wise ]
2. hstack() -> horizontally Stack or Merge Arrays [ Row Wise ]
"""


arr_1 = np.array([1,2,3])
arr_2 = np.array([4,5,6])

print(np.vstack((arr_1, arr_2))) #Vertically Stack
print(np.hstack((arr_1, arr_2))) #Horizontally Stack
