import pandas as pd


employee_data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, 22, 23, 34, 67, 89, 90],
    "salary" : [20000, 230000, 240000, 250000, 90000, 895000, 890072],
    "Performance" : [2.3, 2.4, 5.0, 1.5, 4.7, 3.8, 4.1]
}

df = pd.DataFrame(employee_data)
print(df)

# Insert new Column 1st method
# df['Bonus'] = df['salary'] * 0.2 # 20% increment
# print(df)

# Insert new Column 2nd method
df.insert(0, "empolyee_Id", [1, 2, 3, 4, 5, 6, 7])
print(df)