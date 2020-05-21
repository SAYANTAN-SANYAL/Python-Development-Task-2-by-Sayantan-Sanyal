import pandas as pd
df = pd.read_csv("diamonds.csv")
a = df[['cut', 'price']]
b = a.loc[a['cut'] == 'Ideal']
c = a.loc[a['cut'] == 'Premium']
d = a.loc[a['cut'] == 'Good']
e = a.loc[a['cut'] == 'Very Good']
f = a.loc[a['cut'] == 'Fair']
b_max = b['price'].max()
b_min = b['price'].min()
print("Max price of ideal cut is: ",b_max)
print("Min value of ideal cut is: ",b_min)
c_max = c['price'].max()
c_min = c['price'].min()
print("Max price of premium cut is: ",c_max)
print("Min value of premium cut is: ",c_min)
d_max = d['price'].max()
d_min = d['price'].min()
print("Max price of good cut is: ",d_max)
print("Min value of good cut is: ",d_min)
e_max = e['price'].max()
e_min = e['price'].min()
print("Max price of very good cut is: ",e_max)
print("Min value of very good cut is: ",e_min)
f_max = f['price'].max()
f_min = f['price'].min()
print("Max price of fair cut is: ",f_max)
print("Min value of fair cut is: ",f_min) 