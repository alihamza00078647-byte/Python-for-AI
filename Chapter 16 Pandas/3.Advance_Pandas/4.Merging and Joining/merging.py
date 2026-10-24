import pandas as pd

"""
1. syntax -->  pd.merge(dataset1, dataset2, on="Common_Name", how="How to Join")
-- Inner --> # Only return data where key of both is match.
-- outer --> # Return data without caring about whether the keys of both is match or Not? if value is not match 
-- left -->  # left method -> compares right value to left and then Only gives left that matches with right. 
-- right --> # Right method -> compares left value to left and then Only gives left that matches with right.
-- ** cross --> # 1df = m rows,  #2df = n rows,  #m * n rows
"""
customer = {
    "customerID" : [1, 2, 4],
    "name" : ["Ali", "Sufa", "Musa"] 
}

order = {
    "customerID" : [1, 2, 3],
    "orderAmout" : [200, 400, 500]
}

df_customer = pd.DataFrame(customer)
df_order = pd.DataFrame(order)

# print(df_customer)
# print(df_order)

# merged_data_inner = pd.merge(df_customer, df_order, on="customerID", how="inner")
# Only return data where key of both is match.
# print(merged_data_inner)

# merged_data_outer = pd.merge(df_customer, df_order, on="customerID", how="outer")
# Return data without caring about whether the keys of both is match or Not?
# if value is not match 
# print(merged_data_outer)

# merged_data_left = pd.merge(df_customer, df_order, on="customerID", how="left")
# left method -> compares right value to left and then Only gives left that matches with right.
# print(merged_data_left)

# merged_data_right = pd.merge(df_customer, df_order, on="customerID", how="right")
# Right method -> compares left value to left and then Only gives left that matches with right.

# print(merged_data_right)


merged_data_cross = pd.merge(df_customer, df_order, how="cross")
# 1df = m rows
# 2df = n rows
# m * n rows
print(merged_data_cross)