class Budget:
    def __init__(self, name):
        self.name = name # Name of budget
        self.currency = "€" # Currency of budget

        # Initialize the budget dict along with income & expense -sublists
        self.entries = {"Income": [], "Expense": []}

    # Set budget name
    def name_budget(self, name: str): 
        self.name = name

    # Set new currency for budget
    def set_currency(self, input: str): 
        self.currency = input

    # Add income entry to budget dict
    def add_income(self, name, value): 
        self.entries["Income"].append(f"{name}: {value} {self.currency}")
    
    # Add expense entry to budget dict
    def add_expense(self, name, value):
        self.entries["Expense"].append(f"{name}: {value} {self.currency}")

    # Sum of income
    def sum_income(self):
        total = 0
        for income in self.entries["Income"]:
            total += income[1]
        return total

    # Sum of expenses
    def sum_expenses(self):
        total = 0
        for expense in self.entries["Expense"]:
            total += expense[1]
        return total

    # Total sum
    def sum_total(self):
        income = self.sum_income()
        expenses = self.sum_expenses()
        total = income - expenses
        return total

    def fetch_income_entries(self):
        return self.entries["Income"]

    def fetch_expenses_entries(self):
        return self.entries["Expense"]