
class Adresar:

    def __init__(self, connection, cursor, id):
        self.connection = connection
        self.cursor = cursor
        self.id = id

    @property
    def mail(self):
        query = "select mail from adresar where id=" + str(self.id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

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
    def telefon(self):
        query = 'select telefon from adresar where id=' + str(self.id)
        self.cursor.execute(query)
        return self.cursor.fetchall()

