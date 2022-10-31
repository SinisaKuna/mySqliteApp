def create_table_adresar(cursor):
    adresar_structure = ['ID INTEGER PRIMARY KEY AUTOINCREMENT',
                         'ime text',
                         'prezime text',
                         'ulica text',
                         'posta text',
                         'grad text',
                         'telefon text',
                         'mail text'
                         ]
    create_table(cursor, "adresar", adresar_structure)

def init_insert_adresar(connection, cursor):
    adresar_list = [
        ("Siniša", "Kuna", "Stonska 9", "31000", "Osijek", "098/275-504", "kuna.sinisa@gmail.com"),
        ("Ivan", "Kuna", "Hreljinska 19a", "10000", "Zagreb", "091/2275-504", "ivan.kuna@yahoo.com")
    ]
    polja = "ime, prezime, ulica, posta, grad, telefon, mail"
    for redak in adresar_list:
        query = "insert into adresar (" + str(polja) + ") values " + str(redak)
        cursor.execute(query)
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

    # samo zbog testiranja se pri kreiranju tablice upisuju podaci
    init_insert_adresar(connection, cursor)
