from ui.start_view import StartView
from ui.budget_view import BudgetView

class GUI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""
    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.
        
        Args:
            root: TKinter-elementti, jonka sisään käyttöliittymä alustetaan.
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Metodi, joka avaa aloitusnäkymän."""
        self._show_start_view()

    def _handle_budget_creation(self, budget_name):
        """Metodi, joka käsittelee budjetin luomisen.

        Args:
            budget_name: Merkkijonoarvo, budjetille annettu nimi.
        """
        self._show_budget_view(budget_name)

    def _hide_current_view(self):
        """Metodi, joka tuhoaa nykyisen näkymän."""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_start_view(self):
        """Metodi, joka käynnistää aloitusnäkymän."""
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_budget_creation
        )

        self._current_view.pack()

    def _show_budget_view(self, budget_name):
        """Metodi, joka käynnistää budjettinäkymän.

        Args:
            budget_name: Merkkijonoarvo, budjetille annettu nimi.
        """
        self._hide_current_view()

        self._current_view = BudgetView(
            self._root,
            budget_name,
            self._show_start_view
        )

        self._current_view.pack()