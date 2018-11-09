# lab №4 ex. 4 | Var 1 Sergey Zubrilin 11/10/18


import pandas as pd


file_to_read = 'filter1.xlsx'
df = pd.read_excel(file_to_read)

df.insert(df.shape[1], 'Surplas', [(df.at[x, 'Meters']-(10+(21*df.at[x, 'Quantity_of_people'])))
                                   if df.at[x, 'Meters']-(10+(21*df.at[x, 'Quantity_of_people'])) > 0 else 0
                                   for x in range(df.shape[0])])

pd.options.display.max_columns = 10
pd.options.display.max_rows = 50


df1 = df.loc[df.Privileges == "yes"]
df2 = df.loc[(df.Privileges == "yes") & (df.Surplas == 0)]
df3 = df.loc[(df.Meters > 100)]
df4 = df.loc[(df.Year_of_registration > 1950) & (df.Year_of_registration < 1970)]
df5 = df.loc[(df.Privileges == "yes") & (df.Year_of_registration > 1960)]

df6_1 = df.loc[(df.Privileges == "yes") & (df.Surplas != 0)]
df6_2 = df.loc[(df.Year_of_registration < 1957) & (df.Meters < 100)]
df6 = df6_1.append(df6_2, ignore_index=True)

df7_1 = df.loc[(df.Privileges == "no") & (df.Surplas > 50)]
df7_2 = df.loc[(df.Year_of_registration > 1950) & (df.Year_of_registration < 1970) & (df.Meters > 100)]
df7 = df7_1.append(df7_2, ignore_index=True)

df1.to_html('ex2_1_table.html')
df2.to_html('ex2_2_table.html')
df3.to_html('ex2_3_table.html')
df4.to_html('ex2_4_table.html')
df5.to_html('ex2_5_table.html')
df6.to_html('ex2_6_table.html')
df7.to_html('ex2_7_table.html')
