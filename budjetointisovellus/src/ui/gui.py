from tkinter import Tk
from startview import startView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _show_start_view(self):
        self._current_view = startView(
            self._root,
        )

        self._current_view.pack()

window = Tk()
window.title("TkInter example")

ui = UI(window)
ui.start()

window.mainloop()