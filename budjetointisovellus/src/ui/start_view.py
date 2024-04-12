from tkinter import Tk, ttk, constants

class StartView:
    def __init__(self, root, handle_budget_creation):
        self._root = root
        self._handle_budget_creation = handle_budget_creation
        self._frame = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _init(self):
        self._frame = ttk.Frame(master=self._root)

        title_label = ttk.Label(master=self._frame, text="Overview Screen")
        name_entry_label = ttk.Label(master=self._frame, text="Create a new budget by giving it a name: ")
        self._budget_name_entry = ttk.Entry(master=self._frame)
        button = ttk.Button(
          master=self._frame,
          text="Create",
          command=self._handle_button_click
        )

        title_label.pack()
        name_entry_label.pack()
        self._budget_name_entry.pack()
        button.pack()

    def _handle_button_click(self):
        entry_value = self._budget_name_entry.get()
        self._handle_budget_creation(entry_value)