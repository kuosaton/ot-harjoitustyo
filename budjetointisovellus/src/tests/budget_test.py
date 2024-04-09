import unittest
from budget import Budget

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget()

    def test_budget_dict_is_initialized_correctly(self):
        self.assertEqual(str(self.budget.fetch_all_entries()), "{'Income': [], 'Expenses': []}")

