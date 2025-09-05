import sqlite3


# def dict_factory(cursor, row):
#     fields = [x[0] for x in cursor.description]
#     return {key: value for key, value in zip(fields, row)}

connection = sqlite3.connect('/home/abdullah-saeed/Documents/SQLite/test.db')
# connection.row_factory = dict_factory
cursor = connection.cursor()

cursor.execute("select * from cars where upper(manufacturer) like '_UDI' or upper(manufacturer) like '_MW'")

print(cursor.fetchall())

connection.commit()
connection.close()