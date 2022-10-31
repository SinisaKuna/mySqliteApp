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

#
# ispisujem cijelu tablicu
#
# for row in cursor.execute("select * from adresar"):
#     print(row)
#

#
# ispisujem polja pomocu klase Adresar() za zadani id OK
#
# temp_id = 1
#
# adresar = Adresar(connection, cursor, temp_id)
# print(f'ime i prezime: {adresar.ime_prezime[0][0]}')
#
# adresar = Adresar(connection, cursor, temp_id)
# print(f'adresa: {adresar.adresa[0][0]}')
#
# adresar = Adresar(connection, cursor, temp_id)
# print(f'e-mail: {adresar.mail[0][0]}')
#
# telefon = Adresar(connection, cursor, temp_id)
# print(f'telefon: {adresar.telefon[0][0]}')


#
# brišem zapis OK
#
# temp_id = 1
# adresar = Adresar(connection, cursor, temp_id)
# adresar.brisi()
# # provjer je li obrisano
# for row in cursor.execute("select * from adresar"):
#     print(row)

#
#  mijenjam redak
#
#
for row in cursor.execute("select * from adresar"):
    print(row)
print("///////////////////////")

podaci_za_promjenu = ['Mali', 'Pero', 'Hreljinska 19a', '10000', 'Zagreb', '091/2275-504', 'ivan.kuna@yahoo.com']

adresar = Adresar(connection, cursor, 2)
adresar.promijeni_cijeli_redak(podaci_za_promjenu)
# # provjera je li promijenjeno
for row in cursor.execute("select * from adresar"):
    print(row)

# text = 'd sdf'
# repl = text.replace()
