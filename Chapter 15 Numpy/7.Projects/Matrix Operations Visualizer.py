import numpy as np


"""
yeh question maths mein solve kiye thy. ab direct numpy mein kary gy
3x + y = 9
4x + 7y = 5
""" 

# Take Matrix from left side
matrix = np.array([[3, 5],
                   [4, 7]])

# array at right side
constValues = np.array([7, 2])

# return soultion of x , y in array 
ans = np.linalg.solve(matrix, constValues)


print(ans)


