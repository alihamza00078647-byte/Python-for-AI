import pandas as pd
"""
 ** Concatinating Data **
1. vertically (row-wise)
2. horizontally (column-wise)
 
method --> pd.concate([df1, df2], axis=0, ignore_index=True)
[df1, df2] --> stack them row wise
axis=0 --> Operate on row, axis=1 Operate Column wise
ingore_index = True
"""

df_region1 = pd.DataFrame({
    "customerID" : [1, 2],
    "Name" : ["Abu Rmsa", "Zain"]
})

df_region2 = pd.DataFrame({
    "customerID" : [4, 6],
    "Name" : ["Afaam", "Talha"]
})

# 
concat_row_wise = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)

concat_row_wise = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)
print(concat_row_wise)

