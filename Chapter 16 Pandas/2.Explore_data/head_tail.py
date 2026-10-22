import pandas as pd

"""
** Why we Need Data Analysis **
1. Understand The data Set
2. Identify the Problems in Data
3. Plan Next Steps
"""

df = pd.read_json('.venv\Pandas_Lectures\demo.json')
# head(n) method print the first 5 rows.
# n --> No of Rows that gets instead of 5. 
# print(df.head(2))

# tail(n) method print the last 5 rows.
# n --> No of Rows that gets instead of 5. 

print(df.tail(2))