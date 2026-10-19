import pandas as pd


""" 
TO Read Data from tha Cloud we use Libraby --> gcsfs
"""
# read files

# df_csv = pd.read_csv(r'D:\My Code Base\PYTHON CODE\Python Librabries\Pandas\.venv\Pandas_Lectures\employees.csv')
# print(df_csv )

# df_json = pd.read_json(r'D:\My Code Base\PYTHON CODE\Python Librabries\Pandas\.venv\Pandas_Lectures\demo.json')
# print(df_json)

df_excel = pd.read_excel(r'D:\My Code Base\PYTHON CODE\Python Librabries\Pandas\.venv\Pandas_Lectures\excel_file.xlsx')
print(df_excel)


