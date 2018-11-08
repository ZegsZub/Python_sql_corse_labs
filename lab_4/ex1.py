# lab №4 ex. 1 | Var 1 Sergey Zubrilin 11/10/18


from matplotlib import pyplot as plt
import pandas as pd


file_to_read = 'brexit_sth.csv'
df = pd.read_csv(file_to_read, index_col='Unnamed: 0')

res = df.groupby('age').sum()

res.plot(kind='bar', width=1, figsize=[16, 8])
plt.savefig('ex1_bar.png', dpi=100, bbox_inches='tight')
