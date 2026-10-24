import pandas as pd

"""
1. First We Group the Data. groupby() merge the duplicate and calculate the mean and assign them
 ** output ** 
-- 21  --   260000
-- 22  --   230000
-- 34  --  1145000
-- 40  --   980072

"""

employee_data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, 22, 21, 34, 40, 34, 40],
    "salary" : [20000, 230000, 240000, 250000, 90000, 895000, 890072]
}

df = pd.DataFrame(employee_data)
# grouped = df.groupby('age')['salary'].sum()
# print(grouped)
groupedMulti = df.groupby(['age', 'name'])['salary'].sum()



print(groupedMulti)