import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# Update Records
# c.execute("""UPDATE customers SET first_name = "FirstName"
#              WHERE last_name = "lastname1"
# """)
c.execute("""UPDATE customers SET first_name = "FirstName2"
             WHERE rowid = 4
""")


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