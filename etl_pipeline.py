import pandas as pd
import sqlite3

# 1) EXTRACT
df = pd.read_csv("Superstore.csv")
print("Rows extracted:", len(df))

# 2) TRANSFORM (clean + enrich)
df = df.dropna()

df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
df = df.dropna(subset=["OrderDate"])

df["Revenue"] = df["Sales"] * df["Quantity"]
print("Rows after cleaning:", len(df))

# 3) LOAD (to SQLite DB)
conn = sqlite3.connect("sales.db")
df.to_sql("sales_data", conn, if_exists="replace", index=False)

# 4) VALIDATE
rows_in_db = conn.execute("SELECT COUNT(*) FROM sales_data").fetchone()[0]
print("Rows loaded to DB:", rows_in_db)

conn.close()
print("ETL completed ✅")
