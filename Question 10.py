import pandas as pd
df = pd.read_csv("diamonds.csv")
a = len(df.index)
b = len(df.columns)
print(a)
print(b)
df.dropna(axis=0,inplace=True)
print(df) 