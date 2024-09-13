import sqlite3

# Step-1 : Connection making
connection = sqlite3.connect('customer.db')

# Step-2 : Cursor making
c = connection.cursor() 




# Writing sql commands
sql_commands = """

            INSERT INTO customers VALUES(

               'John' , 'Elder' , 'john@sqlite3.com',
               'Luvkush' , 'Sharma' , 'luvkushSharma@agra.com

            );

"""



# In case of many records we can make tuples and use c.executemany() function for that.
many_customers = [

    ('Vaibhav' , 'Chauhan' , 'vaibhav@gmail.com'),
    ('Hemendra' , 'Yadav' , 'hemendra@gmail.com'),
    ('Anik' , 'Roy' , 'anikroy@gmail.com'),
    ('Ayush' , 'Tiwari' , 'ayushTiwari@gmail.com'),
    ('Ayush' , 'Sharma' , 'ayushSharma@gmail.com'),
]

sql_many = """

        INSERT INTO customers VALUES (? , ? , ?)


"""



try:
    #  c.execute(sql_commands)

    # In case of many Customers
    c.executemany(sql_many , many_customers)

    connection.commit()
    print("Command executed and Commited successfully.")

except:
    connection.rollback()
    print("Commands are rollbacking due to some error.")

finally:
    connection.close()    