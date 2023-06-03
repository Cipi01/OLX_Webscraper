import pandas as pd

df1 = pd.read_excel('OLX_MOTO_28_05_23.xlsx')
df2 = pd.read_excel('OLX_MOTO_29_05_23.xlsx')

merged_df = pd.merge(df1, df2, how='outer', indicator=True)
unique_rows_df = merged_df[merged_df['_merge'] == 'left_only']
unique_rows_df.to_excel('UniqueRows.xlsx', index=False)
