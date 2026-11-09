from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO
from model.biblioteca_DTO import Biblioteca
from model.libro_DTO import Libro

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

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca: str | None = None, genere: str | None = None) -> list[Libro] | None:
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        id_bib = None
        if biblioteca is not None and str(biblioteca) != "0" and str(biblioteca) != "Nessun filtro":
            try:
                id_bib = int(biblioteca)
            except ValueError:
                id_bib = None

        gen = None
        if genere is not None and str(genere) != "Nessun filtro":
            gen = str(genere)

        return self._libro_dao.get_libri_filtrati(id_bib, gen)

    def get_generi(self) -> list[str] | None:
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self) -> list[Biblioteca] | None:
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_all_biblioteche()
