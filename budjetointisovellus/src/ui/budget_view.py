from budget import Budget
import tkinter as tk
from tkinter import ttk, constants, IntVar, Listbox, StringVar

class BudgetView:
    def __init__(self, root, budget_name, handle_return):
        self._root = root
        self._budget = Budget(budget_name)
        self._handle_return = handle_return # For returning to the overview screen
        self._frame = None
        self._entries_frame = None

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    # Initialize name field for entry creation
    def _create_entry_name_field(self):
        entry_name_label = ttk.Label(master=self._frame, text="Give a name:")
        self._entry_name_entry = ttk.Entry(master=self._frame)

        entry_name_label.pack()
        self._entry_name_entry.pack()

    # Initialize value field for entry creation
    def _create_entry_value_field(self):
        entry_value_label = ttk.Label(master=self._frame, text="Give an amount:")
        self._entry_value_entry = ttk.Entry(master=self._frame)

        entry_value_label.pack()
        self._entry_value_entry.pack()

    # Initialize toggle button for entry type selection
    def _create_entry_type_checkbutton(self):
        self._entry_type = IntVar()   
        
        entry_type_checkbutton = ttk.Checkbutton(
            master=self._frame,
            text = "Check for income entry, uncheck for expense entry:",
            variable=self._entry_type,
            onvalue = 1,
            offvalue = 0
        )

        entry_type_checkbutton.pack()

    # This function creates/replaces the entry list frame for the GUI
    def _create_entries_list(self):
        if self._entries_frame:
            self._entries_frame.destroy()

        self._entries_frame = ttk.Frame(master=self._frame)
        self._entries_frame.pack(expand=True, fill=tk.BOTH)

        # Fetch entries
        income_var = StringVar(value=self._budget.entries["Income"])
        expense_var = StringVar(value=self._budget.entries["Expense"])

        # Create listboxes for the budget entries
        income_entries_title_label = ttk.Label(master=self._entries_frame, text="Income entries:")
        income_entries_listbox = Listbox(master=self._entries_frame, listvariable=income_var)

        expense_entries_title_label = ttk.Label(master=self._entries_frame, text="Expense entries:")
        expense_entries_listbox = Listbox(master=self._entries_frame, listvariable=expense_var)

        income_entries_title_label.pack()
        income_entries_listbox.pack(expand=True, fill=tk.BOTH)

        expense_entries_title_label.pack()
        expense_entries_listbox.pack(expand=True, fill=tk.BOTH)

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(master=self._frame, text=f"Viewing budget: {self._budget.name}. Create budget entries below.")
        title_label.pack()

        # Initialize user input fields
        self._create_entry_name_field()
        self._create_entry_value_field()
        self._create_entry_type_checkbutton()

        # Initalize input submit button
        submitButton = ttk.Button(
            master=self._frame,
            text="Create entry",
            command=self._handle_entry_creation
        )

        # Initialize exit button
        returnButton = ttk.Button(
            master=self._frame,
            text="Return to overview",
            command=self._handle_return, 
        )

        submitButton.pack()
        returnButton.pack()

    # When called, this function creates a new entry and calls create_entries_list() to show updated entries
    def _handle_entry_creation(self):
        entry_name = self._entry_name_entry.get()
        entry_value = self._entry_value_entry.get()
        entry_type_value = self._entry_type.get()

        if entry_type_value == 1:
            self._budget.add_income(entry_name, entry_value)
        elif entry_type_value == 0:
            self._budget.add_expense(entry_name, entry_value)
        
        self._create_entries_list()
