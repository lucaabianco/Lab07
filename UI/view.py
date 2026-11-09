import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    NESSUN_FILTRO = "__NESSUN_FILTRO__"

    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        #inizializzo il toggle
        self.toggle_cambia_tema = None

        #inizializzo i dropdown
        self.dd_biblioteca = None
        self.dd_genere = None
        self.lv_libri = None


    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO

        self.dd_biblioteca = ft.Dropdown(label="Biblioteca", width=500, value=self.NESSUN_FILTRO,options=[ft.DropdownOption(key=self.NESSUN_FILTRO, text="Nessun filtro")],
            on_select=self.controller.handler_btn_sel_biblioteca)

        self.dd_genere = ft.Dropdown(
            label="Genere", width=200,
            value=self.NESSUN_FILTRO,
            options=[ft.DropdownOption(key=self.NESSUN_FILTRO, text="Nessun filtro")],
            on_select=self.controller.handler_btn_sel_genere,
        )


        row_sect_2 = ft.Row([self.dd_biblioteca, self.dd_genere],
                     alignment = ft.MainAxisAlignment.CENTER)

        # Sezione 3: Libri
        # TODO
        btn_mostra_libri = ft.Button(content = "Mostra libri",
                                     on_click=self.controller.handler_btn_mostra_libri)

        self.lv_libri = ft.ListView(height=420, width=900, spacing=5, padding=10)



        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            row_sect_2,
            ft.Divider(),

            # Sezione 3: Libri
            # TODO
            btn_mostra_libri,
            ft.Divider(),
            self.lv_libri,
            ft.Divider()
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def popola_biblioteche(self, biblioteche):
        """Aggiunge le biblioteche al relativo dropdown."""
        self.dd_biblioteca.options = [ft.DropdownOption(key=self.NESSUN_FILTRO, text="Nessun filtro")]
        for biblioteca in biblioteche:
            self.dd_biblioteca.options.append(ft.DropdownOption(key=str(biblioteca.id), text=biblioteca.nome))



    def popola_generi(self, generi):
        """Aggiunge tutti i generi distinti al relativo dropdown."""
        self.dd_genere.options = [ft.DropdownOption(key=self.NESSUN_FILTRO, text="Nessun filtro")]
        for genere in generi:
            self.dd_genere.options.append(ft.DropdownOption(key=genere, text=genere))

    def mostra_libri(self, libri, nomi_biblioteche):
        """Mostra i libri filtrati dal Model"""
        self.lv_libri.controls.clear()

        for libro in libri:
            nome_biblioteca = nomi_biblioteche.get(libro.id_biblioteca, str(libro.id_biblioteca))

            anno = libro.anno_pubblicazione
            self.lv_libri.controls.append(ft.ListTile(title=ft.Text(libro.titolo),subtitle=ft.Text(
                                                                        f"Autore: {libro.autore} | Genere: {libro.genere} | "
                                                                        f"Anno: {anno} | Biblioteca: {nome_biblioteca}"),))
        self.page.update()


    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
