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
    # TODO
    def inizializza(self):
        try:
            biblioteche = self._model.get_biblioteche()
            generi = self._model.get_generi()
        except Exception as exception:
            self._view.show_alert(f"Errore relativo ai filtri")
            return

        self._view.includi_biblioteche(biblioteche)
        self._view.includi_generi(generi)
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def handler_btn_sel_biblioteca(self, e):
        scelta = e.control.value
        if scelta == self._view.NESSUN_FILTRO:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = scelta


    def handler_btn_sel_genere(self, e):
        scelta = e.control.value
        if scelta == self._view.NESSUN_FILTRO:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = scelta



    # AZIONE: MOSTRA LIBRI
    # TODO
    def handler_btn_mostra_libri(self, e):
        try:
            libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        except Exception as exception:
            self._view.show_alert(f"Errore relativo al caricamento dei libri")
            return

        for biblioteca in self._model.lista_biblioteche:
            nomi_biblioteche = {biblioteca.id: biblioteca.nome}
        self._view.mostra_libri(libri, nomi_biblioteche)
        if not libri:
            self._view.show_alert("Nessun libro trovato per i filtri inseriti")
