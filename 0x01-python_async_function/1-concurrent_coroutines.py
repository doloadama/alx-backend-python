#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
import time
from '1-concurrent_coroutines' import wait_n

def measure_time(n, max_delay):
    """
    :param n: number of coroutines
    :param max_delay: maximum delay in seconds
    :return: average time in seconds
    """
    start_time = time.time()
    wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
