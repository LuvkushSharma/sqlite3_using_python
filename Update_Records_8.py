import sqlite3

# Step-1 : Connection making
connection = sqlite3.connect('customer.db')

# Step-2 : Cursor making
c = connection.cursor() 


# ------------------------- Updating the records --------------------------

sql_commands = """

        UPDATE customers 
        SET first_name = 'Luvkush' 
        WHERE last_name = 'Sharma'

"""


# Executing the sql commands
c.execute(sql_commands)

# Commit our Updating command
connection.commit()

#  ------------------ Printing the records --------------------------

sql_printing = """

   SELECT rowid , * FROM customers

"""

# Executing the select command
c.execute(sql_printing)

items = c.fetchall()

for i in items:
    print(i)

# Commiting our printing details commands
connection.commit()


# Close our connection
connection.close()

