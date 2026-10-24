import pandas as pd

"""
1. Aggregation functions in pandas --> sum(), min(), max(), mean(), count(), std(), variance()

"""

employee_data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem", "Musa", "Adam", "Eve"],
    "age" : [21, 22, 23, 34, 67, 89, 90],
    "salary" : [20000, 230000, 240000, 250000, 90000, 895000, 890072],
    "Performance" : [2.3, 2.4, 5.0, 1.5, 4.7, 3.8, 4.1]
}


df = pd.DataFrame(employee_data)

print(df['salary'].mean())