import os
class Adresar:

    def __init__(self, connection, cursor, id):
        self.connection = connection
        self.cursor = cursor
        self.id = id

    @property
    def ime_prezime(self):
        query = 'select (ime || " " || prezime) from adresar where id=' + str(self.id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    @property
    def adresa(self):
        query = 'select (ulica || ", " || posta || " " || grad) from adresar where id=' + str(self.id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    @property
    def mail(self):
        query = "select mail from adresar where id=" + str(self.id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    @property
    def telefon(self):
        query = 'select telefon from adresar where id=' + str(self.id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    @property
    def redak(self):
        query = "select * from adresar where id=" + str(self.id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def brisi(self):
        query = 'delete from adresar where id=' + str(self.id)
        self.cursor.execute(query)

    def promijeni_cijeli_redak(self, adresar_list):
        polja = [description[0] for description in self.cursor.description]
        query = "update adresar set "
        for i in range(1, len(polja)):
            query += polja[i] + " = '" + adresar_list[i-1] + "', "
        query = query[0:len(query) - 2] + " where  id = " + str(self.id)
        self.cursor.execute(query)
        self.connection.commit()

    def dodaj_cijeli_redak(self, adresar_list):
        polja = "ime, prezime, ulica, posta, grad, telefon, mail"
        for redak in adresar_list:
            query = "insert into adresar (" + str(polja) + ") values " + str(redak)
            self.cursor.execute(query)
            self.connection.commit()








