import sqlite3

# Step-1 : Connection making
connection = sqlite3.connect('customer.db')

# Step-2 : Cursor making
c = connection.cursor() 


# -------------------------- Limiting the results ----------------------------

# Currently we are having only few records so we are printing them in our result
#  But in the real world problems we are having thousands and millions of records so, in that we case we donot
# want to see all of them.
# Like , if want to just view the few records of a table to geet the insight of it then i will use limit

sql_printing = """

   SELECT rowid , * FROM customers
   LIMIT 2

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

