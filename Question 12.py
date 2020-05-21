import pandas as pd
df = pd.read_csv("diamonds.csv")
print("Shape of original dataframe is:")
print(df.shape)
print("\nSample 75% of diamonds DataFrame's rows without replacement:")
result = df.sample(frac=0.75, random_state=99)
print(result)
print("\n Remaining 25% of the rows:")
temp = df.loc[~df.index.isin(result.index), :]
print(temp) 