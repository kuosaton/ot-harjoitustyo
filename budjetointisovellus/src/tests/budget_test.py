import unittest
from budget import Budget

class TestBudget(unittest.TestCase):
    def test_budget_is_initialized_correctly(self):
        budget = Budget("Test")
        self.assertEqual(str(budget.name), "Test")
        self.assertEqual(str(budget.entries), "{'Income': [], 'Expense': []}")

    def test_name_and_currency_are_changed_correctly(self):
        budget = Budget("Test")
        budget.set_new_name("New name")
        budget.set_new_currency("£")

        self.assertEqual(str(budget.name), "New name")
        self.assertEqual(str(budget.currency), "£")

    def test_entries_are_initialized_and_returned_correctly(self):
        budget = Budget("Test")
        budget.add_expense("nakit ja muusi", 20.80)
        budget.add_income("palkka", 2000)

        self.assertEqual(str(budget.get_entries_expense_str()), "['nakit ja muusi, 20.8€']")
        self.assertEqual(str(budget.get_entries_income_str()), "['palkka, 2000€']")
        self.assertEqual(str(budget.get_entries_all_str()), "['palkka, 2000€'], ['nakit ja muusi, 20.8€']")

    def test_entry_sums_are_returned_correctly(self):
        budget = Budget("Test")
        budget.add_expense("nakit ja muusi", 20.80)
        budget.add_income("palkka", 2000)

        self.assertEqual(str(budget.get_sum_expense()), "20.8")
        self.assertEqual(str(budget.get_sum_income()), "2000.0")
        self.assertEqual(str(budget.get_sum_all()), "1979.2")

    def test_entries_are_deleted_correctly(self):
        budget = Budget("Test")
        budget.add_expense("kissanminttu", 4.26)
        budget.add_income("tyovuoro", 128)

        self.assertEqual(str(budget.get_entries_all_str()), "['tyovuoro, 128€'], ['kissanminttu, 4.26€']")

        budget.remove_income_entry(0)
        budget.remove_income_entry(0) # will get passed because of IndexError

        self.assertEqual(str(budget.get_sum_all()), "-4.26")
        self.assertEqual(str(budget.get_entries_all_str()), "['No income entries'], ['kissanminttu, 4.26€']")

        budget.remove_expense_entry(0)
        budget.remove_expense_entry(0) # will get passed because of IndexError

        self.assertEqual(str(budget.get_entries_all_str()), "['No income entries'], ['No expense entries']")
        self.assertEqual(str(budget.get_sum_income()), "0")
        self.assertEqual(str(budget.get_sum_expense()), "0")
        self.assertEqual(str(budget.get_sum_all()), "0")