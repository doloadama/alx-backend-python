#!/usr/bin/env python3
"""
12. Type Checking
"""


from typing import Tuple, List


def zoom_array(lst: List, factor: int = 2) -> List:
    """
    Returns a new list with each element multiplied
    by factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
