import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'.venv\Matplotlib_Lectures\7.Project\netflix_dirty_data.csv')

# Check format
# print(df.head())

# print(df.info())
# print(df.describe())


df['release_year'] = pd.to_numeric(df['release_year'] , errors="coerce")
print(df)