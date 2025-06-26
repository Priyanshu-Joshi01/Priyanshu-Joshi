import pandas as pd
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Amit', 'Bina', 'Chetan']
})
print(df1)
df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Score': [80, 90, 100]
})
print(df2)

inner = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Merge:\n", inner)


left = pd.merge(df1, df2, on='ID', how='left')
print("Left Join:\n", left)


right = pd.merge(df1, df2, on='ID', how='right')
print("Right Merge:\n", right)


df1_idx = df1.set_index('ID')
df2_idx = df2.set_index('ID')

joined = df1_idx.join(df2_idx, how='right')
print("Index Join:\n", joined)
