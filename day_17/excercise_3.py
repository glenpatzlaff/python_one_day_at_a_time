import unittest
import requests
from unittest.mock import patch

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    return n * factorial(n-1)

def get_api_data(url):
    # Simulate API request
    response = requests.get(url)
    return response.json()

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

class TestAPIData(unittest.TestCase):

    @patch('requests.get')
    def test_get_api_data(self, mock_get):
        mock_get.return_value.json.return_value = {'key': 'value'}
        result = get_api_data('https://fakeurl.com/data')
        self.assertEqual(result, {'key': 'value'})

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFactorialFunction))
    suite.addTest(unittest.makeSuite(TestAPIData))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
