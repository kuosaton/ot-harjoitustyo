from tkinter import ttk, constants

class StartView:
    """Sovelluksen aloitusnäkymästä vastaava luokka."""
    def __init__(self, root, handle_budget_creation):
        """Luokan konstruktori. Luo uuden aloitusnäkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_budget_creation: Kutsuttava-arvo, jota kutsutaan kun luodaan uusi budjetti.
        """
        self._root = root
        self._handle_budget_creation = handle_budget_creation 
        self._frame = None

        self._start()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _create_budget_name_field(self):
        """Metodi, joka alustaa nimen syöttökentän uuden budjetin luomista varten."""
        budget_name_label = ttk.Label(master=self._frame, text="Name of budget:")
        self._budget_name_entry = ttk.Entry(master=self._frame)

        budget_name_label.pack()
        self._budget_name_entry.pack()

    def _start(self):
        """Metodi, joka alustaa näkymän."""
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(master=self._frame, text="Welcome! Enter a budget below.")
        title_label.pack()
        create_budget_button_label = ttk.Label(master=self._frame, text="Input a name. If no budget with that name exists, one is created.")

        create_budget_button_label.pack()

        self._create_budget_name_field()

        create_budget_button = ttk.Button(
            master=self._frame,
            text="Enter",
            command=self._handle_button_click
        )

        create_budget_button.pack()

    def _handle_button_click(self):
        """Metodi, joka vastaa käyttäjäsyötteen käsittelystä uuden budjetin luomiseksi."""
        budget_name_entry = self._budget_name_entry.get()
        if budget_name_entry:
            self._handle_budget_creation(budget_name_entry)
