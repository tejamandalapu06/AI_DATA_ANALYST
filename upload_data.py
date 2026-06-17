import pandas as pd
from config import get_connection

# Read CSV
df = pd.read_csv("data/sales.csv")

conn = get_connection()
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO SALES
        (ORDER_ID, PRODUCT, CATEGORY, SALES_AMOUNT, REGION, ORDER_DATE)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            int(row["ORDER_ID"]),
            row["PRODUCT"],
            row["CATEGORY"],
            float(row["SALES_AMOUNT"]),
            row["REGION"],
            row["ORDER_DATE"]
        )
    )

conn.commit()

print("Data Uploaded Successfully!")

cursor.close()
conn.close()