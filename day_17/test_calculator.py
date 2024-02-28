# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 1), 2)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_large_numbers(self):
        self.assertEqual(self.calc.add(1e30, 1e30), 2e30)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(0, 100), 0)
