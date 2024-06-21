"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.add_num(1, 2)
        self.assertEqual(res, 3)

    def test_subtract_numbers(self):
        res = calc.subtract_num(10, 5)
        self.assertEqual(res, 5)
