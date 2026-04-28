import pandas as pd
import sqlite3

df = pd.read_excel("Employees_Data.xlsx")

conn = sqlite3.connect("database.db")
df.to_sql("users", conn, if_exists="replace", index=False)

conn.close()

print("Done")
