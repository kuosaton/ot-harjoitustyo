class Budget:
    def __init__(self):
        self.name = "" # Name of the budget
        self.currency = "€" # The default currency for returned values is Euros. Can be changed by the user

        # Initialize the budget dict along with income & expense -sublists
        self.entries = {}
        self.entries["Income"] = []
        self.entries["Expense"] = []

    def name_budget(self, name: str): # Give the budget a name
        self.name = name

    def set_currency(self, input: str): # Set new currency
        self.currency = input

    def add_income(self, name: str, amount: float): # Income is added to income-sublist
        self.entries["Income"].append((name, amount))
    
    def add_expense(self, name: str, amount: float): # Same logic as above
        self.entries["Expense"].append((name, amount))

    def sum_income(self): # Sum of the numerical values of income entries
        total = 0
        for income in self.entries["Income"]:
            total += income[1]
        return total

    def sum_expenses(self): # Same logic as above
        total = 0
        for expense in self.entries["Expense"]:
            total += expense[1]
        return total

    def sum_total(self): # Utilizing the earlier functions to return a total sum
        income = self.sum_income()
        expenses = self.sum_expenses()
        total = income - expenses
        return total

    def fetch_income_entries(self): # Return income entries from budget dict
        return self.entries["Income"]

    def fetch_expenses_entries(self): # Same logic as above
        return self.entries["Expense"]