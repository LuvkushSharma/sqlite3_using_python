import sqlite3

# Creating database in the memory
# conn = sqlite3.connect(':memory:')

# Creating a database
connection = sqlite3.connect('customer.db')

# To interact with database we have to use the Cursor
# Creating a cursor
c = connection.cursor()

# Now create a table using this cursor for this we have to use the .execute method
# Note : sqlite3 is case-sensitive.

sql = """
       CREATE TABLE customers(

            first_name varchar(15),
            last_name varchar(15),
            email     varchar(15)

    )
    
    
    """

c.execute(sql)
connection.commit()

# try:
#      c.execute(sql)
#      connection.commit()

#      print("Executed and Commited successfully.")

# except:
#      connection.rollback()
#      print("All the commands are rollback due to some error.")

# finally:
#      connection.close()




