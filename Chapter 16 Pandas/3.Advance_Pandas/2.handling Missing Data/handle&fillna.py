import pandas as pd

"""
1. fillna() method fill All None values -> with Values provide by DA. 
"""
employee_data = {
    "name" : ["Ali", None, "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, None, 24, 34, 67, 89, 90],
    "salary" : [20000, None, 240000, 250000, 90000, 895000, 890072],
    "Performance" : [2.3, 2.5, 5.0, 1.5, 4.7, 3.8, 4.1]
}

df = pd.DataFrame(employee_data)

# Fill Zeros in 
# print(df.fillna(0, inplace=False))

# due to direct change in memory 
# Error -> Invalid value '0' for dtype 'str'. Value should be a string or missing value, got 'int' instead.
# print(df.fillna(0, inplace=True))


df['age'] = df['age'].fillna(df['age'].mean(), inplace=True)
df['salary'] = df['salary'].fillna(df['salary'].mean(), inplace=True)
print(df)
