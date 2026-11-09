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

        if cnx is None:
            raise ConnectionError("Connessione fallita")

        cursor= None
        try:
            query = f"SELECT l.* FROM libro l"

            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                libro = Libro(*row)
                result.append(libro)
            return result #tutti i libri
        finally:
            if cursor is not None:
                cursor.close()
            cnx.close()



    def read_selected_book_from_db(self, genere, id_biblioteca):
        cnx = DBConnect.get_connection()
        if cnx is None:
            raise ConnectionError("Connessione fallita")

        cursor = None
        try:
            query = f"""
                        SELECT l.id, l.titolo, l.autore, l.genere,
                       l.anno_pubblicazione, l.id_biblioteca
                       FROM libro l
                       WHERE l.genere = COALESCE(%s, l.genere) 
                       AND l.id_biblioteca = COALESCE(%s, l.id_biblioteca)
                       ORDER BY l.titolo, l.id 
                    """
            cursor = cnx.cursor()
            cursor.execute(query, (genere, id_biblioteca))
            result = []
            for row in cursor:
                libro = Libro(*row)
                result.append(libro)
            return result

        finally:
            if cursor is not None:
                cursor.close()
            cnx.close()

    def read_genres_from_db(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            raise ConnectionError("Connessione fallita")

        cursor = None
        try:
            query = """
                    SELECT DISTINCT l.genere
                    FROM libro l
                    WHERE l.genere IS NOT NULL
                    ORDER BY l.genere                   
                    """
            cursor = cnx.cursor()
            cursor.execute(query)

            result = []
            for row in cursor:
                result.append(row[0])
        finally:
            if cursor is not None:
                cursor.close()
            cnx.close()
