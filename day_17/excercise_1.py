import unittest

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    return n * factorial(n-1)

class TestFactorialFunction(unittest.TestCase):

    def test_factorial_normal(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_non_integer(self):
        with self.assertRaises(ValueError):
            factorial(2.5)
