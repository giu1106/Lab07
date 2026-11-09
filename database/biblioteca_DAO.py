from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self) -> list[Biblioteca] | None:
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM biblioteca ORDER BY nome"
            cursor.execute(query)
            for row in cursor:
                result.append(
                    Biblioteca(
                        id=row["id"],
                        nome=row["nome"],
                        indirizzo=row["indirizzo"]
                    )
                )
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore: impossibile connettersi al database.")
            return None