import sqlite3

# Connect to the database
conn = sqlite3.connect("data_pipeline.db")
cursor = conn.cursor()

# Fetch first 5 rows from transactions table
cursor.execute("SELECT * FROM transactions LIMIT 5")
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close connection
conn.close()
