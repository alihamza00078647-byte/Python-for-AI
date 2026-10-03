import numpy as np

"""
All Attributes like shape, size, ndim, dtype, astype(data type)
"""



# shape ->  Returns an integer No of (Rows x Columns)
two_dm = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(two_dm.shape)

# size -> returns total Elements of Array or Arrays
print(two_dm.size)

# ndim -> (n for number) & (dim for dimension) returns no of dimension
three_dm = np.array([
    [[1, 2, 3, 4],
     [4, 5, 6, 90]],

    [[12, 23, 45, 65],
    [32, 43, 54, 65]],

    [[9, 87, 80, 50],
     [10, 20, 30, 40]],
])

print(two_dm.ndim)
print(three_dm.ndim)
 

# dtype -> returns the data type of Array
print(three_dm.dtype)



# astype -> typeCast the array
before_typecast_arr = np.array([[1.1, 2.1, 3.4],
                  [4.4, 5.6, 6.8],
                  [7.2, 8.5, 9.9]])

after_typecast_arr = before_typecast_arr.astype(int)
print(after_typecast_arr)




