import sqlite3

# Step-1 : Connection making
connection = sqlite3.connect('customer.db')

# Step-2 : Cursor making
c = connection.cursor() 


# Query the database

sql = """

   SELECT * FROM customers


"""

c.execute(sql)

# It will fetch the one record from the table
print(c.fetchone())

# Fetching 1st element from the first record or tupple.

# Since we had already fetched vaibhav so, now hemendra will fteched by this function
print(c.fetchone()[0])

# Since hemendra is already fetched hence now anik will be fetched.
print(c.fetchone()[2])

# Fetching all the records from the table.
items = c.fetchall()

for details in items:
    print(details)


# printing details in formatted.
for details in items:
    print("First_Name : " , details[0] , " ,Last_Name " , details[1] , " , Email :  " , details[2])

# Commit our command
connection.commit()


# Close our connection
connection.close()

