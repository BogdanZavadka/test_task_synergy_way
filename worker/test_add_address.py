import unittest
from unittest.mock import patch, MagicMock
import requests
from tasks import add_address


class AddAddressTestCase(unittest.TestCase):

    @patch('tasks.requests.get')
    @patch('tasks.requests.post')
    @patch('tasks.random.choice', return_value=1)
    def test_add_address_success(self, mock_choice, mock_post, mock_get):
        mock_location_data = {
            "results": [{
                "location": {
                    "country": "USA",
                    "state": "California",
                    "city": "Los Angeles",
                    "street": {"name": "Sunset Blvd", "number": 123},
                    "postcode": 90001
                }
            }]
        }

        mock_user_list = [{"id": 1}, {"id": 2}]

        mock_get.side_effect = [
            MagicMock(status_code=200, json=lambda: mock_location_data),
            MagicMock(status_code=200, json=lambda: mock_user_list)
        ]

        mock_post.return_value = MagicMock(status_code=201, json=lambda: {"id": 1})

        result = add_address()
        self.assertEqual(result, {"id": 1})

    @patch('tasks.requests.get')
    def test_add_address_randomuser_api_fail(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")
        result = add_address()
        self.assertIsNone(result)

    @patch('tasks.requests.get')
    def test_add_address_user_api_fail(self, mock_get):
        mock_get.side_effect = [
            MagicMock(status_code=200, json=lambda: {"results": [{"location": {}}]}),
            requests.RequestException("Failed fetching users")
        ]
        result = add_address()
        self.assertIsNone(result)

    @patch('tasks.requests.get')
    @patch('tasks.requests.post')
    @patch('tasks.random.choice', return_value=1)
    def test_add_address_invalid_json(self, mock_choice, mock_post, mock_get):
        mock_get.side_effect = [
            MagicMock(status_code=200, json=lambda: {"results": [{"location": {"city": "Kyiv"}}]}),
            MagicMock(status_code=200, json=lambda: [{"id": 1}])
        ]
        result = add_address()
        self.assertIsNone(result)
