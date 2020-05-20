import pandas as pd
df = pd.read_csv("diamonds.csv")
print("The dataframe is: ",df)
rows = df.head(5)
print(rows)