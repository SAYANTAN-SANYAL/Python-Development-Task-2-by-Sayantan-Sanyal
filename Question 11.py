import pandas as pd
df = pd.read_csv("diamonds.csv")
duplicateRows = df[df.duplicated(keep="first")]
print(duplicateRows)
a = len(duplicateRows.index)
print("The number of duplicated rows are: ", a) 