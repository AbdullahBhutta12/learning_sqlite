import sqlite3

connection = sqlite3.connect('/home/abdullah-saeed/Documents/SQLite/test.db')
cursor = connection.cursor()

many_cars = [("Ford", "F150", 4),
             ("BMW", "M3", 4),
             ("Audi", "R8", 2),
             ("Lamborghini", "Huracan", 2)
             ]

sql ="insert into cars(manufacturer, model, number_of_doors) values('Kia', 'Serrento', 4)"

cursor.executemany("insert into cars(manufacturer, model, number_of_doors) values(?,?,?)", many_cars)
# peoples = cursor.fetchall()
# for people in peoples:
#     print(people[1])
connection.commit()
connection.close()