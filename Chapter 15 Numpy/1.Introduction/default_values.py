import numpy as np


# Default Values Zeros -> (3) = 1d, (value, value) = 2d, (value, value, value) = 3d [ value => shape]
zeros_array = np.zeros(8)
# print(zeros_array)

# Default Values will 1
ones_array = np.ones((2, 4))
# print(ones_array)


# default full(shape, desire_value) function
desire_value_array = np.full((2, 3), 20)
print(desire_value_array)