import pandas as pd

employee_data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, 22, 23, 34, 67, 89, 90],
    "salary" : [2000, 23000, 24000, 25000, 9000, 89500, 89072],
    "Performance" : [2.3, 2.4, 5.0, 1.5, 4.7, 3.8, 4.1]
}


df = pd.DataFrame(employee_data)
# update one value in table/data df.loc[row_index, Column_Name] = new Value

# df.loc[6, 'salary'] = 70000
# print(df)

# update the whole column
df['salary'] = df["salary"] * 1.05
# print(df)

