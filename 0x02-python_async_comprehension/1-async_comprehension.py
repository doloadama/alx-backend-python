#!/usr/bin/env python3
"""1-Async Comprehension
"""
from importlib import import_module as using
from typing import Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """
    collect 10 random numbers using an async comprehension over async_generator
    then return 10 random numbers
    """
    return [num async for num in async_generator()]
