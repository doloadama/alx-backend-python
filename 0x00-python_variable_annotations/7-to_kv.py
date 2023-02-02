#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Union, Tuple

"""
7. Complex types - string and int/float to tuple
"""

def to_kv(k: str, v: Union[int,float]) -> tuple[str, float]:
  """
  a type-annotated function to_kv that takes a string k and
  an int OR float v as arguments and returns a tuple.
  The first element of the tuple is the string k.
  The second element is the square of the int/float v
  and should be annotated as a float
  """
  return (k, float(v**2))
