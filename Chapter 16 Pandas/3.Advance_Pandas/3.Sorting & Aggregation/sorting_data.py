import pandas as pd

"""
1. Sorting Value --> df.sort_values(by="Column Name", ascending=True/False, inplace=True)

2. Sorting Multiple-values --> df.sort_values(by=["Column_Name1", "Column_Name2", ...], ascending=True/False, inplace=True)
-- Sort Multiple Columns but the Sorting is Row wise. It means if we sort name then the whole row with that name sort 
-- ascending or in descending order.
"""
employee_data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, 22, 23, 34, 67, 89, 90],
    "salary" : [20000, 230000, 240000, 250000, 90000, 895000, 890072],
    "Performance" : [2.3, 2.4, 5.0, 1.5, 4.7, 3.8, 4.1]
}


df = pd.DataFrame(employee_data)

# Sort In Ascending Order
# df.sort_values(by='name', ascending=True, inplace=True)
# Sort In Descending Order
# df.sort_values(by='name', ascending=False, inplace=True)


# Sort Multiple Columns but 
df.sort_values(by=['age', 'salary'], ascending=[True, False], inplace=True)
print(df)