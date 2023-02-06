#!/usr/bin/env python3
"""
2. Measure the runtime
"""


from asyncio import run
import time
wait_n = __import__(' 1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """_summary_

    Args:
        n (_type_): _description_
        max_delay (_type_): _description_
    Returns:
        _type_: _description_
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    return (end_time - start_time) / n
