import sqlite3
# # Data types: NULL  INTEGER  REAL  TEXT  BLOB



# conn = sqlite3.connect('customer.db')
#
# c = conn.cursor()

# # create a table
# c.execute("""CREATE TABLE customers (
#     first_name TEXT,
#     last_name TEXT,
#     email TEXT
#     )""")

# c.execute("INSERT INTO customers VALUES ('Qasim', 'Bilal', 'qasim@gmail.com')")          # insert one record into table
#
# many_customers = [                                                                   # insert many records into table
#                 ("Basit", "Ali", "basit@fake.com"),
#                 ("Babar", "Aslam", "babar@fake.com"),
#                 ("Azam", "Khan", "azam@khan.com")
#                 ]

# insert = "INSERT INTO customers VALUES (?,?,?)"
# c.executemany(insert, many_customers)


# Query the database

# c.execute("SELECT * FROM customers")
# # print(c.fetchmany(3))
# # print(c.fetchone())
#
# items = c.fetchall()
# print("Name" + "\t\tEmail")
# print("-----" + "\t\t------")
# for item in items:
#     print(item[0] +" "+ item[1] +"\t"+ item[2])


# Primary key

# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# for item in items:
#     print(item)


# Where clause

# c.execute("SELECT * FROM customers WHERE last_name = 'Ali'") # WHERE age >= 20
# items = c.fetchall()
# for item in items:
#     print(item)

# Update record
# c.execute("""UPDATE customers SET first_name = 'Ali'
#             WHERE rowid = 1
# """)

# Delete record
# c.execute("DELETE FROM customers WHERE rowid = 18")
# c.execute("SELECT rowid, * FROM customers")

# ORDER BY
# c.execute("SELECT rowid, * FROM customers ORDER BY first_name DESC")

# And/Or
# c.execute("SELECT rowid, * FROM customers WHERE last_name = 'Ali' AND rowid = 3")

# Drop/delete table
# # c.execute("DROP TABLE customers")

# Limiting result
# c.execute("SELECT rowid, * FROM customers LIMIT 3")
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

# c.execute("SELECT rowid, * FROM customers")
# items = c.fetchall()
# for item in items:
#     print(item)
#
# print("Command executed successfully")
#
# conn.commit()
# conn.close()



