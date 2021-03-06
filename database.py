import sqlite3

# conn = sqlite3.connect(':memory:')

# Query the database and return all records
def show_all():
    # connect to database and create cursor
    conn = sqlite3.connect('customer.db')
    # create a cursor
    c = conn.cursor()
    #  Query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()


# Add a new record to the table
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    conn.commit()
    conn.close()

# Add many Records to the table:
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

# Delete Record from table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)

    conn.commit()
    conn.close()


# Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    # commit and close connection
    conn.commit()
    conn.close()


