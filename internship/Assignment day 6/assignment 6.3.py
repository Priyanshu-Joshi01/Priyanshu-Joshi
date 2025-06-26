import pandas as pd
df_a = pd.DataFrame({'ID': [1, 2], 'Value': ['X', 'Y']})
print(df_a)
df_b = pd.DataFrame({'ID': [3, 4], 'Value': ['Z', 'W']})
print(df_b)
df_c = pd.DataFrame({'ID': [1, 2, 3, 4], 'Score': [10, 20, 30, 40]})
print(df_c)
combined = pd.concat([df_a, df_b])
print(combined)
result = pd.merge(combined, df_c, on='ID')
print("Final Merged Data:\n", result)


# difference between df.join() and pd.merge()
# df.join() -> 1. Uses index only
#              2.use df1.join(df2)
#              3. didnot support multiple key
#
# pd.merge()  -> 1.Can use column or index
#                2.use pd.merge(df1, df2, on='col')
#                3.support multiple key
#                4.More flexible
#
