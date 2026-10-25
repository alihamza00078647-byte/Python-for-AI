import pandas as pd


df = pd.read_csv('.venv\Pandas_Lectures\employees.csv')

print(df['salary(INR)'].astype(float))

# print(df['age'].astype(int))


df.to_csv(r'.venv\Pandas_Lectures\4.Projects\sample.csv')


# print(df.info())
# print(df['salary(INR)'].dtype())