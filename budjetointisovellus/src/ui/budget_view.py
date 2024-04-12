import sys
import os
sys.path.append(os.path.abspath('../')) # lisätään juurikansio src pythonin hakupolkuun luokan Budget hakemista varten
from budget import Budget
import tkinter as tk
from tkinter import Tk, ttk, constants, IntVar, Listbox, Variable

class BudgetView:
    def __init__(self, root, budget, handle_return):
        self._root = root
        self._budget = budget
        self._handle_return = handle_return
        self._frame = None

        self._init()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _init(self):
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(master=self._frame, text=f"Viewing budget: {self._budget.name}")

        entry_heading_label = ttk.Label(master=self._frame, text="Create a new entry: ")
        name_entry_label = ttk.Label(master=self._frame, text="Name of entry")
        self._name_entry = ttk.Entry(master=self._frame)
        value_entry_label = ttk.Label(master=self._frame, text="Value of entry")
        self._value_entry = ttk.Entry(master=self._frame)
        
        self._entry_type = IntVar()   
        
        entry_type_toggle = ttk.Checkbutton(
            master=self._frame,
            text = "Checked = income entry, unchecked = expense entry",
            variable=self._entry_type,
            onvalue = 1,
            offvalue = 0
        )

        submitButton = ttk.Button(
            master=self._frame,
            text="Create entry",
            command=self._handle_button_click
        )

        returnButton = ttk.Button(
            master=self._frame,
            text="Return to overview",
            command=self._handle_return
        )

        title_label.pack()
        returnButton.pack()
        entry_heading_label.pack()
        name_entry_label.pack()
        self._name_entry.pack()
        value_entry_label.pack()
        self._value_entry.pack()
        entry_type_toggle.pack()
        submitButton.pack()

    def _handle_button_click(self):
        entry_name = self._name_entry.get()
        entry_value = self._value_entry.get()
        entry_type_value = self._entry_type.get()

        if entry_type_value == 1:
            self._budget.add_income(entry_name, entry_value)
        elif entry_type_value == 0:
            self._budget.add_expense(entry_name, entry_value)

        self.show_entries()

    def show_entries(self):
        self._frame = ttk.Frame(master=self._root)

        self._income_entries = self._budget.entries["Income"]
        self._expense_entries = self._budget.entries["Expense"]

        income_entries_title_label = ttk.Label(master=self._frame, text="Income entries:")
        self._income_entries_listbox = Listbox(
            master = self._root,
            listvariable = Variable(value=self._income_entries)
        )

        expense_entries_title_label = ttk.Label(master=self._frame, text="Expense entries:")
        self._expense_entries_listbox = Listbox(
            master = self._root,
            listvariable = Variable(value=self._expense_entries)
        )
        income_entries_title_label.pack()
        self._income_entries_listbox.pack(expand=True, fill=tk.BOTH)
        expense_entries_title_label.pack()
        self._expense_entries_listbox.pack(expand=True, fill=tk.BOTH)

