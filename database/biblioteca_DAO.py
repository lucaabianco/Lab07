from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO

    def read_libraries_from_db(self): #legge tutte le biblioteche
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = f"""SELECT b.*
                       FROM biblioteca b
                    """
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                biblioteca = Biblioteca(*row)
                result.append(biblioteca)

            cursor.close()
            cnx.close()
            print("Libraries read from database")
            return result  #lista delle librerie

