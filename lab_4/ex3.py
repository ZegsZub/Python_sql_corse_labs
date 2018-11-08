# lab №4 ex. 3 | Var 1 Sergey Zubrilin 11/10/18


import pandas as pd


# читаем данные из исходного csv в DataFrame
sd1 = 'students1.txt'
sd2 = 'students2.txt'
sd3 = 'students3.txt'
df1 = pd.read_csv(sd1, sep='\s+')
df2 = pd.read_csv(sd2, sep='\s+')
df3 = pd.read_csv(sd3, sep='\s+')
df = pd.merge(df1, df2, on='Name', how='outer')
df = pd.merge(df, df3, on='Name', how='outer')


pd.options.display.max_columns = 100
pd.options.display.max_rows = 50


cor_1_2 = round(df.MathAnalysis1.corr(df.MathAnalysis2, method='pearson', min_periods=1), 4)
cor_1_3 = round(df.MathAnalysis1.corr(df.MathAnalysis3, method='pearson', min_periods=1), 4)
cor_2_3 = round(df.MathAnalysis2.corr(df.MathAnalysis3, method='pearson', min_periods=1), 4)

cor_b = round(df.HistoryOfUkraine.corr(df.SpecialProgrammingLanguages, method='pearson', min_periods=1), 4)


def linearity_estimate(cor):
    if cor < 0.5:
        return 'low'
    elif cor > 0.75:
        return 'high'
    elif 0.5 < cor < 0.75:
        return 'medial'


print(f'Сor(Math1, Math2) = {cor_1_2}, {linearity_estimate(cor_1_2)}\n'
      f'Сor(Math1, Math3) = {cor_1_3}, {linearity_estimate(cor_1_3)}\n'
      f'Сor(Math2, Math3) = {cor_2_3}, {linearity_estimate(cor_2_3)}\n'
      f'Сor(Hist, Prog) = {cor_b}, {linearity_estimate(cor_b)}')
