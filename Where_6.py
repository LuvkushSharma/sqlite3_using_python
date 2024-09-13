import sqlite3

# Step-1 : Connection making
connection = sqlite3.connect('customer.db')

# Step-2 : Cursor making
c = connection.cursor() 


# Query the database

sql = """

   SELECT rowid, * FROM customers where last_name = 'Sharma'


"""

c.execute(sql)

items = c.fetchall()

for i in items:
    print(i)



# Commit our command
connection.commit()


# Close our connection
connection.close()

