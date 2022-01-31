import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT rowid, * FROM customers")
# print(c.fetchone())
# print(c.fetchmany(3))

items = c.fetchall()
# print(items)
for item in items:
    print(item)

# print("NAME " + "\t\tEMAIL")
# print("----" + "\t\t-----")
# for item in items:
#     print(item[0] + " " + item[1] + "\t\t" + item[2])


# print("Command executed successfully...")

# commit our command
conn.commit()

# close our connection
conn.close()