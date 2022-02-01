import database

# delete a record from the database 
# use rowid as string
# database.delete_one('8')


# Lookup Email Address Record
database.email_lookup("name1@gmail.com")

# Add many records
# stuff = [
#     ('name8','lastname8','name8@gmail.com'),
#     ('name9','lastname9','name9@gmail.com')
# ]

# database.add_many(stuff)

# show all the records
# database.show_all()