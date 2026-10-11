import numpy as np

# Traditional Way
list1 = [2, 4, 6]
list2 = [3, 5, 7]
# List Comprehension method ( Shortcut Loop )
result = [x+y for x,y in zip(list1, list2)]
print(result)


""" Loop ki jagah NumPy operation use karo — fast """
arr1 = np.array([2, 4, 6])
arr2 = np.array([3, 5, 7])

res = arr1 + arr2
print(res)

