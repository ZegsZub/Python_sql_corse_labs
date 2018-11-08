# lab №4 ex. 2 | Var 1 Sergey Zubrilin 11/10/18


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


file1 = '2008_part.csv'
file2 = 'airports.csv'
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)


pd.options.display.max_columns = 100
pd.options.display.max_rows = 50


CllC = df1.loc[(df1.CancellationCode).notnull()]
res_df = CllC.groupby('CancellationCode').count()


print(f"1) {res_df['Year'].idxmax()}")

print(f"2) {int(df1.Distance.mean()), df1.Distance.min(), df1.Distance.max()}")

print('3)')
indexes_of_strange = df1.loc[df1.Distance == 24].index
stranger = df1.iloc[indexes_of_strange[0]].FlightNum
res = df1.loc[df1.FlightNum == stranger, ['Year', 'Month', 'DayofMonth', 'Distance']]
res = res.set_index(['Year', 'Month', 'DayofMonth'])


fig = plt.figure()
ax = sns.heatmap(res)
plt.show()
fig.savefig('ex4_heatmap.png', dpi=200)

print('4)')
res_df4 = df1.groupby('Origin').count()
max_flights_origin = res_df4.loc[res_df4.Year == res_df4.max()[0]].index[0]
print(df2.loc[df2.iata == max_flights_origin][['airport', 'city']])

print("5)")
airport_with_max_time = df1.groupby('Origin').mean()[['AirTime']].idxmin()[0]
print(df2.loc[df2.iata == airport_with_max_time][['airport']])

print("6)")
DD = df1.loc[df1.DepDelay > 0]
number_flights = df1.groupby('Origin')['Year'].count()
DD_max = pd.DataFrame(df1.groupby('Origin')['DepDelay'].sum())
DD_max_with_cond = DD_max.loc[number_flights[number_flights > 1000].index].idxmax()[0]
print(df2.loc[df2.iata == DD_max_with_cond][['airport']])

