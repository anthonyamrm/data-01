import pandas as pd

df_market = pd.read_csv('supermarket_sales.csv', sep = ';')
df_market

df_market['Total'] = df_market['Total'].str.replace(',','.').astype(float)
df_market['Rating'] = df_market['Rating'].str.replace(',','.').astype(float)
df_market.groupby("Branch")["Rating"].mean()


df_market["Date"] = pd.to_datetime(df_market["Date"])

a = df_market.groupby('Date')['Total'].sum()
print(a)

b = df_market.groupby('Product line')['Total'].sum()
print(b)

c = df_market.groupby("Branch")['Total'].sum()
print(c)

d = df_market.groupby("Payment")['Total'].sum()
print(d)

df_market.info()