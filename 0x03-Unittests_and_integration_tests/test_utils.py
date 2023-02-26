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
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Test the get_json method to ensure it returns the expected output.
        Args:
            url: url to send http request to
            payload: expected json response
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    tests memoise method of utils.py
    """
    def test_memoize(self) -> None:
        """
        Tests that utils.memoize decorator works
        """
        class TestClass:
            def a_method(self) -> None:
                return 42
            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
