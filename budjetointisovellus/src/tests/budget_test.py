import unittest
from budget import Budget

class TestBudget(unittest.Testcase):
    def start(self):
        self.budget = Budget()

    def test_budget_dict_is_initialized_correctly(self):
        self.assertEqual(str(self.budget.fetch_all_entries), "{'Income': [], 'Expenses': []}")
