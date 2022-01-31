import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()



# Query the database - AND/OR
# c.execute("SELECT rowid, * FROM customers LIMIT 2")
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

items = c.fetchall()

for item in items:
    print(item)

# commit our command
conn.commit()

# close our connection
conn.close()