import unittest
import requests
from unittest.mock import patch

def get_api_data(url):
    # Simulate API request
    response = requests.get(url)
    return response.json()

class TestAPIData(unittest.TestCase):

    @patch('requests.get')
    def test_get_api_data(self, mock_get):
        mock_get.return_value.json.return_value = {'key': 'value'}
        result = get_api_data('https://fakeurl.com/data')
        self.assertEqual(result, {'key': 'value'})
