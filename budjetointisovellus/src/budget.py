class Budget:
    def __init__(self):
        self.name = "" # Name of the budget
        self.currency = "€" # The default currency for returned values is Euros. Can be changed by the user

        # Initialize the budget dict along with income & expense -sublists
        self.budget = {}
        self.budget["Income"] = []
        self.budget["Expenses"] = []

    def name_budget(self, name: str): # Give the budget a name
        self.name = name

    def set_currency(self, input: str): # Set new currency
        self.currency = input

    def add_income(self, name: str, amount: float): # Income is added to income-sublist
        self.budget["Income"].append((name, amount))
    
    def add_expense(self, name: str, amount: float): # Same logic as above
        self.budget["Expenses"].append((name, amount))

    def sum_income(self): # Sum of the numerical values of income entries
        total = 0
        for income in self.budget["Income"]:
            total += income[1]
        return total, self.currency 

    def sum_expenses(self): # Same logic as above
        total = 0
        for expense in self.budget["Expenses"]:
            total += expense[1]
        return total, self.currency

    def sum_total(self): # Utilizing the earlier functions to return a total sum
        income = self.sum_income()
        expenses = self.sum_expenses()
        total = income - expenses

        return f"Income {income}{self.currency} - expenses {expenses}{self.currency} = {total}{self.currency}"

    def fetch_all_entries(self): # Return the whole budget dict
        return self.budget

    def fetch_income_entries(self): # Return only the income entries from the budget dict
        entries = []
        for income in self.budget["Income"]:
            entries.append(income)

        return entries

    def fetch_expenses_entries(self): # Same logic as above
        entries = []
        for expense in self.budget["Expenses"]:
            entries.append(expense)

        return entries
