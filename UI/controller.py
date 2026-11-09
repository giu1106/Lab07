import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    def popola_dropdown(self):
        self._view.dd_biblioteca.options.clear()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option(key="0", text="Nessun filtro"))

        biblioteche = self._model.get_biblioteche()
        if biblioteche is not None:
            for b in biblioteche:
                self._view.dd_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))
        else:
            self._view.show_alert("❌ Errore nella lettura delle biblioteche dal database.")

        self._view.dd_genere.options.clear()
        self._view.dd_genere.options.append(ft.dropdown.Option(key="Nessun filtro", text="Nessun filtro"))

        generi = self._model.get_generi()
        if generi is not None:
            for g in generi:
                self._view.dd_genere.options.append(ft.dropdown.Option(key=g, text=g))
        else:
            self._view.show_alert("❌ Errore nella lettura dei generi dal database.")

        self._view.update()

    def seleziona_biblioteca(self, e):
        val = self._view.dd_biblioteca.value
        if val == "0" or val == "Nessun filtro" or val is None:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = val

    def seleziona_genere(self, e):
        val = self._view.dd_genere.value
        if val == "Nessun filtro" or val is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = val

    def mostra_libri(self, e):
        self._view.lista_libri.controls.clear()
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if libri is None:
            self._view.show_alert("❌ Impossibile connettersi al database.")
        elif len(libri) == 0:
            self._view.show_alert("❌ Nessun libro trovato per i criteri di filtraggio specificati.")
        else:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(f"📖 {libro}"))

        self._view.update()