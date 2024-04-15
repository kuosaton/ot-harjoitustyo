import unittest
from budget import Budget

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.budget = Budget("Test")

    def test_budget_is_initialized_correctly(self):
        self.assertEqual(str(self.budget.name), "Test")
        self.assertEqual(str(self.budget.entries), "{'Income': [], 'Expense': []}")