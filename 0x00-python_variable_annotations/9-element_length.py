#!/usr/bin/env python
"""
9. Let's duck type an iterable object
"""

from typing import Iterable
from typing import List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns the length of each element in the iterable.
    """
    return [(i, len(i)) for i in lst]
