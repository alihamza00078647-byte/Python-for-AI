import pandas as pd

data = {
    "name" : ["Ali", "Waqas", "Sufa", "Saleem"],
    "age" : ["21", "22", "23", "34"],
    "salary" : ["20000", "230000", "240000", "250000"],
    "college" : ["Apna College", "Degree College", "Multan College", "Lahore College"],
    "Coder" : ["harry", "Jerry", "Gerry", "Perry"]
}

# print(data)
df = pd.DataFrame(data)
# print(df)


# if index is false it won't add index Column in File
# df.to_csv(r'.venv\Pandas_Lectures\Introduction\output.csv', index=False)
# df.to_excel(r'.venv\Pandas_Lectures\Introduction\output2.xlsx', index=False)
df.to_json(r'.venv\Pandas_Lectures\Introduction\output3.json', index=False)

