import sqlite3

# conn = sqlite3.connect(':memory:')

# Query the database and return all records
def show_all():
    # connect to database
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



# print(c.fetchall())




