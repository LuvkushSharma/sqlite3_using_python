import sqlite3

# Step-1 : Connection making
connection = sqlite3.connect('customer.db')

# Step-2 : Cursor making
c = connection.cursor() 

# ------------------------------ Droping the table --------------------------

sql_printing = """

   DROP TABLE customers

"""

# Executing the dropping commands
c.execute(sql_printing)

# Commiting the dropped records
connection.commit()



# ----------------------------- Viewing the table ---------------------------

c.execute("SELECT rowid, * FROM customers")

items = c.fetchall()

for i in items:
    print(i)

# Commiting our records
connection.commit()

# Close our connection
connection.close()

