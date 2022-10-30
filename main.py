import os
import sqlite3
import table_create

data_base_name = 'mysqlite.db'

# PAZI: FORSIRANO BRIŠEM mysqlite.db = TESTIRANJE
if os.path.exists(data_base_name):
    os.remove(data_base_name)

if os.path.exists(data_base_name):
    connection = sqlite3.connect(data_base_name)
    cursor = connection.cursor()
else:
    connection = sqlite3.connect(data_base_name)
    cursor = connection.cursor()
    table_create.create_table_adresar(cursor)
    table_create.init_insert_adresar(connection, cursor)







