import sqlite3

# Step-1 : Connection making
connection = sqlite3.connect('customer.db')

# Step-2 : Cursor making
c = connection.cursor() 


sql_printing = """

   SELECT rowid , * FROM customers
   WHERE last_name LIKE 'Ti%' AND first_name LIKE '%h'

"""

# Executing the commands
c.execute(sql_printing)

items = c.fetchall()

for i in items:
    print(i)

# Commiting our records
connection.commit()

# Close our connection
connection.close()

