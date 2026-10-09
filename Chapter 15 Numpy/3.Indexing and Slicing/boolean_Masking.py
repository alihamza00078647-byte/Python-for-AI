import numpy as np

"""
Boolean Masking Means ->  filtering Data based on the Condition
"""

arr = np.array([12, 34, 56, 78, 90, 100, 212, 345, 454])

# Boolean Masking
print(arr[arr > 100])