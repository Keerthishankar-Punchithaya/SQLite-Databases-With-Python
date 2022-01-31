import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)

print(c.fetchall())


# print("Command executed successfully...")

# commit our command
conn.commit()

# close our connection
conn.close()