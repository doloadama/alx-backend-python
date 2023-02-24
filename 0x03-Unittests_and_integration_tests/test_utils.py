#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Union, Tuple, Dict


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
                               path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """
        Tests the acces_nested_map method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",),  KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple,
                                         exception: Exception) -> None:
        """

        Args:
            nested_map (Dict): _description_
            path (Tuple): _description_
            expected (Union[Dict, int]): _description_
        """
        self.assertRaises(access_nested_map(nested_map, path), exception)
