import sqlite3

# Step-1 : Connection making
connection = sqlite3.connect('customer.db')

# Step-2 : Cursor making
c = connection.cursor() 


# ------------------------- Order By our records --------------------------

# Default ordering is in ascending order i.e ASC
# We can also order by last name and it will be arranged in Lexicographical order i.e Alphabetical order.

sql_printing = """

   SELECT rowid , * FROM customers
   ORDER BY rowid DESC

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

