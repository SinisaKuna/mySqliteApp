def create_table_adresar(cursor):
    adresar_structure = [
        (['ime'], ['text']),
        (['prezime'], ['text']),
        (['telefon'], ['text']),
        (['mail'], ['text']),
        (['godina'], ['integer'])
    ]
    create_table(cursor, "adresar", adresar_structure)


def create_table(cursor, table_name, table_structure):
    query = "CREATE TABLE " + table_name + "("
    for i in range(0, len(table_structure)):
        query += str(table_structure[i][0]) + " " + str(table_structure[i][1]) + ";"
    query = query[0:len(query) - 1] + ")"
    query = query.replace("[", "")
    query = query.replace("]", "")
    query = query.replace(";", ",")
    cursor.execute(query)


def init_insert_adresar(connection, cursor):
    adresar_list = [
                    ("Siniša", "Kuna", "098/275-504", "sinisa.kuna@yahoo.com", 1967),
                    ("Ivan", "Kuna", "091/2275-504", "ivan.kuna@yahoo.com", 2000)
                    ]
    cursor.executemany("insert into adresar values (?,?,?,?,?)", adresar_list)
    connection.commit()
