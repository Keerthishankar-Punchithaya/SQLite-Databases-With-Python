import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()



# Query the database - ORDER BY
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name")
c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Na%' OR rowid = 3")

items = c.fetchall()

for item in items:
    print(item)

# commit our command
conn.commit()

# close our connection
conn.close()