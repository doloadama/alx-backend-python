#!/usr/bin/env python3
"""
11. More involved type annotations
"""


from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrives a value from a dictionary using the given key
    """
    if key in dct:
        return dct[key]
    else:
        return default
