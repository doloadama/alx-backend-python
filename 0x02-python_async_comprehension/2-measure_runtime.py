#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions
"""
import asyncio
import time
from importlib import import_module as using
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """will execute async_comprehension four times in parallel using asyncio
    gather.
    measure_runtime should measure the total runtime and return it
    """
    tasks = [async_comprehension() for i in range(4)]
    start = asyncio.get_running_loop().time()
    await asyncio.gather(*tasks)
    end = asyncio.get_running_loop().time()
    return end - start
