class Budget:
    """Yksittäistä budjettia kuvaava luokka.

    Attributes:
        name:       Budjetin nimi.
        currency:   Budjetin valuutta.
        income_n:   Budjetin tulokirjaukselle annettava tunnus. Käytetään kirjauksien poistamiseen.
        expense_n:  Sama kuin ylempi, menokirjauksille.
        entries:    Budjetin sisältö. Sanakirja, joka sisältää alilistat tulo- ja menokirjauksille.
    """
    def __init__(self, name):
        """Konstruktori, luo uuden budjetin.

        Args:
            name: Merkkijonoarvo, budjetille annettu nimi.
        """
        self.name = name
        self.currency = "€"
        self.income_n = 0
        self.expense_n = 0

        self.entries = {"Income": [], "Expense": []}

    def set_new_name(self, new_name):
        """Metodi, joka asettaa budjetille uuden nimen.

        Args:
            new_name: Merkkijonoarvo, budjetille annettu uusi nimi.
        """
        self.name = new_name

    def set_new_currency(self, new_currency):
        """Metodi, joka asettaa budjetille uuden valuutan.

        Args:
            new_currency: Merkkijonoarvo, budjetille annettu uusi valuutta.
        """
        self.currency = new_currency

    def add_income(self, name, value):
        """Metodi, joka lisää budjettiin uuden tulokirjauksen.

        Args:
            name: Merkkijonoarvo, tulokirjaukselle annettu nimi.
            value: Float-arvo, tulokirjaukselle annettu rahamäärä.
        """
        self.entries["Income"].append({'id': self.income_n, 'name': name, 'value': value})
        self.income_n += 1

    def add_expense(self, name, value):
        """Metodi, joka lisää budjettiin uuden menokirjauksen.

        Args:
            name: Merkkijonoarvo, menokirjaukselle annettu nimi.
            value: Float-arvo, menokirjaukselle annettu rahamäärä.
        """
        self.entries["Expense"].append({'id': self.expense_n, 'name': name, 'value': value})
        self.expense_n += 1

    def remove_income_entry(self, id):
        """Metodi, joka poistaa budjetista tulokirjauksen.

        Args:
            id: Kokonaislukuarvo, poistettavan tulokirjauksen tunnus.
        """
        try:
            self.entries["Income"].pop(id)
            self.income_n -= 1
        except IndexError:
            pass

    def remove_expense_entry(self, id):
        """Metodi, joka poistaa budjetista menokirjauksen.

        Args:
            id: Kokonaislukuarvo, poistettavan menokirjauksen tunnus.
        """
        try:
            self.entries["Expense"].pop(id)
            self.expense_n -= 1
        except IndexError:
            pass

    def get_entries_income_str(self):
        """Metodi, joka hakee budjetin tulokirjaukset ja palauttaa ne listassa.

        Returns:
            income_entries: Lista, joka sisältää budjetin tulokirjaukset.
        """
        if not self.entries["Income"]:
            return ["No income entries"]

        income_entries = []
        for income in self.entries["Income"]:
            income_entries.append(f"{income['name']}, {income['value']}{self.currency}")

        return income_entries

    def get_entries_expense_str(self):
        """Metodi, joka hakee budjetin menokirjaukset ja palauttaa ne listassa.

        Returns:
            expense_entries: Lista, joka sisältää budjetin menokirjaukset merkkijonomuodossa.
        """
        if not self.entries["Expense"]:
            return ["No expense entries"]

        expense_entries = []
        for expense in self.entries["Expense"]:
            expense_entries.append(f"{expense['name']}, {expense['value']}{self.currency}")

        return expense_entries

    def get_entries_all_str(self):
        """Metodi, joka hakee budjetin kaikki kirjaukset ja palauttaa ne yhtenä merkkijonona.

        Returns:
            all_entries: Kaikki budjetin kirjaukset yhtenä merkkijonona.
        """
        all_entries = f"{self.get_entries_income_str()}, {self.get_entries_expense_str()}"
        return all_entries

    def get_sum_income(self):
        """Metodi, joka laskee budjetin tulokirjausten rahasumman.

        Returns:
            result: Tulojen rahasumma.
        """
        if not self.entries["Income"]:
            return 0

        result = 0
        for income in self.entries["Income"]:
            result += float(income['value'])
        return round(result, 2)

    def get_sum_expense(self):
        """Metodi, joka laskee budjetin menokirjausten rahasumman.

        Returns:
            result: Menojen rahasumma.
        """
        if not self.entries["Expense"]:
            return 0

        result = 0
        for expense in self.entries["Expense"]:
            result += float(expense['value'])
        return round(result, 2)

    def get_sum_all(self):
        """Metodi, joka laskee tulojen ja menojen rahasumman.

        Returns:
            result: Tulojen ja menojen rahasumma.
        """
        result = 0
        sum_income = self.get_sum_income()
        sum_expenses = self.get_sum_expense()
        result = sum_income - sum_expenses
        return round(result, 2)
