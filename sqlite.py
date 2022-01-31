import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# Query the database
# c.execute("SELECT * FROM customers WHERE last_name = 'Punchithaya'")
c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com'")

items = c.fetchall()
# print(items)
for item in items:
    print(item)

# commit our command
conn.commit()

# close our connection
conn.close()