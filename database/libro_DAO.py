from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_generi(self) -> list[str] | None:
        cnx = DBConnect.get_connection()
        result = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere"
            cursor.execute(query)
            for row in cursor:
                result.append(row["genere"])
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore: impossibile connettersi al database.")
            return None

    def get_libri_filtrati(self, id_biblioteca: int | None = None, genere: str | None = None) -> list[Libro] | None:
        cnx = DBConnect.get_connection()
        result = []
        query = """
            SELECT * FROM libro
            WHERE (%s IS NULL OR id_biblioteca = %s)
              AND (%s IS NULL OR genere = %s)
            ORDER BY titolo
        """
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, (id_biblioteca, id_biblioteca, genere, genere))
            for row in cursor:
                result.append(
                    Libro(
                        id=row["id"],
                        titolo=row["titolo"],
                        autore=row["autore"],
                        genere=row["genere"],
                        anno_pubblicazione=row["anno_pubblicazione"],
                        id_biblioteca=row["id_biblioteca"]
                    )
                )
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore: impossibile connettersi al database.")
            return None