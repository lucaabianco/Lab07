from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def read_book_from_db(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")
            query = f"SELECT l.* FROM libro l"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []

            for row in cursor:
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
            cnx.close()
            print("All books read from database")
            return result #tutti i libri


    def read_selected_book_from_db(self, genere):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = f"""SELECT l.*
                       FROM libro l
                       WHERE l.genere LIKE '{genere}%'
                    """
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                libro = Libro(*row)
                result.append(libro)

            cursor.close()
            cnx.close()
            print("Books (selected) read from database")
            return result  #lista dei libri selezionati per genere



