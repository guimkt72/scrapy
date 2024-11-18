import pandas as pd
import sqlite3
from datetime import datetime



df = pd.read_json('rtx.json')


print(df.columns)


df['brand'] = df['brand'].astype(str)
df['_date_collect'] = datetime.now()
df['price'] = round(df['price'],3)
#df['price'] = df['price'].astype(str)
#df['price'] = df['price'].str.replace('.', '')
#df['price'] = df['price'].astype(int)

df['internacional'] = df['internacional'].fillna('Não Internacional')

df.drop(columns=['full'], inplace=True)

print(df)

conn = sqlite3.connect("example.db")

df.to_sql('rtx_items', conn, if_exists='replace', index=False)

conn.close()