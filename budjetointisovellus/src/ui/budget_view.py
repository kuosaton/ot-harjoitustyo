from budget import Budget
import tkinter as tk
from tkinter import ttk, constants, IntVar, Listbox, StringVar, DoubleVar

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
    def _create_entries_frame(self):
        if self._entries_frame:
            self._entries_frame.destroy()

        self._entries_frame = ttk.Frame(master=self._frame)
        self._entries_frame.pack(expand=True, fill=tk.BOTH)

        # Create entry listboxes, entry sum listboxes and labels
        expense_sum = DoubleVar(value=self._budget.get_sum_expense())
        income_sum = DoubleVar(value=self._budget.get_sum_income())
        total_sum = DoubleVar(value=self._budget.get_sum_all())

        entries_label = ttk.Label(master=self._entries_frame, text="Tip: click entry to delete it!")
        entries_label.pack(pady=10)

        self._create_income_entries_list()
        self._create_expense_entries_list()

        income_entries_sum_label = ttk.Label(master=self._entries_frame, text="Sum of income entries")
        income_entries_sum_listbox = Listbox(master=self._entries_frame, listvariable=income_sum, height=1)

        expense_entries_sum_label = ttk.Label(master=self._entries_frame, text="Sum of expense entries")
        expense_entries_sum_listbox = Listbox(master=self._entries_frame, listvariable=expense_sum, height=1)

        total_sum_label = ttk.Label(master=self._entries_frame, text="Sum of income and expense entries")
        total_sum_listbox = Listbox(master=self._entries_frame, listvariable = total_sum, height=1)

        # Pack up 

        income_entries_sum_label.pack()
        income_entries_sum_listbox.pack(expand=True, fill=tk.BOTH)

        expense_entries_sum_label.pack()
        expense_entries_sum_listbox.pack(expand=True, fill=tk.BOTH)

        total_sum_label.pack()
        total_sum_listbox.pack(expand=True, fill=tk.BOTH)

    # Used by _create_entries_frame()
    def _create_income_entries_list(self):
        income_var = StringVar(value=self._budget.get_entries_income_str())

        income_entries_title_label = ttk.Label(master=self._entries_frame, text="Income entries")
        self._income_entries_listbox = Listbox(master=self._entries_frame, listvariable=income_var, selectmode=tk.SINGLE)

        income_entries_title_label.pack()
        self._income_entries_listbox.pack(expand=True, fill=tk.BOTH)
        self._income_entries_listbox.bind('<<ListboxSelect>>', self._handle_income_entry_deletion)

    # Delete listbox entry by clicking it
    def _handle_income_entry_deletion(self, event):
        selected_index = self._income_entries_listbox.curselection()[0]
        self._budget.remove_income_entry(selected_index)
        self._create_entries_frame()

    # Used by _create_entries_frame()
    def _create_expense_entries_list(self):
        expense_var = StringVar(value=self._budget.get_entries_expense_str())

        expense_entries_title_label = ttk.Label(master=self._entries_frame, text="Expense entries")
        self._expense_entries_listbox = Listbox(master=self._entries_frame, listvariable=expense_var, selectmode=tk.SINGLE)

        expense_entries_title_label.pack()
        self._expense_entries_listbox.pack(expand=True, fill=tk.BOTH)
        self._expense_entries_listbox.bind('<<ListboxSelect>>', self._handle_expense_entry_deletion)

    # Delete listbox entry by clicking it
    def _handle_expense_entry_deletion(self, event):
        selected_index = self._expense_entries_listbox.curselection()[0]
        self._budget.remove_expense_entry(selected_index)
        self._create_entries_frame()


    # Initializing the main budget view frame
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
        # Get user input
        try:
            entry_name = self._entry_name_entry.get()
            entry_value = float(self._entry_value_entry.get())
            entry_type_value = self._entry_type.get()

            if entry_name and entry_value:
                # Checkbutton used by user to define desired entry type
                if entry_type_value == 1:
                    self._budget.add_income(entry_name, entry_value)
                elif entry_type_value == 0:
                    self._budget.add_expense(entry_name, entry_value)
                
                self._create_entries_frame()

        # Do nothing if input values are not of expected type
        except ValueError:
            pass