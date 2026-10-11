import numpy as np

""" How Numpy handles Arrays of different Shapes ( __Rules__ ) """

# 1. Matching Elements -->  [1, 2, 3] + [4, 5, 6]    Results = [5, 7, 9]
arr1 = np.array([12, 33, 21])
arr2 = np.array([10, 20, 30])
result1 = arr1 + arr2
print(result1)



# 2. Expanding Single Element  --> [1 , 2, 3] + 10   Results =  [11, 12, 13]
arr = np.array([12, 34, 56])
result2 = arr * 2
print(result2)


# 3. Incompatible Shapes  --> [1, 2, 3] + [4, 5]     Results = Error
arr3 = np.array([12, 33, 21])
arr4 = np.array([10, 20])
result3 = arr3 + arr4
print(result3) # Error Occur
