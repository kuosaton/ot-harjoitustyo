from tkinter import Tk
from start_view import StartView
from budget_view import BudgetView
import sys
import os
sys.path.append(os.path.abspath('../')) # lisätään juurikansio src pythonin hakupolkuun luokan Budget hakemista varten
from budget import Budget

class UI:
    def __init__(self, root):
        self._root = root
        self._budget = None
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_budget_creation(self, name):
        self._budget = Budget()
        self._budget.name_budget(name)
        self._show_budget_view()

    def _handle_return(self):
        self._show_start_view()

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_budget_creation
        )

        self._current_view.pack()

    def _show_budget_view(self):
        self._hide_current_view()

        self._current_view = BudgetView(
            self._root,
            self._budget,
            self._handle_return,
        )

        self._current_view.pack()
        
window = Tk()
window.title("BudgetApp")

ui = UI(window)
ui.start()

window.mainloop()