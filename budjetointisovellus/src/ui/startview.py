import sys
import os
sys.path.append(os.path.abspath('../')) # lisätään juurikansio src pythonin hakupolkuun luokan Budget hakemista varten
from budget import Budget
from tkinter import Tk, ttk, constants

class startView:
    def __init__(self, root):
        self.budget = Budget()
        self._root = root
        self._frame = None
        self.start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def start(self):
        self._frame = ttk.Frame(master=self._root)

        title_label = ttk.Label(master=self._root, text="Overview")
        name_entry_label = ttk.Label(master=self._root, text="Name of budget")
        self._budget_name_entry = ttk.Entry(master=self._root)
        button = ttk.Button(
          master=self._root,
          text="Enter",
          command=self._handle_button_click
        )

        title_label.pack()
        name_entry_label.pack()
        self._budget_name_entry.pack()
        button.pack()

    def _handle_button_click(self):
        entry_value = self._budget_name_entry.get()
        self.budget.name_budget(entry_value)
        print(f"Name of the budget is: {self.budget.name}")
        
