import unittest
from unittest.mock import patch, MagicMock
from tasks import add_card
import requests


class AddCardTestCase(unittest.TestCase):

    @patch('tasks.requests.get')
    @patch('tasks.requests.post')
    @patch('tasks.random.choice', return_value=1)
    @patch('tasks.random.randint', return_value=123)
    def test_add_card_success(self, mock_randint, mock_choice, mock_post, mock_get):
        card_data = {
            "credit_card_number": "4111111111111111",
            "credit_card_expiry_date": "2025-12-31",
            "credit_card_type": "Visa"
        }

        users_data = [{"id": 1}, {"id": 2}]

        mock_get.side_effect = [
            MagicMock(status_code=200, json=lambda: card_data),
            MagicMock(status_code=200, json=lambda: users_data)
        ]

        mock_post.return_value = MagicMock(status_code=201, json=lambda: {"id": 1})

        result = add_card()
        self.assertEqual(result, {"id": 1})

    @patch('tasks.requests.get')
    def test_add_card_fetch_card_data_fail(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")
        result = add_card()
        self.assertIsNone(result)

    @patch('tasks.requests.get')
    def test_add_card_fetch_users_fail(self, mock_get):
        mock_get.side_effect = [
            MagicMock(status_code=200, json=lambda: {"credit_card_number": "1234"}),
            requests.RequestException("DB error")
        ]
        result = add_card()
        self.assertIsNone(result)

    @patch('tasks.requests.get')
    @patch('tasks.requests.post')
    @patch('tasks.random.choice', return_value=1)
    @patch('tasks.random.randint', return_value=123)
    def test_add_card_invalid_json(self, mock_randint, mock_choice, mock_post, mock_get):
        invalid_data = {"credit_card_type": "Visa"}
        mock_get.side_effect = [
            MagicMock(status_code=200, json=lambda: invalid_data),
            MagicMock(status_code=200, json=lambda: [{"id": 1}])
        ]
        result = add_card()
        self.assertIsNone(result)
