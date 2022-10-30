import os
import sqlite3
import table_create

data_base_name = 'mysqlite.db'


# # PAZI: FORSIRANO BRIŠEM mysqlite.db = TESTIRANJE
# if os.path.exists(data_base_name):
#     os.remove(data_base_name)

if os.path.exists(data_base_name):
    connection = sqlite3.connect(data_base_name)
    cursor = connection.cursor()
else:
    connection = sqlite3.connect(data_base_name)
    cursor = connection.cursor()
    table_create.inititialize_tables(connection, cursor)


print("********************************************************")
for row in cursor.execute("select * from adresar"):
    print(row)

print("********************************************************")
for row in cursor.execute("select * from pokloni"):
    print(row)







