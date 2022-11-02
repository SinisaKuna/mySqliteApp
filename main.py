import os
import sqlite3
import table_create
from adresar import Adresar

data_base_name = 'mysqlite.db'

#
# START uspostavljanje veze sa bazom
#

# START PAZI!!! FORSIRANO BRIŠEM mysqlite.db dok traje TESTIRANJE
if os.path.exists(data_base_name):
    os.remove(data_base_name)
# END

connection = table_create.connect_database(data_base_name)
cursor = connection.cursor()


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
# adresar = Adresar(connection,  temp_id)

# print(f'ime i prezime: {adresar.ime_prezime}')

# temp_id = 1
# print(Adresar(connection,  temp_id).ime_prezime)
#
# adresar = Adresar(connection, temp_id)
# print(f'adresa: {adresar.adresa}')
# #
# adresar = Adresar(connection, temp_id)
# print(f'e-mail: {adresar.mail}')
# #
# telefon = Adresar(connection, temp_id)
# print(f'telefon: {adresar.telefon}')


#
# brišem zapis OK
#
# for row in cursor.execute("select * from adresar"):
#     print(row)
# print("/////////////")
# temp_id = 1
# adresar = Adresar(connection, temp_id)
# adresar.brisi()
#
# # provjera je li obrisano
# for row in cursor.execute("select * from adresar"):
#     print(row)

#
#  mijenjam redak
#
#
# for row in cursor.execute("select * from adresar"):
#     print(row)
# print("///////////////////////")
#
# podaci_za_promjenu = ['Mali', 'Pero', 'Hreljinska 19a', '10000', 'Zagreb', '099/0000-999', 'ivan.kuna@yahoo.com']
# temp_id = 2
# adresar = Adresar(connection, temp_id)
# adresar.promijeni_cijeli_redak(podaci_za_promjenu)
# # # provjera je li promijenjeno
# for row in cursor.execute("select * from adresar"):
#     print(row)

# for row in cursor.execute("select * from adresar"):
#     print(row)
#
# query = "update adresar set telefon='1234567890' where id=2"
# cursor.execute(query)
# connection.commit()
#
# print("///////////////////////")
# for row in cursor.execute("select * from adresar"):
#     print(row)


#
# dodajem zapis u bazu
#
# for row in cursor.execute("select * from adresar"):
#     print(row)
#
# print("///////////////////////")
#
# podaci_za_unos = [('Mali', 'Pero', 'Ulica jablanova bb', '10000', 'Zagreb', '099/0000-999', 'mali.pero@yahoo.com')]
#
# adresar = Adresar(connection, 0)
# adresar.dodaj_cijeli_redak(podaci_za_unos)
# # # provjera je li dodano
# for row in cursor.execute("select * from adresar"):
#     print(row)

for row in cursor.execute("select * from adresar"):
    print(row)
