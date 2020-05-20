import pandas as pd
df = pd.read_csv("diamonds.csv")
a = df[['carat', 'color']]
print(a)
b = df.iloc[4]
print(b) 