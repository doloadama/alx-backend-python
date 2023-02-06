#!/usr/bin/env python3
"""
2. Measure the runtime
"""


import asyncio
import time
from 1-concurrent_coroutines import wait_n


def measure_time(n, max_delay):
    """_summary_

    Args:
        n (_type_): _description_
        max_delay (_type_): _description_
    Returns:
        _type_: _description_
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    total_time = time.time() - start_time
    return total_time / n
