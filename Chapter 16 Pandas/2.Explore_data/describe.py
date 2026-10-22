import pandas as pd


employee_data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem"],
    "age" : [21, 22, 23, 34],
    "salary" : [20000, 230000, 240000, 250000],
    "college" : ["Apna College", "Degree College", "Multan College", "Lahore College"],
    "Coder" : ["harry", "Jerry", "Gerry", "Perry"],
    "Performance" : [2.3, 2.4, 5.0, 1.5]
}


df = pd.DataFrame(employee_data)
# Returns --> count, mean, std, min, 25%, 50%, 75%, max
print(df.describe())
"""
# count --> count the No of values in each Column of your Data
# mean --> find the average value of your Data
# std --> find the standard deviation of your Data
# 25% --> first 25% data avg.
# 50% --> Next 25% data avg.
# 75% --> Next 75% data avg.
# max --> Max value of data
"""




