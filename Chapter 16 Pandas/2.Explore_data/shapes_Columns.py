import pandas as pd

"""
 ** Problems **
1. How big the data is ?
2. what are the names of columns ?

shape  --> shape ( Attribute ) tells the rows and columns in dataset
columns --> returns the names of columns
"""

employee_data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, 22, 23, 34, 67, 89, 90],
    "salary" : [20000, 230000, 240000, 250000, 90000, 895000, 890072],
    "Performance" : [2.3, 2.4, 5.0, 1.5, 4.7, 3.8, 4.1]
}

df = pd.DataFrame(employee_data)

# returns (rows, columns) -> (7, 4)
print(f'Shape is = {df.shape}')

# return columns Name in list with data type
print(f'Shape is = {df.columns}')











