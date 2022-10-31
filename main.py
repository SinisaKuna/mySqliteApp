import os
import sqlite3
import table_create
from adresar import Adresar

data_base_name = 'mysqlite.db'

#
# START uspostavljanje veze sa bazom
#
# # PAZI: FORSIRANO BRIŠEM mysqlite.db = TESTIRANJE
if os.path.exists(data_base_name):
    os.remove(data_base_name)

if os.path.exists(data_base_name):
    connection = sqlite3.connect(data_base_name)
    cursor = connection.cursor()
else:
    connection = sqlite3.connect(data_base_name)
    cursor = connection.cursor()
    table_create.inititialize_tables(connection, cursor)
#
# END uspostavljanje veze sa bazom
#

#
# testiranje
#

# ispisuje tablicu
print("********************************************************")

for row in cursor.execute("select * from adresar"):
    print(row)

print("********************************************************")

temp_id = 2

adresar = Adresar(connection, cursor, temp_id)
print(f'ime i prezime: {adresar.ime_prezime[0][0]}')

adresar = Adresar(connection, cursor, temp_id)
print(f'adresa: {adresar.adresa[0][0]}')

adresar = Adresar(connection, cursor, temp_id)
print(f'e-mail: {adresar.mail[0][0]}')

telefon = Adresar(connection, cursor, temp_id)
print(f'telefon: {adresar.telefon[0][0]}')
