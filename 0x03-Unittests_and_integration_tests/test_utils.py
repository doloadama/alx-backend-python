#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Sequence, Dict
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from
    unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Sequence,
                               expected: int) -> None:
        """
        Tests the acces_nested_map method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Sequence,
                                        ) -> None:
        """

        Args:
            nested_map (Dict): _description_
            path (Tuple): _description_
            expected (Union[Dict, int]): _description_
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests utils.get_Json
    """

    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
    ])
    @patch("request.get")
    def get_json(self,tests_url, test_payload, mock_requests_get):
        """
        Args:
            url (str): _description_

        Returns:
            Dict: _description_
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(tests_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(tests_url)
