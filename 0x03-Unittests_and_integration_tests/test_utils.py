#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Sequence, Dict


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
