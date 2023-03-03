import unittest
from unittest.mock import patch
from todocli.api import find, send_request, ApiConnectionError, MethodNotAllowed


class FormattersTestCase(unittest.TestCase):
    def setUp(self):
        self.data = [
            {'_id': '640214290e9fd8ba2aef9d1f', 'text': 'task1', '__v': 0},
            {'_id': '6402142b0e9fd8ba2aef9d22', 'text': 'task2', '__v': 0},
            {'_id': '6402142c0e9fd8ba2aef9d25', 'text': 'task3', '__v': 0}
        ]

    @patch('todocli.api.get_all')
    def test_find(self, mock_get_all):
        mock_get_all.return_value = self.data
        result = find("640214290e9fd8ba2aef9d1f")
        self.assertEqual(result, True)    \


    @patch('todocli.api.get_all')
    def test_find_not_found(self, mock_get_all):
        mock_get_all.return_value = self.data
        result = find("1")
        self.assertEqual(result, False)

    @patch('requests.get')
    def test_send_request_GET(self, mock_get_all):
        mock_get_all.return_value.status_code = 200
        mock_get_all.return_value.json.return_value = self.data
        result = send_request("GET", "url")
        self.assertEqual(result, self.data)

    @patch('requests.get')
    def test_send_request_UNKNOWN(self, mock_requests_get):
        self.assertRaises(MethodNotAllowed, send_request, "UNKNOWN", "url")

    @patch('requests.get')
    def test_send_request_ApiConnectionError(self, mock_requests_get):
        mock_requests_get.return_value.status_code = 404
        self.assertRaises(ApiConnectionError, send_request, "GET", "url")


if __name__ == '__main__':
    unittest.main()
