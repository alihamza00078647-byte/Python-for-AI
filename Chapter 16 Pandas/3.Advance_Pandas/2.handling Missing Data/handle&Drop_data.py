import pandas as pd

"""
1. dropna() method remove All values None Values from Rows And Columns. 
"""
employee_data = {
    "name" : ["Ali", None, "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, None, 24, 34, 67, 89, 90],
    "salary" : [20000, None, 240000, 250000, 90000, 895000, 890072],
    "Performance" : [2.3, None, 5.0, 1.5, 4.7, 3.8, 4.1]
}

df = pd.DataFrame(employee_data)

# Remove All Rows With Values Null. axis=0 -> rows && axis=1 column
print(df.dropna(axis=0, inplace=False))
