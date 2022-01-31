import sqlite3

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor
c = conn.cursor()

many_customer = [
                    ('name1','lastname1','name1@gmail.com'),
                    ('name2','lastname2','name2@gmail.com'), 
                    ('name3','lastname3','name3@gmail.com')
                ]

# c.execute("INSERT INTO customers VALUES ('Name2', 'Lastname2', 'name2@gmail.com')")
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)

print("Command executed successfully...")

# commit our command
conn.commit()

# close our connection
conn.close()