#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """will execute async_comprehension four times in parallel using asyncio
    gather.
    measure_runtime should measure the total runtime and return it
    """
    numb = 0
    for i in range(4):
        print(await async_comprehension(i))
        numb += 1
    return numb
