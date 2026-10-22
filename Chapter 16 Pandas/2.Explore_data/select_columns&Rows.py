import pandas as pd

"""
1-  ** Select Specific Column **
Use Square brackets that returns series or multiple data frames
-- column = df["Column_Name"]
-- subset = df["Column_Name1", "Column_Name2", "Column_Name3"]


2-  ** filter Rows ** 
Using Boolean Conditions Returns specific rows that met the conditions [ boolean indexing ]
-- filtered_Rows = df[df["Salary"] > 50000]

3-  ** Combine multiple conditions **
-- filtered_Rows = df[(df["salary"]  > 50000) & (df["salary"]  < 80000))]
"""

employee_data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, 22, 23, 34, 67, 89, 90],
    "salary" : [20000, 230000, 240000, 250000, 90000, 895000, 890072],
    "Performance" : [2.3, 2.4, 5.0, 1.5, 4.7, 3.8, 4.1]
}


df = pd.DataFrame(employee_data)
# access single Column & return a Series.
# print(df['salary'])


# Select multiple Columns passing list
subset = df[["name","salary"]]
# print(subset)

# filter the Rows by one condition
high_salary = df[df["salary"] == 895000]
# print(high_salary)

# filter the Rows by multiple conditions
high_salaries = df[(df['salary'] > 250000) & (df['salary'] < 895000)]
print(high_salaries)