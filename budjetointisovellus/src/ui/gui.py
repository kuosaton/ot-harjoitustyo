from tkinter import Tk
from start_view import StartView
from budget_view import BudgetView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _handle_budget_creation(self, budget_name):
        self._show_budget_view(budget_name)

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_budget_creation
        )

        self._current_view.pack()

    def _show_budget_view(self, budget_name):
        self._hide_current_view()

        self._current_view = BudgetView(
            self._root,
            budget_name,
            self._show_start_view
        )

        self._current_view.pack()


window = Tk()
window.title("Budgeting App")

ui = UI(window)
ui.start()

window.mainloop()