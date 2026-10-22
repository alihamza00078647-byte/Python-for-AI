import pandas as pd

"""
*** Problems ? *** 
1. How many rows and columns  
2. What type of data available in Columns ( Columns data types )
3. what are the missing values
4. Not Null values Counts
"""

# info method is sovle the Issues

df = pd.read_json('.venv\Pandas_Lectures\demo.json')
# Provide the Summary of data
print(df.info())



