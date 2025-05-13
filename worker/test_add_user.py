import unittest
from unittest.mock import patch

import requests

from tasks import add_user


class AddUserTestCase(unittest.TestCase):

    @patch('tasks.requests.post')
    @patch('tasks.requests.get')
    def test_add_user_success(self, mock_get, mock_post):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [{
                "name": {"first": "John", "last": "Doe"},
                "gender": "male",
                "dob": {"age": 30},
                "phone": "1234567890",
                "email": "john.doe@example.com"
            }]
        }

        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"id": 1}

        result = add_user()
        self.assertEqual(result, {"id": 1})
        self.assertTrue(mock_post.called)

    @patch('tasks.requests.get')
    def test_add_user_get_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network error")
        result = add_user()
        self.assertIsNone(result)

    @patch('tasks.requests.get')
    @patch('tasks.requests.post')
    def test_add_user_post_failure(self, mock_get, mock_post):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "results": [{
                "name": {"first": "John", "last": "Doe"},
                "gender": "male",
                "dob": {"age": 30},
                "phone": "1234567890",
                "email": "john.doe@example.com"
            }]
        }
        mock_post.side_effect = requests.exceptions.HTTPError("500 Internal Server Error")
        result = add_user()
        self.assertIsNone(result)
