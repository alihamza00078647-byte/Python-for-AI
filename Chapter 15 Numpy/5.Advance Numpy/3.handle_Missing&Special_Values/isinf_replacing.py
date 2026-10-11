import numpy as np

"""
isinf(array) -> is used when number exceeds python's number limit
Example => 10^1000, 1/0

"""

arr = np.array([1,2,np.inf, 8, -np.inf])
# return a booolean array
res = np.isinf(arr)
print(res) 


""" Replacing a Number with inf. No """
arr2 = np.array([1,2,np.inf, 8, -np.inf])
# posinf -> positive infinity && negative infinity 
clean_arr = np.nan_to_num(arr2, posinf=100, neginf=-200)
print(clean_arr)