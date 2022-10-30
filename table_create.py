def create_table_adresar(cursor):
    adresar_structure = ['ime text',
                         'prezime text',
                         'telefon text',
                         'mail text',
                         'godina integer'
                         ]
    create_table(cursor, "adresar", adresar_structure)


def init_insert_adresar(connection, cursor):
    adresar_list = [
        ("Siniša", "Kuna", "098/275-504", "sinisa.kuna@yahoo.com", 1967),
        ("Ivan", "Kuna", "091/2275-504", "ivan.kuna@yahoo.com", 2000)
    ]
    cursor.executemany("insert into adresar values (?,?,?,?,?)", adresar_list)
    connection.commit()


def create_table_pokloni(cursor):
    adresar_structure = ['pokloni text']
    create_table(cursor, "pokloni", adresar_structure)


def init_insert_pokloni(connection, cursor):
    pokloni_list = [("Paket",), ("Torta",)]
    # print(pokloni_list)
    cursor.executemany("insert into pokloni values (?)", pokloni_list)
    connection.commit()


# OVO JE SISTEMSKA FUNKCIJA I NE TREBA JE DIRATI
def create_table(cursor, table_name, table_structure):
    query = "CREATE TABLE " + table_name + "("
    for i in range(0, len(table_structure)):
        query += str(table_structure[i]) + ","

    query = query[0:len(query) - 1] + ")"
    cursor.execute(query)


def inititialize_tables(connection, cursor):
    create_table_adresar(cursor)
    init_insert_adresar(connection, cursor)
    create_table_pokloni(cursor)
    init_insert_pokloni(connection, cursor)
