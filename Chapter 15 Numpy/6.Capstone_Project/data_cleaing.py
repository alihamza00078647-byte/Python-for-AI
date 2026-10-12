import pandas as pd
import numpy as np


# loading the dataSet
df = pd.read_csv(r"D:\My Code Base\PYTHON CODE\Numpy\myenv\Numpy_Practice\6.Capstone_Project\employees.csv")
# print(df.head()) # print 1st 5 index values
# print(df['salary (INR)'].dtype) # Check salary (INR) Column's data type



# Step 1: Spaces hatao, phir NaN/inf ko real missing value banao
df['salary(INR)'] = df['salary(INR)'].str.strip()
df['salary(INR)'] = df['salary(INR)'].replace({'NaN': np.nan, 'inf': np.nan})
# Step 2: String se number mein convert karo
df['salary(INR)'] = pd.to_numeric(df['salary(INR)'], errors='coerce')



""" Check missing Values """ 
print('Missing Values in each Column')
print(df.isnull().sum())



# Change NaN values of Salary to mean. 
df['salary(INR)'].fillna(df['salary(INR)'].mean(), inplace=True)

# # Change NaN values of performance_rating to median. 
df['performance_rating'].fillna(df['performance_rating'].median(), inplace=True)

# # Replace infinite values with nan
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# # get NaN values take mean(average) then replace that mean values with NaN.
df.fillna(df.mean(numeric_only=True), inplace=True)


# # Remove duplicate records
df.drop_duplicates(inplace=True)


# Remove Negative Value
df['salary(INR)'] = np.where(df['salary(INR)'] < 0, df['salary(INR)'].mean(), df['salary(INR)'])

# handle outliner ( salaries that exceeds the normal limit )
mean_salary = df['salary(INR)'].mean()
std_salary = df['salary(INR)'].std()


# Lower limit of Salary Max
lower_bound = mean_salary - (3 * std_salary)
# Upper limit of Salary Max
upper_bound = mean_salary + (3 * std_salary)


# remove rows where salaries too high or low
df = df[(df['salary(INR)'] >= lower_bound) & (df['salary(INR)'] <= upper_bound)]

# Saving the file
df.to_csv('cleaned_data_file.csv', index=False);

print('data is Cleaned Save file as cleaned_data_file.csv');
