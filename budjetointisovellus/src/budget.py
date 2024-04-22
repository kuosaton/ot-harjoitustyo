class Budget:
    def __init__(self, name):
        self.name = name # Name of budget
        self.currency = "€" # Currency of budget
        self.income_n = 0 # For numbering income entries
        self.expense_n = 0 # For numbering expense entries

        # Initialize the budget dict along with income & expense -sublists
        self.entries = {"Income": [], "Expense": []}

    def set_new_name(self, new_name):
        self.name = new_name

    def set_new_currency(self, new_currency):
        self.currency = new_currency

    # Add income entry to budget dict
    def add_income(self, name, value):
        self.entries["Income"].append({'id': self.income_n, 'name': name, 'value': value})
        self.income_n += 1

    # Add expense entry to budget dict
    def add_expense(self, name, value):
        self.entries["Expense"].append({'id': self.expense_n, 'name': name, 'value': value})
        self.expense_n += 1

    def remove_income_entry(self, id):
        try:
            self.entries["Income"].pop(id)
            self.income_n -= 1
        except IndexError:
            pass

    def remove_expense_entry(self, id):
        try:
            self.entries["Expense"].pop(id)
            self.expense_n -= 1
        except IndexError:
            pass

    # Fetch income entries in a clean str format
    def get_entries_income_str(self):
        if not self.entries["Income"]:
            return ["No income entries"]

        income_entries = []
        for income in self.entries["Income"]:
            income_entries.append(f"{income['name']}, {income['value']}{self.currency}")

        return income_entries

    # Fetch expense entries in a clean str format
    def get_entries_expense_str(self):
        if not self.entries["Expense"]:
            return ["No expense entries"]

        expense_entries = []
        for expense in self.entries["Expense"]:
            expense_entries.append(f"{expense['name']}, {expense['value']}{self.currency}")

        return expense_entries

    # Fetch all entries in a clean str format
    def get_entries_all_str(self):
        return f"{self.get_entries_income_str()}, {self.get_entries_expense_str()}"

    # Sum of income
    def get_sum_income(self):
        if not self.entries["Income"]:
            return 0

        result = 0
        for income in self.entries["Income"]:
            result += float(income['value'])
        return round(result, 2)

    # Sum of expenses
    def get_sum_expense(self):
        if not self.entries["Expense"]:
            return 0

        result = 0
        for expense in self.entries["Expense"]:
            result += float(expense['value'])
        return round(result, 2)

    # Total sum
    def get_sum_all(self):
        result = 0
        sum_income = self.get_sum_income()
        sum_expenses = self.get_sum_expense()
        result = sum_income - sum_expenses
        return round(result, 2)
