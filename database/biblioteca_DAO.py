from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def read_libraries_from_db(self): #legge tutte le biblioteche
        cnx = DBConnect.get_connection()
        if cnx is None:
            raise ConnectionError("Connessione fallita")

        cursor= None
        try:
            query = f"""SELECT b.*
                       FROM biblioteca b
                    """
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)
            return result  #lista delle biblioteche
        finally:
            if cursor is not None:
                cursor.close()
            cnx.close()