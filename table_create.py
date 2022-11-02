import os
import sqlite3


def connect_database(data_base_name):

    if os.path.exists(data_base_name):
        connection = sqlite3.connect(data_base_name)
    else:
        connection = sqlite3.connect(data_base_name)
        inititialize_tables(connection)
    return connection

def create_table_adresar(connection):
    adresar_structure = ['ID INTEGER PRIMARY KEY AUTOINCREMENT',
                         'ime text',
                         'prezime text',
                         'ulica text',
                         'posta text',
                         'grad text',
                         'telefon text',
                         'mail text'
                         ]
    create_table(connection, "adresar", adresar_structure)


def init_insert_adresar(connection):
    adresar_list = [
        ("Siniša", "Kuna", "Stonska 9", "31000", "Osijek", "098/275-504", "kuna.sinisa@gmail.com"),
        ("Ivan", "Kuna", "Hreljinska 19a", "10000", "Zagreb", "091/2275-504", "ivan.kuna@yahoo.com")
    ]

    # names = [description[0] for description in cursor.description]
    # names = ['ID', 'ime', 'prezime', 'ulica', 'posta', 'grad', 'telefon', 'mail']
    polja = "ime, prezime, ulica, posta, grad, telefon, mail"
    for redak in adresar_list:
        query = "insert into adresar (" + str(polja) + ") values " + str(redak)
        connection.cursor().execute(query)
    connection.commit()


# OVO JE SISTEMSKA FUNKCIJA I NE TREBA JE DIRATI
def create_table(connection, table_name, table_structure):
    query = "CREATE TABLE " + table_name + "("
    for i in range(0, len(table_structure)):
        query += str(table_structure[i]) + ","
    query = query[0:len(query) - 1] + ")"
    connection.cursor().execute(query)


def inititialize_tables(connection):
    create_table_adresar(connection)

    # samo zbog testiranja se pri kreiranju tablice upisuju podaci
    init_insert_adresar(connection)
