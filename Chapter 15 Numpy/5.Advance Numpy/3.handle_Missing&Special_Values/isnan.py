import numpy as np
""" 
Q1. Why we use ?  
** Because In Real World data We deal with missing values and then fill it **

np.isnan --> detect missing values
np.nan_to_num --> replace missing values to Numbers
np.isinf  --> Check the infinite values
"""
# np.isnan return a boolean array
arr = np.array([1,2,np.nan, 4, 8, np.nan])
print(np.isnan(arr)) # missing value returns True

""" ****
Q2. Interview question ==> Can we compare (np.nan == np.nan) 
Ans.  No, We can only use this function to find missing values 
**** """