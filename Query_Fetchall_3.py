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

# print(c.fetchone())
# print(c.fetchmany(2))
print(c.fetchall())

print("Command executed succesfully.")

# Commit our command
connection.commit()


# Close our connection
connection.close()


"""
C:\Users\Luvkush sharma>cd "C:\Users\Luvkush sharma\Desktop\DBMS\Sqlite"

C:\Users\Luvkush sharma\Desktop\DBMS\Sqlite>python Query_Fetchall.py
[('Vaibhav', 'Chauhan', 'vaibhav@gmail.com'), ('Hemendra', 'Yadav', 'hemendra@gmail.com'), ('Anik', 'Roy', 'anikroy@gmail.com'), ('Vaibhav', 'Chauhan', 'vaibhav@gmail.com'), ('Hemendra', 'Yadav', 'hemendra@gmail.com'), ('Anik', 'Roy', 'anikroy@gmail.com')]
Command executed succesfully.


"""