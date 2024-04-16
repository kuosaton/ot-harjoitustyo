from tkinter import ttk, constants

class StartView:
    def __init__(self, root, handle_budget_creation):
        self._root = root
        self._handle_budget_creation = handle_budget_creation 
        self._frame = None

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    # Initialize name field for creating budget
    def _create_budget_name_field(self):
        budget_name_label = ttk.Label(master=self._frame, text="Name of budget:")
        self._budget_name_entry = ttk.Entry(master=self._frame)

        budget_name_label.pack()
        self._budget_name_entry.pack()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(master=self._frame, text="Welcome! Create a budget below.")
        title_label.pack()

        self._create_budget_name_field()

        create_budget_button = ttk.Button(
            master=self._frame,
            text="Create budget",
            command=self._handle_button_click
        )

        create_budget_button.pack()

    # Fetch budget name input and call budget creation function
    def _handle_button_click(self):
        budget_name_entry = self._budget_name_entry.get()
        self._handle_budget_creation(budget_name_entry)
