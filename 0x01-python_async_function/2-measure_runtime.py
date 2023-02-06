#!/usr/bin/env python3
"""
2. Measure the runtime
"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """_summary_
    Args:
        n (_type_): _description_
        max_delay (_type_): _description_
    Returns:
        _type_: _description_
    """
    start = time.time()
    wait_n(n, max_delay)
    end = time.time()
    total_time = end - start
    return total_time / n
