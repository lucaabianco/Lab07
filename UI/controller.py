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

    # POPOLA DROPDOWN
    def inizializza(self):
        try:
            biblioteche = self._model.get_biblioteche()
            generi = self._model.get_generi()
        except Exception as exception:
            self._view.show_alert(f"Errore relativo ai filtri")
            return

        self._view.popola_biblioteche(biblioteche)
        self._view.popola_generi(generi)
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def handler_btn_sel_biblioteca(self, e):
        scelta = e.control.value
        self.biblioteca_selezionata = (
            None if scelta in (None, self._view.NESSUN_FILTRO) else scelta
        )

    def handler_btn_sel_genere(self, e):
        scelta = e.control.value
        self.genere_selezionato = (
            None if scelta in (None, self._view.NESSUN_FILTRO) else scelta
        )



    # AZIONE: MOSTRA LIBRI
    # TODO
    def handler_btn_mostra_libri(self, e):
        try:
            libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        except Exception as exception:
            self._view.show_alert(f"Errore relativo al caricamento dei libri")
            return

        nomi_biblioteche = {}

        for biblioteca in self._model.lista_biblioteche:
            nomi_biblioteche[biblioteca.id] = biblioteca.nome


        self._view.mostra_libri(libri, nomi_biblioteche)
        if not libri:
            self._view.show_alert("Nessun libro trovato per i filtri selezionati")
