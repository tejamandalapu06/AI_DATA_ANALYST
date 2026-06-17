from config import get_connection

conn = get_connection()
cursor = conn.cursor()

# Total Sales
cursor.execute("""
SELECT SUM(SALES_AMOUNT)
FROM SALES
""")

print("Total Sales:")
print(cursor.fetchone()[0])

# Top Product
cursor.execute("""
SELECT PRODUCT, SALES_AMOUNT
FROM SALES
ORDER BY SALES_AMOUNT DESC
LIMIT 1
""")

print("\nTop Product:")
print(cursor.fetchone())

# Sales by Region
cursor.execute("""
SELECT REGION,
       SUM(SALES_AMOUNT)
FROM SALES
GROUP BY REGION
ORDER BY 2 DESC
""")

print("\nSales By Region:")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
