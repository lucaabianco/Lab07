from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()
        self.lista_biblioteche = []

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        if biblioteca is not None:
            id_biblioteca = int(biblioteca)
        else:
            id_biblioteca = None

        return self._libro_dao.read_book_from_db()

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.read_book_from_db()


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        self.lista_biblioteche = self._biblioteca_dao.read_libraries_from_db()
        return self.lista_biblioteche

"""
if __name__ == '__main__':
    m = Model()
    print(m.get_biblioteche())
"""
