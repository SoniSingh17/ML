import sqlite3
import pandas as pd

conn = sqlite3.connect("sample.db")
df = pd.read_sql_query("SELECT * FROM users", conn)
print(df)
conn.close()
