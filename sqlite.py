import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# Drop Table
c.execute("DROP TABLE customers")
conn.commit()

# Query the database 
c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for item in items:
    print(item)

# commit our command
conn.commit()

# close our connection
conn.close()