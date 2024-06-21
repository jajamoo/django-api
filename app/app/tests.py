"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calc.addNum(1, 2)
        self.assertEqual(res, 3)

    def test_subtract_numbers(self):
        res = calc.subtractNum(10, 5)
        self.assertEqual(res, 5)
