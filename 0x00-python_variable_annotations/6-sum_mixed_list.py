#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of all elements in the list.
    """
    return sum(mxd_lst)
