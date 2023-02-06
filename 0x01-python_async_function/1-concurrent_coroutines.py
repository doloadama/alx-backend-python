#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
import time
from '1-concurrent_coroutines' import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    :param n: number of coroutines
    :param max_delay: maximum delay in seconds
    :return: average time in seconds
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
