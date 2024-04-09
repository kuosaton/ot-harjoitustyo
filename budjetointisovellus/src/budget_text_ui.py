from budget import Budget
import random
import time

class Interface:
    def __init__(self):
        self.budget = Budget()
        self.jokes = True

    def help(self):
        print(f"Commands:")
        print(f"1: Give the budget a name")
        print(f"2: Add new income entry")
        print(f"3: Add new expense entry")
        print(f"4: Fetch all income entries")
        print(f"5: Fetch all expense entries")
        print(f"6: Fetch all budget entries")
        print(f"7: Calculate sum of income and expenses entries")
        print(f"8: Disable jokes (not recommended)")
        print(f"9: Give another joke (highly recommended)")
        print(f"Q: Quit")
        print(f"H: Help")

    def fetch_a_joke(self): # Very important
        joke_entries = {
                        0: "What word is spelled wrong on every dictionary? - Wrong.",
                        1: "Me: I've lost the dictionary! Her: Can you look upstairs? Me: I can't look up anything.",
                        }
        return random.choice(joke_entries)
    
    def disable_jokes(self):
        print("We are sorry (not really) to inform you that this function is currently not in operation.")
        self.jokes = False

    def start(self):
        if self.jokes == True:
            print("")
            print(f"Welcome to the budget text UI! We know that budgets can be boring, which is why we offer you a complimentary joke!")
            print("")
            time.sleep(1)
            print(self.fetch_a_joke())
            time.sleep(1)
            print("")
        else:
            print(f"Welcome to the budget text UI! You have opted to disable jokes, which is a little saddening.")
            print("")

        self.help()

        while True:
            print("")
            command = input("Input any command from 1-9, H for help, or Q to quit: ")

            if command == "1":
                name = str(input("Give the budget a name: "))
                self.budget.name_budget(name)
                print("The name of the budget has been set to", self.budget.name)

            elif command == "2":
                name = str(input("Give a title for the entry: "))
                amount = float(input("Give an amount: "))
                self.budget.add_expense(name, amount)
                print("Income entry added!")

            elif command == "3":
                name = str(input("Give a title for the entry: "))
                amount = float(input("Give an amount: "))
                self.budget.add_expense(name, amount)
                print("Expense entry added!")

            elif command == "4":
                print(self.budget.fetch_income_entries())

            elif command == "5":
                print(self.budget.fetch_expenses_entries())

            elif command == "6":
                print(self.budget.fetch_all_entries())

            elif command == "7":
                print(self.budget.sum_total())

            elif command == "8":
                self.disable_jokes()

            elif command == "9":
                print(self.fetch_a_joke())

            elif command == "Q":
                break

            elif command == "H":
                self.help()

            else:
                print("Error: Invalid input :(")
                self.help()

if __name__ == "__main__":
    budgetInterface = Interface()
    budgetInterface.start()