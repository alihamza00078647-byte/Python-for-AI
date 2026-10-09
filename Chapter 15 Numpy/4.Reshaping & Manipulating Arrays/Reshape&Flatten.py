import numpy as np

"""
Methods -> Reshape(row, column) -> Specify New Shapes from 1D Array -> Multi dimension 
** if dimensions Match

"""

before_arr = np.array([12, 34, 56, 78, 33, 90])
# reshape does not create new arr but it returns a view
# thats why it affects the original array.
after_arr = before_arr.reshape(2,3)
# print(after_arr)

# Flattering Arrays
"""
Convert Multi Dimensional Array -> 1D Array 

ravel() -> returns view [ Affect the Origin Array ]
flatten() -> returns copy [ Does Not Affect the Origin Array ]
"""

arr_2d = np.array([[12, 34, 56], [78, 33, 90]])

print(arr_2d.ravel())
print(arr_2d.flatten())







