import numpy as np
import pandas as pd


csv_file = pd.read_csv('.venv\Pandas_Lectures\employees.csv')


# checking summary of file.
print(csv_file.info())


csv_file['age'].fillna(csv_file['age'].mean(), axis=0, inplace=True)
# print(age_data)



# perData = csv_file['performance_rating'].fillna(csv_file['performance_rating'].mean(), axis=0, inplace=True)
# print(perData)
csv_file['performance_rating'].fillna(csv_file['performance_rating'].mean(), axis=0, inplace=True)


csv_file.to_json(r'.venv\Pandas_Lectures\4.Projects\filterData.json')




