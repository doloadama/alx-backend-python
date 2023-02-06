#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines at the same time with async
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def measure_time(n: int, max_delay: int) -> float:
    """
    :param n: number of coroutines
    :param max_delay: maximum delay in seconds
    :return: average time in seconds
    """
    delay_time = [asyncio.create_task(wait_random(max_delay))
                  for _ in range(n)]
    return [await task for task in asyncio.as_completed(delay_time)]
